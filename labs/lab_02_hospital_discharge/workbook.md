# Scenario

A hospital is struggling with bed availability. Patients who are "medically ready for discharge" are staying in beds for an extra 8-12 hours because of administrative blockers: waiting for a doctor's final signature, waiting for pharmacy medications, or waiting for transport. The hospital wants a system to identify these blockers and alert the right people.

# Part 1: Clarifying questions

Goal:
1. ________________________________
2. ________________________________

Users:
> Who is interacting with the system? Who is the most critical persona causing the bottleneck?
1. ________________________________
2. ________________________________

Data:
> What data sources exist? Are they real-time or batch? Are they notoriously messy or delayed?
1. ________________________________
2. ________________________________

Constraints:
> Are there strict latency, legal, safety, or offline requirements?
1. ________________________________
2. ________________________________

What assumptions will you make if the interviewer does not answer?
1. ________________________________

# Part 2: Decomposition

Current workflow:
1. ________________________________
2. ________________________________

Bottlenecks:
1. ________________________________

Core entities:
1. ________________________________
2. ________________________________

State transitions (for a Discharge Task):
1. ________________________________
2. ________________________________

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

Why did you choose this workflow?
__________________________________

What breaks if the data is stale?
__________________________________

What needs to be audited?
__________________________________

# Part 6: Interview Simulation

Curveball 1: A doctor signs the form, but the system doesn't update for 2 hours due to an upstream batch process. What happens?
Your response:
__________________________________

Curveball 2: Multiple departments point fingers at each other for the delay. How does your system resolve this?
Your response:
__________________________________

# Self-grade

Score 1–5.

Total: __ / 50
