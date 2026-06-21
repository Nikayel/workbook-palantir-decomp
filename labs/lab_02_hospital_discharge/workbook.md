Status: Spec incomplete — fill in all blank fields before implementing

# Scenario

A hospital is struggling with bed availability. Patients who are "medically ready for discharge" are staying in beds for an extra 8-12 hours because of administrative blockers: waiting for a doctor's final signature, waiting for pharmacy medications, or waiting for transport. The hospital wants a system to identify these blockers and alert the right people.

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

Constraints:
> Are there strict latency, legal, safety, or offline requirements?
Question: [blank]
Assumption: [blank]

# Part 2: Decomposition

Current workflow:
1. [blank]
2. [blank]

Bottlenecks:
1. [blank]

Core entities:
1. [blank]
2. [blank]

State transitions (for a Discharge Task):
1. [blank]
2. [blank]

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

### Bottleneck Identification
How will you mathematically define a "bottleneck" between departments in code?
[blank]

### Data Messiness
What happens if the legacy system drops the "discharge_ordered" timestamp? How will you handle missing sequential data?
[blank]

### Alerting Thresholds
At what point (1 hour? 4 hours?) do you actually flag an anomaly to a human?
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

Why did you choose this workflow?
[blank]

What breaks if the data is stale?
[blank]

What needs to be audited?
[blank]

# Part 6: Interview Simulation

Curveball 1: A doctor signs the form, but the system doesn't update for 2 hours due to an upstream batch process. What happens?
Your response:
[blank]

Curveball 2: Multiple departments point fingers at each other for the delay. How does your system resolve this?
Your response:
[blank]

# Self-grade

Score 1–5.

Total: __ / 50
