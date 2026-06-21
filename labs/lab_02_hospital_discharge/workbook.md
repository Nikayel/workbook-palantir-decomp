Status: Spec incomplete — fill in all blank fields before implementing

# Scenario

A hospital is struggling with bed availability. Patients who are "medically ready for discharge" are staying in beds for an extra 8-12 hours because of administrative blockers: waiting for a doctor's final signature, waiting for pharmacy medications, or waiting for transport. The hospital wants a system to identify these blockers and alert the right people.

# Part 1: Clarifying questions

Goal:
1. ________________________________
2. ________________________________

Users:
> Who is interacting with the system? Who is the most critical persona causing the bottleneck?
Question: ________________________________
Assumption: ________________________________

Data:
> What data sources exist? Are they real-time or batch? Are they notoriously messy or delayed?
Question: ________________________________
Assumption: ________________________________

Constraints:
> Are there strict latency, legal, safety, or offline requirements?
Question: ________________________________
Assumption: ________________________________

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

### Bottleneck Identification
How will you mathematically define a "bottleneck" between departments in code?
__________________________________________________

### Data Messiness
What happens if the legacy system drops the "discharge_ordered" timestamp? How will you handle missing sequential data?
__________________________________________________

### Alerting Thresholds
At what point (1 hour? 4 hours?) do you actually flag an anomaly to a human?
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
