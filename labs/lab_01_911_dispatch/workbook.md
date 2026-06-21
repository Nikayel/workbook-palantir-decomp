Status: Spec incomplete — fill in all blank fields before implementing

# Scenario

You are building a system for a city's emergency dispatch center. Currently, dispatchers receive a call, look at a map, and manually decide which responder (police, fire, ambulance) to send. This takes too long and sometimes the closest responder is on a break or lacks the right equipment. They want a system to automatically recommend the top 3 best responders for an incident.

# Part 1: Clarifying questions

> In a Palantir interview, demonstrating you can extract the true constraints from an ambiguous prompt is critical. Use this section to write down the questions you would ask the interviewer before writing any code.

Pause. Do not design yet.

Goal:
> What is the primary business or operational outcome we are optimizing for?
Question: ________________________________
Assumption: ________________________________

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

Scale:
> What is the volume of data? Thousands of events or millions? Can the active state fit in memory?
Question: ________________________________
Assumption: ________________________________

<details>
<summary>Small hint</summary>

Think about the dispatcher, the response time, the current workflow, and the messiest data source (GPS).
</details>

# Part 2: Decomposition

Current workflow:
1. ________________________________
2. ________________________________
3. ________________________________

Bottlenecks:
1. ________________________________

Core entities:
1. ________________________________
2. ________________________________

State transitions (for a Responder):
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
*Complete the fields below before writing any code. These are specific to this lab's operational reality.*

### Ranking Strategy
How will the system rank responders? Will you filter first by equipment, or distance? How will you handle responders who are currently on break?
__________________________________________________

### Concurrency Boundary
What happens if two dispatchers try to assign the same responder to two different incidents at the exact same time?
__________________________________________________

### Fallback Behavior
What does your function return if no responders have the required equipment within a 50-mile radius? Note: failing open is dangerous.
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

Edge cases to handle:
1. ________________________________
2. ________________________________

# Part 5: System Design Reasoning

Why did you choose these entities?
__________________________________

Why did you choose this workflow?
__________________________________

Why is this the right MVP?
__________________________________

What would you intentionally NOT build first?
__________________________________

What breaks if the data is stale?
__________________________________

What needs to be audited?
__________________________________

What needs permissions?
__________________________________

What should be real-time vs batch?
__________________________________

What is the simplest version that would still help the user?
__________________________________

What is the riskiest assumption?
__________________________________

# Part 6: Interview Simulation

## 90-Second Explanation
Practice your talk track. Use the template in `templates/blank_90_second_talktrack.md`.

## Curveballs (answer out loud or write)

Curveball 1: The GPS data for responders is delayed by 5 minutes.
Your response:
__________________________________
__________________________________
__________________________________

Curveball 2: A dispatcher overrides the system's #1 recommendation and picks #3. How do we track this?
Your response:
__________________________________
__________________________________
__________________________________

Curveball 3: There are no available responders in the entire city. What does the system do?
Your response:
__________________________________
__________________________________
__________________________________

# Self-grade

Score 1–5.

Ambiguity handling: __ / 5  
Clarifying questions: __ / 5  
Workflow decomposition: __ / 5  
Data model: __ / 5  
API/action design: __ / 5  
System design reasoning: __ / 5  
Coding correctness: __ / 5  
Edge cases: __ / 5  
MVP judgment: __ / 5  
Communication: __ / 5  

Total: __ / 50

One thing I did well:
__________________________________

One thing I missed:
__________________________________

One thing I will improve next lab:
__________________________________
