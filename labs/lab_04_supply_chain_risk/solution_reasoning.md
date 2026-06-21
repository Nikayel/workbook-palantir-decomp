# Solution Reasoning

## 0. Clarifying Questions Answer Key
- **Goal**: 
  - *Question*: Do we need to reroute supply, or just identify which cars are delayed?
  - *Assumption*: I'll assume the primary goal is just mapping the blast radius of the disruption.
- **Users**: 
  - *Question*: Who consumes this data?
  - *Assumption*: I'll assume supply chain managers looking at a dashboard.
- **Data**: 
  - *Question*: Is the dependency graph a strict tree, or a directed graph with cycles?
  - *Assumption*: I'll assume it's a directed graph that might contain cycles (Supplier A relies on B, B relies on A).
- **Constraints**: 
  - *Question*: How quickly do they need this report after a disaster hits?
  - *Assumption*: I'll assume within minutes, not milliseconds.
- **Scale**: 
  - *Question*: How many nodes (suppliers/parts) are in the graph?
  - *Assumption*: I'll assume ~100,000 nodes, which can be traversed quickly using BFS/DFS in memory.


## 1. Why these users?
Supply Chain Managers need to quickly contact alternate suppliers or delay production lines.

## 2. Why this workflow?
By mapping the graph in advance, a disruption event triggers an automated DFS/BFS to instantly highlight affected end-products, turning a 3-day Excel exercise into a 5-second query.

## 3. Why this data model?
Nodes are Suppliers and Products. Edges are Dependencies.

## 4. Why these APIs/actions?
- `POST /simulate-disruption`: Allows the user to do scenario planning ("what if Port X closes?").

## 5. Failure modes
- **Data silos**: Enterprise data is notoriously messy. Product Mappings might be out of date.
- **Cycles in data**: Bad data entry might create `A -> B -> A`. The code must use a `visited` set.

## 6. Strong vs weak answer
**Weak**: "I'll put it all in a SQL database and use JOINs." (Deep dependencies require recursive queries which are slow and hard to maintain in pure SQL without graph tools).
**Strong**: "I'll model this as a directed acyclic graph (DAG). I will run a BFS from the point of disruption, collecting all downstream nodes, and map those to the final SKUs."
