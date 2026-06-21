# Scenario

A manufacturing plant has 500 CNC machines. They currently do preventative maintenance every 30 days, which wastes time if the machine is fine, and misses breakdowns that happen on day 15. They have raw sensor data (temperature, vibration) streaming in. They want a system to detect anomalies and automatically create maintenance tickets for technicians before a machine breaks.

# Part 1: Clarifying questions

Goal:
1. ________________________________

Users:
1. ________________________________

Data:
1. ________________________________

Constraints:
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

# Part 3: System / API Design

API / Action design:
1. ________________________________

MVP vs V2:
MVP: ________________________________
V2: ________________________________

Tradeoff table:
| Decision | Option A | Option B | Choice | Why |
|---|---|---|---|---|
| ________________ | ________________ | ________________ | ________________ | ________________ |

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

Curveball 1: The sensor breaks and starts sending a value of 9999 for temperature.
Your response:
__________________________________

Curveball 2: The model generates too many alerts and the technicians ignore them.
Your response:
__________________________________

# Self-grade

Score 1–5.

Total: __ / 50
