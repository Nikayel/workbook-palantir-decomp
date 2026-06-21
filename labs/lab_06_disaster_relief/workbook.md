Status: Spec incomplete — fill in all blank fields before implementing

# Scenario

After a hurricane, multiple shelters have varying needs for water and medical kits. An NGO has 3 supply depots with limited inventory and a fleet of trucks. Road closures are changing every hour. They currently coordinate via radio and a whiteboard, which leads to some shelters getting double supplies while others get none. They need a system to allocate supplies optimally.

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

Bottlenecks:
1. [blank]

Core entities:
1. [blank]

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

### Offline Sync
How will you handle data sync when a truck returns from an offline area? What is the payload structure?
[blank]

### Conflict Resolution
What if two offline field workers claim the last pallet of water at the exact same timestamp? Which write wins?
[blank]

### Prioritization Logic
How do you rank critical supplies (medical) versus standard supplies (blankets) in a constrained truck?
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

What breaks if the data is stale?
[blank]

What should be real-time vs batch?
[blank]

# Part 6: Interview Simulation

Curveball 1: A road closes after a truck has already been dispatched.
Your response:
[blank]

Curveball 2: There is no cell service at the shelters to report their needs.
Your response:
[blank]

# Self-grade

Score 1–5.

Total: __ / 50
