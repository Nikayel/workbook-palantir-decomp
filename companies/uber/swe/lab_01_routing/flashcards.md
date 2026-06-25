# Flashcards — Uber SWE Lab 01: Dijkstra Routing

---

**Card 01 — Dijkstra Time Complexity (E log V)**

Q: What is Dijkstra's time complexity with a min-heap and why?

A: **O((V + E) log V)**, often simplified to O(E log V) for sparse graphs.

- Each vertex is added to the heap at most once per incoming edge: O(E) heap insertions
- Each heap insertion/extraction is O(log V) — heap size is bounded by number of nodes
- Total: O(E log V)

For Uber's city graph with V = 10,000 nodes and E = 50,000 edges:
- O(E log V) = 50,000 × 14 ≈ 700,000 operations — fast enough for < 100ms

Without a heap (naive): O(V²) = 100,000,000 — too slow.

---

**Card 02 — When to Use Bellman-Ford**

Q: Name three cases where you'd use Bellman-Ford instead of Dijkstra.

A:
1. **Negative edge weights present**: Dijkstra produces incorrect results with negative weights. Bellman-Ford handles them correctly.
2. **Negative cycles need to be detected**: Bellman-Ford can detect negative cycles (a cycle whose total weight is negative — Dijkstra cannot).
3. **Simpler implementation acceptable**: Bellman-Ford is O(VE), which is slower, but the code is simpler (no heap). Acceptable for small graphs.

At Uber: no negative weights in real routing (travel time can't be negative), so Dijkstra is always preferred.

---

**Card 03 — Negative Weight Detection**

Q: How does Bellman-Ford detect negative cycles?

A: Bellman-Ford runs V-1 relaxation passes (V = number of vertices). After V-1 passes, if any edge can still be relaxed (i.e., dist[u] + weight(u,v) < dist[v]), a negative cycle exists.

```python
def has_negative_cycle(graph, source):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    nodes = list(graph.keys())
    
    for _ in range(len(nodes) - 1):
        for u in nodes:
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    
    # Check for negative cycle
    for u in nodes:
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                return True   # negative cycle detected
    return False
```

---

**Card 04 — Path Reconstruction with Prev Map**

Q: How do you reconstruct the full path from start to end after running Dijkstra?

A: Maintain a `prev` dict that maps each node to its predecessor on the shortest path. After Dijkstra completes:

```python
# Reconstruct by following prev pointers from end to start
path = []
node = end
while node is not None:
    path.append(node)
    node = prev[node]
path.reverse()   # now start → end
```

Why reverse? We build the path backwards (end → start) following prev pointers, then reverse to get the correct order.

Edge case: if `prev[end]` is still None and `end != start`, no path exists.

---

**Card 05 — Uber ETA = Time Not Distance**

Q: Why does Uber optimize for travel time rather than distance?

A: A 2-mile route on a highway might take 5 minutes. A 1-mile route through downtown during rush hour might take 20 minutes. ETA (Estimated Time of Arrival) is what riders and drivers care about — not physical distance.

In Uber's routing:
- Edge weights = estimated travel time in seconds (adjusted for current traffic)
- Dijkstra finds the minimum-time path, not the minimum-distance path
- Traffic data updates edge weights in near-real-time (Uber has its own traffic sensing from GPS data of all moving vehicles)

This is why Uber's ETA predictions are more accurate than static map routing: they use real-time crowdsourced traffic data.

---

**Card 06 — Directed vs Undirected Graph Representation**

Q: How is a directed graph represented differently from an undirected graph in an adjacency list?

A:
```python
# Directed graph (one-way roads)
directed = {
    'A': [('B', 5)],      # A→B only; B cannot reach A via this edge
    'B': [('C', 3)],
    'C': []
}

# Undirected graph (two-way roads)
undirected = {
    'A': [('B', 5)],
    'B': [('A', 5), ('C', 3)],  # both directions stored
    'C': [('B', 3)]
}
```

For Uber: city graphs are **directed** because one-way streets exist. For every one-way street A→B, you add only `A: [(B, w)]`, not `B: [(A, w)]`.

---

**Card 07 — Precompute vs On-Demand Routing Tradeoff**

Q: Should Uber precompute all shortest paths or compute on demand per request?

A: Neither extreme is optimal. Uber uses a hybrid approach:

**On-demand Dijkstra per request:**
- Pro: always uses current traffic data
- Con: expensive at 1M+ requests/minute

**Fully precomputed (all-pairs shortest paths):**
- Pro: O(1) lookup
- Con: O(V²) storage (100M paths for 10K nodes), impossible to keep current with traffic

**Uber's actual approach (approximate):**
- Precompute shortest paths on a base static graph
- Apply real-time traffic as a multiplicative factor on edge weights
- Use hierarchical routing (precomputed highway routes + fine-grained local Dijkstra)
- Cache recently computed routes for common (driver_location, pickup_zone) pairs

"Act like owners" framing: the cost of on-demand = CPU spend; the cost of precompute = staleness + memory. Uber chooses based on where the real cost is.

---

**Card 08 — Traffic-Aware Edge Weights**

Q: How does Uber incorporate real-time traffic into its graph edge weights?

A: Every Uber vehicle (driver app) continuously broadcasts GPS coordinates to Uber's servers. By aggregating the speed of all vehicles on each road segment, Uber can estimate current travel time per segment.

Edge weight update:
```
base_weight = road_length / speed_limit   # static baseline
traffic_factor = actual_speed / speed_limit   # < 1 = congested, > 1 = flowing
current_weight = base_weight / traffic_factor
```

Weights are updated every ~30 seconds. Dijkstra runs on the current weight snapshot. This is why Uber ETA degrades during incidents — the routing graph reflects the traffic buildup in near-real-time.

---

**Card 09 — "Act Like Owners" in SWE Context**

Q: What does Uber's "act like owners" norm mean for a SWE making an algorithm choice?

A: An owner doesn't just pick an algorithm that works — they pick the one that's right for the business. This means:

1. **Model the cost**: Dijkstra at 100ms × 1M requests/min = significant compute spend. Is that acceptable?
2. **Consider the trade-off**: precomputing saves compute but uses memory and becomes stale. What's Uber's real constraint?
3. **Think about the customer**: a stale route that sends a driver into a traffic jam hurts rider ETA = fewer trips = less revenue
4. **Make the call**: don't just say "it depends." Give a recommendation with a reasoning: "I'd start with on-demand Dijkstra and add caching for top-10-requested route pairs in each city."

Saying "it depends" without a recommendation is not acting like an owner.

---

**Card 10 — Scale Reasoning (1M Requests/Min → Precomputation/Caching)**

Q: If Uber serves 1M routing requests per minute, how do you scale Dijkstra?

A: 1M requests/min = ~16,667 requests/second.

At 10ms per Dijkstra call: 1 server handles ~100 requests/sec → you need ~167 servers. Expensive.

Optimizations:
1. **Horizontal scaling**: route requests to different servers by city region
2. **Caching**: many requests are (driver_in_zone_X, pickup_in_zone_Y) — precompute and cache zone-to-zone ETAs
3. **Graph pruning**: for a pickup 2 miles away, you don't need to run Dijkstra on the entire city graph. Run only on the relevant subgraph (H3 hexagon or bounding box)
4. **Contraction hierarchies**: precompute a hierarchical routing structure that reduces query time to < 1ms (used by OpenStreetMap and Google Maps)
5. **Approximate routing**: at scale, a path that's 5% suboptimal but computed 10× faster is often the right trade-off
