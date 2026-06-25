Status: Ready — work through all parts in order

# Meta SWE Lab 02 — CodeSignal 4-Stage In-Memory Key-Value Store

**Role:** SWE | **Tier:** 2 | **Est. time:** 90 min | **Difficulty:** Medium | **Format:** CodeSignal ICF

---

## Scenario

You're taking Meta's CodeSignal OA. The clock is running. You've been given a single problem presented in 4 progressive levels — each level builds on the one before, and your code from prior levels must continue to pass. The problem: build an in-memory key-value store with time-to-live (TTL) support.

Level 1 wants basic SET/GET/DELETE. Level 2 adds TTL expiry. Level 3 hardens edge cases — overwriting a key resets its TTL, deleting an expired key returns False, and GET on an expired key returns None (not the stale value). Level 4 extends to GET_RANGE: retrieve all values stored for a key between two timestamps.

You have 90 minutes. Strategy: complete L1 and L2 fully before touching L3. A partial L3 with passing L1–L2 scores higher than a broken L3 that crashes L1.

---

## Milestones

- [ ] M1 · L1 Complete — basic SET/GET/DELETE working, all L1 tests passing
- [ ] M2 · L2 Complete — TTL expiry logic working; GET on expired key returns None
- [ ] M3 · L3 Complete — edge cases hardened: overwrite resets TTL; DELETE of expired returns False; no stale data leaked
- [ ] M4 · L4 Complete — GET_RANGE implemented; history tracking does not break L1–L3
- [ ] M5 · Defended — curveballs answered (thread safety, persistence, Redis comparison)
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Part 0: Forethought

**Goal:** Build all 4 levels with passing tests. Maintain backward compatibility at each level. Do not break what you already have.

**Target time:** 90 min (L1 = 10 min, L2 = 20 min, L3 = 20 min, L4 = 30 min, buffer = 10 min)

**Confidence (1–5):** ___

**Key risk:** ___

**The #1 CodeSignal ICF mistake:** Touching L3 before L1–L2 are locked in. Partial L3 that crashes prior levels = lowest tier score.

---

## Part 1: Clarifying Questions

In a real CodeSignal OA, you cannot ask clarifying questions — the spec is the spec. But thinking through these before you code will prevent you from building the wrong internal model.

**Category: Goal**
Question: What is a "key" — any string? Case-sensitive?
Assumption: Any string key, case-sensitive. "Key" and "key" are different.

<details>
<summary>Hint</summary>
Case sensitivity matters if you're normalizing keys anywhere. Don't — treat keys as opaque strings and let the dict handle it.
</details>

**Category: Users / Behavior**
Question: If a key is SET with TTL=5 and then SET again (overwrite), does the new TTL reset the clock or inherit the old expiry?
Assumption: A new SET always resets the clock. The key's expiry is based on the most recent SET call.

<details>
<summary>Hint</summary>
This is the critical L3 edge case. Most candidates build L2 assuming expiry is never overwritten. When L3 adds overwrite behavior, they have to refactor. Think ahead: store expiry_time as absolute time (time.time() + ttl), not TTL duration. Then overwrite is trivial.
</details>

**Category: Data**
Question: What type is the value? Can it be None?
Assumption: Values are strings or integers. None is reserved for "key not found" — we will not allow None as a stored value.

<details>
<summary>Hint</summary>
If None is a valid value, you need a sentinel object (like a class-level NOT_FOUND = object()) instead of returning None for missing keys. Clarifying this saves a nasty bug.
</details>

**Category: Constraints**
Question: Is time.time() monotonic? Could two SET calls at the exact same millisecond cause issues?
Assumption: We'll use time.time() (floating point seconds). Ties are acceptable — last write wins within the same second.

<details>
<summary>Hint</summary>
In production, use time.monotonic() for internal timing to avoid clock skew. time.time() is wall clock and can go backward (NTP adjustment, DST). For this lab, time.time() is fine — but knowing this shows depth.
</details>

**Category: Scale**
Question: For GET_RANGE (L4) — how many SET calls per key might there be? Can history be unbounded?
Assumption: For this lab, history is unbounded. In production, you'd cap history per key or use a time-based eviction policy.

<details>
<summary>Hint</summary>
Unbounded history means GET_RANGE is O(h) where h = history entries for that key. If h is large, you'd use a sorted structure (sorted list by timestamp) and binary search for the range. For this lab, linear scan is acceptable.
</details>

---

## Checkpoint M1 Marker

Before coding: confirm your data structure design. What does `self.store` hold at each level?

Level 1: `{key: value}`
Level 2: `{key: (value, expiry_time_or_None)}`
Level 3: Same as L2 (just harden the edge cases — no structural change needed)
Level 4: `{key: [(value, set_time, expiry_time_or_None), ...]}` — list of all historical entries

Write this design in your scratch space before touching the keyboard.

---

## Part 2: Decomposition

### Workflow

```
SET(key, value, ttl=None)
    → store (value, expiry = now + ttl if ttl else None)
    → if overwrite: reset expiry (do not inherit old expiry)

GET(key)
    → look up key
    → if not found: return None
    → if expiry is set AND now > expiry: treat as not-found (return None)
    → else: return value

DELETE(key)
    → if not found (or expired): return False
    → else: remove and return True

GET_RANGE(key, start_ts, end_ts)   [L4 only]
    → look through all historical (value, set_time, expiry) entries for this key
    → return list of values where set_time is in [start_ts, end_ts]
    → include entries even if they are now expired (range query is historical)
```

### Bottleneck Analysis

- GET: O(1) — direct hash map lookup + expiry check
- SET: O(1) amortized
- DELETE: O(1)
- GET_RANGE: O(h) where h = number of SET calls for this key — can optimize to O(log h) with binary search on sorted list

### State Transitions

```
Key lifecycle:
    [not set] → SET → [alive]
                        ↓ (ttl expires)
                     [expired] → GET returns None
                               → DELETE returns False
                        ↓ (SET again)
                     [alive, new expiry]
```

### Key Design Decision

**Store absolute expiry time, not TTL duration.**

Bad: `self.store[key] = (value, ttl_seconds)`  — you'd have to track when it was set to compute expiry on read
Good: `self.store[key] = (value, time.time() + ttl if ttl else None)` — expiry check is a single comparison

This makes overwrite trivial: just overwrite with the new absolute expiry. No need to recalculate anything.

---

## Checkpoint M2 Marker

Before writing L2 code: confirm you're storing `expiry_time` (absolute) not `ttl` (relative). If your L1 stored just `value`, you need to migrate to `(value, None)` tuple before adding L2. Do this migration at the L2 boundary — not inside L1 logic.

---

## Part 3: Contract Design

### Input/Output Table

| Method | Input | Output | Notes |
|---|---|---|---|
| `set(key, value)` | str, any | None | Adds or overwrites. No TTL — key persists forever. |
| `set(key, value, ttl)` | str, any, int | None | Key expires after `ttl` seconds from now. Overwrites reset TTL. |
| `get(key)` | str | value or None | Returns None if not found OR expired. Cannot distinguish the two from outside. |
| `delete(key)` | str | bool | True if key existed and was NOT expired. False otherwise. |
| `get_range(key, start, end)` | str, float, float | list | Historical values where set_time in [start, end]. Empty list if none. |

### Named Design Decisions

**Decision 1: Lazy expiry (not eager)**
We check expiry at read time (GET, DELETE) rather than running a background sweep. This means expired keys occupy memory until accessed. Pro: simple, no threads needed. Con: memory bloat if many keys expire but are never accessed. Redis uses lazy + background sweep (periodic sweep of a sample of expiring keys).

**Decision 2: Absolute timestamps, not relative TTL**
Store `time.time() + ttl` at write time. All subsequent reads compare `time.time() > stored_expiry`. This makes overwrite semantics trivial and keeps the expiry check a single comparison.

**Decision 3: History stored as append-only list (L4)**
Each SET call appends to a per-key history list. GET_RANGE does a linear scan. This is simple but O(h) per range query. Alternative: use `bisect` on a sorted-by-timestamp list for O(log h) range lookup.

**Decision 4: GET_RANGE includes expired entries**
Range queries are historical — they return values that were stored in the time window even if those values have since expired. This matches the semantics of audit logs and time-series stores.

### Tradeoff Table

| Design axis | Our choice | Alternative | When to switch |
|---|---|---|---|
| Expiry enforcement | Lazy (at read time) | Eager background sweep | Switch if memory matters and many keys expire without reads |
| TTL storage | Absolute expiry time | Relative TTL at write | Almost never — absolute is strictly better |
| History structure | Append-only list | Sorted list + bisect | Switch if GET_RANGE is hot path with large history per key |
| Thread safety | Not thread-safe | Add threading.Lock | Switch the moment this is called from multiple threads |

---

## Checkpoint M3 Marker

Before coding L4: verify that your L1–L3 tests still pass with your current implementation. If L4 requires a structural change (adding history list), make sure you update SET in a backward-compatible way — history tracking should be additive, not replacing the primary lookup path.

---

## Part 4: Build — Progressive Levels

### Level 1 — Basic SET / GET / DELETE

```python
class KVStore:
    def __init__(self):
        self.store = {}  # key -> value

    def set(self, key: str, value) -> None:
        # TODO: store the key-value pair
        pass

    def get(self, key: str):
        # TODO: return value if key exists, else return None
        pass

    def delete(self, key: str) -> bool:
        # TODO: remove key if it exists, return True
        # If key doesn't exist, return False
        pass
```

**L1 Tests — must pass before moving to L2:**
```python
store = KVStore()

store.set("a", 1)
assert store.get("a") == 1

store.set("a", 2)          # overwrite
assert store.get("a") == 2

assert store.get("b") is None   # missing key

assert store.delete("a") == True
assert store.get("a") is None
assert store.delete("a") == False   # already deleted
assert store.delete("z") == False   # never existed

print("L1: PASS")
```

**L1 Reference Solution (write yours first):**
```python
def set(self, key: str, value) -> None:
    self.store[key] = value

def get(self, key: str):
    return self.store.get(key, None)

def delete(self, key: str) -> bool:
    if key in self.store:
        del self.store[key]
        return True
    return False
```

---

### Level 2 — Add TTL Support

Migrate `self.store` to `{key: (value, expiry_time_or_None)}`.

```python
import time

class KVStore:
    def __init__(self):
        self.store = {}  # key -> (value, expiry_time or None)

    def set(self, key: str, value, ttl: int = None) -> None:
        # TODO: compute expiry as time.time() + ttl if ttl else None
        # Store (value, expiry) tuple
        pass

    def get(self, key: str):
        # TODO: look up key
        # If found, check if expiry is set and if time.time() > expiry
        # If expired: return None (and optionally clean up the key)
        # If not expired: return the value
        pass

    def delete(self, key: str) -> bool:
        # TODO: handle expired key (return False if expired)
        pass
```

**L2 Tests:**
```python
import time

store = KVStore()

store.set("x", 10, ttl=1)    # expires in 1 second
assert store.get("x") == 10   # still alive

time.sleep(1.1)
assert store.get("x") is None  # expired

store.set("y", 20)             # no TTL — persists forever
time.sleep(0.5)
assert store.get("y") == 20    # still alive

store.set("z", 30, ttl=2)
assert store.delete("z") == True   # alive, should delete
assert store.get("z") is None

print("L2: PASS")
```

**L2 Reference Solution:**
```python
def set(self, key: str, value, ttl: int = None) -> None:
    expiry = time.time() + ttl if ttl is not None else None
    self.store[key] = (value, expiry)

def get(self, key: str):
    if key not in self.store:
        return None
    value, expiry = self.store[key]
    if expiry is not None and time.time() > expiry:
        del self.store[key]   # lazy cleanup
        return None
    return value

def delete(self, key: str) -> bool:
    if key not in self.store:
        return False
    value, expiry = self.store[key]
    if expiry is not None and time.time() > expiry:
        del self.store[key]
        return False    # expired = doesn't exist
    del self.store[key]
    return True
```

---

### Level 3 — Edge Case Hardening

No structural change needed from L2. These tests expose logic gaps in your L2 implementation.

**L3 Tests:**
```python
import time

store = KVStore()

# Edge case 1: Overwrite resets TTL
store.set("k", "v1", ttl=1)
time.sleep(0.5)
store.set("k", "v2", ttl=10)   # overwrite with longer TTL
time.sleep(0.8)
assert store.get("k") == "v2"   # should still be alive (10 sec TTL from overwrite)

# Edge case 2: Overwrite removes TTL (makes key permanent)
store.set("m", "temp", ttl=1)
store.set("m", "perm")           # overwrite with no TTL
time.sleep(1.5)
assert store.get("m") == "perm"  # should be permanent

# Edge case 3: DELETE of expired key returns False
store.set("e", "expires", ttl=1)
time.sleep(1.2)
assert store.delete("e") == False   # expired = not found

# Edge case 4: GET of expired key returns None (not the old value)
store.set("f", "old", ttl=1)
time.sleep(1.2)
assert store.get("f") is None

# Edge case 5: SET with TTL=0 expires immediately
store.set("instant", "gone", ttl=0)
time.sleep(0.01)
assert store.get("instant") is None

print("L3: PASS")
```

**L3 Key insight:** If your L2 `set()` correctly overwrites `self.store[key]` with a new `(value, expiry)` tuple every time, then overwrite-resets-TTL is automatic. No special case needed. If you stored TTL separately from value, you have a bug.

---

### Level 4 — GET_RANGE (Historical Values)

Add history tracking to `set()`. Add `get_range()` method. Do not break L1–L3.

```python
import time

class KVStore:
    def __init__(self):
        self.store = {}    # key -> (value, expiry_time or None)    [primary lookup]
        self.history = {}  # key -> [(value, set_time, expiry_time or None), ...]

    def set(self, key: str, value, ttl: int = None) -> None:
        # TODO: same as L2, but also append to self.history[key]
        pass

    def get_range(self, key: str, start_ts: float, end_ts: float) -> list:
        # TODO: scan self.history[key] for entries where set_time in [start_ts, end_ts]
        # Return list of values (not tuples) in chronological order
        # Return [] if key has no history or no entries in range
        # Include entries that have since expired (this is a historical query)
        pass
```

**L4 Tests:**
```python
import time

store = KVStore()

t0 = time.time()
store.set("p", "v1")
time.sleep(0.1)
store.set("p", "v2")
time.sleep(0.1)
store.set("p", "v3", ttl=1)
t1 = time.time()

# Should return all 3 values set between t0 and t1
result = store.get_range("p", t0 - 0.05, t1 + 0.05)
assert result == ["v1", "v2", "v3"], f"Got {result}"

# Narrow range — only the first value
result = store.get_range("p", t0 - 0.05, t0 + 0.05)
assert len(result) == 1
assert result[0] == "v1"

# Key with no history
result = store.get_range("nonexistent", t0, t1)
assert result == []

# L1–L3 must still pass after adding history
store2 = KVStore()
store2.set("a", 1)
assert store2.get("a") == 1
assert store2.delete("a") == True

print("L4: PASS")
```

**L4 Reference Solution:**
```python
def set(self, key: str, value, ttl: int = None) -> None:
    expiry = time.time() + ttl if ttl is not None else None
    set_time = time.time()
    self.store[key] = (value, expiry)
    if key not in self.history:
        self.history[key] = []
    self.history[key].append((value, set_time, expiry))

def get_range(self, key: str, start_ts: float, end_ts: float) -> list:
    if key not in self.history:
        return []
    return [
        v for v, set_time, _ in self.history[key]
        if start_ts <= set_time <= end_ts
    ]
```

---

## Checkpoint M4 Marker

Run all tests (L1 through L4) before declaring done. If any test fails after a later-level change, you have a regression. Fix it before moving to Part 5.

---

## Part 5: Reasoning — 10 WHY Questions

**1. Why use lazy expiry (check at read time) instead of a background thread that sweeps expired keys?**
___

**2. Why store absolute expiry time instead of the TTL duration?**
___

**3. Why does overwrite-resets-TTL work automatically in the reference implementation?**
___

**4. What happens if two SET calls happen at the exact same millisecond? Is there a race condition in a single-threaded Python program?**
___

**5. Why does DELETE of an expired key return False rather than True?**
___

**6. Why does GET_RANGE include historically-expired entries?**
___

**7. What is the time complexity of GET_RANGE in the reference implementation?**
___

**8. How would you make GET_RANGE O(log h) instead of O(h)?**
___

**9. What is the risk of using time.time() for expiry? When would time.monotonic() be better?**
___

**10. How does the 4-level ICF format test something different than a single hard problem?**
___

---

## Part 6: Interview Simulation

### 90-Second Talk Track

"This is a build-and-evolve problem — I'm designing a class that I'll iterate on across 4 levels. My top priority is finishing L1 and L2 cleanly before touching L3. For L1: simple dict. For L2: I'm migrating to a (value, expiry) tuple, storing absolute expiry time so overwrite is trivial. For L3: if my L2 is correct, the edge cases should pass automatically — overwrite replaces the whole tuple. For L4: I add a separate history list per key. The primary store path stays fast; history is append-only. Let me start with L1."

### Curveballs

**Curveball 1:** "How would you make this thread-safe?"

Instructions: Answer before looking at the hint. Think about which operations are atomic in Python and which are not.

<details>
<summary>Hint</summary>
Python's GIL protects individual bytecode operations, but compound read-modify-write operations (check-then-act) are NOT atomic. In a multi-threaded setting, two threads could both `get()` a key, both find it not-expired, and then both proceed — that's fine. But if one `delete()`s while another is mid-read, you have a race.

Fix: add `threading.Lock()` in `__init__`. Wrap all public methods with `with self.lock:`. This makes the store thread-safe with a global lock — simple but potentially a bottleneck. For higher concurrency, use per-key locks or a lock-striping approach.
</details>

___

**Curveball 2:** "What if we need to persist this to disk on shutdown?"

Instructions: Name at least 2 approaches with one tradeoff for each.

<details>
<summary>Hint</summary>
Option A: On shutdown, serialize self.store to JSON (write to disk). On startup, load from JSON. Problem: if TTL has elapsed during downtime, you need to recalculate expiry on load. Absolute expiry timestamps survive serialization correctly — another reason to store absolute expiry.

Option B: Write-ahead log (WAL). Every SET/DELETE is appended to a log file immediately. On startup, replay the log. Faster recovery, supports crash-resilience (not just graceful shutdown). More complex.

Option C: Periodic snapshots (like Redis RDB). Full store → disk every N seconds. Tradeoff: up to N seconds of data loss on crash.
</details>

___

**Curveball 3:** "How does this compare to Redis's TTL implementation?"

Instructions: Be specific about at least 2 differences.

<details>
<summary>Hint</summary>
1. **Lazy expiry:** Both Redis and our implementation use lazy expiry (check at access time). Redis also adds a background sweep that randomly samples expiring keys every 100ms and deletes a batch — we don't have this.

2. **Persistence:** Redis supports RDB snapshots and AOF (append-only file) for durability. We are purely in-memory.

3. **History / GET_RANGE:** Redis does not natively support historical value queries. Redis Streams partially addresses this but it's a different data structure.

4. **Data types:** Redis supports Strings, Lists, Sets, Sorted Sets, Hashes. We only support string keys mapping to single values.

5. **Memory:** Redis can set a maxmemory policy (evict LRU, LFU, etc.) when memory fills. We have no eviction.
</details>

___

---

## Part 7: Self-Grade + Reflection

### SWE Rubric

| Dimension | 1 | 2 | 3 | 4 | 5 | Score |
|---|---|---|---|---|---|---|
| **Communication / think-aloud** | Silent | Occasional narration | Explains steps when asked | Consistent narration | Narrates design decisions and tradeoffs in real time | ___ |
| **Problem solving** | Could not progress past L1 | L1–L2 with major hints | L1–L2 independently, L3 with hints | L1–L3 independently | L1–L4 with clean design and no regressions | ___ |
| **Correctness** | L1 broken | L1 passing | L1–L2 passing | L1–L3 passing | L1–L4 all tests passing | ___ |
| **Code quality** | Unreadable | Functional but inconsistent | Readable, some redundancy | Clean, no redundancy, consistent naming | Production-quality: clear abstractions, well-named, easy to evolve | ___ |
| **Testing & edge cases** | No self-testing | Tested happy path | L3 edge cases named | L3 edge cases coded | All edge cases including TTL=0, overwrite, expired-delete coded and tested | ___ |
| **Debugging** | Could not find own bugs | Found bugs with heavy hints | Found bugs with nudge | Found and fixed regressions independently | Caught regressions before running tests; explained root cause | ___ |
| **Time management** | Never reached L2 | L1–L2 in time | L1–L3 in time | All 4 levels in 90 min | All 4 levels with time for curveball discussion | ___ |

**Total: ___ / 35**

### Reflection

What level tripped you up most?

___

Did your L2 design make L3 easy or hard?

___

What would you design differently if you did L1 knowing L4 was coming?

___

### Ready-When Checklist

- [ ] L1 through L4 all pass with the reference test suite
- [ ] I can explain why absolute expiry > relative TTL in one sentence
- [ ] I can explain lazy expiry vs eager sweep with a concrete tradeoff
- [ ] I can describe how to make this thread-safe and what "thread-safe" means specifically
- [ ] I can compare my design to Redis on at least 3 dimensions
- [ ] I completed all 4 levels in under 90 minutes with no hints
