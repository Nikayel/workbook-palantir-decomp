Status: Spec incomplete — fill in all blank fields before implementing

# Scenario

An automotive manufacturer has thousands of suppliers globally. When a natural disaster occurs (e.g., a port closure or earthquake), supply chain managers scramble to figure out which of their final cars will be delayed. Currently, they use Excel to trace the dependency graph from raw material -> sub-assembly -> car. They need a system to automatically propagate risk through the dependency graph.

# Part 1: Clarifying questions

Goal:
Question: [blank]
Assumption: [blank]

Users:
> Who is interacting with the system? Who is the most critical persona causing the bottleneck?
Question: [blank]
Assumption: [blank]

Data:
> What data sources exist? Are they real-time or batch? Are they notoriously messy or delayed?
Question: [blank]
Assumption: [blank]

# Part 2: Decomposition

Current workflow:
1. [blank]

Bottlenecks:
1. [blank]

Core entities:
1. [blank]
2. [blank]
3. [blank]

# Part 3: System / API Contract

## Input / Output Contract
*Complete the tables below to define your API / function signature.*

**Input:**
| Parameter | Type | Description |
|-----------|------|-------------|
| [blank] | [blank] | [blank] |
| [blank] | [blank] | [blank] |

**Output:**
| Key | Type | Description |
|-----|------|-------------|
| [blank] | [blank] | [blank] |



## Detailed Design Decisions
*Complete the fields below before writing any code.*

### Traversal Approach
Will you use BFS or DFS to propagate disruption risk through the supplier graph, and why?
[blank]

### Cycle Detection
What if supplier A depends on B, and B depends on A? How will your code avoid crashing?
[blank]

### Risk Aggregation
How do you combine multiple minor risks from downstream suppliers into a single risk score?
[blank]



## Implementation Notes
*Fill this in after implementing, before moving to the tests.*

One edge case or implementation detail that surprised you:
[blank]

# Part 4: Coding Task
Open `starter.py` and implement the logic. Run `python tests.py`.

# Part 5: System Design Reasoning

Why did you choose these entities?
[blank]

What breaks if the data is stale?
[blank]

What should be real-time vs batch?
[blank]

# Part 6: Interview Simulation

Curveball 1: Some suppliers don't report their sub-tier suppliers. You have gaps in the graph.
Your response:
[blank]

Curveball 2: A disruption happens, but there is alternate inventory in a warehouse.
Your response:
[blank]

# Self-grade

Score 1–5.

Total: __ / 50
