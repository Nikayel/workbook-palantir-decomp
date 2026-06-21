Status: Spec incomplete — fill in all blank fields before implementing

# Scenario

After a hurricane, multiple shelters have varying needs for water and medical kits. An NGO has 3 supply depots with limited inventory and a fleet of trucks. Road closures are changing every hour. They currently coordinate via radio and a whiteboard, which leads to some shelters getting double supplies while others get none. They need a system to allocate supplies optimally.

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

### Offline Sync
How will you handle data sync when a truck returns from an offline area? What is the payload structure?
__________________________________________________

### Conflict Resolution
What if two offline field workers claim the last pallet of water at the exact same timestamp? Which write wins?
__________________________________________________

### Prioritization Logic
How do you rank critical supplies (medical) versus standard supplies (blankets) in a constrained truck?
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

Curveball 1: A road closes after a truck has already been dispatched.
Your response:
__________________________________

Curveball 2: There is no cell service at the shelters to report their needs.
Your response:
__________________________________

# Self-grade

Score 1–5.

Total: __ / 50
