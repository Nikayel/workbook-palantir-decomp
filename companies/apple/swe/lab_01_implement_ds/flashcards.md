# Flashcards — Lab 01 Implement-a-Data-Structure

**Company:** Apple | **Lab:** 01 | **Style:** Implement MinStack with O(1) auxiliary tracking

---

## Card 1: Min-Stack Auxiliary Invariant

**Q:** What invariant does the auxiliary min_stack maintain at every position?

**A:** At index `i`, `min_stack[i]` equals the minimum of all values in `stack[0..i]` (inclusive). This means `min_stack[-1]` always equals the current minimum of the entire stack. When we pop position `i`, we simultaneously pop the minimum record for that position, and `min_stack[-1]` automatically becomes the minimum of the remaining elements — no scanning needed.

---

## Card 2: Why the Parallel Stack Works

**Q:** Why does popping from both stacks simultaneously preserve the min-stack invariant?

**A:** Because the invariant is indexed by stack depth. When stack has depth 3, min_stack has depth 3, and min_stack[2] = min of stack[0..2]. When we pop one element, both stacks shrink to depth 2, and min_stack[1] = min of stack[0..1] — which was already correct when it was written during push. The invariant self-heals because it was correctly established at push time.

---

## Card 3: Space vs Time Tradeoff in getMin()

**Q:** MinStack uses O(n) extra space. Is that worth it? When might it NOT be worth it?

**A:** Worth it when getMin() is called frequently (every pop, every display update, in a tight loop). The O(n) space cost is paid once; the O(1) time savings compound.

NOT worth it when: the stack has millions of entries and getMin() is called rarely. In that case, you might prefer O(n) scan at query time and save the 2x memory. At Apple, the right answer is: measure first, optimize where the profiler says to.

---

## Card 4: MonotonicStack Use Cases

**Q:** Name 3 algorithm problems where a MonotonicStack is the key insight.

**A:**
1. **Next Greater Element:** For each element, find the next element to its right that is larger. Push to a decreasing monotonic stack; when you find an element larger than the top, the top's answer is the current element.
2. **Stock Span Problem:** How many consecutive days before today had a price <= today's price? Use a decreasing monotonic stack of prices.
3. **Largest Rectangle in Histogram:** For each bar, find how far left and right it can extend. Use monotonic stacks to precompute left-boundary and right-boundary in O(n).

Pattern: monotonic stacks solve "next/previous greater/smaller" queries in O(n) total time.

---

## Card 5: Apple DRI Communication Principle

**Q:** What is the DRI principle at Apple and how does it affect how you explain technical work?

**A:** DRI = Directly Responsible Individual. At Apple, every decision has exactly one named owner — not "the team." In interviews and in explanations:
- Say "I decided X because..." not "we decided X"
- When explaining a system, name who owns each part
- When explaining a data structure to a junior dev, be the DRI of the explanation: own it, don't hedge with "I think maybe"

The MinStack explanation curveball tests DRI communication: can you explain a non-trivial invariant with confidence and clarity to someone more junior?

---

## Card 6: Why Apple Cares About Domain Depth Over LeetCode Grinding

**Q:** Why does Apple weight domain knowledge (ARC, pointers, the team's specific stack) over LeetCode performance?

**A:** Apple's products ship to hundreds of millions of devices. A memory leak in an iOS app is a real user experience failure. An off-by-one in a memory allocator is a kernel panic. Apple interviewers hire for "can this person contribute to our codebase on week 3" — which requires knowing how their specific tools work, not just being able to reverse a linked list. A candidate who understands ARC retain cycles is immediately useful on an iOS team; a LeetCode grind expert who can't explain `[weak self]` is not.

---

## Card 7: ARC Basics — Why Swift Needs Weak References

**Q:** What is ARC and why does Swift need `weak` references at all?

**A:** ARC = Automatic Reference Counting. Swift tracks how many strong references point to each object. When the count hits 0, the object is deallocated. Problem: if object A holds a strong reference to B, and B holds a strong reference to A, neither count ever reaches 0. Both leak forever — a retain cycle. Solution: one side of the cycle uses `weak var` (or `unowned`) which doesn't increment the reference count. When the other object is deallocated, the weak reference automatically becomes `nil`.

---

## Card 8: "Implement from Scratch" Discipline

**Q:** Apple asks you to implement a min-stack. You know Python has heapq. What do you do?

**A:** You implement it from scratch using a plain list and an auxiliary stack. `heapq` does not give O(1) getMin unless you use it correctly AND it doesn't integrate with push/pop the way the question asks. More importantly: Apple is testing whether you can reason about and implement a data structure, not whether you know a library. Using `heapq` or `SortedList` signals you're avoiding the design question. Implement it yourself. Name the invariant. Show the reasoning.

---

## Card 9: Apple Craft Culture — Attention to Detail

**Q:** What behaviors signal "craft" in an Apple technical interview?

**A:**
- Asking about edge cases before coding (empty stack, same value pushed twice, overflow)
- Naming the invariant before implementing it (shows you understand, not just code)
- Handling `None`/`nil` gracefully and consistently
- Explaining the space-time tradeoff without being asked
- Noticing that `<=` vs `<` matters in the optimized min-stack
- Explaining implementation to a junior dev clearly (DRI communication)

What signals low craft: silent coding, skipping edge cases, using library shortcuts without acknowledging you're doing so, vague explanations.

---

## Card 10: When Pop of Empty Stack = Crash vs None (Defensive Programming Choice)

**Q:** Your MinStack.pop() is called on an empty stack. Should it raise an exception or return silently?

**A:** Both are defensible — the key is to state your choice and be consistent.

- **Raise `IndexError`:** Follows "fail fast" philosophy. Caller knows immediately if they have a logic error. Preferred when calling code should know not to pop empty stacks (and a pop on empty is a programming error, not a recoverable state).

- **Return silently (no-op):** Defensive programming. Safer for APIs where callers may not check. Preferred when the stack is used in concurrent contexts where timing makes "empty" ambiguous.

For Apple interview: state your choice upfront, be consistent across all methods (`top()`, `getMin()`), and make sure the caller can detect the empty state (return `None` or raise, consistently).
