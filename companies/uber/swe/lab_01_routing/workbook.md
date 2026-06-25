Status: Ready — work through all parts in order

# Lab 01 · Graph / Shortest-Path Routing — Dijkstra
**Uber SWE · Tier 1 · ~75 minutes**

---

## 🪜 Milestones

- [ ] M1 · Clarified — asked about: directed vs undirected, negative weights possible, disconnected graph, what to return if no path
- [ ] M2 · Approached — chose Dijkstra for non-negative weights, named when you'd use Bellman-Ford instead
- [ ] M3 · Coded — clean Dijkstra with min-heap, returning both time and path
- [ ] M4 · Tested — tested: direct edge, multi-hop shortest path, no path exists, single node
- [ ] M5 · Extended — can adapt to also return the full path (not just the travel time)
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Scenario

You're in an **Uber phone screen**. The interviewer says:

> "Given a city road network represented as a weighted directed graph, implement a function that finds the shortest route from a driver's current location to a pickup point. The edge weights represent travel time in seconds. There may be one-way roads."
>
> "You have 45 minutes. Narrate your approach."

This problem maps directly to Uber's core technology: **ETA calculation**. Uber's dispatch system runs Dijkstra-like algorithms millions of times per day to estimate driver arrival times and match drivers to riders.

---

## Part 0: Forethought

Before clarifying — 3 minutes:

1. What does "ETA" stand for and why is Uber uniquely interested in shortest-path problems?
   [blank]

2. Why would you need a directed graph for a city road network? Give one real-world example.
   [blank — hint: one-way streets]

3. What's the difference between minimizing distance and minimizing time? Which does Uber care about?
   [blank]

---

**--- CHECKPOINT: Forethought complete. Move to Part 1. ---**

---

## Part 1: Clarifying Questions — With Uber Flavor

These are the clarifying questions you'd ask in a real Uber interview. Write your reasoning after each one.

**Goal: Minimize travel time or distance?**
"Uber uses ETA = time, not distance. Drivers take the fastest route, not the shortest route. I'll treat edge weights as travel time in seconds."
[Your reasoning: blank]

**User type: What's the use case for this function?**
"Driver needs real-time routing, not a pre-computed route. So I need this to run fast per query."
[Why this matters for algorithm choice: blank]

**Data: Is the graph updated in real-time for traffic?**
"Uber's ETA includes traffic — edge weights can change. But for this problem, let's assume a static snapshot."
[What you'd do differently with dynamic weights: blank]

**Constraints: Any performance requirement?**
"Must complete in < 100ms per query for real-time use." 
[blank — how does this affect your algorithm choice?]

**Scale: How big is the graph?**
"Assume 10,000 nodes (city blocks) and 50,000 edges. Fits comfortably in memory."
[blank — does this change your approach?]

**Negative weights: Are there any?**
"No negative weights." 
[Why this matters: blank — if there were, Dijkstra is incorrect; Bellman-Ford handles negative weights]

**Disconnected graph: What to return if no path exists?**
"Return (infinity, []) — no path found."
[blank — what does this imply in Uber's product context?]

---

**--- CHECKPOINT: Clarifying questions written. Move to Part 2. ---**

---

## Part 2: Approach (Narrate Aloud)

Write your narration:

"For a weighted directed graph with non-negative weights, the classic algorithm is..."
[blank — continue: name Dijkstra, explain the invariant, name the data structure]

"I chose Dijkstra over BFS because..."
[blank — BFS finds shortest path by edge count, not by weight; Dijkstra handles weighted edges]

"I chose Dijkstra over Bellman-Ford because..."
[blank — Bellman-Ford handles negative weights but is O(VE); Dijkstra is O(E log V) with a heap]

"To also return the path (not just the time), I'll..."
[blank — describe the `prev` map / parent pointer approach]

Time complexity: O([blank]) — why? [blank]
Space complexity: O([blank]) — why? [blank]

---

**--- CHECKPOINT: Approach narrated. Move to Part 3. ---**

---

## Part 3: Implementation (Blank Slate)

Implement Dijkstra from scratch. No hints provided here — this is your timed practice.

```python
import heapq
from typing import Dict, List, Tuple

def shortest_route(
    graph: Dict[str, List[Tuple[str, int]]],
    start: str,
    end: str
) -> Tuple[int, List[str]]:
    """
    Find the shortest route in a weighted directed graph.
    
    Args:
        graph: adjacency list — {node: [(neighbor, weight), ...]}
        start: driver's current location
        end:   pickup point
    
    Returns:
        (time_seconds, path) — or (float('inf'), []) if no path exists
    """
    # Your implementation here
    pass
```

---

**--- CHECKPOINT: Implementation attempted. Move to Part 4. ---**

---

## Part 4: Worked Solution

Compare your implementation against this. Do NOT read until you've attempted Part 3.

```python
import heapq
from typing import Dict, List, Tuple, Optional

def shortest_route(
    graph: Dict[str, List[Tuple[str, int]]], 
    start: str, 
    end: str
) -> Tuple[int, List[str]]:
    """
    Find shortest route in a weighted directed graph using Dijkstra's algorithm.
    
    Args:
        graph: adjacency list — {node: [(neighbor, weight), ...]}
        start: starting node (driver location)
        end:   destination node (pickup point)
    
    Returns:
        (time_seconds, path) or (float('inf'), []) if no path exists
    """
    # Initialize distances to infinity for all known nodes
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    
    # Parent map for path reconstruction
    prev = {node: None for node in graph}
    
    # Min-heap: (distance, node)
    heap = [(0, start)]
    
    while heap:
        d, node = heapq.heappop(heap)
        
        # Stale entry: we've already found a shorter path to this node
        if d > dist[node]:
            continue
        
        # Early exit: we've reached the destination
        if node == end:
            break
        
        # Relax all edges from current node
        for neighbor, weight in graph.get(node, []):
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                prev[neighbor] = node
                heapq.heappush(heap, (dist[neighbor], neighbor))
    
    # No path found
    if dist[end] == float('inf'):
        return float('inf'), []
    
    # Reconstruct path by following parent pointers backwards
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = prev[node]
    
    return dist[end], path[::-1]   # Reverse to get start → end order
```

Key design decisions to understand:

1. **`if d > dist[node]: continue`** — the "stale entry" check. The heap may contain outdated entries for a node after we've already found a shorter path. We skip them.

2. **`graph.get(node, [])` instead of `graph[node]`** — handles nodes that appear as destinations but have no outgoing edges (dead ends).

3. **`prev` map** — by tracking the previous node for each node in the shortest path, we can reconstruct the full route by following pointers from `end` back to `start`.

4. **Early exit at `end`** — we can stop as soon as we pop the destination from the heap, because the heap guarantees we popped the shortest path to it.

---

**--- CHECKPOINT: Solution reviewed. Move to Part 5. ---**

---

## Part 5: Test Cases

Walk through each test case. Write expected output and trace through the code.

**Test 1: Multi-hop shortest path**
```python
graph = {
    'A': [('B', 10), ('C', 3)],
    'B': [('D', 2)],
    'C': [('B', 4), ('D', 8)],
    'D': []
}
# Call: shortest_route(graph, 'A', 'D')
```
Expected time: [blank — trace through: A→C(3), C→B(3+4=7), B→D(7+2=9). So 9 seconds via A→C→B→D]
Expected path: [blank]
Your trace: [blank]

**Test 2: Direct edge only**
```python
graph = {
    'driver': [('pickup', 5)],
    'pickup': []
}
# Call: shortest_route(graph, 'driver', 'pickup')
```
Expected: (5, ['driver', 'pickup'])
Your trace: [blank]

**Test 3: No path (disconnected graph)**
```python
graph = {
    'A': [('B', 1)],
    'B': [],
    'C': [('D', 1)],
    'D': []
}
# Call: shortest_route(graph, 'A', 'D')
```
Expected: (inf, [])
Your trace: [blank — why does dist['D'] remain infinity?]

**Test 4: Single node**
```python
graph = {'A': []}
# Call: shortest_route(graph, 'A', 'A')
```
Expected: (0, ['A'])
Your trace: [blank — does your implementation handle start == end correctly?]

---

**--- CHECKPOINT: Test cases traced. Move to Part 6. ---**

---

## Part 5 Extension: Uber-Specific Reasoning

Answer these before moving to curveballs:

**Why Dijkstra and not BFS?**
[blank — BFS gives shortest path by number of edges, not by weight. In Uber's road network, a 2-hop route might be faster than a 1-hop route if the 1-hop road is congested.]

**What if edge weights represent current traffic (updated every 30 seconds)? How do you handle stale routing?**
[blank — options: re-run Dijkstra on every request with fresh weights (expensive), cache routes and invalidate on traffic event (complex), use approximate methods like landmark-based routing or contraction hierarchies]

**How would Uber use this at scale (millions of drivers, millions of requests/minute)?**
[blank — precompute shortest paths for common city graphs, use geospatial indexing to limit the graph size per query, distribute computation across servers by region]

**What's the "act like an owner" decision here — precompute or compute on demand?**
[blank — this is an Uber 8-norms question. Act like owner means: model the cost trade-off. Precomputing for a city takes disk/memory but reduces per-query cost. On-demand gives fresher data but costs more per request. Uber likely uses a hybrid: precomputed base graph + real-time traffic overlay.]

---

**--- CHECKPOINT: Uber reasoning complete. Move to Part 6. ---**

---

## Part 6: Curveballs

**Curveball 1:**
"A road becomes blocked due to an accident. How does your system update routing in under 1 second?"
[blank — consider: you can't re-run Dijkstra for every driver. Options: mark the edge as unavailable (weight = infinity), fan out a lightweight update to affected routes, use a message queue to notify routing servers. "Act like owners" — what's the cost of a 30-second delay for 10,000 affected drivers?]

**Curveball 2:**
"We need to route 1,000 drivers simultaneously to 1,000 pickups (the matching problem). How does Dijkstra help?"
[blank — Dijkstra tells you the cost (ETA) between any driver-pickup pair. The matching problem (minimum cost bipartite matching) is a separate algorithm (Hungarian algorithm or auction). But Dijkstra is used to populate the cost matrix. This is actually how Uber dispatch works.]

**Curveball 3:**
"What if some edge weights are negative? For example, Uber gives the driver a credit for taking a longer route to avoid a congested zone."
[blank — Dijkstra fails with negative weights (it may finalize a node with a suboptimal path). Switch to Bellman-Ford: O(VE) time but handles negative weights. Or: eliminate negative weights by adding a constant offset to all edges (Johnson's algorithm). Note: Uber would not actually do this — drivers don't get credits for taking longer routes. This curveball tests your algorithmic boundary knowledge.]

---

**--- CHECKPOINT: Curveballs answered. Move to Part 7. ---**

---

## Part 7: Self-Assessment Rubric

Score yourself honestly. Total = 35 points. Target: ≥ 28 to be ready.

| Dimension | 5 | 3 | 1 | Your Score |
|---|---|---|---|---|
| Communication / Think-Aloud | Narrated Dijkstra invariant, heap choice, stale-entry check, and path reconstruction throughout | Narrated most of the algorithm with some gaps | Coded silently; couldn't explain design choices | /5 |
| Problem Solving | Chose Dijkstra immediately, named Bellman-Ford as the negative-weight alternative, explained early exit optimization | Got to Dijkstra but needed prodding; or didn't know Bellman-Ford | Chose BFS or brute-force; couldn't explain why Dijkstra is correct for non-negative weights | /5 |
| Correctness | Full implementation correct: stale-entry check, path reconstruction, disconnected graph case, start == end case | Most cases correct; one edge case buggy | Missing stale-entry check (infinite loop risk) or path reconstruction wrong | /5 |
| Code Quality | Clean: descriptive variable names (`dist`, `prev`, `heap`), type hints, accurate docstring, no magic numbers | Mostly clean; one or two style issues | Hard to read; cryptic names; missing structure | /5 |
| Testing & Edge Cases | Proactively tested all four cases: multi-hop, direct, no-path, single-node | Tested 2-3 of the 4 | Only tested the happy path | /5 |
| Debugging | Caught and corrected at least one error (e.g., forgot the stale-entry check) during implementation | Got confused about the stale-entry check but resolved it | Could not implement stale-entry check without seeing the solution | /5 |
| Time Management | Finished implementation + tests with time for Uber-specific reasoning | Finished implementation, light on tests or reasoning | Did not finish a working implementation | /5 |

**Total: /35**

---

### Reflection

What was the hardest part of this problem — the algorithm, the path reconstruction, or the Uber-specific framing?
[blank]

---

### Ready-When Checklist

- [ ] I can implement Dijkstra with a min-heap from scratch in under 15 minutes
- [ ] I can explain the stale-entry check in one sentence
- [ ] I can explain path reconstruction with the `prev` map in one sentence
- [ ] I know when to use Bellman-Ford instead of Dijkstra (negative weights)
- [ ] I can explain Dijkstra's time complexity O(E log V) and why
- [ ] I can frame this problem in Uber's "act like owners" norm
- [ ] Self-score ≥ 28/35
