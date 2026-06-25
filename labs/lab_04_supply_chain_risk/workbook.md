Status: Ready — work through all parts in order

# Scenario

An automotive manufacturer has thousands of suppliers globally. When a natural disaster occurs (e.g., a port closure or earthquake), supply chain managers scramble to figure out which of their final cars will be delayed. Currently, they use Excel to trace the dependency graph from raw material -> sub-assembly -> car. They need a system to automatically propagate risk through the dependency graph.

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
> How many suppliers and parts are in the graph? Can the entire dependency graph fit in memory?
Question: [blank]
Assumption: [blank]

> 🚩 **Checkpoint M1** — You should have 5 questions each paired with an assumption. If you skipped any, go back now.

---

# Part 2: Decomposition

Current workflow:
1. [blank]

Bottlenecks:
1. [blank]

Core entities:
1. [blank]
2. [blank]
3. [blank]

State transitions (for a Supplier):
1. [blank]
2. [blank]

> 🚩 **Checkpoint M2** — You have a workflow, exactly one bottleneck, 2+ entity names (nouns only), and state transitions that are DB lifecycle (not UI). If any are missing, fill them before continuing.

---

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

### Traversal Approach
Will you use BFS or DFS to propagate disruption risk through the supplier graph, and why?
[blank]

### Cycle Detection
What if supplier A depends on B, and B depends on A? How will your code avoid crashing?
[blank]

### Risk Aggregation
How do you combine multiple minor risks from downstream suppliers into a single risk score?
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

Curveball 1: Some suppliers don't report their sub-tier suppliers. You have gaps in the graph.
Your response:
[blank]
[blank]
[blank]

Curveball 2: A disruption happens, but there is alternate inventory in a warehouse.
Your response:
[blank]
[blank]
[blank]

Curveball 3: The supply chain manager wants to model a "what-if" scenario — what if this port closes for 30 days? How does your system support that?
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
