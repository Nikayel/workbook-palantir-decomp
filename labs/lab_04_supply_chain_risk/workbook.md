# Scenario

An automotive manufacturer has thousands of suppliers globally. When a natural disaster occurs (e.g., a port closure or earthquake), supply chain managers scramble to figure out which of their final cars will be delayed. Currently, they use Excel to trace the dependency graph from raw material -> sub-assembly -> car. They need a system to automatically propagate risk through the dependency graph.

# Part 1: Clarifying questions

Goal:
1. ________________________________

Users:
1. ________________________________

Data:
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

# Part 3: System / API Design

API / Action design:
1. ________________________________

MVP vs V2:
MVP: ________________________________
V2: ________________________________

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
