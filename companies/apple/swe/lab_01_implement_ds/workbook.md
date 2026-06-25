# Lab 01 — Implement a Data Structure: MinStack

**Company:** Apple
**Role:** SWE
**Style:** Implement-a-data-structure / design-a-primitive (Apple's practical approach)
**Tier:** 1
**Estimated time:** 40 minutes
**Status: Ready — work through all parts in order**

---

## Milestones

- [ ] M1 · Clarified — asked about: thread safety, integer-only or generic, behavior on pop of empty stack
- [ ] M2 · Designed — named the auxiliary stack data structure and its invariant BEFORE writing code
- [ ] M3 · Coded Part A — MinStack with push/pop/top/getMin() all O(1)
- [ ] M4 · Extended — getMax() added without breaking existing O(1) complexity for any operation
- [ ] M5 · Edge-case tested — empty stack pop, single element, pushing the same value twice in a row
- [ ] M6 · Ready — self-graded >= 28/35

---

## Scenario

"You're in an Apple technical screen. The interviewer says:

'Implement a min-stack: a stack that supports push, pop, top, and getMin() in O(1) time. Then extend it: add a getMax() operation without changing the O(1) complexity of existing operations.'

Language: Python or Swift — pick the one you're comfortable with. You have 40 minutes."

**What this tests:** Whether you can implement a non-trivial data structure from scratch, reason about invariants, handle extension cleanly, and communicate your design before coding. Apple cares about "implement from scratch" discipline — not `import heapq`.

---

## Part 0: Forethought (5 min — before designing)

"A stack that gets min in O(1) — what's the naive approach and why is it wrong?"
```
[blank — hint: you could scan all elements, but what's the cost?]
```

"What information would you need to store to answer getMin() without scanning?"
```
[blank — think about: at each state of the stack, what is the minimum?]
```

"What does 'push the same value twice' mean for a min-stack?"
```
[blank — e.g., push(3), push(3): after first pop, is 3 still the min?]
```

---

## Part 1: Clarifying Questions

Simulate asking these before writing code. State your assumption for each:

| Question | Your assumption for this exercise |
|---|---|
| Thread safety required? | [blank — assume single-threaded unless told otherwise] |
| Integer-only or generic? | [blank — integers for now; generic is a follow-up] |
| Behavior on pop of empty stack? | [blank — return None or raise? State your choice] |
| What if min/max called on empty stack? | [blank — return None or raise?] |
| Memory constraint? | [blank — no constraint, but be aware of 2x space] |

---

## Part 2: Design Before Coding

**Name your approach and its invariant:**

The key insight is:
```
[blank — describe the auxiliary stack approach in one sentence before looking at the solution]
```

**Invariant of the auxiliary min_stack:**
```
[blank — "At position i, min_stack[i] always equals..."]
```

**Draw the state after: push(5), push(3), push(7), push(2)**

| main stack | min_stack | max_stack |
|---|---|---|
| [blank] | [blank] | [blank] |

**After pop() once:**

| main stack | min_stack | max_stack |
|---|---|---|
| [blank] | [blank] | [blank] |

---

## Part 3A: Implement MinStack (Core — Part A)

Study the annotated solution. Then close it and implement it from memory.

**Annotated Solution (read this, then close it):**

```python
class MinStack:
    """
    KEY INSIGHT: maintain a separate 'min_stack' that at each position stores
    the minimum value in the main stack up to and including that position.

    When we push(val):
      - Push val onto main stack
      - Push min(val, min_stack[-1]) onto min_stack
        (if min_stack is empty, push val)

    When we pop():
      - Pop from BOTH stacks simultaneously
      - This maintains the invariant: min_stack[i] = min(stack[0..i])

    Why this works: min_stack[-1] always equals the current minimum of the
    entire stack, because when we pop an element, we also pop its corresponding
    minimum record. The minimum "rewinds" to whatever it was before that push.

    Space cost: O(n) additional space — doubles memory usage.
    Worth it? Yes. getMin() goes from O(n) to O(1). At Apple scale, O(n)
    on every getMin() call in a hot path is unacceptable.
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []  # parallel: min_stack[i] = min of stack[0..i]

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        # Choice: silently do nothing on empty stack
        # Alternative: raise IndexError("pop from empty MinStack")
        # Your choice — but state it

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
```

**Now implement it from memory (close the above):**

```python
class MinStack:
    def __init__(self):
        # [blank]
    
    def push(self, val: int) -> None:
        # [blank]
    
    def pop(self) -> None:
        # [blank]
    
    def top(self) -> int:
        # [blank]
    
    def getMin(self) -> int:
        # [blank]
```

---

## Part 3B: Edge Case Verification

Trace through each manually before testing:

**Case 1: Empty stack operations**
```
stack = MinStack()
result = stack.getMin()  # expect: [blank]
result = stack.top()     # expect: [blank]
stack.pop()              # expect: [blank — crash? silent? your choice]
```

**Case 2: Push same value twice**
```
stack = MinStack()
stack.push(3)
stack.push(3)
# getMin() = [blank]
stack.pop()
# getMin() after pop = [blank — should still be 3, not None]
```

**Case 3: Min is at the bottom**
```
stack = MinStack()
stack.push(1)   # min = 1
stack.push(5)   # min = 1
stack.push(10)  # min = 1
stack.pop()     # min = [blank]
stack.pop()     # min = [blank]
stack.pop()     # min = [blank — now empty]
```

---

## Part 4: Extend to getMax()

"Now add getMax() without changing the O(1) complexity of ANY existing operation."

**Design change (name it before coding):**
```
[blank — you need a parallel max_stack with the same invariant as min_stack]
```

**Invariant of max_stack:**
```
[blank — "At position i, max_stack[i] always equals..."]
```

**Implement MinMaxStack from scratch:**

```python
class MinMaxStack:
    """MinStack extended with O(1) getMax()."""
    
    def __init__(self):
        # [blank]
    
    def push(self, val: int) -> None:
        # [blank]
    
    def pop(self) -> None:
        # [blank]
    
    def top(self) -> int:
        # [blank]
    
    def getMin(self) -> int:
        # [blank]
    
    def getMax(self) -> int:
        # [blank]
```

---

## Part 5: Design Reasoning

**Why does the auxiliary stack approach work? (State the invariant formally)**
```
[blank — "The invariant is: for all i, min_stack[i] = min(stack[0], stack[1], ..., stack[i]).
When we pop position i, we pop the invariant for that position, restoring the invariant
for position i-1 automatically."]
```

**What's the space cost? Is it worth it?**
```
[blank — O(n) extra. Justify the tradeoff: O(n) space vs O(n) time on every getMin() call]
```

**If you used a single tuple (val, current_min) per stack entry instead of two stacks, would the complexity change?**
```
[blank — No: same information, different layout. Space O(n), time O(1). Which is more readable?]
```

**How would you implement this in Swift? What language features would you use?**
```swift
// Sketch your Swift implementation here:
// [blank — think: struct vs class, value vs reference semantics, Array<Int>]
```

---

## Part 6: Curveballs

**Curveball 1: MonotonicStack**
"Now implement a MonotonicStack — a stack where elements are always in decreasing order. If you push an element larger than the top, you pop until the order is restored. What algorithm problem does this solve?"

```python
class MonotonicStack:
    """
    Maintains decreasing order.
    Use case: [blank — hint: "next greater element" problem]
    """
    def __init__(self):
        self.stack = []
    
    def push(self, val: int) -> None:
        # TODO: pop smaller elements before pushing
        # [blank]
    
    def top(self) -> int:
        # [blank]
```

What can you use a MonotonicStack for?
```
[blank — next greater element, stock span problem, largest rectangle in histogram]
```

**Curveball 2: Memory Profiler Says 2x Expected**
"Apple's memory profiler shows your MinStack is using 2x the memory expected. How do you reduce it while keeping O(1) getMin()?"

```
Approach: [blank — hint: min_stack doesn't need to store a value when the min doesn't change]
Optimization: [blank — only push to min_stack when the new value is <= current min]
Tradeoff: [blank — pop() must now check if the popped value equals min_stack[-1] before popping min_stack]
```

Write the optimized version:
```python
class OptimizedMinStack:
    """Only stores a new entry in min_stack when the min actually changes."""
    
    def __init__(self):
        self.stack = []
        self.min_stack = []  # only pushed when new val <= current min
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
    
    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
```

**Why does <= instead of < matter when pushing to min_stack?**
```
[blank — if you push the same value twice and only store it once, popping the first
occurrence would incorrectly clear the min before the second occurrence is popped]
```

**Curveball 3: Explain to a Junior Developer**
"Explain your MinStack implementation to a junior developer who doesn't know what an auxiliary stack is. (DRI communication signal — Apple values clarity of explanation)"

```
Your explanation (write it out):
[blank — practice: use an analogy or step-by-step trace]
```

---

## Part 7: Self-Assessment Rubric

Score yourself honestly. Target >= 28/35 before moving on.

| Dimension | 5 — Strong | 3 — Solid | 1 — Needs Work | Your Score |
|---|---|---|---|---|
| Clarifying questions | Asked about edge cases (empty stack, same value twice, thread safety) before coding | Asked about 1–2 | Jumped straight to code | __ /5 |
| Design before coding | Named auxiliary stack invariant before writing any code | Described it vaguely | Started coding without design | __ /5 |
| Core implementation | All 4 operations O(1), edge cases handled (empty stack) | Push/pop/getMin correct, top/edge cases wrong | O(n) getMin or incorrect logic | __ /5 |
| getMax() extension | Added correctly with parallel max_stack, O(1), no existing operations affected | getMax() works but is O(n) | Could not extend | __ /5 |
| Edge case handling | Traced all 3 edge cases correctly (empty, same value, min at bottom) | 2 of 3 correct | Did not trace edge cases | __ /5 |
| Design reasoning | Articulated invariant, space/time tradeoff, and Swift translation | Some reasoning, imprecise | Did not explain design choices | __ /5 |
| Curveball handling | Addressed MonotonicStack use case + memory optimization | One curveball | Could not handle extension | __ /5 |

**Total: __ / 35**

---

## Reflection

**What's the one sentence that describes the MinStack insight?**
```
[blank — write it from memory]
```

**What would break if you used < instead of <= when pushing to the optimized min_stack?**
```
[blank]
```

**If Apple asked you to implement a stack that tracks the MEDIAN in O(1) time, how would you approach it?**
```
[blank — this is a stretch extension: hint — two heaps, max-heap and min-heap]
```

---

## Ready-When Checklist

- [ ] I can implement MinStack from scratch in < 5 minutes without looking at notes
- [ ] I can trace the min_stack state after any sequence of push/pop operations
- [ ] I can extend to MinMaxStack cleanly and explain the invariant change
- [ ] I can explain the optimized min_stack (only push on change) and why <= matters
- [ ] I can explain the implementation to a junior dev in plain English (DRI signal)
- [ ] I scored >= 28/35

---

*Next lab: `lab_02_ios_arc` — iOS ARC memory management, retain cycles, weak references*
