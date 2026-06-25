Status: Ready — work through all parts in order

# Scenario

You need to design a Case Management Platform for investigating high-priority operational incidents. 
Users (Analysts) will open cases, attach evidence (links to other systems), change case states, and close cases.
Supervisors must approve closures.

## 🪜 Milestones — check them off as you go
- [ ] M1 · Scoped — requirements clarified, constraints named
- [ ] M2 · Designed — data model + state machine defined
- [ ] M3 · API designed — endpoints specified with request/response
- [ ] M4 · Built — reference solution passes tests (`node tests.js`)
- [ ] M5 · Defended — handled concurrency + conflict-resolution curveballs
- [ ] M6 · Ready — self-graded ≥ 35/50

# Part 0: Forethought
> **Do this first.** Set a timer before starting.

Goal (one sentence): [blank]
Target time: 60 minutes
Confidence before starting (1–5): [blank]

# Part 1: Design

> **Before you write:** Read the scenario once. Close it. Write your questions from memory.

Fill out the templates in the `templates/` folder to design:
- Data model
- State machine
- APIs

> 🚩 **Checkpoint M1** — You have named the key requirements, at least 2 constraints, and identified the primary user personas. Missing anything? Fill it now.

> 🚩 **Checkpoint M2** — Data model has concrete field types, state machine shows all valid transitions with guards, at least one invalid transition explicitly blocked. Do not open api_design.js until this is done.

> 🚩 **Checkpoint M3** — Every API endpoint has: HTTP method + path, request body schema, response schema, and at least one error case. Tradeoffs for at least 2 design decisions are written down.

# Part 2: Coding Task

Open `api_design.js` and `state_machine.js`. Implement the validation logic and route handlers.

> 🚩 **Checkpoint M4** — Run `node tests.js`. All tests green before continuing.

# Part 3: Interview Simulation

> **Instructions:** Answer each curveball out loud before reading the next one. Time yourself — 90 seconds per curveball.

Curveball 1: An analyst tries to close a case, but the system crashes halfway through writing the audit log.
Your response (Idempotency / Transactions):
[blank]

Curveball 2: A supervisor needs to see all cases closed in the last 24 hours. How do you index the database?
Your response:
[blank]

Curveball 3: Two analysts simultaneously transition the same case to different states. How do you prevent a split-brain?
Your response:
[blank]

# Part 7: Self-grade + reflection

> Score each row 1–5. Be honest — this is for you.

| Dimension | 5 | 3 | 1 | Your score |
|---|---|---|---|---|
| Clarifying questions | Named requirements, constraints, and personas before designing | Named requirements but missed constraints or personas | Jumped straight to API design | __ /5 |
| Decomposition | Clear data model with concrete types; state machine covers all transitions including invalid ones | Data model present but types vague; state machine missing edge transitions | No data model or state machine before coding | __ /5 |
| API contract | Every endpoint has method, path, request/response schema, and error cases; 2+ design decisions documented | Most endpoints specified; some missing error cases or types | Endpoints named but no schema | __ /5 |
| Coding correctness | All tests green, validation logic handles invalid state transitions, audit log written | Core logic correct, 1–2 edge cases missed (e.g. concurrent writes) | Tests fail or state machine not enforced | __ /5 |
| Edge cases | Named and handled: concurrent state changes, crash mid-write, missing supervisor approval | 1–2 named, not all handled | Declared done without testing edge cases | __ /5 |
| System reasoning | Explains WHY for every decision; names what NOT to build; identifies riskiest assumption | Some WHY answers, misses a few | Describes WHAT, not WHY | __ /5 |
| Curveball handling | Answered all 3 without freezing; each response names a concrete mitigation | Answered 2 of 3; vague mitigations | Froze or said "I don't know" | __ /5 |
| MVP judgment | Clear V1 scope with explicit cuts; defers non-essential features with rationale | V1 defined but cuts not justified | Feature-creep or too minimal | __ /5 |
| Communication | Narrated tradeoffs; structured response; no jargon | Understandable but verbose | Silent or jargon-heavy | __ /5 |
| Time management | Finished core in < 60 min without hints | Finished but needed hints | Ran out of time on Part 1 | __ /5 |

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
