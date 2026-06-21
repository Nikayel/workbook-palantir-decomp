# Coding Patterns

## 1. Top-K Items (Priority Queue)
When you need the "top 3 responders", use a min-heap or just sort if N is small.
- Python: `heapq.nsmallest(k, items, key=...)`
- Time: O(N log K)

## 2. Graph Traversal (BFS / DFS)
When finding a dependency chain or supply chain risk.
- Use a `visited` set to avoid cycles.

## 3. Time-Series & Intervals
When dealing with timestamps or shifts.
- Sort by start time.
- Merge overlapping intervals.

## 4. State Machines
When dealing with status changes (e.g., Pending -> Active -> Done).
- Use a dictionary or switch statement to define `VALID_TRANSITIONS`.
- Raise an error if an invalid transition is attempted.
