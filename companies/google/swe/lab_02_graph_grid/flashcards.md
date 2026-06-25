# Flashcards — Google SWE Lab 02: Graph/Grid Traversal

*10 cards for spaced repetition. Study 24–48 hours after completing the workbook.*

---

## Card 1 — BFS vs DFS: The Choosing Rule

**Q:** When facing a grid traversal problem in an interview, how do you decide between BFS and DFS? State a concrete rule of thumb.

**A:** Use **DFS** when: (1) the traversal is simpler to express recursively and recursion depth isn't a concern (small-to-medium grid), or (2) you need to explore deep paths (e.g., finding a path through a maze). Use **BFS** when: (1) stack overflow is a risk (very large grids, 10k+ cells per component), (2) you need shortest-path behavior (fewest hops), or (3) you prefer iterative code. For Number of Islands specifically, both work identically — default to recursive DFS for brevity in a phone screen, but flag BFS if the interviewer mentions a large grid.

---

## Card 2 — In-Place Marking vs Visited Set

**Q:** In a grid traversal, what are the two ways to mark cells as visited? What is the tradeoff between them?

**A:** 
- **In-place marking:** Overwrite `grid[r][c]` with a sentinel value (e.g., '0' or '2') to indicate "visited." Advantage: O(1) extra space. Disadvantage: modifies the input, which may violate the caller's expectations or break concurrent access.
- **Separate visited set:** Use a `set` of `(r, c)` tuples. Advantage: input is unchanged; safe for read-only grids. Disadvantage: O(m×n) extra space for the set.
In a Google interview, in-place marking is standard and expected. Always clarify: "Is it okay if I modify the grid in-place?" before doing it.

---

## Card 3 — 4-Directional vs 8-Directional Traversal

**Q:** Number of Islands uses 4-directional (horizontal + vertical) adjacency. What changes if the problem uses 8-directional adjacency (including diagonals)?

**A:** With 4 directions, neighbors of (r, c) are: `(r+1, c), (r-1, c), (r, c+1), (r, c-1)`. With 8 directions, add the four diagonals: `(r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1)`. The traversal code changes only in the list of directions. However, 8-directional adjacency creates fewer, larger islands (more cells connect), so the count typically decreases. Always clarify adjacency definition in Part 1 — don't assume.

---

## Card 4 — Union-Find Alternative

**Q:** Describe how Union-Find (Disjoint Set Union) solves Number of Islands in 3–4 sentences. When would you prefer it over DFS?

**A:** Initialize each '1' cell as its own component. For each '1' cell, union it with any adjacent '1' cells. After processing the entire grid, count the number of distinct roots — each root represents one island. Prefer Union-Find when: (1) the grid changes dynamically (cells are added/removed one at a time and you need the island count after each change), or (2) you're processing a distributed/streaming grid where DFS over the whole grid isn't feasible. Union-Find with path compression and union by rank runs in near-O(1) per operation (amortized O(α(n)) where α is the inverse Ackermann function).

---

## Card 5 — O(m×n) Complexity Justification

**Q:** Why is the time complexity of Number of Islands O(m×n), and not O(m×n × something)?

**A:** Each cell is visited at most once. When DFS (or BFS) starts from a cell, it immediately marks that cell as visited. The outer loop checks every cell, but only calls DFS on unvisited '1' cells. Each DFS call does O(1) work per cell and then marks it — ensuring it's never called again. Across all islands, the total number of DFS recursive calls equals the total number of '1' cells, which is at most m×n. Total work: O(m×n) for the outer loop + O(m×n) for all DFS calls combined = O(m×n). There's no multiplier because the marking prevents re-entry.

---

## Card 6 — Why Grid Problems Map to Graphs

**Q:** State the formal mapping from a grid problem to a graph. Why does recognizing this help in interviews?

**A:** Formal mapping: nodes = grid cells, edges = pairs of cells satisfying the adjacency condition (4-directional here). A grid is just a structured graph where each node has at most 4 neighbors, and adjacency is implicit in the indices rather than in an explicit adjacency list. Recognizing this helps because: (1) you can immediately apply standard graph algorithms (BFS, DFS, Union-Find, shortest path) without reinventing them for the grid format; (2) you can discuss complexity using standard graph terms (O(V + E) = O(m×n + 4×m×n) = O(m×n)); (3) you demonstrate conceptual breadth to the interviewer, which scores GCA points.

---

## Card 7 — Recursive vs Iterative DFS Tradeoff

**Q:** What is the concrete downside of recursive DFS on a very large grid, and how do you fix it?

**A:** Python's default recursion limit is 1,000 calls. An island that spans the entire grid could require m×n recursive calls — easily exceeding the limit and raising a `RecursionError`. Fix options: (1) **Iterative DFS with explicit stack:** Replace recursion with a `while stack:` loop using a list as a stack. Push starting cell, pop and process, push unvisited neighbors. (2) **BFS:** Same idea but with a deque. (3) **Increase Python's recursion limit** via `sys.setrecursionlimit()` — works but is hacky and may still crash on very large inputs. In an interview, mention the recursion limit risk and offer to show the iterative version if asked.

---

## Card 8 — Common Grid Edge Cases

**Q:** List the 6 edge cases every grid traversal solution must handle explicitly.

**A:**
1. **Empty grid:** `grid = []` — check `if not grid`.
2. **Empty row:** `grid = [[]]` — check `if not grid[0]`.
3. **Single cell, land:** `[['1']]` → 1 island.
4. **Single cell, water:** `[['0']]` → 0 islands.
5. **All land:** One giant island that touches all edges → 1 island.
6. **All water:** No islands → 0.
The base case of your DFS must handle both out-of-bounds (r < 0, r ≥ rows, c < 0, c ≥ cols) AND already-visited/water cells (`grid[r][c] != '1'`). Combining these into one condition is idiomatic: `if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1': return`.

---

## Card 9 — Toroidal Wrapping Concept

**Q:** How do you modify a grid traversal to work on a toroidal grid (where edges wrap around)?

**A:** Replace hard boundary checks with modular arithmetic. Instead of returning early when `r < 0` or `r >= rows`, compute the neighbor row as `(r + dr) % rows` and the neighbor column as `(c + dc) % cols`. This ensures cells on the left edge are adjacent to cells on the right edge, and the top row is adjacent to the bottom row. You still need to mark cells as visited to avoid infinite loops. The tricky part: a toroidal grid has no "outside" — every cell has exactly 4 neighbors. This can cause a single island to contain all '1' cells even if they're not geographically adjacent in the non-toroidal sense.

---

## Card 10 — "When to Use BFS vs DFS" Rule Summary

**Q:** Summarize the BFS-vs-DFS decision in a single interview-ready sentence for each of the 3 most common grid problem types.

**A:**
- **Island counting (this lab):** Either works identically; use DFS for brevity, BFS if grid is very large or stack overflow is a concern.
- **Shortest path in an unweighted grid (e.g., maze):** Always BFS — it finds the shortest path by level, which DFS cannot guarantee.
- **Detecting whether a path exists:** DFS is typically simpler; BFS works too but is heavier. Use DFS unless you also need the shortest path.
Bonus: For problems requiring you to process cells in a specific order (e.g., by distance from source), BFS with a queue naturally gives you that ordering for free.

---

*10 cards · Google SWE Lab 02 · Review 24–48 hrs after completing workbook*
