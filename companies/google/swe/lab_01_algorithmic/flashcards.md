# Flashcards — Google SWE Lab 01: LRU Cache Design-a-Data-Structure

*10 cards for spaced repetition. Study these 24–48 hours after completing the workbook. Cover the answer and try to recall it before reading.*

---

## Card 1 — LRU Eviction Policy Definition

**Q:** What does "Least Recently Used" mean as an eviction policy, and in what contexts is it a good choice?

**A:** LRU evicts the cache entry that has not been accessed for the longest time. When the cache is full and a new entry must be inserted, the LRU entry is removed first.

LRU is a good choice when access patterns exhibit temporal locality — recently accessed items are likely to be accessed again soon (web page caches, CPU memory caches, database buffer pools). It is a poor choice when access patterns are sequential scans (every item is accessed once in order, so LRU would evict items that will never be reused — this is called the "sequential flood" problem).

---

## Card 2 — Why Doubly-Linked List for O(1) Remove

**Q:** Why does O(1) removal from any position in a linked list require a doubly-linked list specifically? What operation does a singly-linked list fail to do in O(1)?

**A:** To remove a node from a doubly-linked list, you need to update two pointers: the predecessor's `next` and the successor's `prev`. A doubly-linked list gives you `node.prev` directly, so you can reach the predecessor in O(1).

A singly-linked list only gives you `node.next`. To find the predecessor and update its `next` pointer, you must scan from the head — O(n). This makes removal from the middle of a singly-linked list O(n) unless you have the predecessor in hand.

For LRU Cache: when `get(key)` is called, the node may be anywhere in the list. You need to unlink it and move it to the MRU end. That unlink must be O(1). Only a doubly-linked list makes this possible.

---

## Card 3 — Hash Map for O(1) Lookup: Why Store Node Pointers

**Q:** In the raw doubly-linked list LRU implementation, the hash map stores Node objects (pointers), not just values. Why? What breaks if you store only the value?

**A:** The hash map must give you the Node object so you can call `_remove(node)` — which requires `node.prev` and `node.next`. If the map stored only the value, you would have the value but not the node's position in the list. To find the node and unlink it, you'd have to scan the list from the head — O(n) — which breaks the O(1) guarantee.

Storing the Node pointer means: `cache[key]` gives you the node in O(1), `node.prev` and `node.next` let you unlink in O(1), and `node.val` gives you the value in O(1). All three in one lookup.

Additional: Node also stores `key` so that when evicting the LRU node, you can delete it from the hash map via `del cache[node.key]` without a reverse lookup.

---

## Card 4 — Sentinel Node Pattern

**Q:** What are sentinel head and tail nodes in a doubly-linked list, and what problem do they solve?

**A:** Sentinel nodes are dummy nodes at the LRU end (head) and MRU end (tail) of the list that are never removed and never contain real data. They always have valid `prev` and `next` pointers.

Problem they solve: without sentinels, `_remove` must handle "is this the first node?" and "is this the last node?" as special cases. `_add_to_tail` must handle "is the list empty?" Adding these checks introduces branching that is easy to get wrong.

With sentinels: `_remove` always has `node.prev` and `node.next` (they are at minimum the sentinels). `_add_to_tail` always inserts between `self.tail.prev` and `self.tail`. The four-pointer-update pattern is identical regardless of list size. Zero special cases.

Sentinel pattern is the standard approach for production doubly-linked list implementations for this reason.

---

## Card 5 — OrderedDict.move_to_end()

**Q:** What does `OrderedDict.move_to_end(key)` do, what is its time complexity, and what is the common mistake when using it in LRU Cache?

**A:** `move_to_end(key)` moves the specified key-value pair to the end (MRU position) of the ordered dict. By default (`last=True`), it moves to the last position. Passing `last=False` moves to the first position. Time complexity: O(1) — the OrderedDict internally uses a doubly-linked list.

Common mistakes:
1. Forgetting `move_to_end` in `get` — without it, accessing a key does NOT update its recency. The key stays at its original position and will be evicted at the wrong time.
2. Calling `move_to_end` AFTER `self.cache[key] = value` for existing keys — in Python's OrderedDict, reassigning an existing key does NOT move it. You must call `move_to_end` explicitly (before or after the assignment, both work since the position update and value update are independent operations on the OrderedDict's internal structures).
3. Using `popitem(last=True)` for eviction — this removes the MRU entry, not the LRU. Always use `popitem(last=False)`.

---

## Card 6 — When to Use OrderedDict vs Raw Doubly-Linked List

**Q:** In an interview, when should you use Python's `OrderedDict` for LRU Cache versus implementing a raw doubly-linked list? What does each choice signal to the interviewer?

**A:** Use `OrderedDict` first: it demonstrates you know the standard library and can write idiomatic Python quickly. It also gets you to a working, testable solution faster — important under time pressure.

The interviewer will then often say: "Great — now implement it without OrderedDict." This is the more important question. It tests whether you understand the mechanism (doubly-linked list + hash map) or just knew the library shortcut.

Signals from each choice:
- OrderedDict only: demonstrates Python fluency but leaves questions about your data structures understanding.
- Raw DLL: demonstrates you understand WHY the solution works — the pointer mechanics, the sentinel pattern, the O(1) remove proof.
- Both in sequence (easy then hard): demonstrates both fluency and depth. This is the ideal interview arc.

In a Google phone screen with 45 minutes, do the OrderedDict version first (10 min) then the raw DLL (20 min) and use the remaining time for system reasoning and curveballs.

---

## Card 7 — LRU vs LFU vs FIFO

**Q:** Compare LRU, LFU, and FIFO as cache eviction policies. When is each one appropriate?

**A:**

**FIFO (First In, First Out):**
- Evicts the entry that has been in the cache the longest, regardless of how often or recently it was accessed.
- Simplest to implement: a queue.
- Appropriate when all cache entries have similar lifespan expectations and access frequency is not meaningful.
- Fails under workloads where popular items were cached early and must be repeatedly re-fetched after FIFO evicts them.

**LRU (Least Recently Used):**
- Evicts the entry that has not been accessed for the longest time.
- Appropriate for most web and database caching workloads with temporal locality.
- Fails under sequential scan workloads (sequential flood).

**LFU (Least Frequently Used):**
- Evicts the entry with the lowest access count. Ties broken by LRU.
- Appropriate when access frequency is a better predictor of future access than recency — e.g., a media streaming cache where popular songs stay popular for weeks.
- More complex to implement at O(1): requires frequency buckets + min_freq tracking.
- Fails when frequency counts are stale — an item popular a month ago will never be evicted even if never accessed again.

---

## Card 8 — Thread Safety with threading.Lock()

**Q:** How do you make the LRU Cache thread-safe? Show the pattern, name the performance trade-off, and name a higher-performance alternative.

**A:** Simplest correct approach — coarse-grained mutex:

```python
import threading

class LRUCache:
    def __init__(self, capacity):
        # ... init cache, head, tail, dict ...
        self.lock = threading.Lock()
    
    def get(self, key):
        with self.lock:
            # ... existing get logic ...
    
    def put(self, key, value):
        with self.lock:
            # ... existing put logic ...
```

`with self.lock:` acquires the lock at the top and releases it when the block exits (including on exception).

Trade-off: coarse-grained mutex serializes all reads and writes. Under high read concurrency (many threads calling `get` simultaneously), all threads wait for one lock. This limits throughput.

Higher-performance alternative: reader-writer lock (RWLock). Allows multiple concurrent reads but requires exclusive access for writes. In Python's standard library there is no built-in RWLock — you would use `threading.Lock` for writes and `threading.Semaphore` or a third-party library for the reader-writer pattern. In Java, `ReentrantReadWriteLock` provides this natively.

In a Google interview, stating the basic Lock approach and mentioning the reader-writer lock trade-off is sufficient to demonstrate production awareness.

---

## Card 9 — Time and Space Complexity of LRU Cache

**Q:** State the time and space complexity of the LRU Cache implemented with a doubly-linked list and hash map. Justify each.

**A:**

**Time complexity:**
- `get(key)`: O(1). One dict lookup, one `_remove` (4 pointer updates), one `_add_to_tail` (4 pointer updates). Each step is O(1).
- `put(key, value)`: O(1). One dict lookup, one `_remove` (if existing), one `_add_to_tail`, one dict insert/delete, and optional one eviction (`_remove` on LRU + dict delete). All O(1).
- Total: O(1) amortized for both operations. No operation scales with cache size.

**Space complexity:**
- O(capacity). The hash map holds at most `capacity` key-to-Node entries. The doubly-linked list holds at most `capacity` nodes plus 2 sentinels (constant). Total space is proportional to capacity.
- Note: each Node object consumes constant space (key, val, prev, next). The hash map entry consumes constant space. So total space is O(capacity) × O(1) per entry = O(capacity).

---

## Card 10 — GCA Scoring: Process Over Answer

**Q:** What does Google's GCA (General Cognitive Ability) dimension measure in a phone screen, and why does it mean you should narrate design decisions — not just code decisions — as you work?

**A:** GCA measures how you approach novel problems: how you decompose, what questions you ask, what tradeoffs you consider, and how you update when new information arrives. It is not a test of recall.

In a design-a-DS lab, the model score comes from narrating: why you need two data structures (not one), why a doubly-linked list specifically, why sentinel nodes, what happens on the evict path. Each of these is a design decision, not a code decision. Stating the code without narrating the design leaves the interviewer unable to assess your systems thinking.

Practical rule: before writing ANY line of code, state the data structure and why. "I'll use a hash map and a doubly-linked list because I need O(1) lookup AND O(1) removal from an arbitrary position. A hash map alone can't maintain order. A singly-linked list can't remove in O(1) from the middle." This 30-second narration earns more GCA score than a perfectly correct implementation written in silence.

---

*10 cards · Google SWE Lab 01 · LRU Cache Design-a-DS · Review 24–48 hrs after completing workbook*
