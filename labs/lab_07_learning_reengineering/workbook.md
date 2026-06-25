Status: Ready — work through all parts in order

# Scenario

You have inherited a legacy piece of code written by a former intern. It is supposed to assign support tickets to agents. However, users are complaining that tickets are being assigned to agents who are currently on vacation, the highest priority tickets are being ignored, and sometimes the system throws weird errors.

Your job is to read the code, find the bugs, fix them, and add a new feature.

## 🪜 Milestones — check them off as you go
- [ ] M1 · Read — understood what the code is trying to do (without running it)
- [ ] M2 · Audited — listed 5+ bugs/issues
- [ ] M3 · Tested — wrote tests that expose the bugs
- [ ] M4 · Fixed — all bugs fixed, tests green
- [ ] M5 · Extended — new feature added without breaking existing tests
- [ ] M6 · Ready — self-graded ≥ 35/50

# Part 0: Forethought
> **Do this first.** Set a timer before starting.

Goal (one sentence): [blank]
Target time: 60 minutes
Confidence before starting (1–5): [blank]

# Part 1: Understand the Code

> **Before you write:** Read the scenario once. Close it. Write your questions from memory.

Read `starter.py`. Without running it, explain what it is *trying* to do:
[blank]
[blank]

> 🚩 **Checkpoint M1** — You have written what the code is trying to do in your own words, without running it. If you cannot explain its intent, re-read starter.py before continuing.

# Part 2: Find the Bugs

List the 5 bugs you found in the code.
1. [blank]
2. [blank]
3. [blank]
4. [blank]
5. [blank]

> 🚩 **Checkpoint M2** — You have listed 5+ specific bugs (not vague descriptions). Each bug names: what line or function, what it does wrong, and what the correct behavior should be. Missing anything? Fill it now.

# Part 3: Write Tests

Open `tests.py`. Write tests that trigger the bugs you found.

> 🚩 **Checkpoint M3** — Each bug from Part 2 has a corresponding failing test. Run `python tests.py` — tests should FAIL right now (they expose real bugs). Do not fix anything yet.

# Part 4: Fix and Extend

Fix the bugs in `starter.py`.

**New Requirement**:
The business now wants to route tickets based on `language`. If a ticket is marked `es` (Spanish), it MUST go to an agent who has `es` in their `languages` array.

> 🚩 **Checkpoint M4** — Run `python tests.py`. All tests green before continuing.

# Part 5: Reasoning

Why did the original code mutate the input array? Why is that bad?
[blank]

How did you preserve the existing behavior while adding the language requirement?
[blank]

# Part 6: Interview Simulation

> **Instructions:** Answer each curveball out loud before reading the next one. Time yourself — 90 seconds per curveball.

Curveball 1: A new requirement says that if no agent speaks the required language, the ticket should be queued rather than assigned to a random agent. How do you change the code without breaking existing behavior?
Your response:
[blank]

Curveball 2: The system needs to handle 10,000 tickets per minute. Where does your current implementation break down first?
Your response:
[blank]

Curveball 3: The intern who wrote this code is asked to review your changes. They argue that mutating the input is faster. How do you respond?
Your response:
[blank]

# Part 7: Self-grade + reflection

> Score each row 1–5. Be honest — this is for you.

| Dimension | 5 | 3 | 1 | Your score |
|---|---|---|---|---|
| Code reading | Explained intent accurately without running code; identified all major data flows | Explained most of the intent; missed 1 data flow | Could not explain without running; guessed | __ /5 |
| Bug identification | Named 5+ bugs with file/line/description of wrong vs correct behavior | Named 3–4 bugs; descriptions vague | Named 0–2 bugs or only surface-level descriptions | __ /5 |
| Test quality | Each bug has a focused failing test before fixing; tests are specific and readable | Tests exist but cover only some bugs; some tests too broad | No tests written before fixing, or tests always pass | __ /5 |
| Coding correctness | All bugs fixed, all tests green, no regressions | Core bugs fixed, 1–2 edge cases missed | Tests fail or new bugs introduced | __ /5 |
| Feature extension | New feature added cleanly; existing tests still green; no mutations of caller data | New feature works but breaks 1 existing test | Feature doesn't work or causes regressions | __ /5 |
| Defensive programming | Input validation, handles None/empty, no silent failures | Handles some edge cases | Assumes happy path only | __ /5 |
| Code quality | Clear names, small functions, no side effects, self-documenting | Readable but some long functions or unclear names | Hard to follow; magic numbers; no comments | __ /5 |
| Curveball handling | Answered all 3 without freezing; each response names a concrete mitigation | Answered 2 of 3; vague mitigations | Froze or said "I don't know" | __ /5 |
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
