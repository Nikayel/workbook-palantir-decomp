# Google SWE Lab 02 — Graph/Grid Traversal
## Number of Islands (Tier 2 — Completion)

**Tier:** 2 (Completion) — Structure and contract are provided. The key algorithmic choices — traversal method, visited-marking strategy, neighbor logic — are left blank for you to fill in. You cannot pass this lab by copying; you have to supply the substance.

**Before you start:** Set a timer for 50 minutes. Write all code in a plain text area. No IDE. Narrate out loud.

**Prerequisite:** You should have completed Lab 01 (Meeting Rooms) before this lab. The GCA narration habits from Lab 01 apply here too.

---

## Milestones

- [ ] M1 · Clarified — asked at least 2 substantive questions before writing any code
- [ ] M2 · Approached — stated whether you're using BFS or DFS and WHY (the choice is yours to make)
- [ ] M3 · Coded — filled in all 4 TODO blocks in the starter code with working logic
- [ ] M4 · Tested — walked through at least 3 test cases out loud, including at least 1 edge case **(hard gate)**
- [ ] M5 · Optimized — stated time complexity O(m×n), discussed Union-Find as a stretch alternative
- [ ] M6 · Ready — self-graded ≥ 24/35 on two separate attempts

---

## Part 0 — Forethought

**Goal:** Count the number of islands in a grid using graph traversal, while narrating clearly for GCA scoring. Make an explicit choice between BFS and DFS and defend it.

**Target time:** 50 minutes. Suggested breakdown:
- 5 min — clarifying questions
- 8 min — approach (BFS vs DFS decision)
- 3 min — contract review
- 20 min — fill in the TODO blocks
- 7 min — test cases out loud (M4 gate)
- 5 min — complexity and Union-Find mention
- 7 min — curveballs

**Your BFS/DFS decision (fill in before starting Part 4):**

I will use: [ ] BFS [ ] DFS

My reason (write one sentence): [blank — you must state this before coding]

**Confidence rating before starting (circle one):** 1 — 2 — 3 — 4 — 5

**What I want to get right this session:** [blank]

---

## Part 1 — Clarifying Questions

*The scenario: You're in a Google phone screen, plain Google Doc. The interviewer says:*

> "Given an m×n grid of '0's (water) and '1's (land), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically."

*Ask your questions before writing any code.*

**Q1: What type are the grid values — characters ('0'/'1') or integers (0/1)?**
Assumption: [blank — make a choice and state it]

**Q2: Can the grid be empty, or have zero rows/columns?**
Assumption: [blank]

**Q3: Is diagonal adjacency considered? (i.e., are cells touching at corners part of the same island?)**
Assumption: [blank — the problem says horizontal/vertical, but confirm you heard it]

**Q4: Is the grid modified in place allowed, or must I preserve the input?**
Assumption: [blank — this determines whether you mark cells in-place or use a separate visited set]

**Q5: What is the expected grid size? Does it affect my approach choice (BFS vs DFS stack depth)?**
Assumption: [blank]

**Checkpoint M1:** Check the box above if you asked at least 2 questions before proceeding to Part 2.

---

## Part 2 — Decomposition

*Fill in the blanks. This is Tier 2 — you supply the substance.*

### The Core Insight

A grid can be modeled as a graph where:
- Each cell is a node
- Two cells are connected by an edge if they are [blank — what relationship must they have?]

Counting islands becomes: count the number of [blank — what graph concept?] in this graph.

### Algorithm Sketch

1. Iterate over every cell in the grid.
2. When we find a cell containing [blank], we've found the start of a new island.
3. We increment our counter and immediately [blank] from that cell — visiting and marking every connected land cell.
4. After the traversal, all cells of that island are [blank — what state are they in?], so we won't count them again.
5. We continue until every cell has been visited.

### BFS vs DFS — Your Choice

**Arguments for DFS:**
- Simpler recursive implementation (fewer lines of code)
- Stack depth is bounded by O(m×n) in worst case — could cause stack overflow on very large grids
- Easier to write in a Google Doc quickly

**Arguments for BFS:**
- Iterative (uses an explicit queue), no risk of stack overflow
- More natural for "spreading from a point" problems
- Slightly more code in a plain doc

**Your choice and reasoning (fill in):** [blank — commit to one and defend it]

**Checkpoint M2:** Check the box above after committing to a traversal method and writing your reason.

---

## Part 3 — Contract

*This is provided for you (Tier 2 perk). Review it before coding.*

**Function signature:**
```
num_islands(grid: List[List[str]]) -> int
```

**Input:**
- `grid`: An m×n 2D list of strings, where each cell is either '1' (land) or '0' (water).
- Dimensions: 1 ≤ m, n ≤ 300.
- Grid may be empty (return 0) or have no islands (return 0).

**Output:**
- A single integer: the number of islands.

**Edge cases:**
- Empty grid `[]` or `[[]]` → return `0`
- Grid of all water → return `0`
- Grid of all land (one giant island) → return `1`
- Single cell `[['1']]` → return `1`
- Single cell `[['0']]` → return `0`
- Grid with multiple disconnected 1-cell islands → return count of those cells

**Modification note:** In-place marking (changing '1' → '0' or '2' during traversal) is permitted and is the standard approach for this problem in interviews.

---

## Part 4 — Code

*Fill in every TODO block. Do not skip any. Each blank represents a genuine algorithmic decision you must make.*

```python
def num_islands(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        # TODO: base case — what stops the recursion?
        # (Think: when should we return immediately without doing anything?)
        # [blank — fill in the base case condition]
        
        # TODO: mark visited — how do you avoid revisiting this cell?
        # (Think: what value do you write back to grid[r][c]? Why?)
        # [blank — fill in the marking logic]
        
        # TODO: explore neighbors — which 4 directions do you recurse into?
        # (Think: up/down/left/right as (r±1, c) and (r, c±1))
        # [blank — fill in 4 recursive calls]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                # TODO: what do you do when you find an island cell?
                # (Think: two things happen here)
                # [blank — fill in]
    
    return count
```

### Your Completed Implementation

*Write the full, filled-in version here. This is what you'd have in the Google Doc.*

```python
# YOUR COMPLETE IMPLEMENTATION

def num_islands(grid):
    # [blank — write the complete filled-in version here]
    pass
```

---

### Narration Practice — Test Cases Out Loud

**Test 1:** Empty grid `[]` → Expected: `0`
Trace: [blank — where in your code does this get caught?]

**Test 2:** 
```
[['1','1','1'],
 ['1','1','1'],
 ['1','1','1']]
```
Expected: `1` (one giant island)
Trace: [blank — trace through the outer loop and show why count reaches exactly 1]

**Test 3:**
```
[['1','1','0','0','0'],
 ['1','1','0','0','0'],
 ['0','0','1','0','0'],
 ['0','0','0','1','1']]
```
Expected: `3`
Trace: [blank — identify the 3 islands and show when count increments]

**Test 4:** `[['0','0','0'],['0','0','0']]` → Expected: `0` (all water)
Trace: [blank]

**Test 5:** Single-cell grid `[['1']]` → Expected: `1`
Trace: [blank]

**Checkpoint M4 (hard gate):** Check the box only after narrating at least 3 of these test cases out loud. Do not proceed to Part 5 until M4 is checked.

---

## Part 5 — System / Reasoning Write-Up

*This section is mostly blank (Tier 2). Answer in your own words.*

**Q1: What is the time complexity of your solution? Justify it.**
[blank]

*Hint: You visit each cell at most once (marked as visited after first visit). The total number of cells is m×n. Each dfs call is O(1) amortized across all calls.*

**Q2: What is the space complexity? Where does the space go?**
[blank]

*Hint: Consider two sources — the recursion stack and the in-place marking (no extra array). What is the worst-case recursion depth?*

**Q3: Why does marking cells as visited (in-place or via a set) prevent double-counting?**
[blank]

**Q4: If you used in-place marking, you modified the input grid. Is this always acceptable? When might you NOT want to modify the input?**
[blank]

**Q5: Describe Union-Find as an alternative approach in 3–4 sentences. When would you prefer it over DFS/BFS?**
[blank]

*Hint: Union-Find treats each '1' cell as its own component initially, then unions adjacent '1' cells. The number of components after all unions = the number of islands. Preferred when you need to answer dynamic queries (e.g., add water/land cells one by one and count islands at each step).*

---

## Part 6 — Interview Simulation

### 90-Second Narration

*Set a timer. Without notes, narrate your complete approach — clarification, decomposition, algorithm choice, complexity — in 90 seconds.*

[blank — your narration notes or reflection afterward]

---

### Curveball 1 — Largest Island Area

**Interviewer:** "Now, instead of counting the number of islands, find the area of the largest island."

**Your answer:** [blank]

*Things to address:* How does your traversal change? You'd accumulate a count during each DFS/BFS (each cell contributes 1 to the area). Track the max across all starting cells. Your base case remains the same. Time complexity stays O(m×n).

---

### Curveball 2 — Toroidal Grid (Wrapping Edges)

**Interviewer:** "What if the grid wraps around — the left edge connects to the right edge, and the top edge connects to the bottom edge? (Like a torus or a globe.)"

**Your answer:** [blank]

*Things to address:* Your neighbor computation needs to use modular arithmetic: up = `(r - 1) % rows`, down = `(r + 1) % rows`, left = `(c - 1) % cols`, right = `(c + 1) % cols`. The rest of the algorithm is identical. This can create fewer, larger islands since cells across opposite edges now touch. The time complexity stays O(m×n).

---

### Curveball 3 — Scaling to 1 Million Rows

**Interviewer:** "What if the grid is 1,000,000 rows × 1,000,000 columns? What breaks?"

**Your answer:** [blank]

*Things to address:*
- Recursive DFS will overflow the call stack for a 1-trillion-cell grid with one giant island (stack depth = number of cells).
- Solution: switch to iterative DFS (explicit stack) or BFS (explicit queue). Either eliminates the recursion depth limit.
- Memory: storing the grid itself is O(m×n) = O(10^12) — 1 terabyte if each cell is 1 byte. You'd need a sparse representation or streaming approach.
- Parallelism: break the grid into tiles, process each tile on a separate machine, then resolve border conflicts using Union-Find on the boundaries.

---

## Part 7 — SWE Rubric

*Self-grade after completing the lab.*

| Dimension | 5 — Strong | 3 — Adequate | 1 — Weak | Your Score |
|---|---|---|---|---|
| Communication / think-aloud | Explicitly stated BFS vs DFS choice with reasoning before coding; narrated base case, marking strategy, and neighbor logic out loud | Made the BFS/DFS choice but didn't explain why; coded silently after | No BFS/DFS explanation; went straight to code; interviewer can't follow the reasoning | __ /5 |
| Problem solving | Mapped grid to graph problem explicitly; named traversal approach; mentioned Union-Find as alternative in Part 5 | Solved correctly but didn't articulate the graph abstraction | Got stuck or produced incorrect solution; didn't recognize this as a graph traversal problem | __ /5 |
| Correctness | All 5 test cases pass; handles empty grid, all-land, all-water, multi-island, single-cell | Core logic correct; 1 edge case missed (e.g., empty grid check missing) | Fails on basic cases; visited marking buggy causing infinite loop or double-counting | __ /5 |
| Code quality | All 4 TODOs filled with clear, named logic; base case covers both out-of-bounds AND water cells; no redundant checks | All TODOs filled but logic slightly convoluted or redundant | One or more TODOs missing or incorrect; code would not run without fixes | __ /5 |
| Testing and edge cases | Traced all 5 test cases out loud, including all-land and multi-island; checked M4 gate | Traced 2–3 cases, skipped at least one edge case | Declared done after coding; no tracing | __ /5 |
| Complexity analysis | Correct O(m×n) time and O(m×n) space (for recursion stack); compared to Union-Find; mentioned stack overflow risk for very large grids | Stated O(m×n) but didn't break down where the space comes from | No complexity stated or wrong (e.g., said O(n²) without defining n) | __ /5 |
| Time management | Completed all TODOs and tested in < 35 min; curveballs in remaining time | Finished TODOs but rushed on testing; ran out of time for curveballs | Did not complete all TODOs within time | __ /5 |

**Total: __ / 35**

---

## You're Ready When...

- You fill all 4 TODOs correctly without referring to a hint
- You trace the 3-island test case correctly without running code
- You explain the Union-Find alternative coherently in Part 5
- You self-grade ≥ 24/35 on two separate attempts

**Next lab:** [→ Lab 03: Mock Phone Screen — Anagram Pairs](../lab_03_mock_screen/workbook.md)

---

*Google SWE Lab 02 · Tier 2 (Completion) · v1.0*
