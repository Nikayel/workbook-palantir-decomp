Status: Spec incomplete — fill in all blank fields before implementing

# Scenario

You are building a system for a city's emergency dispatch center. Currently, dispatchers receive a call, look at a map, and manually decide which responder (police, fire, ambulance) to send. This takes too long and sometimes the closest responder is on a break or lacks the right equipment. They want a system to automatically recommend the top 3 best responders for an incident.

# Part 1: Clarifying questions

> In a Palantir interview, demonstrating you can extract the true constraints from an ambiguous prompt is critical. Use this section to write down the questions you would ask the interviewer before writing any code.

Pause. Do not design yet.

Goal:
> What is the primary business or operational outcome we are optimizing for?
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

Scale:
> What is the volume of data? Thousands of events or millions? Can the active state fit in memory?
Question: [blank]
Assumption: [blank]

<details>
<summary>Small hint</summary>

Think about the dispatcher, the response time, the current workflow, and the messiest data source (GPS).
</details>

# Part 2: Decomposition

Current workflow:
*(Tutorial: Map the existing legacy/broken process so you can find the exact step that causes the bottleneck. E.g. "1. User calls, 2. Dispatcher looks at map")*
1. [blank]
2. [blank]
3. [blank]

Bottlenecks:
*(Tutorial: Which specific step from the workflow above is the slowest or most error-prone?)*
1. [blank]

Core entities:
*(Tutorial: These are the "Nouns" or Database Tables for your NEW system. Do NOT list properties like 'address' here, just the object name like 'Incident' or 'Responder'.)*
1. [blank]
2. [blank]

State transitions (for a Responder):
*(Tutorial: This is the database lifecycle for the core entity, NOT the user's UI flow. E.g. OPEN -> IN_PROGRESS -> RESOLVED)*
1. [blank]
2. [blank]

# Part 3: System / API Contract

## Input / Output Contract
*(Tutorial: Think of this as the exact JSON payload or function arguments you will write in starter.py. Inputs are specific variables like 'incident: dict' or 'incident_id: str', NOT abstract concepts. Outputs are exactly what the function returns.)*
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
*Complete the fields below before writing any code. These are specific to this lab's operational reality.*

### Ranking Strategy
How will the system rank responders? Will you filter first by equipment, or distance? How will you handle responders who are currently on break?
[blank]

### Concurrency Boundary
What happens if two dispatchers try to assign the same responder to two different incidents at the exact same time?
[blank]

### Fallback Behavior
What does your function return if no responders have the required equipment within a 50-mile radius? Note: failing open is dangerous.
[blank]

Tradeoff table:
| Decision | Option A | Option B | Choice | Why |
|---|---|---|---|---|
| [blank] | [blank] | [blank] | [blank] | [blank] |



## Implementation Notes
*Fill this in after implementing, before moving to the tests.*

One edge case or implementation detail that surprised you:
[blank]

# Part 4: Coding Task
Open `starter.py` and implement the logic. Run `python tests.py`.

Edge cases to handle:
1. [blank]
2. [blank]

# Part 5: System Design Reasoning

Why did you choose these entities?
[blank]

Why did you choose this workflow?
[blank]

Why is this the right MVP?
[blank]

What would you intentionally NOT build first?
[blank]

What breaks if the data is stale?
[blank]

What needs to be audited?
[blank]

What needs permissions?
[blank]

What should be real-time vs batch?
[blank]

What is the simplest version that would still help the user?
[blank]

What is the riskiest assumption?
[blank]

# Part 6: Interview Simulation

## 90-Second Explanation
Practice your talk track. Use the template in `templates/blank_90_second_talktrack.md`.

## Curveballs (answer out loud or write)

Curveball 1: The GPS data for responders is delayed by 5 minutes.
Your response:
[blank]
[blank]
[blank]

Curveball 2: A dispatcher overrides the system's #1 recommendation and picks #3. How do we track this?
Your response:
[blank]
[blank]
[blank]

Curveball 3: There are no available responders in the entire city. What does the system do?
Your response:
[blank]
[blank]
[blank]

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
[blank]

One thing I missed:
[blank]

One thing I will improve next lab:
[blank]
