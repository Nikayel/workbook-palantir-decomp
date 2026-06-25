# Google SWE Lab 01 — Design-a-Data-Structure
## LRU Cache (Tier 1 — Worked)

**Tier:** 1 (Worked) — Two-tier solution provided. Study and understand the OrderedDict version first, then implement the raw doubly-linked-list version from scratch. The point of this lab is not recall — it is proving you understand the mechanism well enough to build it from primitives.

**Before you start:** You are about to simulate a Google phone screen. The rules of this lab:
- Write all code in a plain text area. Do NOT use an IDE, REPL, or syntax highlighter.
- Narrate out loud as you work — say your reasoning as if the interviewer can hear you.
- Set a timer for 45 minutes before you open Part 1. Stop when it goes off.

---

## Milestones

Check these off as you complete each part. M4b is the hard gate — do not self-grade until it is checked.

- [ ] M1 · Clarified — asked about O(1) requirement, capacity=0 edge, thread safety, key/value types
- [ ] M2 · Modeled — named the two data structures (hash map + doubly-linked list) and explained why each one
- [ ] M3 · Designed — O(1) get/put contract proven on paper before writing a single line of code
- [ ] M4a · Built (easy) — OrderedDict solution passing all 5 test cases
- [ ] M4b · Built (hard) — raw doubly-linked list solution passing all 5 test cases **(hard gate)**
- [ ] M5 · Extended — can explain how to make LRUCache thread-safe with a lock
- [ ] M6 · Ready — self-graded ≥ 28/35 on two separate attempts

---

## Part 0 — Forethought

**Goal:** Design an LRU Cache that satisfies an O(1) get/put contract, implement it in two ways (library shortcut, then from scratch), and narrate clearly enough to score well on GCA. The interviewer is grading your modeling and communication as much as your code.

**Target time:** 45 minutes total. Suggested breakdown:
- 5 min — clarifying questions (Part 1)
- 8 min — decomposition and modeling (Part 2)
- 3 min — sign the contract (Part 3)
- 10 min — Tier 1a: OrderedDict implementation + test (Part 4a)
- 12 min — Tier 1b: raw DLL implementation (Part 4b)
- 5 min — system reasoning (Part 5)
- 7 min — curveballs (Part 6)

**Key reminder:** GCA is scored on PROCESS, not just the final answer. Narrate every design decision before you code it. An interviewer who sees you name "hash map plus doubly-linked list for O(1) get and O(1) remove" before writing a line is evaluating your systems thinking, not your typing speed.

**Confidence rating before starting (circle one):** 1 — 2 — 3 — 4 — 5

**What I want to get right this session:** [blank — write your personal goal for this attempt]

---

## Part 1 — Clarifying Questions

*Google style: always clarify before designing. The interviewer expects this. Jumping straight to code signals poor communication skills and poor engineering instinct.*

The scenario: You're in a Google phone screen. The interviewer shares a Google Doc — no syntax highlighting, no autocomplete. They say:

> "Design an LRU Cache that supports get(key) and put(key, value). get should return -1 for missing or evicted keys. put should evict the least-recently-used entry when the cache is full. Capacity is fixed at construction time."

You have 45 minutes.

**Model questions to ask (with rationale):**

**Q1: "Is O(1) time for both get and put a requirement, or is O(log n) acceptable?"**
Rationale: This is the most important design constraint. O(1) forces doubly-linked list + hash map. O(log n) allows a heap or sorted structure. You must nail this down before choosing your data structure.
*Assumption for this lab: Yes, O(1) time for both get and put is required.*

**Q2: "What should happen if capacity is 0?"**
Rationale: Capacity zero is an edge case that forces you to define whether puts are no-ops or errors. This matters for constructor logic.
*Assumption: Capacity 0 means the cache is disabled — all gets return -1 and all puts are no-ops.*

**Q3: "Is thread safety required?"**
Rationale: In production, caches are often shared across threads. The answer changes whether you add a Lock. Asking signals production awareness.
*Assumption for the base implementation: No thread safety required. Mention it as an extension.*

**Q4: "Are keys and values restricted to integers, or can they be any type?"**
Rationale: LeetCode constrains to int, but in real systems keys might be strings, values might be objects. The answer affects type hints but not the core design.
*Assumption: Integer keys and integer values (matching LeetCode 146), but the design generalizes.*

**Q5: "Does a get on an existing key count as 'using' it — i.e., does get update recency?"**
Rationale: This is a subtle but critical specification. Most LRU implementations say yes — accessing a key via get moves it to most-recently-used. Confirming this before coding prevents a class of bugs.
*Assumption: Yes — get updates recency.*

**Checkpoint M1:** Check the box above if you asked at least 3 of these before designing.

---

## Part 2 — Decomposition

*Before writing a single line of code, model the system out loud. Name the entities, operations, and state.*

### Entities

- **Cache entry:** a (key, value) pair with an implicit recency ordering.
- **LRU end:** the entry that was used least recently — the eviction candidate.
- **MRU end:** the entry that was used most recently — the last-accessed or last-inserted entry.

### Operations

| Operation | What it must do | Time constraint |
|---|---|---|
| `get(key)` | Return value if present; mark as MRU; return -1 if absent | O(1) |
| `put(key, value)` | Insert or update; mark as MRU; evict LRU if over capacity | O(1) |
| `evict()` | Remove the LRU entry (internal) | O(1) |

### The O(1) Problem

Naive approach: store entries in a list, sorted by recency. get is O(n) (scan for key). Eviction is O(1) (remove the front). Too slow.

Better approach: store entries in a dict (O(1) lookup) + doubly-linked list (O(1) insert/remove given a node pointer). The dict maps each key to the Node in the linked list. The linked list maintains recency order.

**Why doubly-linked list and not singly?**
To remove a node from the middle of the list in O(1), you need to update both its predecessor and its successor. A singly-linked list only gives you the successor — finding the predecessor requires an O(n) scan. Doubly-linked gives you both in O(1).

**Why sentinel head and tail?**
Sentinel nodes (dummy head at the LRU end, dummy tail at the MRU end) eliminate all conditional logic for inserting at the front or removing at the back. Every insert and remove operation always has valid prev and next pointers, even when the list has zero real entries. This removes a class of off-by-one bugs.

**State model:**

```
LRU end                      MRU end
[sentinel head] <-> [node A] <-> [node B] <-> [sentinel tail]
                      (oldest)                  (newest)
```

When we access B (get or put), B moves to the position just before sentinel tail. When we need to evict, we remove the node just after sentinel head.

**Checkpoint M2:** Check the box above if you named both data structures and explained why O(1) requires doubly-linked list specifically.

---

## Part 3 — Contract

*Sign this before you code. This is what you're implementing.*

**Class interface:**
```
LRUCache(capacity: int)
    get(key: int) -> int
    put(key: int, value: int) -> None
```

**Preconditions:**
- `capacity` ≥ 0. If capacity is 0, all puts are no-ops, all gets return -1.
- Keys are integers. Values are integers.
- `get` and `put` each run in O(1) time (amortized).

**Postconditions of `get(key)`:**
- If key is in the cache: returns cache[key] and marks key as most-recently-used.
- If key is absent or evicted: returns -1. Does not change cache state.

**Postconditions of `put(key, value)`:**
- If key is already in cache: updates the value in place and marks as MRU.
- If key is new AND len(cache) < capacity: inserts (key, value) as MRU.
- If key is new AND len(cache) == capacity: evicts the LRU entry, then inserts (key, value) as MRU.

**Edge cases confirmed (from Part 1):**
- `LRUCache(0)` — all operations are no-ops or return -1.
- `get` on a key that was evicted returns -1 (same as missing).
- `put` on an existing key does NOT change the cache size — it updates in place and moves to MRU.
- `put` followed immediately by `get` returns the just-put value.

---

## Part 4a — Implementation: OrderedDict (Tier 1 Easy)

*Read through the model solution carefully. Understand every line and comment. Then scroll to "Your Turn" and re-implement from scratch in the blank cell.*

### Model Solution — OrderedDict

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  # key -> value, insertion/access order tracked
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # mark as recently used (moves to MRU end)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # update recency before overwriting value
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # evict LRU (first/oldest = last=False)
```

**Annotations — make sure you understand each one:**

- `OrderedDict()` — a dict that remembers insertion order (and tracks access order via `move_to_end`). Under the hood, it is a hash map + doubly-linked list — exactly our design from Part 2. We are using the standard library's version.
- `move_to_end(key)` — moves the specified key to the end (MRU position) of the ordered dict. This is the O(1) recency update. Without this call in `get`, getting a key would NOT mark it as recently used, which is a semantic bug.
- `self.cache[key] = value` after `move_to_end` — safe because move_to_end already repositioned the node; the assignment updates the value without reinserting.
- `popitem(last=False)` — removes and returns the first item (LRU end). `last=True` would remove the MRU end, which is wrong.
- `if len(self.cache) > self.capacity` — note we check AFTER inserting, not before. If capacity is 0, this always evicts immediately, making the cache a no-op. If capacity is N and we just inserted item N+1, we evict once.

**What if we forgot `move_to_end` in `get`?**
get would return the correct value but would NOT update recency. Example: cache = {A, B, C} at capacity. Access A via get. Then put D. Expected evict: B (LRU). Without move_to_end in get, we'd evict A (still marked as LRU). This is a semantic bug that passes basic tests but fails recency-specific tests.

**What if we put `move_to_end` AFTER the assignment in `put`?**
For existing keys, `self.cache[key] = value` would reinstate the key at the MRU end by default in Python 3.7+ dicts — but OrderedDict does NOT move on reassignment. So `move_to_end` must come first (or you'd lose recency update on existing keys).

---

### Your Turn — OrderedDict Implementation

*Close the model above. Without looking back, implement the OrderedDict solution yourself.*

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        # [blank — implement here]
        pass
    
    def get(self, key: int) -> int:
        # [blank]
        pass
    
    def put(self, key: int, value: int) -> None:
        # [blank]
        pass
```

**Test cases (trace through your implementation manually):**

**Test 1:** Basic get/put/evict
```
cache = LRUCache(2)
cache.put(1, 1)   # cache: {1:1}
cache.put(2, 2)   # cache: {1:1, 2:2}
cache.get(1)      # returns 1; cache: {2:2, 1:1} — 1 is now MRU
cache.put(3, 3)   # evicts 2 (LRU); cache: {1:1, 3:3}
cache.get(2)      # returns -1 (evicted)
cache.put(4, 4)   # evicts 1 (LRU); cache: {3:3, 4:4}
cache.get(1)      # returns -1 (evicted)
cache.get(3)      # returns 3
cache.get(4)      # returns 4
```

**Test 2:** Update existing key does not grow cache
```
cache = LRUCache(2)
cache.put(1, 1)   # {1:1}
cache.put(2, 2)   # {1:1, 2:2}
cache.put(1, 10)  # update key 1; {2:2, 1:10} — 1 is MRU
cache.put(3, 3)   # evicts 2 (LRU); {1:10, 3:3}
cache.get(2)      # returns -1
cache.get(1)      # returns 10
```

**Test 3:** Capacity 1
```
cache = LRUCache(1)
cache.put(1, 1)   # {1:1}
cache.put(2, 2)   # evicts 1; {2:2}
cache.get(1)      # returns -1
cache.get(2)      # returns 2
```

**Test 4:** get updates recency
```
cache = LRUCache(2)
cache.put(2, 1)
cache.put(1, 1)
cache.get(2)      # access 2 — now MRU; 1 is LRU
cache.put(4, 1)   # evicts 1 (LRU), not 2
cache.get(1)      # returns -1 (evicted)
cache.get(2)      # returns 1
```

**Test 5:** Capacity 0 (edge)
```
cache = LRUCache(0)
cache.put(1, 1)   # no-op (capacity 0)
cache.get(1)      # returns -1
```

**Checkpoint M4a:** Check the box at the top when all 5 test cases pass in your head or on paper.

---

## Part 4b — Implementation: Raw Doubly-Linked List (Tier 1 Hard)

*Now implement the same LRU Cache WITHOUT using OrderedDict. Use a raw doubly-linked list and a regular dict. This proves you understand the mechanism, not just the library call.*

### Starter Code — Fill in the TODOs

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        # Sentinel head (LRU end) and tail (MRU end)
        self.head = Node()  # dummy LRU sentinel
        self.tail = Node()  # dummy MRU sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        # TODO: unlink node from doubly-linked list
        # node.prev and node.next are guaranteed non-None (sentinels ensure this)
        pass
    
    def _add_to_tail(self, node):
        # TODO: add node just before self.tail (= mark as MRU)
        pass
    
    def get(self, key: int) -> int:
        # TODO: return val and move to MRU position; return -1 if absent
        pass
    
    def put(self, key: int, value: int) -> None:
        # TODO: insert or update; mark as MRU; evict LRU if over capacity
        pass
```

### Model Solution — Raw DLL (Read AFTER your attempt)

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        self.head = Node()  # sentinel: LRU end
        self.tail = Node()  # sentinel: MRU end
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Unlink node from its current position
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node):
        # Insert node just before self.tail (= most-recently-used position)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)       # unlink from current position
        self._add_to_tail(node)  # re-insert at MRU end
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing: remove from current position, update value, re-add at MRU
            node = self.cache[key]
            self._remove(node)
            node.val = value
            self._add_to_tail(node)
        else:
            # New entry
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_tail(node)
            if len(self.cache) > self.capacity:
                # Evict LRU: the node just after self.head
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key]  # remove from dict using node.key
```

**Annotations — most important details:**

- `_remove(node)` — four pointer updates. You MUST update both sides: `prev_node.next = next_node` and `next_node.prev = prev_node`. Missing one direction leaves a dangling pointer.
- `_add_to_tail(node)` — inserts between `self.tail.prev` (current MRU) and `self.tail` (sentinel). Four pointer updates in the correct order: set node's pointers first, then update neighbors.
- `del self.cache[lru_node.key]` — this is why Node stores `key`: to find and delete the dict entry when evicting. If Node did not store `key`, you could not remove the dict entry in O(1).
- Sentinel nodes — `_remove` and `_add_to_tail` never need null checks because sentinel head and tail always provide valid prev/next pointers. The list is never truly empty (always has at least head <-> tail).

**Your raw DLL implementation (write it out here):**

[blank — write the full implementation without looking at the model]

---

## Part 5 — System Reasoning

*Answer these in writing. These are the questions Google interviewers use to probe whether you understand your own design.*

**Q1: Why doubly-linked list and not singly-linked?**
[blank — your answer]

*Model answer:* To remove a node from the middle of the list in O(1), you need to update both the predecessor's `next` and the successor's `prev`. A singly-linked list only gives you the next pointer — finding the predecessor requires O(n) traversal. Doubly-linked gives you `node.prev` in O(1), enabling O(1) removal from any position.

**Q2: Why sentinel head and tail instead of None-checked real head and tail?**
[blank — your answer]

*Model answer:* Sentinels eliminate all edge case branches. Without sentinels, `_add_to_tail` must check "is the list empty?" and `_remove` must check "is this the first or last node?" These checks are easy to get wrong. With sentinels, the list is never structurally empty — head.next is always valid, tail.prev is always valid. Every operation has the same four-pointer-update structure regardless of list size.

**Q3: Why does the hash map store Node pointers (not just values)?**
[blank — your answer]

*Model answer:* The O(1) remove requirement means when we call `get(key)`, we need to jump directly to the node's position in the doubly-linked list and unlink it — without scanning. The hash map gives us O(1) key lookup, and storing the Node pointer means we immediately have `node.prev` and `node.next`. If we stored only the value, we'd have to scan the list to find the node to remove, giving O(n) remove.

**Q4: What is the time and space complexity of the raw DLL implementation?**
[blank — your answer]

*Model answer:* Time: O(1) for both `get` and `put`. Each operation calls `_remove` (4 pointer updates = O(1)) and `_add_to_tail` (4 pointer updates = O(1)) plus one dict lookup/insert/delete (O(1) amortized). Space: O(capacity) — the dict and the linked list each hold at most `capacity` entries.

**Q5: How does LRU generalize to LFU (Least Frequently Used)?**
[blank — your answer]

*Model answer:* LFU evicts the entry with the lowest access frequency (not the least recently accessed). LFU requires tracking frequency per key AND within the same frequency bucket, still evicting the LRU entry. The standard O(1) LFU implementation uses: (1) a dict key→(value, freq), (2) a dict freq→OrderedDict of keys at that freq, (3) a `min_freq` integer. On access, key's freq is incremented, moved between freq buckets. More complex state than LRU but same principle of hash-map-backed ordered structure.

---

## Part 6 — Curveballs

### Curveball 1 — Thread Safety

**Interviewer:** "Make it thread-safe. What's the simplest correct approach?"

**Your answer:** [blank]

*Model answer:* Wrap the entire `get` and `put` with a `threading.Lock()`. Acquire the lock at the top of each method and release at the bottom (use `with self.lock:`). This is the simplest correct approach — a coarse-grained mutex. In Python with the GIL, this may be redundant for some use cases, but it is semantically correct and safe.

A more performant approach for high-concurrency systems: reader-writer lock (allows concurrent reads, exclusive writes). But in an interview, "threading.Lock() as a with-statement" is the correct baseline. Show you know the construct.

```python
import threading

class LRUCache:
    def __init__(self, capacity: int):
        # ... existing init ...
        self.lock = threading.Lock()
    
    def get(self, key: int) -> int:
        with self.lock:
            # ... existing get logic ...
    
    def put(self, key: int, value: int) -> None:
        with self.lock:
            # ... existing put logic ...
```

---

### Curveball 2 — LFU Cache

**Interviewer:** "Now design an LFU (Least Frequently Used) cache. How does your design change?"

**Your answer:** [blank]

*Model answer:* LFU evicts the key with the lowest use count. Ties broken by LRU within the same frequency. The design requires three structures instead of two:
1. `key_map: dict[key -> (value, freq)]` — O(1) value and frequency lookup.
2. `freq_map: dict[freq -> OrderedDict of keys]` — O(1) access to all keys at a given frequency, in LRU order within that frequency.
3. `min_freq: int` — tracks the current minimum frequency so eviction is O(1).

On `get(key)`: look up value, increment freq, move key from `freq_map[f]` to `freq_map[f+1]`, update `min_freq` if needed.
On `put(key, value)`: same as get for existing keys, plus eviction: if over capacity, pop the LRU key from `freq_map[min_freq]`.

---

### Curveball 3 — Production Scale

**Interviewer:** "In production, keys are strings not integers, values can be any object, and there are 10 million entries. What changes?"

**Your answer:** [blank]

*Model answer:*
- **Type generics:** Make the class generic: `LRUCache[K, V]` with type hints. The algorithm is unchanged.
- **10M entries:** Memory is the concern. Each entry uses ~200-400 bytes (Node object + dict entry + overhead). 10M entries = 2-4 GB. You may need to shard across multiple cache instances or machines.
- **Serialization:** Values as "any object" means you cannot assume they are hashable or picklable. If you need to persist or distribute the cache, you must add a serialization layer.
- **Distributed LRU:** A single-process LRU does not scale horizontally. For distributed LRU: use Redis with LRU eviction policy (maxmemory-policy allkeys-lru). The algorithm is the same; the implementation moves off-process.
- **Monitoring:** Track hit rate, eviction rate, p99 get/put latency. A declining hit rate signals the capacity is too small.

---

## Part 7 — SWE Rubric

*Self-grade after completing the lab. Score yourself as an interviewer would — not as someone who knows what you were trying to do.*

| Dimension | 5 — Strong | 3 — Adequate | 1 — Weak | Your Score |
|---|---|---|---|---|
| Communication / think-aloud | Clarified before designing, named both data structures with rationale before coding, narrated every pointer update in _remove and _add_to_tail | Coded with some narration, but the data structure choice was not explained aloud | Coded silently; interviewer cannot tell why doubly-linked list was chosen | __ /5 |
| Design / modeling | Named hash map + doubly-linked list from Part 2 and explained O(1) remove requires doubly-linked; explained sentinel pattern | Chose correct structures but could not explain why singly-linked is insufficient | Used OrderedDict without understanding it; could not build the DLL version | __ /5 |
| Correctness (M4a) | OrderedDict version passes all 5 test cases including capacity-0 and update-existing | Passes 3-4 cases; misses either update-existing or capacity-0 | Fails basic get/put/evict flow | __ /5 |
| Correctness (M4b) | Raw DLL version passes all 5 test cases; _remove and _add_to_tail are both correct with 4 pointer updates each | DLL version passes 3-4 cases; one pointer direction missing in _remove or _add_to_tail | DLL version does not run or has logical errors in pointer updates | __ /5 |
| System reasoning | Answered all 5 Part 5 questions correctly without looking at model answers; articulated LFU generalization | Answered 3-4 questions; one major blank (e.g., why store key in Node) | Could not explain the sentinel pattern or why dict stores Nodes | __ /5 |
| Curveballs | Handled all 3 curveballs with specific answers; used threading.Lock correctly; described LFU's three data structures | Handled 1-2 curveballs; generic or incomplete answers | Could not reason about thread safety or LFU design | __ /5 |
| Time management | Completed M4a and M4b and reached Part 5 within 45 minutes | Completed M4a but ran out of time before finishing M4b | Did not finish M4a within time | __ /5 |

**Total: __ / 35**

---

## You're Ready When...

- You implement the raw DLL version (Part 4b) from scratch in under 20 minutes without looking at any hints
- You trace Test 1 correctly on paper — following the pointer updates — without running code
- You answer Curveball 1 (thread safety) and Curveball 2 (LFU) without freezing
- You self-grade ≥ 28/35 on two separate attempts

**Next lab:** [→ Lab 02: Rate Limiter — Sliding Window Design](../lab_02_graph_grid/workbook.md)

---

*Google SWE Lab 01 · Tier 1 (Worked) · Design-a-Data-Structure · v2.0*
