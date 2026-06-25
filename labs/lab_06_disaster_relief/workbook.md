Status: Ready — work through all parts in order

# Scenario

After a hurricane, multiple shelters have varying needs for water and medical kits. An NGO has 3 supply depots with limited inventory and a fleet of trucks. Road closures are changing every hour. They currently coordinate via radio and a whiteboard, which leads to some shelters getting double supplies while others get none. They need a system to allocate supplies optimally.

## 🪜 Milestones — check them off as you go
- [ ] M1 · Scoped — clarifying questions + assumptions written
- [ ] M2 · Decomposed — entities + the one bottleneck named
- [ ] M3 · Designed — contract / tradeoffs / success metric defined
- [ ] M4 · Built — tests green (`python tests.py`)
- [ ] M5 · Defended — survived all 3 curveballs out loud
- [ ] M6 · Ready — self-graded ≥ 35/50 on two attempts

# Part 0: Forethought
> **Do this first.** Set a timer before starting.

Goal (one sentence): [blank]
Target time: 60 minutes
Confidence before starting (1–5): [blank]

# Part 1: Clarifying questions

> **Before you write:** Read the scenario once. Close it. Write your questions from memory.

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

> 🚩 **Checkpoint M1** — You have 5 questions each paired with an assumption. If any are missing, go back now.

# Part 2: Decomposition

Current workflow:
1. [blank]

Bottlenecks:
1. [blank]

Core entities:
1. [blank]

> 🚩 **Checkpoint M2** — Workflow mapped, exactly one bottleneck named, 2+ entity names (nouns, not properties), state transitions show DB lifecycle. Missing anything? Fill it now.

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

> 🚩 **Checkpoint M3** — Contract table has concrete types, 2+ named design decisions filled, tradeoff table complete. Do not open starter.py until this is done.

# Part 4: Coding Task
Open `starter.py` and implement the logic. Run `python tests.py`.

> 🚩 **Checkpoint M4** — Run `python tests.py`. All tests green before continuing.

# Part 5: System Design Reasoning

Why did you choose these entities?
[blank]

What breaks if the data is stale?
[blank]

What should be real-time vs batch?
[blank]

# Part 6: Interview Simulation

> **Instructions:** Answer each curveball out loud before reading the next one. Time yourself — 90 seconds per curveball.

Curveball 1: A road closes after a truck has already been dispatched.
Your response:
[blank]

Curveball 2: There is no cell service at the shelters to report their needs.
Your response:
[blank]

Curveball 3: Two depots both claim they sent supplies to the same shelter, but the shelter says it received nothing.
Your response:
[blank]

# Part 7: Self-grade + reflection

> Score each row 1–5. Be honest — this is for you.

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
