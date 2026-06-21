Status: Spec incomplete — fill in all blank fields before implementing

# Scenario

A manufacturing plant has 500 CNC machines. They currently do preventative maintenance every 30 days, which wastes time if the machine is fine, and misses breakdowns that happen on day 15. They have raw sensor data (temperature, vibration) streaming in. They want a system to detect anomalies and automatically create maintenance tickets for technicians before a machine breaks.

# Part 1: Clarifying questions

Goal:
1. ________________________________

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

Bottlenecks:
1. ________________________________

Core entities:
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

### Time-Windowing
How will you group real-time sensor readings? Sliding windows or tumbling windows?
__________________________________________________

### Missing Data Handling
What if a sensor goes offline for 5 minutes? Do you interpolate the temperature, or drop the window?
__________________________________________________

### Alert Definition
Is an anomaly a sudden spike, or a sustained high temperature? How do you code that difference?
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
