# Scenario

After a hurricane, multiple shelters have varying needs for water and medical kits. An NGO has 3 supply depots with limited inventory and a fleet of trucks. Road closures are changing every hour. They currently coordinate via radio and a whiteboard, which leads to some shelters getting double supplies while others get none. They need a system to allocate supplies optimally.

# Part 1: Clarifying questions

Goal:
1. ________________________________

Users:
> Who is interacting with the system? Who is the most critical persona causing the bottleneck?
1. ________________________________

Data:
> What data sources exist? Are they real-time or batch? Are they notoriously messy or delayed?
1. ________________________________

Constraints:
> Are there strict latency, legal, safety, or offline requirements?
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

Curveball 1: A road closes after a truck has already been dispatched.
Your response:
__________________________________

Curveball 2: There is no cell service at the shelters to report their needs.
Your response:
__________________________________

# Self-grade

Score 1–5.

Total: __ / 50
