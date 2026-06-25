# Flashcards — Google SWE Lab 03: Mock Phone Screen Review

*5 review cards synthesizing the key lessons from Labs 01, 02, and 03. Study before your actual phone screen.*

---

## Card 1 — GCA Narration (Lab 01 Review)

**Q:** You're in a Google phone screen. You've just received a problem. What are the FIRST 3 things you say, in order, before writing any code?

**A:**
1. **Restate the problem in your own words.** "So I'm given X and I need to return Y — let me make sure I understand." This shows you listen, and it catches misunderstandings early.
2. **Ask at least 2 clarifying questions.** Focus on: edge cases (empty/single/null input), data type assumptions (char vs string vs int), and output format (count vs list vs map). Say: "Before I start, a couple of questions..."
3. **Name the brute force.** "My first instinct is [naive approach], which would be O(?) — let me see if I can do better." Never jump to the optimized solution silently. The brute force statement is required for a strong GCA score even if you immediately discard it.

---

## Card 2 — Heap Scheduling (Lab 01 Review)

**Q:** When is a min-heap the right data structure for a scheduling or assignment problem? State the recognition pattern.

**A:** Recognition pattern: "I need to repeatedly find the minimum element, update it, and find the new minimum." If you find yourself wanting to "check the earliest available room / slot / worker / machine," that's a min-heap. The heap gives O(1) access to the minimum and O(log n) for insert and update. Contrast with: a sorted list (O(n) insert), a counter (O(1) but no ordering), or a full sort (O(n log n) but not dynamic). For Meeting Rooms: the minimum end time = the room that frees up soonest. For any similar problem where you repeatedly reuse the "most available" resource, think min-heap first.

---

## Card 3 — Graph Traversal on Grids (Lab 02 Review)

**Q:** You see a 2D grid problem in a Google interview. What is the complete mental checklist you run through before writing any code?

**A:**
1. **Clarify adjacency:** 4-directional (up/down/left/right) or 8-directional (diagonals too)? Say it explicitly.
2. **Clarify cell types:** What values mean "traversable" vs "blocked"? ('1' vs '0', '#' vs '.', etc.)
3. **Choose traversal:** BFS or DFS? State your choice and the reason. Default to DFS for brevity; mention BFS if stack overflow is a risk.
4. **Choose visited marking:** In-place (overwrite the cell) or external set? Ask if input modification is okay.
5. **Write the base case first:** What conditions cause the DFS to return immediately? (Out-of-bounds AND already-visited/wrong-type.)
6. **Trace the 5 edge cases:** empty grid, single cell (land), single cell (water), all land, all water.

---

## Card 4 — Complexity Analysis Cold (All Labs Review)

**Q:** In a mock interview with no hints, how do you derive time complexity for an algorithm you've just written? Give the 3-step method.

**A:**
1. **Count the outer loops.** How many times does the outermost loop execute? n iterations for a list, m×n for a grid.
2. **Count the inner work per iteration.** For each iteration, what's the most expensive operation? A heap push is O(log n). A hash map lookup is O(1). A linear scan is O(n).
3. **Multiply and simplify.** Outer loop × inner work = total. If there are multiple phases (e.g., a sort plus a loop), add them and take the dominant term. Example for Meeting Rooms: sort = O(n log n), loop with heap = O(n log n), total = O(n log n). For Number of Islands: outer loop = O(m×n), total DFS calls across all islands = O(m×n) (each cell visited once), total = O(m×n). Say this out loud step by step — the derivation scores GCA points, not just the answer.

---

## Card 5 — Edge Case Checklist (All Labs Review)

**Q:** What is the universal edge case checklist you should run through for EVERY algorithm problem in a Google interview?

**A:** Remember the acronym **SENSE**:
- **S — Single element:** What happens with exactly 1 item? (1 meeting, 1 cell, 1 word)
- **E — Empty input:** What happens with 0 items? Return 0, return [], or return None — be explicit in your contract.
- **N — Null / negative / zero:** Are negative values possible? Can integers be 0? Can strings be empty ""?
- **S — Same values / all same:** All overlapping meetings, all land cells, all identical words — does your algorithm degenerate?
- **E — Extreme scale:** What happens with n = 10^6? Does your approach still hold, or does it break (recursion depth, time limit, memory)?

Run through SENSE before checking M4. You can do it in 60 seconds out loud ("Let me trace through my edge cases quickly...") and it demonstrably improves your score.

---

*5 cards · Google SWE Lab 03 (Mock Screen Review) · Study the morning of your interview*
