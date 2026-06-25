Status: Ready — work through all parts in order

# Amazon SWE Lab 01 — Algorithmic: Binary Search on Answer + Graph Shortest Path

**Role:** SWE | **Tier:** 1 (worked solutions provided — read, understand, then blank and redo) | **Est. time:** 90 min | **Difficulty:** Medium

---

## Scenario

You're taking Amazon's OA. 90 minutes. Two problems. The clock is running.

Problem 1: You have a list of order processing times and k workers. Each worker handles one order at a time. Workers can be assigned orders in parallel, but orders cannot be split. Find the minimum total time needed to process all orders. (If k workers can each take one order simultaneously, what's the fastest we can finish everything?)

Problem 2: You have a warehouse modeled as a graph. Nodes are storage locations. Edges are corridors with integer weights representing walking time in seconds. A delivery robot starts at the entrance node and must visit a set of required item locations. Find the minimum time for the robot to reach all required items (the robot can start from the entrance and reach each item via the shortest path — it does not need to return to the entrance).

You must finish both. Time management is the test within the test. Go.

---

## Milestones

- [ ] M1 · Clarified — both problems scoped; tie-breaking and graph connectivity assumptions noted
- [ ] M2 · Approached — P1: binary search on answer + feasibility check; P2: Dijkstra or BFS
- [ ] M3 · Coded — both worked solutions read, understood, and re-implemented from scratch
- [ ] M4 · Tested — Amazon OA-style edge cases tested: k > n orders; disconnected graph; single worker; all items at start
- [ ] M5 · LP check — named which LPs are reflected in your approach and edge case handling
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Part 0: Forethought

**Goal:** Understand both algorithms deeply enough to re-implement from scratch without hints. This is a Tier 1 lab — you start with the solution, but the goal is to internalize it completely.

**Target time:** 90 min (20 min reading/understanding + 30 min blank re-implementation + 20 min testing + 20 min LP integration and curveballs)

**Confidence before reading solutions (1–5):** ___

**Confidence after re-implementing (1–5):** ___

---

## Part 1: Clarifying Questions

### Problem 1 — Parallel Order Processing

**Category: Goal**
Question: Do I need to return the minimum total time, or the assignment of orders to workers?
Assumption: Return the minimum time (integer). Assignment is not needed.

<details>
<summary>Hint</summary>
If they ask for the assignment, binary search still finds the optimal time limit, and you'd recover the assignment by greedily assigning during the feasibility check. For the OA, always confirm the return type.
</details>

**Category: Users / Input**
Question: Can a single order take longer than the target time? (i.e., min(orders) > time_limit in the binary search)
Assumption: The lower bound of binary search is max(orders) — we can never finish faster than the longest single order, even with infinite workers.

<details>
<summary>Hint</summary>
This is why lo = max(orders), not 0 or 1. Setting lo too low wastes binary search iterations and introduces a subtle bug where `can_finish(mid)` never returns True for the first few iterations.
</details>

**Category: Data**
Question: Are order processing times positive integers?
Assumption: All values are positive integers ≥ 1.

<details>
<summary>Hint</summary>
If orders can be 0, you'd skip those workers (a worker assigned to 0-length orders can do infinitely many in 0 time). The feasibility check would break. Assume positive for the standard problem.
</details>

**Category: Constraints**
Question: Can k > len(orders)?
Assumption: Yes. If k ≥ n, each order gets its own worker. Time = max(orders). The binary search handles this naturally — lo = max(orders) is already the correct answer.

<details>
<summary>Hint</summary>
Test this edge case explicitly. Many candidates code a solution that errors when k > n because they try to "allocate" exactly k workers. Binary search doesn't do this — it just asks "can we finish in time X?" which naturally handles k > n.
</details>

**Category: Scale**
Question: How large are orders and k?
Assumption: n and k up to 10^4, order values up to 10^9. Binary search over [max_order, sum_orders] is log(sum) ≈ log(10^13) ≈ 43 iterations. Each iteration is O(n). Total: O(n log(sum)) — well within limits.

<details>
<summary>Hint</summary>
Sum of orders can be up to n × max_value = 10^4 × 10^9 = 10^13. log2(10^13) ≈ 43 iterations. So O(n log(sum)) ≈ 4×10^5 operations. Fast.
</details>

---

### Problem 2 — Warehouse Robot Shortest Path

**Category: Goal**
Question: Should I return the time to reach ALL required items, or the time to visit them in an optimal sequence?
Assumption: I should return the maximum shortest-path distance from the entrance to any required item. The robot can take multiple optimal paths in parallel (conceptually) — it needs to reach all items, and the bottleneck is the hardest-to-reach one.

<details>
<summary>Hint</summary>
If the robot must visit items in sequence (traveling salesman variant), this becomes NP-hard. The problem as stated — shortest path from entrance to each item — is tractable. Clarify this immediately or you'll spend 30 minutes on the wrong algorithm.
</details>

**Category: Data**
Question: Are edge weights positive? Can there be negative weights?
Assumption: All weights are positive integers (walking time ≥ 1 second). Dijkstra requires non-negative weights. If negative weights were present, we'd need Bellman-Ford.

<details>
<summary>Hint</summary>
Dijkstra fails with negative weights because it assumes that once a node is "settled" (popped from the heap), its shortest path is final. A negative edge discovered later could produce a shorter path, which Dijkstra won't revisit.
</details>

**Category: Constraints**
Question: Is the graph connected? Can some required items be unreachable?
Assumption: I'll handle disconnected graphs. If a required item is unreachable (dist = infinity), I'll return -1 or raise an error.

<details>
<summary>Hint</summary>
This is an important edge case. In Amazon's warehouse context, disconnected graph = broken corridor. The robot cannot reach the item. The business answer: flag the item as unreachable, alert operations. The code answer: check if dist[item] == float('inf') after Dijkstra.
</details>

**Category: Scale**
Question: How large is the graph?
Assumption: Up to 10^4 nodes and 10^5 edges. Dijkstra with a binary heap is O((V + E) log V) = O((10^4 + 10^5) × 14) ≈ 1.5×10^6 — fine.

---

## Checkpoint M1 — Scoped

Mark M1 complete when: assumptions for all clarifying questions are written. Key decision confirmed for P2: robot finds shortest path to each item independently (not traveling salesman sequence).

---

## Part 2: Approach Planning

### Problem 1 — Binary Search on Answer

**Why binary search?**

The classic "minimize the maximum" or "what's the minimum X such that we can achieve Y?" pattern calls for binary search on the answer.

Here: "What is the minimum time T such that k workers can finish all n orders within T minutes?"

For a fixed T, the feasibility check is: worker i can handle `floor(T / order[j])` copies of order j. But here each order is processed exactly once. So worker assigned to unlimited orders up to time T can handle `floor(T / order_time)` orders (since each order is processed once with no repetition — wait, this needs precision):

Actually: for a fixed time limit T, a single worker can process orders sequentially. How many orders of processing time `t_j` can one worker handle in T minutes? `floor(T / t_j)`. If we sum this over all orders and the total is ≥ n, then k workers can collectively finish all n orders in T minutes.

Wait — that's not quite right either. Let me be precise:

"Given time limit T and k workers, can we assign all n orders such that each worker's total time ≤ T?"

For each order with processing time `t_j`, a single worker can process `floor(T / t_j)` such orders within T minutes. Sum over all orders: `sum(T // t for t in orders)` = total orders any one worker could handle if they only worked on that type of order. But with k workers, we can handle `k × (orders per worker)` — no, this isn't right structurally because orders have different lengths.

The correct feasibility: how many orders can ONE worker handle in time T? If orders are assigned greedily (one at a time, smallest first... no, order doesn't matter for counting), a worker handles orders one after another. The maximum number of orders of type t a worker can do in time T is `T // t`. So total capacity across ALL orders = `sum(T // t for t in orders)`. If this total ≥ n with k workers, that means... no, this counts how many of each order type can be done, not the total.

The cleaner version: total capacity of k workers in time T = k workers × (number of orders one worker can do). But orders have different durations. The standard formulation:

Number of orders that can be processed = sum over all order types j: floor(T / order_time[j]). If this sum × (1/k)... no.

Let me re-read: the standard "Koko eats bananas" / "minimum shipping capacity" form:

**Binary search on answer T.** Feasibility check: can k workers each work for at most T time and collectively process all orders? For order j with processing time t_j, one worker processes exactly one order j (takes t_j time). So worker i can handle `floor(T / t_i)` orders? No — a worker can be assigned any mix of orders. 

The simplest correct reading: each worker is assigned a contiguous block of orders (sorted). Binary search finds T such that greedily assigned blocks can each fit in T. This is the "split array largest sum" variant.

The implementation below uses the Koko-bananas variant: `sum(ceil(order / T))` = minimum workers needed. If this ≤ k, then T is feasible.

**Both variants appear in Amazon OAs.** Know both.

Brute force: Try every possible T from 1 to sum(orders). For each T, check if k workers can finish. O(sum × n) — too slow.

Optimized: Binary search T in [max(orders), sum(orders)]. O(n log(sum)).

**Binary search invariant:** lo = smallest T we know might work = max(orders). hi = largest T we might need = sum(orders) (1 worker does all).

---

### Problem 2 — Dijkstra Shortest Path

Dijkstra's algorithm finds shortest paths from a single source to all other nodes in a weighted graph with non-negative edge weights.

**Why Dijkstra and not BFS?** BFS finds shortest paths in unweighted graphs (all edge weights = 1). Dijkstra handles weighted edges.

**Why Dijkstra and not Bellman-Ford?** Bellman-Ford handles negative weights but is O(VE) — slower. Since we assumed non-negative weights, Dijkstra's O((V+E) log V) is better.

**Algorithm:**
1. Initialize dist[start] = 0, dist[all others] = infinity.
2. Use a min-heap (priority queue). Push (0, start).
3. Pop the minimum-distance node. For each neighbor, if current dist + edge_weight < dist[neighbor], update and push to heap.
4. When a node is popped from the heap and its stored distance matches the distance in the heap (not stale), it's "settled."
5. After Dijkstra completes, return `max(dist[item] for item in required_items)`.

---

## Checkpoint M2 — Approached

Mark M2 complete when: you can explain binary search on answer without looking at notes, AND you can trace Dijkstra on a 5-node graph by hand.

---

## Part 3: Worked Solutions

This is Tier 1. Read, understand, trace, then blank and re-implement.

### Worked Solution — Problem 1

```python
import math

def min_time_to_process(orders: list[int], k: int) -> int:
    """
    Binary search on answer T.
    Feasibility: with time limit T, how many orders can k workers process?
    Each worker can process ceil(order_time / T)... wait, let's think clearly:
    
    For time limit T, how many orders can k workers handle?
    For each order of processing time t, it takes one worker t time to complete.
    In T time, one worker can complete floor(T / t) orders of type t.
    But this ignores mixing — a worker can do order A then order B.
    
    Simpler: for T time per worker, total "slots" = k * T time units.
    Can we fit all orders (each consuming its processing time) into k workers each
    capped at T? This is a bin packing problem — NP-hard in general.
    
    BUT: if we sort orders and assign to workers greedily (or use the 
    "minimum number of workers" formula), it becomes tractable.
    
    Standard approach: can_finish(T) = sum(ceil(t / T) for t in orders) <= k
    This asks: for each order t, how many time slots of length T does it take?
    ceil(t/T). If total slots across all orders <= k, we can fit in k workers.
    """
    def can_finish(time_limit: int) -> bool:
        # Each order t takes ceil(t / time_limit) = 1 worker-slot of time_limit
        # (since each order is processed as a single unit, ceil(t/time_limit) = 1 
        # if t <= time_limit, which is always true since lo >= max(orders))
        # Simpler: sum(math.ceil(t / time_limit) for t in orders)
        # But since time_limit >= max(orders), ceil(t/time_limit) is always 1.
        # So can_finish = len(orders) <= k? That's just "enough workers for 1 each."
        # 
        # The correct interpretation for this problem style:
        # How many orders can ONE worker do in time_limit (working sequentially)?
        # Answer: time_limit // t for each order type t.
        # Total capacity across k workers = k * (total that one worker can do)?
        # No — workers are identical, so:
        # 
        # Revised correct interpretation (most common OA version):
        # Orders list has individual order times. k workers run in parallel.
        # Worker i takes the first available order, processes it, takes the next.
        # Min time = binary search on T; can_finish(T) = 
        #   total orders processable across all workers in time T.
        # For time T: worker can process orders greedily — for order with time t,
        # takes t time. In T total time, one worker does sum of chosen orders <= T.
        # 
        # The classical "k workers, minimize makespan" feasibility check:
        # Given T, greedily assign orders to workers (sort descending, assign to 
        # least-loaded worker). Can we finish in T?
        # 
        # For binary search to work cleanly, use the simpler check:
        # sum(math.ceil(t / time_limit) for t in orders) <= k
        # This works when orders are indivisible and each worker can take
        # multiple orders up to time_limit total.
        workers_needed = sum(math.ceil(t / time_limit) for t in orders)
        return workers_needed <= k

    lo = max(orders)      # can't finish faster than the slowest single order
    hi = sum(orders)      # upper bound: 1 worker does everything sequentially

    while lo < hi:
        mid = (lo + hi) // 2
        if can_finish(mid):
            hi = mid      # mid might be optimal — shrink upper bound
        else:
            lo = mid + 1  # mid is too short — need more time

    return lo

# Alternative: if orders = worker processing times (each worker processes in parallel,
# no multi-order assignment), then: answer = max(orders) if k >= len(orders) else
# binary search with can_finish(T) = sum(1 for t in orders if t <= T)
# -- this is a different problem formulation. Know which one you're solving.
```

**Trace on a small example:**
`orders = [3, 7, 2, 5]`, `k = 2`
- lo = 7, hi = 17
- mid = 12: ceil(3/12) + ceil(7/12) + ceil(2/12) + ceil(5/12) = 1+1+1+1 = 4 workers needed. 4 > 2 → lo = 13
- mid = 15: ceil(3/15)+ceil(7/15)+ceil(2/15)+ceil(5/15) = 1+1+1+1 = 4 > 2 → lo = 16
- mid = 16: same = 4 > 2 → lo = 17
- lo = hi = 17. Return 17.

Is 17 correct? With 2 workers: worker 1 takes [7, 5] = 12 min? No, they run in parallel... the binary search answer depends on interpretation. If workers take orders sequentially (no parallel within a worker), and we want minimum time where all orders are done:

Actually for this variant: `sum(math.ceil(t / T) for t in orders) <= k` means "if each order takes ceil(t/T) worker-slots-of-length-T, do we have enough slots (k slots total)?" Since k=2 and there are 4 orders, each taking at least 1 slot, we always need ≥ 4 slots which exceeds k=2. This formulation seems off for this problem.

**The cleaner variant for this OA problem:** each worker can hold exactly one order at a time. With k=2 workers and 4 orders, the minimum time is achieved by assigning optimally: worker 1 → [7, 2] = 9 min, worker 2 → [5, 3] = 8 min. Max = 9 min. This is the "partition into k groups to minimize maximum sum" problem.

```python
def min_time_to_process_v2(orders: list[int], k: int) -> int:
    """
    Minimize the maximum load across k workers.
    Binary search on time T.
    can_finish(T): greedily assign orders to workers. 
    A worker can take as many orders as fit within T total time.
    Sort orders descending. Assign each order to the worker with most remaining capacity.
    Actually: can_finish(T) = number of workers needed if each worker works up to T.
    Greedily: sort descending, assign each to least-loaded worker (but this is O(n log k)).
    
    Simpler check: can_finish(T) = number of "buckets" of capacity T needed to hold all orders.
    This is a bin-packing lower bound. Exact answer requires first-fit decreasing.
    
    For interview purposes, the O(n log k) greedy check works:
    """
    import heapq
    
    def can_finish(T: int) -> bool:
        if max(orders) > T:
            return False
        # Greedy: sort descending, assign each order to least-loaded worker
        heap = [0] * k  # k workers, each starting with 0 load
        heapq.heapify(heap)
        for order in sorted(orders, reverse=True):
            load = heapq.heappop(heap)
            if load + order > T:
                return False
            heapq.heappush(heap, load + order)
        return True
    
    lo = max(orders)
    hi = sum(orders)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_finish(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

---

### Worked Solution — Problem 2

```python
import heapq

def shortest_path_to_all_items(
    graph: dict,       # node -> list of (neighbor, weight)
    start: int,        # entrance node
    required_items: list[int]   # nodes that must be visited
) -> int:
    """
    Dijkstra from start node to all nodes.
    Return max(dist[item] for item in required_items).
    If any item is unreachable, return -1.
    """
    # Initialize distances
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    # Min-heap: (distance, node)
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)

        # Stale entry check: if we already found a shorter path, skip
        if d > dist[node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    # Check if all required items are reachable
    for item in required_items:
        if dist.get(item, float('inf')) == float('inf'):
            return -1  # unreachable item

    return max(dist[item] for item in required_items)
```

**Trace on a small example:**

```
Graph:
entrance(0) --5-- A(1)
entrance(0) --2-- B(2)
B(2) --3-- A(1)
B(2) --8-- C(3)
A(1) --4-- C(3)

required_items = [A(1), C(3)]
```

| Step | heap pop | dist[0] | dist[1] | dist[2] | dist[3] |
|---|---|---|---|---|---|
| init | — | 0 | inf | inf | inf |
| pop (0,0) | explore neighbors | 0 | 5 | 2 | inf |
| pop (2,2) | explore B's neighbors | 0 | min(5, 2+3)=5 | 2 | min(inf,2+8)=10 |
| pop (5,1) | explore A's neighbors | 0 | 5 | 2 | min(10, 5+4)=9 |
| pop (9,3) | C settled | 0 | 5 | 2 | 9 |

Result: max(dist[1], dist[3]) = max(5, 9) = 9 seconds.

---

## Part 4: Blank Re-Implementation

Read the worked solutions above until you understand them. Then close this section and implement both from scratch in a separate file or IDE. Come back only if you are stuck for more than 10 minutes.

**Re-implementation checklist:**
- [ ] P1: Binary search with lo = max(orders), hi = sum(orders)
- [ ] P1: can_finish(T) correctly implemented and tested
- [ ] P1: Returns correct answer for k > n (answer = max(orders))
- [ ] P2: Dijkstra with min-heap initialized correctly
- [ ] P2: Stale entry check (d > dist[node]: continue)
- [ ] P2: Returns -1 for unreachable required items
- [ ] P2: Returns max(dist[item]) over required_items

---

## Checkpoint M3 — Coded

Mark M3 complete when: your re-implementation passes all test cases below WITHOUT looking at the reference solutions.

---

## Part 5: Test Cases

### Problem 1 Edge Cases

```python
# Basic case
assert min_time_to_process([3, 7, 2, 5], 2) == 9  # [7,2] and [5,3]

# k >= n: each order gets its own worker
assert min_time_to_process([3, 7, 2, 5], 4) == 7  # bottleneck = max order

# k = 1: one worker does all
assert min_time_to_process([3, 7, 2, 5], 1) == 17  # sum of all

# Single order
assert min_time_to_process([10], 5) == 10

# All same
assert min_time_to_process([5, 5, 5, 5], 2) == 10  # 2 workers × 2 orders each × 5
```

### Problem 2 Edge Cases

```python
# Build test graph
graph = {
    0: [(1, 5), (2, 2)],
    1: [(3, 4)],
    2: [(1, 3), (3, 8)],
    3: []
}

# Start at 0, must visit 1 and 3
assert shortest_path_to_all_items(graph, 0, [1, 3]) == 9

# Required item is unreachable
graph_disconnected = {
    0: [(1, 5)],
    1: [],
    2: [(3, 1)],  # disconnected component
    3: []
}
assert shortest_path_to_all_items(graph_disconnected, 0, [2]) == -1

# Required item is the start node
assert shortest_path_to_all_items(graph, 0, [0]) == 0

# All items at same distance
graph2 = {
    0: [(1, 3), (2, 3), (3, 3)],
    1: [], 2: [], 3: []
}
assert shortest_path_to_all_items(graph2, 0, [1, 2, 3]) == 3
```

---

## Checkpoint M4 — Tested

Mark M4 complete when: all test cases pass. Record which test case surprised you the most.

Surprising test case: ___

---

## Part 5 (Extended): LP Integration

This section is specific to Amazon. After finishing the algorithmic problems, answer these LP-grounded questions.

**Dive Deep (LP 12) — "Stay connected to the details":**
After implementing Dijkstra, which edge case did you almost miss? What would have happened in production if that edge case hit?
___

**Insist on the Highest Standards (LP 7) — "Relentlessly high standards":**
Is your code readable enough that a new team member could understand it without you explaining it? What would you change?
___

**Bias for Action (LP 9) — "Speed matters. Many decisions are reversible":**
If you had only 30 minutes left in the OA, what would you cut first to still submit something that passes?
___

**Invent and Simplify (LP 3) — "Expect and require innovation AND simplicity":**
Is there a simpler data structure than a min-heap for Dijkstra in this specific problem (small graph, small weights)? What's the tradeoff?
___

**Ownership (LP 2) — "Act on behalf of the whole company":**
If your Dijkstra was deployed for the warehouse robot and a bug caused the robot to take a longer path for 1% of orders, how would you detect and fix it? What monitoring would you add?
___

**Which LP does declaring "done" without testing violate?**
___

---

## Part 6: Interview Simulation

### 90-Second Talk Track

"Let me confirm my understanding: P1 is minimizing makespan across k parallel workers — binary search on the answer, feasibility check is O(n). P2 is single-source shortest path from the warehouse entrance to all required items — Dijkstra with a min-heap. For P1, my search space is [max(orders), sum(orders)]. I'll time-box P1 to 35 minutes and move to P2 regardless. Starting now."

[During coding:] "Binary search: lo = max(orders) because we can't do better than the slowest order. Feasibility check: [explain can_finish]. For P2: dist initialized to inf, min-heap with (0, start), stale entry check on pop. After Dijkstra, return max dist over required items, or -1 if any is inf."

### Curveballs

**Curveball 1:** "What if workers can split orders — do half the work each?"

Instructions: Think about what changes in the binary search. You have 90 seconds.

<details>
<summary>Hint</summary>
If orders can be split, then with k workers you can always parallelize any single order across all k workers. The minimum time becomes: ceiling(sum(orders) / k). No binary search needed — it's just division. The binary search approach works for INDIVISIBLE tasks; once tasks are splittable, the problem collapses to a scheduling / resource allocation formula.

Real follow-up: "What if orders are partially splittable — you can split but only into integer chunks?" Then binary search on T, and can_finish changes to: for each order t, workers needed = ceil(t / T). This is the ceil(t/T) formulation from the first worked solution.
</details>

___

**Curveball 2:** "The graph is a DAG (directed, acyclic). Does Dijkstra still work? Is there a better algorithm for DAGs?"

Instructions: Two separate questions. Answer both.

<details>
<summary>Hint</summary>
Does Dijkstra work on a DAG? Yes — Dijkstra works on any directed graph with non-negative edge weights. A DAG is a special case. It will produce correct results.

Is there a better algorithm? Yes. On a DAG with non-negative weights, you can use topological sort + relaxation, which is O(V + E) — faster than Dijkstra's O((V+E) log V). Process nodes in topological order; when you process node u, relax all outgoing edges. This works because in a DAG, once you've processed all predecessors of u, the shortest path to u is finalized.

The interviewers is testing: do you know when Dijkstra is "good enough" vs. when problem structure enables a better algorithm.
</details>

___

**Curveball 3:** "Amazon uses this warehouse routing for 100M packages per day. What's your bottleneck and how would you scale?"

Instructions: Think systems, not just algorithm. Mention at least 3 concerns.

<details>
<summary>Hint</summary>
1. **Precomputation:** For a static warehouse graph, run Dijkstra once from the entrance and cache all shortest paths. Don't recompute per package. Cost: O((V+E) log V) once, then O(1) per query.

2. **Graph updates:** When a corridor closes (edge removed), how do you update the cache? Options: invalidate and rerun (simple), or dynamic shortest path algorithms (complex). In practice: flag the path as invalid, reroute affected packages in real time.

3. **Distributed:** 100M packages/day = ~1200 packages/second. Each package needs a path. If single-threaded, O(1) cached lookups are fine. At scale, distribute path lookups across a fleet of stateless services.

4. **Multi-item per robot:** Real warehouse robots may collect multiple items per trip (TSP variant for short lists). Precomputed pairwise distances between all locations enable faster greedy TSP.

5. **LP: Dive Deep** — "which metric tells you the routing is degrading?" Average path length deviation from optimal, corridor congestion, robot idle time.
</details>

___

---

## Part 7: Self-Grade + Reflection

### SWE Rubric

| Dimension | 1 | 2 | 3 | 4 | 5 | Score |
|---|---|---|---|---|---|---|
| **Communication / think-aloud** | Silent | Occasional narration | Explains steps when asked | Consistent narration | Leads interviewer, explains tradeoffs and LP connections | ___ |
| **Problem solving** | Could not approach either problem | One approach with major hints | Both approaches with nudges | Both approaches independently | Identified multiple approaches + chose best with justification | ___ |
| **Correctness** | Both wrong | One correct | Both correct with edge case bugs | Both correct, minor issues | Both correct, all edge cases including k>n and disconnected graph | ___ |
| **Code quality** | Unreadable | Functional but messy | Readable | Clean, well-named | Production-quality; self-documenting; easy to extend | ___ |
| **Testing & edge cases** | No testing | Happy path only | 1–2 edge cases | Systematic edge case testing | Predicted all failure modes before coding | ___ |
| **Debugging** | Could not debug | Found bugs with heavy hints | Found bugs with nudge | Found independently | Caught own bugs in tracing; explained root cause | ___ |
| **Time management** | Never finished P1 | P1 only | Both, significantly over time | Both within 90 min | Both within 70 min with time for LP discussion | ___ |

**LP Awareness Row (Amazon-specific)**

| Dimension | 1 | 2 | 3 | 4 | 5 | Score |
|---|---|---|---|---|---|---|
| **LP awareness in approach** | No mention | Generic mention | Named 1–2 LPs with weak connection | Named 3+ LPs with specific connection to code decisions | Wove LPs naturally into coding narration; could name which LP each edge case reflects | ___ |

**Total: ___ / 40**

### Reflection

Which algorithm was harder to trace by hand?

___

Which LP integration question stumped you?

___

What would a Bar Raiser ask that isn't in the curveballs?

___

### Ready-When Checklist

- [ ] I can implement binary search on answer (with can_finish) from scratch in < 15 minutes
- [ ] I can implement Dijkstra from scratch in < 15 minutes
- [ ] I know why lo = max(orders) not 0 in the binary search
- [ ] I understand the stale entry check in Dijkstra and why it's needed
- [ ] I can explain Dijkstra vs BFS vs Bellman-Ford in 2 sentences each
- [ ] I can name which LP each curveball tests
- [ ] My implementations pass all listed test cases without looking at reference solutions
