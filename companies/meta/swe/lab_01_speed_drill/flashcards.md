# Meta SWE Lab 01 — Flashcards

10 cards. Study until each answer comes in < 5 seconds.

---

## Card 01 — Sliding Window Template

**Q:** Write the sliding window template (longest substring variant) from memory.

**A:**
```python
def sliding_window(s):
    state = {}   # tracks window contents
    left = 0
    best = 0

    for right in range(len(s)):
        # 1. Add s[right] to window state
        state[s[right]] = state.get(s[right], 0) + 1

        # 2. Shrink window while invariant is violated
        while [INVARIANT_VIOLATED]:
            state[s[left]] -= 1
            if state[s[left]] == 0:
                del state[s[left]]
            left += 1

        # 3. Update best
        best = max(best, right - left + 1)

    return best
```

For longest-without-repeating, invariant = any character count > 1. Use last-seen index (not count) for O(1) jump optimization.

---

## Card 02 — Floyd's Cycle Detection: Two Phases

**Q:** What are the two phases of Floyd's cycle detection and what does each accomplish?

**A:**

**Phase 1 — Detect:**
- slow moves 1 step per iteration, fast moves 2 steps
- If slow == fast at any point → cycle exists, remember meeting node
- If fast or fast.next becomes None → no cycle, return None

**Phase 2 — Find Start:**
- Reset slow to head. Keep fast at meeting node.
- Move both 1 step at a time.
- Where they meet = cycle start node.

**Why Phase 2 works:** The math shows that distance(head → cycle_start) ≡ distance(meeting_point → cycle_start) mod cycle_length. Walking both at speed 1 from head and meeting point causes them to arrive at cycle start simultaneously.

---

## Card 03 — Hash Set vs Floyd's for Cycle Detection

**Q:** Both hash set and Floyd's detect cycles in O(n) time. Why use Floyd's?

**A:**

| | Hash Set | Floyd's |
|---|---|---|
| Time | O(n) | O(n) |
| Space | O(n) | **O(1)** |
| Finds start? | Yes (revisited node) | Yes (Phase 2) |
| Code complexity | Lower | Slightly higher |

Use Floyd's when space is constrained. Use hash set when code simplicity matters more than memory. In interviews, Floyd's is the "impressive" answer — but always explain WHY you chose it (space tradeoff), not just that you know it.

---

## Card 04 — Longest Substring Variants

**Q:** What are the three main variants of the longest substring problem and how does the window condition change for each?

**A:**

| Variant | Window invariant | State to track |
|---|---|---|
| No repeating chars | All chars unique | char → last_seen_index (or count) |
| At most k distinct chars | ≤ k distinct chars in window | char → count; shrink when distinct count > k |
| At most k replacements | (window size) - (max count char) ≤ k | char → count; max_count of any single char |

All three use the same outer for-loop structure. Only the shrink condition and state change.

---

## Card 05 — Linked List Cycle Start: Proof Sketch

**Q:** Prove (without full math) why resetting one pointer to head after Phase 1 finds the cycle start.

**A:**

Let:
- F = length from head to cycle start
- h = length from cycle start to meeting point (inside cycle)
- C = cycle length

After Phase 1 meeting: slow traveled F + h steps. Fast traveled 2(F + h) steps. Difference = F + h = multiple of C (fast lapped slow some number of times). So F + h = kC, which means F = kC - h.

Walking F steps from head = walking kC - h steps from meeting point. Since kC - h steps inside the cycle lands you at cycle_start (you go around k times and come back h steps), both pointers arrive at cycle_start simultaneously.

---

## Card 06 — Speed Strategy for Two-Problem Screens

**Q:** What is the Meta-calibrated strategy for a 45-min, 2-problem phone screen?

**A:**

1. **Read both problems first** (60 sec): get the full picture before diving into P1.
2. **Clarify P1 fast** (60–90 sec): one assumption per category, state it, move on.
3. **Code P1** (15 min target): brute force in words first (5 sec), then optimal.
4. **Hard stop at 18 min**: even if P1 isn't perfect, transition to P2.
5. **Clarify + code P2** (17 min): same approach.
6. **Return to P1** if time allows (5 min): polish edge cases.
7. **Reserve 5–10 min** for walk-through and curveball.

If you spend 25+ minutes on P1, you are sacrificing P2 and likely failing the screen.

---

## Card 07 — Meta Interview Pace Expectations

**Q:** What does "Meta pace" mean for a SWE screen, and how is it different from other companies?

**A:**

Meta pace = **2 mediums in 45 minutes, including clarifications and walk-through.**

Other companies (Google, Amazon): often 1 medium or 1 hard in 45–60 minutes, with more discussion time.

Meta tests whether you can pattern-match quickly and execute without much hand-holding. The interviewer will not redirect you if you're going too slow — that silence IS the feedback. You must manage your own time.

Training target: solve 2 random mediums in 35 minutes, then use 10 minutes to explain. If you can't hit this consistently, repeat Lab 01 daily.

---

## Card 08 — Two-Pointer Patterns

**Q:** Name 4 two-pointer patterns and a canonical problem for each.

**A:**

| Pattern | Description | Example |
|---|---|---|
| **Slow/Fast (Floyd's)** | Different speeds on same structure | Cycle detection, find middle of list |
| **Left/Right converge** | Both ends toward middle | Two Sum (sorted), Container with Most Water |
| **Sliding window** | Right expands, left catches up | Longest substring, minimum window |
| **Partition** | One pointer for write position | Remove duplicates, Move Zeroes |

Key: "two pointers" is not one pattern — it's a family. Name the specific variant when explaining your approach.

---

## Card 09 — Hash Map vs Hash Set Tradeoffs

**Q:** When do you use a hash map vs a hash set in string/array problems?

**A:**

**Use hash set when:** You only need membership (is X present?) — e.g., cycle detection (visited nodes), checking for duplicates.

**Use hash map when:** You need to associate a value with each key — e.g., character → last seen index (sliding window), character → count (frequency problems).

**Space:** Both O(k) where k = number of distinct keys.

**Trick:** Hash set = hash map where value is always `True`. Many languages implement set using map internally.

---

## Card 10 — Time Management in Two-Problem Rounds

**Q:** What are the top 3 time-wasting mistakes in two-problem Meta screens?

**A:**

1. **Over-clarifying.** Asking 5+ questions per problem when 2–3 assumptions would suffice. Spend < 90 seconds total on both problems combined.

2. **Premature optimization.** Spending 5 minutes debating whether to use a hash map or a Trie when a hash map is clearly sufficient. State your choice with one-sentence justification and code it.

3. **Perfectionism on P1.** Polishing edge cases on P1 for 5 minutes while P2 is untouched. A working P1 + working P2 beats a perfect P1 every time. Partial credit on both > perfect credit on one.

**Rule of thumb:** If you've been on one problem for more than 60% of your time budget, stop and start the next one.
