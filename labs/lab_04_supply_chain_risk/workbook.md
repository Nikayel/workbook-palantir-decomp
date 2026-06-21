Status: Spec incomplete — fill in all blank fields before implementing

# Scenario

An automotive manufacturer has thousands of suppliers globally. When a natural disaster occurs (e.g., a port closure or earthquake), supply chain managers scramble to figure out which of their final cars will be delayed. Currently, they use Excel to trace the dependency graph from raw material -> sub-assembly -> car. They need a system to automatically propagate risk through the dependency graph.

# Part 1: Clarifying questions

Goal:
1. ________________________________

Users:
> Who is interacting with the system? Who is the most critical persona causing the bottleneck?
1. ________________________________

Data:
> What data sources exist? Are they real-time or batch? Are they notoriously messy or delayed?
1. ________________________________

What assumptions will you make if the interviewer does not answer?
1. ________________________________

# Part 2: Decomposition

Current workflow:
1. ________________________________

Bottlenecks:
1. ________________________________

Core entities:
1. ________________________________
2. ________________________________
3. ________________________________

# Part 3: System / API Contract

## Input / Output Contract
*Complete the tables below to define your API / function signature.*

**Input:**
| Parameter | Type | Description |
|-----------|------|-------------|
| _________ | ____ | ___________ |
| _________ | ____ | ___________ |

**Output:**
| Key | Type | Description |
|-----|------|-------------|
| ___ | ____ | ___________ |



## Detailed Design Decisions
*Complete the fields below before writing any code.*

### Traversal Approach
Will you use BFS or DFS to propagate disruption risk through the supplier graph, and why?
__________________________________________________

### Cycle Detection
What if supplier A depends on B, and B depends on A? How will your code avoid crashing?
__________________________________________________

### Risk Aggregation
How do you combine multiple minor risks from downstream suppliers into a single risk score?
__________________________________________________



## Implementation Notes
*Fill this in after implementing, before moving to the tests.*

One edge case or implementation detail that surprised you:
__________________________________________________

# Part 4: Coding Task
Open `starter.py` and implement the logic. Run `python tests.py`.

# Part 5: System Design Reasoning

Why did you choose these entities?
__________________________________

What breaks if the data is stale?
__________________________________

What should be real-time vs batch?
__________________________________

# Part 6: Interview Simulation

Curveball 1: Some suppliers don't report their sub-tier suppliers. You have gaps in the graph.
Your response:
__________________________________

Curveball 2: A disruption happens, but there is alternate inventory in a warehouse.
Your response:
__________________________________

# Self-grade

Score 1–5.

Total: __ / 50
