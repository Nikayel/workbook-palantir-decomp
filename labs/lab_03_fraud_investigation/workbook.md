Status: Spec incomplete — fill in all blank fields before implementing

# Scenario

A financial institution is getting overwhelmed with credit card fraud alerts. Their analysts currently look at a spreadsheet of raw transactions and have to manually look up the customer's history in 3 different tools to decide if a transaction is fraud. The process is slow and misses complex patterns. They want a platform to automatically score transactions and prioritize the riskiest ones for manual review.

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
2. ________________________________

# Part 2: Decomposition

Current workflow:
1. ________________________________
2. ________________________________

Bottlenecks:
1. ________________________________

Core entities:
1. ________________________________
2. ________________________________

State transitions (for an Alert):
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

### Anomaly Scoring
How will you weight different risk factors (e.g. shared IP vs. unusually large transaction)?
__________________________________________________

### False Positive Tradeoff
Alert fatigue is a huge issue. How will you ensure your threshold doesn't overwhelm analysts?
__________________________________________________

### Traversal Depth
When searching for linked fraudulent accounts, how deep will your graph traversal go to prevent infinite loops?
__________________________________________________

Tradeoff table:
| Decision | Option A | Option B | Choice | Why |
|---|---|---|---|---|
| ________________ | ________________ | ________________ | ________________ | ________________ |



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

What should be real-time vs batch?
__________________________________

# Part 6: Interview Simulation

Curveball 1: The algorithm creates too many false positives, and analysts are ignoring the alerts.
Your response:
__________________________________

Curveball 2: A customer travels to Europe, making all their transactions look like "impossible travel."
Your response:
__________________________________

# Self-grade

Score 1–5.

Total: __ / 50
