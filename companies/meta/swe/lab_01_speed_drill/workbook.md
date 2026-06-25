Status: Ready — work through all parts in order

# Meta SWE Lab 01 — Two-Medium Speed Drill

**Role:** SWE | **Tier:** 2 | **Est. time:** 45 min | **Difficulty:** Medium

---

## Scenario

You're on a Meta phone screen. The clock starts the moment the interviewer says "go." You have 45 minutes. There are two medium LeetCode problems. Problem 1: Given a string `s`, find the length of the longest substring without repeating characters. Problem 2: Given the head of a linked list, detect if it has a cycle and return the node where the cycle begins. The interviewer expects you to finish both. You must manage your own time — no one will tell you to move on.

---

## Milestones

- [ ] M1 · Scoped — both problems read, clarifications for each noted (< 2 min total)
- [ ] M2 · Approached — brute force and optimized approach named for each problem
- [ ] M3 · Coded — both solutions written
- [ ] M4 · Tested — walked 2 test cases per problem aloud
- [ ] M5 · Timed — total time logged; was it under 35 minutes of coding time?
- [ ] M6 · Ready — self-graded ≥ 28/35 (or ≥ 34/40 with speed row)

---

## Part 0: Forethought

**Goal:** Finish both problems correctly in < 35 minutes of coding time, leaving 10 minutes for walk-through and follow-ups.

**Target time:** 45 min total (35 coding + 10 review/explanation)

**Time split strategy:** P1 target = 15 min. P2 target = 20 min. Buffer = 10 min. If P1 hits 18 min, start P2 immediately — return to polish P1 at the end.

**Confidence (1–5):** ___

**What do I need to watch out for?**

___

---

## Part 1: Clarifying Questions

Keep these fast. Your goal is < 2 minutes total for both problems. State the question, then state your assumption. Don't wait for the interviewer to confirm — just say "I'll assume X unless you tell me otherwise."

### Problem 1 — Longest Substring Without Repeating Characters

**Category: Goal**
Question: Should I return the length of the substring, or the substring itself?
Assumption: I'll return the integer length. If you need the actual string, the approach is the same — I just track indices.

<details>
<summary>Hint</summary>
LeetCode 3 asks for length. In Meta screens they usually match. But asking signals you read carefully.
</details>

**Category: Users / Input**
Question: Does the substring have to be contiguous? Or is it any subsequence of non-repeating chars?
Assumption: Contiguous substring — the classic sliding window problem. A subsequence would require a different approach (and a higher answer).

<details>
<summary>Hint</summary>
"Substring" always means contiguous. "Subsequence" does not. Clarifying this shows you know the difference.
</details>

**Category: Data**
Question: What characters can appear? ASCII only, or Unicode?
Assumption: ASCII printable characters (128 possible). If Unicode, my hash map still works — just a larger key space.

<details>
<summary>Hint</summary>
If the interviewer says "only lowercase letters," you can use an array of size 26 instead of a hash map — O(1) guaranteed space.
</details>

**Category: Constraints**
Question: What is the length range of `s`?
Assumption: Up to 5×10^4 characters. My O(n) sliding window is fine.

<details>
<summary>Hint</summary>
If s can be 10^6 or longer, you'd want the same O(n) — no issue. If s can be empty, your return value should be 0 (not an error).
</details>

**Category: Scale**
Question: Is this called once per request or in a tight loop over millions of strings?
Assumption: One-shot call. If called in a loop, I'd pre-compile character lookup. Same algorithm, different constant factors.

<details>
<summary>Hint</summary>
Asking about call frequency shows systems awareness even in an algorithmic round. One sentence is enough — don't dwell.
</details>

---

### Problem 2 — Linked List Cycle Start

**Category: Goal**
Question: Do you want the node object where the cycle begins, or its value, or its index?
Assumption: Return the node object (ListNode). Return None if there is no cycle.

<details>
<summary>Hint</summary>
LeetCode 142 returns the node. Clarifying "None vs. special sentinel vs. -1" takes 5 seconds and prevents a wrong return type.
</details>

**Category: Users / Input**
Question: Is the entire list a cycle (tail points to head), or can the cycle start mid-list?
Assumption: The cycle can start anywhere — mid-list or at the head. My algorithm handles both.

<details>
<summary>Hint</summary>
Floyd's algorithm works regardless of where the cycle starts. This clarification mostly shows you've thought about the edge case.
</details>

**Category: Data**
Question: Can the list have duplicate values? Could two different nodes have the same val?
Assumption: Yes, duplicate values are possible. I compare nodes by reference (object identity), not by value.

<details>
<summary>Hint</summary>
This is a critical distinction. Returning a node with val == 2 is wrong if there are two nodes with val 2. Always return the node object.
</details>

**Category: Constraints**
Question: What is the size of the list?
Assumption: Up to 10^4 nodes. O(n) time and O(1) space (Floyd's) is well within limits.

<details>
<summary>Hint</summary>
If the interviewer says "up to 10^8 nodes," O(n) is still fine. O(1) space becomes more important at scale.
</details>

**Category: Scale**
Question: Do I need to handle a null/None head?
Assumption: Yes — if head is None or head.next is None, there can be no cycle. Return None immediately.

<details>
<summary>Hint</summary>
This is the first edge case to code. It's also the one candidates forget most often. State it aloud before you start coding.
</details>

---

## Checkpoint M1 — Scoped

Mark M1 complete when: you have stated an assumption for every category above, and you have written them in your scratch space. Time check: < 2 minutes elapsed since you read the problems.

---

## Part 2: Approach Planning

Fill in the blanks before looking at Part 3.

### Problem 1 — Approach

**Brute force:**
Try every possible substring starting at index i, ending at j. Check if all characters are unique (use a set). Track the maximum length seen.
Time complexity: O(___) — why? ___
Space complexity: O(___)

**Optimized — Sliding Window:**
Maintain a window [left, right]. Expand right one character at a time. When `s[right]` is already in the window, shrink from the left until it's not. Track max window size.

Key insight: ___

Time complexity: O(___) time, O(___) space

**What state do I need to track?**
- `left`: left boundary of window
- `char_index`: maps each character → its last seen index (so we can jump `left` directly)
- `max_len`: answer so far

**Window shrink strategy — two options:**
Option A: Move `left` one step at a time until the duplicate is gone.
Option B: Jump `left` directly to `char_index[s[right]] + 1`.
Which is faster? ___ Why? ___

<details>
<summary>Hint: window shrink</summary>
Option B is better — O(1) jump per step vs. O(n) crawl in the worst case. But: you must guard with `max(left, char_index[s[right]] + 1)` because the stored index might be before your current left boundary (character was seen but is no longer in the window).
</details>

---

### Problem 2 — Approach

**Brute force — Hash Set:**
Traverse the list. At each node, check if it's already in a visited set. If yes → cycle start. If we reach None → no cycle.
Time: O(n), Space: O(n)

**Optimized — Floyd's Cycle Detection:**

**Phase 1 (detect):** Use a slow pointer (moves 1 step) and a fast pointer (moves 2 steps). If they meet, there is a cycle.

**Phase 2 (find start):** After Phase 1, reset one pointer to ___ and keep the other at ___. Move both one step at a time. Where they meet = cycle start.

Why does Phase 2 work? ___

<details>
<summary>Hint: Phase 2 math</summary>
Let F = distance from head to cycle start. Let C = cycle length. Let h = distance from meeting point back to cycle start (inside cycle). After Phase 1 meeting: slow has traveled F + h steps. Fast has traveled 2(F + h) steps. The extra distance fast traveled is a multiple of C: 2(F+h) - (F+h) = F+h = kC for some k. So F = kC - h, meaning if you walk F steps from head AND kC - h steps from meeting point, you arrive at the cycle start simultaneously. Setting one pointer to head and walking both at speed 1 makes them meet exactly at the cycle start.
</details>

**Edge cases to name aloud:**
- head is None → ___
- No cycle → ___
- Cycle starts at head (pos 0) → ___

---

## Checkpoint M2 — Approached

Mark M2 complete when: you can name the time/space complexity of both optimized solutions, and you can explain Phase 2 of Floyd's without notes.

---

## Part 3: Code

Write your solutions below (or in your IDE). The starters have TODOs — fill them in.

### Problem 1: Longest Substring Without Repeating Characters

```python
def length_of_longest_substring(s: str) -> int:
    # TODO: initialize your window state
    # char_index maps character -> its most recent index
    # [blank]

    left = 0
    max_len = 0

    for right in range(len(s)):
        # TODO: if s[right] is already in the window (its last seen index >= left),
        # jump left to just past that index
        # [blank]

        # TODO: record the current index of s[right]
        # [blank]

        # TODO: update max_len with the current window size
        # [blank]

    return max_len
```

**Completed solution (write yours first, then check):**

```python
def length_of_longest_substring(s: str) -> int:
    char_index = {}   # char -> last seen index
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)

    return max_len
```

**Why `char_index[s[right]] >= left`?**
___

---

### Problem 2: Linked List Cycle Start

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_cycle(head: ListNode) -> ListNode:
    # Edge case: handle empty list or single node
    # [blank]

    # Phase 1: TODO — detect cycle with fast/slow pointers
    # Initialize slow and fast
    # [blank]

    # Move until they meet or fast reaches None
    # [blank]

    # If no cycle found, return None
    # [blank]

    # Phase 2: TODO — find the start of the cycle
    # Reset one pointer to head, keep other at meeting point
    # [blank]

    # Move both one step at a time until they meet
    # [blank]

    # Return the meeting node (= cycle start)
    # [blank]
```

**Completed solution (write yours first, then check):**

```python
def detect_cycle(head: ListNode) -> ListNode:
    if not head or not head.next:
        return None

    slow, fast = head, head

    # Phase 1: detect
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None  # fast reached end → no cycle

    # Phase 2: find start
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow
```

**Note the `else` on the `while` loop.** In Python, the `else` clause of a `while` runs when the condition becomes False (i.e., `fast` or `fast.next` is None — no cycle). This is idiomatic and clean. Know it.

---

## Checkpoint M3 — Coded

Mark M3 complete when: both functions are written and you have NOT run them yet. Do Part 4 (test cases) mentally before executing.

---

## Part 4: Test Cases

Walk through these aloud on your scratch space. Do not rely on running the code.

### Problem 1 Test Cases

| Input | Expected | Your trace |
|---|---|---|
| `""` | `0` | ___ |
| `"bbbbb"` | `1` | ___ |
| `"abcabcbb"` | `3` | ___ |
| `"pwwkew"` | `3` | ___ |
| `"abcde"` | `5` | ___ |
| `" "` (space) | `1` | ___ |

**Trace `"abcabcbb"` step by step:**

| right | s[right] | left before | char_index update | window | max_len |
|---|---|---|---|---|---|
| 0 | a | 0 | a→0 | [0,0] = 1 | 1 |
| 1 | b | 0 | b→1 | [0,1] = 2 | 2 |
| 2 | c | 0 | c→2 | [0,2] = 3 | 3 |
| 3 | a | 0→1 | a→3 | [1,3] = 3 | 3 |
| 4 | b | 1→2 | b→4 | [2,4] = 3 | 3 |
| 5 | c | 2→3 | c→5 | [3,5] = 3 | 3 |
| 6 | b | 3→5 | b→6 | [5,6] = 2 | 3 |
| 7 | b | 5→7 | b→7 | [7,7] = 1 | 3 |

Return: 3. Correct.

### Problem 2 Test Cases

| Input | Expected |
|---|---|
| [3,2,0,-4], cycle at pos 1 | Node with val=2 |
| [1,2], cycle at pos 0 | Node with val=1 |
| [1], no cycle | None |
| [], no cycle | None |

**Trace [3→2→0→-4→(back to 2)] manually:**
- slow: 3→2, fast: 3→0
- slow: 2→0, fast: -4→0 ... (continue until slow is fast)
- Phase 2: slow reset to head (3), fast stays at meeting point. Both move 1 step at a time → they meet at node 2.

---

## Checkpoint M4 — Tested

Mark M4 complete when: you have traced at least 2 test cases per problem on paper and found any bugs before running.

---

## Part 5: Reasoning — Speed-Focused WHY Questions

Answer each. These are the follow-up questions you will get in the real interview.

**1. Why sliding window for P1 and not brute force?**
___

**2. Why Floyd's for P2 and not a hash set (which is also O(n))?**
___

**3. What is the exact time and space complexity of each solution?**
P1: Time ___, Space ___
P2: Time ___, Space ___

**4. What edge cases almost tripped you?**
___

**5. In P1, why do you need `char_index[s[right]] >= left` and not just `s[right] in char_index`?**
___

**6. In P2 Phase 2, why does resetting to head and stepping both pointers at speed=1 work?**
___

**7. If the string in P1 is all unique characters, what happens? Trace through.**
___

**8. What if the cycle in P2 is the entire list (tail points to head)?**
___

**9. Can you solve P1 in O(n) with O(1) space if input is only lowercase letters?**
___

**10. What's the tradeoff between Option A (crawl left) and Option B (jump left) in the sliding window?**
___

---

## Part 6: Interview Simulation

### 90-Second Talk Track (memorize this structure, not the words)

"I'll start by making sure I understand both problems before I code anything. [5 sec clarifications per problem.] My plan: P1 with a sliding window using a hash map — O(n) time, O(min(n, alphabet)) space. P2 with Floyd's cycle detection — O(n) time, O(1) space. I'll time-box P1 to 15 minutes. Starting now."

[Narrate while coding:] "Initializing char_index as a dict and left as 0... Right pointer sweeps from 0 to n-1... When I see a repeated char I jump left... Updating max_len each step... Done. Let me trace 'abcabcbb'..."

[Transition:] "P2: first I check for None head. Phase 1: slow and fast pointers... when they meet, cycle exists... Phase 2: reset slow to head, move both at speed 1... they meet at cycle start. Done."

### Curveballs

**Curveball 1:** "Now do longest substring with AT MOST k distinct characters."

What changes? How does your sliding window adapt? You have 90 seconds.

Instructions: Answer aloud without looking at code. Hint if stuck:

<details>
<summary>Hint</summary>
Same sliding window, but now the invariant is "at most k distinct chars in window." When you exceed k distinct chars, shrink from the left. Track character counts (not just last-seen index) so you know when a character's count hits 0 and you can remove it from your distinct-char set.
</details>

___

**Curveball 2:** "For the linked list — what if it's doubly linked? Does Floyd's still work?"

Instructions: Think before answering. Trick question embedded here.

<details>
<summary>Hint</summary>
Floyd's works on the forward traversal — it doesn't use `.prev` at all. So yes, it still works. But: in a doubly linked list, you could also detect cycles by checking if `node.prev.next is node` ever fails. Different approach, same O(n) outcome. The question is testing whether you understand *why* Floyd's works (forward pointers only) vs. memorizing it.
</details>

___

**Curveball 3:** "Your P1 solution is O(n) — can you do it O(n) but with O(1) space?"

Instructions: This is a trick. Think carefully.

<details>
<summary>Hint</summary>
If the input is only lowercase letters (26 chars), you can use an array of size 26 instead of a hash map — still O(1) space technically (bounded constant). If the input is full ASCII (128 chars), same trick with size-128 array. If it's arbitrary Unicode, you cannot achieve O(1) space with a hash map approach. The "O(1) space" answer only works when alphabet size is bounded and constant. Say this aloud.
</details>

___

---

## Part 7: Self-Grade + Reflection

### SWE Rubric

| Dimension | 1 | 2 | 3 | 4 | 5 | Score |
|---|---|---|---|---|---|---|
| **Communication / think-aloud** | Silent | Occasional narration | Explains steps when asked | Consistent narration | Leads interviewer through thinking, zero dead air | ___ |
| **Problem solving** | Stuck, needed hints | Brute force only | Got optimized with nudge | Got optimized independently | Identified multiple approaches, chose best with justification | ___ |
| **Correctness** | Solution wrong | One solution correct | Both correct with bugs | Both correct, minor issues | Both correct, handles all edge cases | ___ |
| **Code quality** | Unreadable | Functional but messy | Readable, some issues | Clean, well-named, good structure | Production-quality: clean, consistent, no redundancy | ___ |
| **Testing & edge cases** | No testing | Tested happy path only | Tested 1-2 edge cases | Tested systematically | Predicted failure modes before coding; tested all boundary cases | ___ |
| **Debugging** | Could not debug | Found bugs with heavy hints | Found bugs with nudge | Found bugs independently | Caught own bugs during tracing; explained root cause | ___ |
| **Time management** | Never finished P1 | Finished P1 only | Finished both, rushed | Finished both with time to explain | Finished both in < 35 min, explained clearly, handled follow-up | ___ |

**Meta-Specific Row**

| Dimension | 1 | 2 | 3 | 4 | 5 | Score |
|---|---|---|---|---|---|---|
| **Speed / Time efficiency** | Only P1 complete | P1 + P2 partial (< 50%) | Both done, > 45 min | Both done in 35–45 min | Both done in < 35 min with time for curveball | ___ |

**Total: ___ / 40**

### Reflection

What went well?

___

What would you do differently?

___

Which curveball surprised you most?

___

### Ready-When Checklist

- [ ] I can solve P1 from scratch in < 15 minutes with clean code
- [ ] I can solve P2 from scratch in < 20 minutes with clean code
- [ ] I can explain Floyd's Phase 2 math without notes
- [ ] I can handle the k-distinct-chars variant without thinking
- [ ] My code compiles and passes all listed test cases on first run
- [ ] I narrated the entire session aloud as if the interviewer were present
