Status: Ready — work through all parts in order

# Scenario

You are building a system for a city's emergency dispatch center. Currently, dispatchers receive a call, look at a map, and manually decide which responder (police, fire, ambulance) to send. This takes too long and sometimes the closest responder is on a break or lacks the right equipment. They want a system to automatically recommend the top 3 best responders for an incident.

## 🪜 Milestones

- [ ] M1 · Scoped — clarifying questions + assumptions written
- [ ] M2 · Decomposed — entities + the one bottleneck named
- [ ] M3 · Designed — contract / tradeoffs / success metric defined
- [ ] M4 · Built — tests green (`python tests.py`)
- [ ] M5 · Defended — survived all 3 curveballs out loud
- [ ] M6 · Ready — self-graded ≥ 35/50 on two attempts

---

# Part 0: Forethought

Goal (one sentence): [blank]
Target time: 60 minutes
Confidence before starting (1–5): [blank]

---

# Part 1: Clarifying questions

> **Before you write:** Read the scenario once. Close it. Write your questions from memory.

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

> 🚩 **Checkpoint M1** — You should have 5 questions each paired with an assumption. If you skipped any, go back now.

---

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

> 🚩 **Checkpoint M2** — You have a workflow, exactly one bottleneck, 2+ entity names (nouns only), and state transitions that are DB lifecycle (not UI). If any are missing, fill them before continuing.

---

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

> 🚩 **Checkpoint M3** — Your contract table has concrete types (not "[blank]"), you've named 2+ design decisions, and filled the tradeoff table. Do this before opening starter.py.

---

# Part 4: Coding Task
Open `starter.py` and implement the logic. Run `python tests.py`.

Edge cases to handle:
1. [blank]
2. [blank]

> 🚩 **Checkpoint M4** — Run `python tests.py`. All tests must be green before moving on.

---

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

---

# Part 6: Interview Simulation

## 90-Second Explanation
Practice your talk track. Use the template in `templates/blank_90_second_talktrack.md`.

## Curveballs (answer out loud or write)

> **Instructions:** Answer each curveball out loud (or write) before reading the next one. Time yourself — you have 90 seconds per curveball.

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

---

# Part 7: Self-grade + reflection

> Score each row 1–5 using the descriptors. Be honest — this is for you.

| Dimension | 5 | 3 | 1 | Your score |
|---|---|---|---|---|
| Clarifying questions | 5 paired Q+A tied to design decisions | 3–4 questions, some assumptions, loose tie | 0–1 questions, jumped to solution | __ /5 |
| Decomposition | Clear workflow → bottleneck, entity names are nouns (not properties), state transitions are DB lifecycle | Workflow present but bottleneck unclear; mixed properties and entities | Minimal decomp, no clear states | __ /5 |
| API contract | Concrete types in every table cell; 2+ named decisions; tradeoff table filled | Some cells filled, 1 decision named | All blank or abstract concepts | __ /5 |
| Coding correctness | All tests green, handles edge cases | Core logic correct, 1–2 edge cases missed | Tests fail or logic broken | __ /5 |
| Edge cases | Named and handled: empty input, stale data, no results, concurrency | 1–2 named, not all handled | Declared done without testing | __ /5 |
| System reasoning | Explains WHY for every decision; names what NOT to build; identifies riskiest assumption | Some WHY answers, misses a few | Describes WHAT, not WHY | __ /5 |
| Curveball handling | Answered all 3 without freezing; each response names a concrete mitigation | Answered 2 of 3; vague mitigations | Froze or said "I don't know" | __ /5 |
| MVP judgment | Clear V1 scope with explicit cuts; defers non-essential features with rationale | V1 defined but cuts not justified | Feature-creep or too minimal | __ /5 |
| Communication | Narrated tradeoffs; structured response; no jargon | Understandable but verbose | Silent or jargon-heavy | __ /5 |
| Time management | Finished core in < 60 min without hints | Finished but needed hints | Ran out of time on Part 3 | __ /5 |

**Total: __ / 50**

One thing I did well: [blank]
One thing I missed: [blank]
Confidence now (1–5): [blank] ← compare to your Part 0 prediction
Lowest rubric row → my next action: [blank]

## ✅ You're ready when…
- [ ] You go scenario → working solution in < 45 min **without** the hints.
- [ ] You give the 90-second talk track out loud **without notes**.
- [ ] You answer all 3 curveballs **without freezing**.
- [ ] You self-grade ≥ 35/50 on **two** attempts running.

> Any unchecked box is your next rep. Repeat until all four are checked.
