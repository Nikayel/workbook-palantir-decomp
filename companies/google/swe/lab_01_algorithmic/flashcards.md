# Flashcards — Google SWE Lab 01: Algorithmic Fundamentals

*10 cards for spaced repetition. Study these 24–48 hours after completing the workbook. Cover the answer and try to recall it before reading.*

---

## Card 1 — GCA Scoring: Process Over Answer

**Q:** What does GCA (General Cognitive Ability) actually measure in a Google interview, and why does it mean you should narrate your thinking even if it slows you down?

**A:** GCA measures how you reason through novel problems, not whether you recall known solutions. Interviewers score your PROCESS — how you decompose the problem, articulate tradeoffs, handle uncertainty, and update your approach. A candidate who narrates a brute force, explains why it's insufficient, and walks to the optimized approach scores higher than a candidate who silently produces the optimal answer in half the time. Narrating slows you down slightly but dramatically raises your GCA score. The rule: never go silent for more than 30 seconds.

---

## Card 2 — Min-Heap for Scheduling Problems

**Q:** Why is a min-heap the right data structure for the Meeting Rooms problem? What property of a heap does this problem exploit?

**A:** The min-heap stores room end times and always gives O(1) access to the minimum — the room that frees up soonest. This is exactly the operation needed: for each new meeting, check whether the earliest-ending room is free (end ≤ start). If yes, reuse it. If no, open a new room. No other structure gives O(1) minimum access with O(log n) update. A sorted array would require O(n) insertion to maintain order; a hash set has no ordering. The heap is a perfect match for "I only ever need the minimum, and I update frequently."

---

## Card 3 — Sort By Start: Why It Matters

**Q:** The Meeting Rooms algorithm sorts intervals by start time. What is the loop invariant this establishes, and what goes wrong if you sort by end time instead?

**A:** Invariant after sorting by start: when we process meeting i, all meetings j < i have already been assigned to rooms. The heap contains the current end times of all occupied rooms, in sorted order. If you sort by end time instead, you process meetings in the order they finish — but a meeting with an early end time might start AFTER a meeting with a late end time. You'd free up rooms for meetings that haven't started yet and potentially give the wrong answer. Example: [[1,10],[2,3],[4,5]] sorted by end is [[2,3],[4,5],[1,10]]. Processing [1,10] last when it starts before everything else produces an incorrect room count.

---

## Card 4 — Complexity Analysis: n log n

**Q:** State the time and space complexity of the optimized Meeting Rooms solution and justify each.

**A:** Time: O(n log n). The sort is O(n log n) and dominates. The loop runs n times; each iteration does at most one heap operation (heappush or heapreplace), each of which is O(log n). Total: O(n log n) + O(n log n) = O(n log n). Space: O(n). The heap can hold at most n entries — in the worst case, every meeting overlaps with every other, so you open n rooms and store n end times. No additional data structures are used.

---

## Card 5 — Why Brute Force Is O(n²)

**Q:** Describe the brute-force approach to Meeting Rooms and explain exactly why its time complexity is O(n²).

**A:** Brute force: sort by start time (O(n log n)). For each new meeting (n meetings), scan every existing room (up to n rooms) to find one whose end time ≤ the meeting's start time. If found, update that room's end time. If not, open a new room. The scan is O(n) in the worst case (all rooms occupied). Across n meetings: O(n) scans × O(n) cost each = O(n²) total. The key observation is that the brute force inspects every room to find the minimum, while the heap inspects only the minimum, cutting the scan to O(log n).

---

## Card 6 — Googleyness Signals

**Q:** Name 4 specific Googleyness signals and give one concrete interview behavior that demonstrates each.

**A:**
1. **Intellectual humility:** When the interviewer pushes back, say "That's a great point — let me reconsider" and actually update your approach. Do not defend your first instinct past the point of reason.
2. **Curiosity:** Ask genuine questions about the problem. "What's the expected scale of the input?" or "Would the caller care about rooms with multiple concurrent occupants?" show you're thinking beyond the spec.
3. **Collaborative problem solving:** Explicitly invite the interviewer in. "I'm thinking min-heap here — does that resonate with you, or would you nudge me a different direction?" This is not weakness; it's Googleyness.
4. **Comfort with ambiguity:** If the problem is underspecified, make an explicit assumption and state it clearly rather than waiting for a complete spec. "I'll assume endpoints are exclusive — let me know if that's wrong."

---

## Card 7 — Narrating Tradeoffs

**Q:** When an interviewer asks "what's your approach?", what is the ideal structure of your verbal response for maximum GCA score?

**A:** Use a three-part structure: (1) State the brute force in one sentence. (2) Explain the bottleneck — why the brute force is slow. (3) Name the optimized approach and the insight that enables it. Example: "My brute force is to scan all rooms for each meeting — that's O(n²). The bottleneck is the linear scan. The insight is I only need the minimum end time, which a min-heap gives me in O(1) with O(log n) updates — bringing the total to O(n log n)." This structure demonstrates you know multiple approaches, understand their tradeoffs, and can communicate precisely. Never jump straight to the optimal solution without first naming the naive approach.

---

## Card 8 — Edge Case Checklist for Interval Problems

**Q:** What 5 edge cases should you always check for interval / scheduling problems?

**A:**
1. **Empty input:** `[]` → return 0 (or equivalent base case). Forgetting this is a common silent bug.
2. **Single element:** `[[1,5]]` → return 1. Verifies your loop handles n=1 without breaking.
3. **All overlapping:** Every meeting conflicts with every other → result equals len(intervals). Verifies the heap grows correctly.
4. **No overlaps:** Meetings are sequential with gaps → result is 1. Verifies room reuse works.
5. **Adjacent endpoints:** `[[1,5],[5,10]]` → answer depends on inclusive vs. exclusive spec (1 or 2). This is the question you must clarify in Part 1, and you must trace this case explicitly to prove your assumption is correctly implemented.

---

## Card 9 — Hiring Committee Packet Framing

**Q:** Google's Hiring Committee reads your interview packet but never meets you. What does this mean for how you should behave during a phone screen?

**A:** Everything you say and do during the interview is transcribed or summarized by the interviewer into a written packet. The HC reads the packet cold — no video, no voice, no body language. This means: (1) Your verbal clarity matters as much as your code. If you didn't explain why you chose the heap, the packet won't mention it, and HC won't know. (2) Sloppy variable names or undocumented logic in the Google Doc looks worse in the packet than it felt in the moment. (3) Correcting yourself out loud is a positive signal — it shows metacognition. Write as if you're writing for a reader who wasn't there.

---

## Card 10 — Plain-Doc Coding Discipline

**Q:** What 3 habits should you build for coding in a plain Google Doc (no IDE) during Google phone screens?

**A:**
1. **Write your own structure.** No autocomplete means you manually open every block. Develop a habit of writing `def`, `:`, and indentation consistently before filling in the body.
2. **Spell out variable names.** Without syntax highlighting, `r` and `rooms` look equally valid on the screen but `rooms` is dramatically easier for the interviewer to follow in real-time and in the HC packet later.
3. **Comment the intent, not the mechanics.** In a plain doc, a comment like `# min-heap: tracks room end times` on the line where you initialize the heap signals to the interviewer (and HC) exactly what you were thinking. You won't have the ability to run the code, so comments become your only secondary communication channel.

---

*10 cards · Google SWE Lab 01 · Review 24–48 hrs after completing workbook*
