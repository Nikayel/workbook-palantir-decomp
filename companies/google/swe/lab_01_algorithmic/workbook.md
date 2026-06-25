# Google SWE Lab 01 — Algorithmic Fundamentals
## Meeting Rooms (Tier 1 — Worked)

**Tier:** 1 (Worked) — ~60% pre-filled. Study the model carefully, understand every decision, then blank it and re-implement from scratch.

**Before you start:** You are about to simulate a Google phone screen. The rules of this lab:
- Write all code in a plain text area. Do NOT use an IDE, REPL, or syntax highlighter.
- Narrate out loud as you work — say your reasoning aloud as if the interviewer can hear you.
- Set a timer for 45 minutes before you open Part 1. Stop when it goes off.

---

## Milestones

Check these off as you complete each part. M4 is a hard gate — do not continue past Part 4 until it is checked.

- [ ] M1 · Clarified — asked at least 2 substantive questions before writing any code
- [ ] M2 · Approached — explained brute force first, then articulated the optimized approach before coding
- [ ] M3 · Coded — working implementation written in plain text, no IDE assistance
- [ ] M4 · Tested — walked through at least 3 test cases out loud, including at least 1 edge case **(hard gate)**
- [ ] M5 · Optimized — stated O(n log n) time, O(n) space, and named the algorithmic approach (min-heap)
- [ ] M6 · Ready — self-graded ≥ 28/35 on two separate attempts

---

## Part 0 — Forethought

**Goal:** Solve the Meeting Rooms problem correctly while narrating clearly enough to score well on GCA. The answer matters, but your process is what the interviewer is actually evaluating.

**Target time:** 45 minutes total. Suggested breakdown:
- 5 min — clarifying questions (Part 1)
- 8 min — approach and decomposition (Part 2)
- 3 min — sign the contract (Part 3)
- 15 min — code (Part 4)
- 7 min — test cases out loud (Part 4 continued, M4 gate)
- 5 min — complexity and optimization (Part 5)
- 7 min — curveballs (Part 6)

**Key reminder:** GCA is scored on PROCESS, not just the final answer. An interviewer who sees you arrive at a suboptimal solution while clearly narrating every step will score you higher than a candidate who silently produces the optimal solution. Narrate constantly.

**Confidence rating before starting (circle one):** 1 — 2 — 3 — 4 — 5

**What I want to get right this session:** [blank — write your personal goal for this attempt]

---

## Part 1 — Clarifying Questions

*Google style: always clarify before coding. The interviewer expects this. Jumping straight to code signals poor communication.*

The scenario: You're in a Google phone screen. The interviewer shares a Google Doc — no syntax highlighting, no autocomplete. They say:

> "Given a list of meeting intervals [start, end], return the minimum number of meeting rooms required."

You have 45 minutes.

**Model questions to ask (with rationale):**

**Q1: "What do the start and end values represent — are they in minutes, hours, or arbitrary integers?"**
Rationale: Clarifies the domain without over-constraining the solution. Integers are easiest to reason about.
*Assumption: Arbitrary integers. No unit conversion needed.*

**Q2: "Are endpoints inclusive or exclusive — does a meeting from [1,5] conflict with one from [5,10]?"**
Rationale: This is the most important edge case. Two meetings sharing an endpoint may or may not conflict depending on the spec. You must nail this down before coding.
*Assumption for this lab: Endpoints are exclusive — [1,5] ends before [5,10] starts, so they do NOT conflict and can share a room.*

**Q3: "Can the input be empty, or contain a single meeting?"**
Rationale: Forces you to define the base case explicitly, which you'll need in your code.
*Assumption: Yes — handle empty list (return 0) and single meeting (return 1).*

**Q4: "Can start equal end — zero-length meetings?"**
Rationale: Edge case for interval validity. Clarifying now prevents a subtle bug later.
*Assumption: start < end always. Zero-length meetings are not in scope.*

**Q5: "Should I return just the count of rooms, or also a mapping of which meeting goes in which room?"**
Rationale: Clarifies scope. The simpler version (count only) is typical for a phone screen.
*Assumption: Return the count only.*

**Checkpoint M1:** Check the box above if you asked at least 2 of these before coding.

---

## Part 2 — Decomposition

*Before writing a single line of code, explain your approach out loud. Start with brute force. Then improve.*

### Brute Force Approach

**Idea:** Sort meetings by start time. For each meeting, check if any existing room is free (i.e., its last meeting has ended). If yes, assign the meeting to that room. If no room is free, open a new room.

**How to check "is room free":** Iterate through all current rooms and look at their end times. If any room's end time is ≤ the new meeting's start time, it's free.

**Time complexity:** O(n²) — for each of n meetings, you scan up to n rooms.
**Space complexity:** O(n) — in the worst case, n rooms.

**Why this is too slow:** With n = 10,000 meetings, you do 100,000,000 comparisons. The interviewer will ask you to optimize after you explain this.

**Narration (say this out loud):** "My brute-force is to sort by start time, then for each meeting greedily assign it to the first available room by scanning all rooms. That's O(n²) because of the scan. Can I do better? Yes — instead of scanning all rooms, I should track only the earliest-ending room, because that's the only one that matters for the next assignment."

### Optimized Approach — Min-Heap

**Key insight:** You only ever need to check whether the earliest-ending room is free. You don't need to scan all rooms — just peek at the minimum end time.

**Data structure:** A min-heap (priority queue) keyed on end times. The root of the heap is always the room that frees up soonest.

**Algorithm:**
1. Sort meetings by start time.
2. Initialize an empty min-heap.
3. For each meeting [start, end]:
   - If the heap is non-empty AND the smallest end time ≤ start: the earliest room is free. Replace its end time with the new end time (heapreplace).
   - Otherwise: no room is free. Push a new end time (heappush) — this opens a new room.
4. The size of the heap at the end is the answer.

**Why sort by start?** You must process meetings in the order they arrive. If you don't sort, you might assign a room to a later meeting while an earlier meeting is still occupying it.

**What breaks if you sort by end instead?** You'd process meetings in the wrong order. A meeting that starts later but ends earlier would get processed first, potentially freeing a room that hasn't actually started yet.

**State:** rooms = min_heap of room end times
**Loop invariant:** After processing meeting i, rooms contains the end times of all rooms that are currently occupied by meetings 0..i.

**Time complexity:** O(n log n) — sort is O(n log n), each heap operation is O(log n), done n times.
**Space complexity:** O(n) — heap holds at most n end times (worst case: all meetings overlap).

**Checkpoint M2:** Check the box above if you explained both approaches before writing any code.

---

## Part 3 — Contract

*Sign this before you code. This is what you're implementing.*

**Function signature:**
```
min_meeting_rooms(intervals: List[List[int]]) -> int
```

**Input:**
- `intervals`: A list of [start, end] pairs where start and end are integers and start < end.
- Order of input is NOT guaranteed to be sorted.
- May be empty.

**Output:**
- A single integer: the minimum number of rooms needed to hold all meetings without conflicts.
- Conflicts mean two meetings overlap in time (a meeting's end time is strictly greater than the next meeting's start time, given our exclusive-endpoint assumption).

**Edge cases (from Part 1 clarifications):**
- Empty list `[]` → return `0`
- Single meeting `[[1,5]]` → return `1`
- All meetings overlapping (e.g., `[[1,10],[2,9],[3,8]]`) → return `len(intervals)` = `3`
- No overlaps (e.g., `[[1,2],[3,4],[5,6]]`) → return `1`
- Adjacent meetings sharing an endpoint (e.g., `[[1,5],[5,10]]`) → return `1` (exclusive endpoints, they don't conflict)

---

## Part 4 — Code

### Model Solution (Study This First)

*Read through the model solution carefully. Understand each line and each comment before proceeding. Then scroll down and re-implement it from scratch in the blank cell.*

```python
import heapq

def min_meeting_rooms(intervals):
    # Edge case: no meetings
    if not intervals:
        return 0
    
    # Step 1: Sort by start time so we process meetings in order
    intervals.sort(key=lambda x: x[0])
    
    # Step 2: Min-heap tracks the end times of rooms in use
    # The smallest value = the room that frees up soonest
    rooms = []
    
    for start, end in intervals:
        # Step 3: Can we reuse an existing room?
        # The heap root is the earliest-ending room.
        # If its end time <= our start, the room is free.
        if rooms and rooms[0] <= start:
            # Reuse: replace the old end time with our new end time
            # heapreplace is equivalent to heappop + heappush, but faster
            heapq.heapreplace(rooms, end)
        else:
            # No room is free — open a new one
            heapq.heappush(rooms, end)
    
    # Step 4: The number of items in the heap = rooms in use = answer
    return len(rooms)
```

**Annotations (make sure you understand each one):**

- `intervals.sort(key=lambda x: x[0])` — Sort by start time. We use key= to sort by the first element of each pair, not lexicographically.
- `rooms = []` — An empty list used as a min-heap via the heapq module.
- `rooms[0]` — The smallest element in the heap. In Python's heapq, index 0 is always the minimum.
- `heapreplace(rooms, end)` — Atomically pops the minimum and pushes `end`. Use this instead of pop+push when you know the new value is valid — it's slightly faster and cleaner.
- `heappush(rooms, end)` — Adds `end` to the heap. This represents opening a new room.
- `return len(rooms)` — The heap contains one entry per occupied room. Its size is the answer.

**What would break if we used `heappop` + `heappush` instead of `heapreplace`?**
Nothing functionally — it's equivalent but slightly slower (two heap operations instead of one). In an interview, either is fine; `heapreplace` signals you know the library.

**What would break if we forgot to sort?**
A later meeting with an earlier end time would look like it frees a room before an earlier meeting with a later end time. We'd incorrectly reuse rooms that are still occupied. This is a critical bug.

---

### Your Turn — Implement From Scratch

*Close or fold the model above. Without looking back, implement the solution yourself. Write it as if you're in a Google Doc — no IDE, no autocomplete.*

```python
# YOUR IMPLEMENTATION — write it without looking at the model above

import heapq

def min_meeting_rooms(intervals):
    # [blank — implement here]
    pass
```

**Your implementation (write it out):**

[blank]

---

### Narration Practice — Walk Through These Test Cases Out Loud

*Before checking your implementation, narrate each test case as if to an interviewer. Say: "For input X, I expect Y because..." and then trace through your code manually.*

**Test 1:** `[]` → Expected: `0`
Trace: [blank — narrate why the empty case returns 0 and where in your code it's handled]

**Test 2:** `[[1,5]]` → Expected: `1`
Trace: [blank — walk through the loop once and show that exactly 1 item ends up in the heap]

**Test 3:** `[[1,5],[2,6],[3,7]]` → Expected: `3`
Trace: 
- Sort: already sorted.
- [1,5]: heap is empty → push 5. rooms = [5]
- [2,6]: rooms[0] = 5, 5 > 2 → no free room → push 6. rooms = [5, 6]
- [3,7]: rooms[0] = 5, 5 > 3 → no free room → push 7. rooms = [5, 6, 7]
- Return len([5, 6, 7]) = 3. Correct.

**Test 4:** `[[1,5],[5,10]]` → Expected: `1` (with exclusive endpoints)
Trace:
- Sort: already sorted.
- [1,5]: push 5. rooms = [5]
- [5,10]: rooms[0] = 5, 5 ≤ 5 → free room → heapreplace(5 → 10). rooms = [10]
- Return len([10]) = 1. Correct.

**Test 5:** `[[1,10],[2,4],[3,5]]` → Expected: `3`
Trace:
- Sort: already sorted (starts are 1, 2, 3).
- [1,10]: push 10. rooms = [10]
- [2,4]: rooms[0] = 10, 10 > 2 → push 4. rooms = [4, 10]
- [3,5]: rooms[0] = 4, 4 > 3 → push 5. rooms = [4, 5, 10]
- Return 3. Correct.

**Checkpoint M4 (hard gate):** Check the box at the top only after completing at least 3 of these traces out loud.

---

## Part 5 — System / Reasoning Write-Up

*Adapted for an algorithmic lab: answer these questions in writing as if justifying your choices to a senior engineer reviewing your code.*

**Q1: Why a min-heap and not a sorted list or a simple array?**
[blank — your answer here]

*Model answer to compare after:* A sorted array would require O(n) insertion to maintain order, giving O(n²) overall. A min-heap gives O(log n) insertion and O(1) peek at the minimum — exactly the operations we need. We never need to look at any element other than the minimum, so the heap's structure is a perfect fit.

**Q2: Why sort by start time and not by end time?**
[blank — your answer here]

*Model answer:* We process meetings in arrival order. Sorting by start time means when we process meeting i, every earlier meeting is already "in" the heap. If we sorted by end time, we'd be processing meetings in the order they finish, which breaks the invariant — we'd try to assign rooms to meetings before knowing which other meetings are starting at the same time.

**Q3: What breaks if we sort by end time instead of start time?**
[blank — your answer here]

*Model answer:* Consider [[1,10],[2,3],[4,5]]. Sort by end: [[2,3],[4,5],[1,10]]. We process [2,3] first, then [4,5] (reuses room), then [1,10]. But [1,10] starts at 1 — before [2,3] even started! We'd assign [1,10] to a "free" room when it actually conflicts with [2,3] and [4,5]. The result would be wrong.

**Q4: What's the time complexity of the naive O(n²) approach and why?**
[blank — your answer here]

**Q5: How would you explain this solution to a non-technical person?**
[blank — your answer here]

*Model answer hint:* "Imagine you're a room scheduler at a conference. Meetings arrive and you need to assign each one a room. If any room has ended its meeting before the new one starts, you reuse it. You keep a list of when each room's current meeting ends, and you always check the room that's going to free up soonest. If that room is still busy when the new meeting starts, you open a new room. At the end, you count how many rooms you opened."

---

## Part 6 — Interview Simulation

### 90-Second Narration

*Set a timer for 90 seconds. Without looking at your notes, narrate your full approach as if the interviewer just asked you to explain your solution. Cover: what you understood from the problem, your brute force, why you improved it, the data structure choice, and the complexity.*

[blank — your narration notes here, or record yourself and play it back]

---

### Curveball 1 — Space Compression

**Interviewer:** "Can you do this in O(1) space?"

**Your answer:** [blank]

*Model answer:* No, not with this approach. The heap is O(n) because in the worst case (all meetings overlap), we need to track n room end times. There's no way to determine the minimum rooms needed without tracking the state of active meetings, and that state is inherently O(n). The honest answer is: "I don't think O(1) space is achievable here, because we need to track at minimum which rooms are active. I could reduce the constant factor but not the space class. Want me to explain why?" Saying this clearly and confidently is better than guessing.

**GCA note:** The interviewer may be testing whether you know the difference between "I can't do it in O(1)" (correct answer) and "I don't know how" (different answer). Knowing what's impossible is a sign of strong reasoning.

---

### Curveball 2 — Multi-Day Meetings

**Interviewer:** "What if meetings can span multiple days? For example, a meeting might run from Monday 9am to Wednesday 5pm."

**Your answer:** [blank]

*Things to address:*
- Does your existing algorithm still work? (Yes — if you represent times as absolute integers, e.g., minutes since epoch, nothing changes.)
- What new edge cases arise? (Meetings that overlap across midnight, timezone issues, daylight saving time.)
- What changes to the contract? (Input format: timestamp instead of hour. Output: still a count.)
- Is the algorithm itself different? (No — it's purely a data representation change.)

---

### Curveball 3 — Return Room Assignments

**Interviewer:** "Instead of returning just the count, return the actual room assignments — a list where the ith element is the room number assigned to meeting i."

**Your answer:** [blank]

*Things to address:*
- The current algorithm loses track of which room corresponds to which end time.
- You'd need to store (end_time, room_number) tuples in the heap instead of bare end times.
- When you reuse a room, you need to record which room number was reused.
- After processing, you'd map each meeting back to its assigned room.
- Output: a list of room numbers in input order (not sorted order).

*Sketch of the approach:*
```python
# Instead of rooms = [] (just end times), use:
# rooms = [] where each entry is (end_time, room_id)
# Track room_count to assign new IDs
# Build a result[] indexed by original meeting index
```

The algorithm complexity stays the same: O(n log n). Only the bookkeeping changes.

---

## Part 7 — SWE Rubric

*Self-grade after completing the lab. Score yourself as an interviewer would — not as someone who knows what you were trying to do.*

| Dimension | 5 — Strong | 3 — Adequate | 1 — Weak | Your Score |
|---|---|---|---|---|
| Communication / think-aloud | Clarified before coding, narrated brute force → optimized, explained each step of the algorithm out loud | Coded with some explanation after the fact, or explained some steps but not others | Coded silently, no narration; interviewer would have no idea what you were thinking | __ /5 |
| Problem solving | Named brute force AND optimized, stated why the min-heap approach is correct and why it improves on brute force | Found a working solution but didn't articulate alternatives or the reasoning behind the choice | Brute force only, or got stuck and didn't progress; no mention of optimization | __ /5 |
| Correctness | All 5 test cases pass with no bugs; handles empty input, single meeting, all-overlap, no-overlap, adjacent-endpoint | Core logic correct, 1 edge case missed (e.g., empty list not handled) | Fails on multiple test cases; fundamental logic error | __ /5 |
| Code quality | Clean variable names (rooms, start, end), no magic numbers, readable without IDE context; heapreplace used correctly | Functional but verbose, or some unclear naming, but correct | Buggy variable reuse, unclear names, or would not survive a code review | __ /5 |
| Testing and edge cases | Traced through at least 3 test cases (including empty and all-overlap) out loud before declaring done | Traced through 1–2 cases | Declared done without testing; moved straight from code to Part 5 | __ /5 |
| Complexity analysis | Correctly stated O(n log n) time and O(n) space; explained why the sort dominates; compared to brute force O(n²) | Named a complexity but imprecise (e.g., said O(n) time, which is wrong) | Did not state complexity; or stated it only when prompted without explanation | __ /5 |
| Time management | Finished core solution in < 35 min, with time to discuss curveballs | Finished but rushed; curveballs got cut short | Ran out of time before completing the solution; did not reach Part 5 | __ /5 |

**Total: __ / 35**

---

## You're Ready When...

- You finish the blank re-implementation (Part 4, your turn) in under 30 minutes without looking at the model
- You trace all 5 test cases correctly without running the code
- You answer Curveballs 1 and 2 without freezing (Curveball 3 is a stretch goal)
- You self-grade ≥ 24/35 on two separate attempts (attempt 1 is calibration; attempt 2 is your real score)

**Next lab:** [→ Lab 02: Graph/Grid — Number of Islands](../lab_02_graph_grid/workbook.md)

---

*Google SWE Lab 01 · Tier 1 (Worked) · v1.0*
