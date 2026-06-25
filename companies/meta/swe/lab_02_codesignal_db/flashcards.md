# Meta SWE Lab 02 — Flashcards

10 cards. Study until each answer comes in < 5 seconds.

---

## Card 01 — ICF 4-Level Structure

**Q:** What is the CodeSignal ICF (Industry Coding Framework) format and what is the key strategy?

**A:**

ICF presents a single problem in 4 progressive levels. Each level is a superset of the previous — your code from L1 must still pass when L2 is added, and so on.

**Structure:**
- L1: Core functionality (simple, fast to implement)
- L2: Key feature addition (often changes data structures)
- L3: Edge case hardening (exposes flaws in L2 design)
- L4: Extension/scale (adds new operation or query type)

**Strategy:**
1. Read all 4 levels BEFORE writing any code — L4 may reveal you need a different L1 data structure.
2. Complete L1 and L2 fully before touching L3.
3. Partial L3 with passing L1–L2 scores higher than broken L3 that crashes L1.
4. Time budget: ~20% L1, 25% L2, 25% L3, 30% L4.

---

## Card 02 — TTL Implementation Patterns

**Q:** What are the two approaches to storing TTL, and which is strictly better?

**A:**

**Option A: Store relative TTL**
`self.store[key] = (value, ttl_seconds, set_time)`
- Expiry check: `time.time() > set_time + ttl`
- Problem: Must store set_time separately. Overwrite: must update both value and set_time. More fields, more bugs.

**Option B: Store absolute expiry time**
`self.store[key] = (value, time.time() + ttl if ttl else None)`
- Expiry check: `time.time() > expiry` — one comparison
- Overwrite: `self.store[key] = (new_value, time.time() + new_ttl if new_ttl else None)` — automatic reset
- Strictly better: simpler check, overwrite is free, serializes cleanly

**Always use Option B.**

---

## Card 03 — time.time() vs time.monotonic()

**Q:** When should you use time.time() vs time.monotonic() for TTL, and why does it matter?

**A:**

`time.time()`: Wall-clock time in seconds since Unix epoch. Can go backward due to NTP adjustments or DST changes. Returns float with microsecond precision.

`time.monotonic()`: Time since an arbitrary start point. Guaranteed to never go backward. Not synced to real-world time.

**For TTL in interview labs:** `time.time()` is fine — clock skew is a theoretical concern, not a practical one.

**For TTL in production:** Use `time.monotonic()` so that an NTP correction (which can cause `time.time()` to jump backward) doesn't cause keys to never expire or to expire prematurely.

**Pro answer:** "I'll use `time.time()` for simplicity here, but in production I'd use `time.monotonic()` for TTL intervals to be robust against clock skew."

---

## Card 04 — Why Overwrite Resets TTL

**Q:** If you store absolute expiry time, why does overwrite-resets-TTL work automatically with no special case?

**A:**

Because every `set()` call writes a brand new `(value, expiry)` tuple, completely replacing the old one.

```python
def set(self, key, value, ttl=None):
    expiry = time.time() + ttl if ttl else None
    self.store[key] = (value, expiry)  # total replacement
```

The old expiry is destroyed. The new expiry is computed from `time.time()` at the moment of the new `set()` call. There is no code path where the old expiry "leaks through." This is the power of immutable tuples as values — you can't accidentally mutate the expiry.

Contrast with a buggy design: `self.store[key]['value'] = value` (only updates the value, leaves old expiry in place) → overwrite does NOT reset TTL. L3 test fails.

---

## Card 05 — Thread Safety in Key-Value Stores

**Q:** What makes a KV store not thread-safe, and what is the minimal fix?

**A:**

**The problem:** Python's GIL protects individual bytecode instructions but not compound operations. A `get()` that checks expiry then returns a value is a check-then-act sequence — two threads can interleave:
- Thread A: checks expiry (alive) → context switch
- Thread B: deletes the key
- Thread A: returns value — but from a deleted key? Depends on implementation.

Also: `if key not in self.store: del self.store[key]` raises KeyError if another thread deleted between the check and the delete.

**Minimal fix:**
```python
import threading

def __init__(self):
    self.store = {}
    self.lock = threading.Lock()

def get(self, key):
    with self.lock:
        # all logic here is now atomic
        ...
```

**Global lock** = simple, correct, bottleneck under high concurrency.
**Per-key locks** = more complex, better throughput.
**Lock striping** = hash key to one of N locks — balance between simplicity and concurrency.

---

## Card 06 — Redis TTL Internals

**Q:** How does Redis implement TTL expiry, and how does it differ from our lazy-only approach?

**A:**

Redis uses a **two-pronged approach:**

**1. Lazy expiry (same as ours):** When a key is accessed (GET, EXPIRE, etc.), Redis checks if it's expired. If yes, it deletes the key and returns nil.

**2. Active expiry (we don't have this):** Redis runs a background job every 100ms that:
- Samples 20 random keys from the set of keys with TTL set
- Deletes any that are expired
- If > 25% of sampled keys were expired, repeat immediately (indicating high expiry density)

**Why the difference matters:**
- Lazy only: expired keys occupy memory until accessed. A key set-and-forgotten expires "in memory" but is never reclaimed.
- Redis active sweep: limits memory bloat for set-and-forgotten keys.

**Additional Redis TTL facts:**
- TTL is stored as absolute Unix timestamp (milliseconds) in a separate hash (expires dict)
- `PERSIST` command removes TTL (makes key permanent)
- `TTL` command returns remaining seconds (-1 = no TTL, -2 = key doesn't exist)

---

## Card 07 — Designing for Evolution (ICF Pattern)

**Q:** If you knew L4 requires history tracking, how would you design L1 differently?

**A:**

**Naive L1 design:** `self.store = {key: value}` — migrate to `(value, expiry)` at L2, then add `self.history` at L4.

**Forward-looking L1 design:** Start with `self.store = {key: (value, expiry, set_time)}` and `self.history = {}`. Adds minimal overhead, but now L2 and L4 are simpler migrations.

**The lesson:** In ICF, read all levels before coding. If L4 requires a fundamentally different data structure, design for it in L1, not L4. The penalty for refactoring L1 mid-way is high — you may break tests that were passing.

**Practical rule:** Spend 3–5 minutes designing your data structures on paper before writing a single line. Draw the dict/class structure for each level. Migration cost is O(levels_remaining × refactor_time). Design cost is O(5 minutes). Always pay the design cost upfront.

---

## Card 08 — In-Memory Store Patterns

**Q:** Name 3 common in-memory store patterns used in CodeSignal/interview problems.

**A:**

**Pattern 1: Versioned KV store**
`{key: [(version, value), ...]}`
Supports GET_VERSION: return value at a specific version number. Often used in database MVCC problems.

**Pattern 2: Timestamped KV store (this lab)**
`{key: [(value, timestamp, expiry), ...]}`
Supports GET_RANGE: return values written in a time window.

**Pattern 3: Transaction-aware KV store**
Maintain a transaction stack. SET during a transaction is staged, not committed. COMMIT flushes to main store. ROLLBACK discards staged changes. Used in CodeSignal-style database simulation problems.

All three share the same L1 structure. The difference is what you append to history and how you query it.

---

## Card 09 — Key Expiry Strategies

**Q:** Name 3 expiry strategies for a KV store, with tradeoffs.

**A:**

| Strategy | How it works | Pro | Con |
|---|---|---|---|
| **Lazy (check on access)** | Check expiry at GET/DELETE time | Simple, no background threads | Expired keys occupy memory indefinitely |
| **Eager/proactive (background sweep)** | Periodic sweep deletes expired keys | Reclaims memory promptly | Requires threads; may delete keys mid-access (needs locks) |
| **TTL heap** | Min-heap of (expiry_time, key); pop and delete when top expires | Efficient O(log n) deletion order | More complex; heap must stay in sync with store |

Interview context: lazy is correct for L1–L3. Mention eager sweep as the production improvement. TTL heap is the sophisticated answer if asked "how would you make memory-efficient at scale?"

---

## Card 10 — CodeSignal OA Time Management

**Q:** What is the optimal time allocation for a 90-minute CodeSignal ICF OA?

**A:**

**Total: 90 minutes**

| Phase | Time | Goal |
|---|---|---|
| Read all 4 levels | 5 min | Understand the full scope before writing L1 |
| Design data structures | 5 min | Sketch on paper/notepad — prevents costly refactors |
| L1 implementation + tests | 10 min | Should be reflex-fast |
| L2 implementation + tests | 20 min | Core feature — do not leave without passing L2 tests |
| L3 edge case hardening | 20 min | If L2 design was correct, most of these are free |
| L4 extension | 25 min | Add history/range — ensure no regressions |
| Final test run + cleanup | 5 min | Run all tests; clean up names/comments |

**Rule:** If you're still on L2 at the 45-minute mark, skip L3 and attempt L4 in whatever time remains. Examiners see passing test counts, not which levels you attempted. L1 + L2 + L4 (even partial) may score higher than L1 + L2 + broken L3.
