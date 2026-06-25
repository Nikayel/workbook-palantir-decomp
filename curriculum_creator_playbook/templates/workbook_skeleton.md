Status: Spec incomplete — fill in all blank fields before implementing

<!--
AUTHORING NOTES (delete before shipping):
- This is the GENERIC 8-part skeleton. Strip/adapt per role (03 §9) and tier (03 §3).
- Tier 1 (worked): fill ~60–80% as an annotated model; blank only the last steps.
- Tier 2 (completion): pre-fill structure; blank the load-bearing cells.
- Tier 3 (blank/mock): leave everything blank; keep only the rubric.
- Replace [blank] with model content in solution_reasoning.md, NEVER inline.
-->

# Scenario
<2–6 sentences of authentic, messy, company-skinned scenario. Include ≥1 nasty data/constraint wrinkle. Pull the product surface from the company pack.>

## 🪜 Milestones — check them off as you go
<!-- For coding labs, split M4 into L1→L4 code milestones, each gated by a test group. -->
- [ ] M1 · Scoped — clarifying questions + assumptions written
- [ ] M2 · Decomposed — entities + the one bottleneck identified
- [ ] M3 · Designed — contract / API / success-metric defined
- [ ] M4 · Built — < tests green | artifact complete & self-checked >
- [ ] M5 · Defended — survived all 3 curveballs out loud
- [ ] M6 · Ready — self-graded ≥ <bar>/<max>

# Part 0: Forethought
Goal (one sentence): [blank]
Target time: [blank] minutes
Confidence before starting (1–5): [blank]

# Part 1: Clarifying questions
> Demonstrate you can extract real constraints from an ambiguous prompt. Pair every question with an immediate assumption so you never freeze.

Pause. Do not design yet.

Goal:
> What business/operational outcome are we optimizing?
Question: [blank]
Assumption: [blank]

Users:
> Who interacts with the system? Who is the bottleneck persona?
Question: [blank]
Assumption: [blank]

Data:
> What sources exist? Real-time or batch? Messy or delayed?
Question: [blank]
Assumption: [blank]

Constraints:
> Latency, legal, safety, offline requirements?
Question: [blank]
Assumption: [blank]

Scale:
> Volume? Does the active state fit in memory?
Question: [blank]
Assumption: [blank]

<details><summary>Small hint (Tier 1/2 only)</summary>
<!-- a nudge toward the messiest data source / the real bottleneck -->
</details>

# Part 2: Decomposition
Current workflow:
*(Tutorial: map the existing/broken process to find the bottleneck step.)*
1. [blank]
2. [blank]
3. [blank]

Bottleneck:
*(Tutorial: which single step above is slowest or most error-prone?)*
1. [blank]

Core entities:
*(Tutorial: the nouns/tables of your NEW system — object names like 'Incident', NOT properties like 'address'.)*
1. [blank]
2. [blank]

State transitions (for the core entity):
*(Tutorial: the DB lifecycle, NOT the UI flow. e.g. OPEN → IN_PROGRESS → RESOLVED.)*
1. [blank]

# Part 3: System / contract design
## Input / Output contract
*(Tutorial: the exact function signature / JSON payload. Concrete variables, not abstract concepts.)*

**Input:**
| Parameter | Type | Description |
|---|---|---|
| [blank] | [blank] | [blank] |

**Output:**
| Key | Type | Description |
|---|---|---|
| [blank] | [blank] | [blank] |

## Named design decisions (2–4, specific to this lab's reality)
### [blank decision name]
[blank]

## Tradeoff table
| Decision | Option A | Option B | Choice | Why |
|---|---|---|---|---|
| [blank] | [blank] | [blank] | [blank] | [blank] |

# Part 4: Build
Open `starter.<ext>` and implement the TODOs. Run the tests.
<!-- PM labs: replace with "write the artifact" (PR-FAQ / memo / metric tree).
     Technical PM: produce a spec/SQL/data-model, not production code.
     SWE codebase: use the ICF 4-level structure (L1 design → L2 logic → L3 refactor → L4 extend). -->

Edge cases to handle:
1. [blank]
2. [blank]

# Part 5: System / reasoning write-up
Why these entities? [blank]
Why this workflow? [blank]
Why is this the right MVP? [blank]
What would you intentionally NOT build first? [blank]
What breaks if the data is stale? [blank]
What needs to be audited? [blank]
What needs permissions? [blank]
What should be real-time vs batch? [blank]
What is the simplest version that still helps the user? [blank]
What is the riskiest assumption? [blank]

# Part 6: Interview simulation
## 90-second talk track
<!-- use templates/blank_90_second_talktrack.md from the repo root -->

## Curveballs (answer out loud)
Curveball 1: [blank — inject a desirable difficulty: delayed data / an override / a total-failure case]
Your response: [blank]

Curveball 2: [blank]
Your response: [blank]

Curveball 3: [blank]
Your response: [blank]

# Part 7: Self-grade + reflection
<!-- paste the role-specific countable rubric from templates/rubric_bank.md -->
Score each row 1–5 against the descriptors.

Total: __ / __

One thing I did well: [blank]
One thing I missed: [blank]
Confidence now (1–5): [blank]   ← compare to your Part 0 prediction
Lowest rubric row → my next action: [blank]

## ✅ You're ready when…
<!-- 3–5 checkable, interview-realistic signals: cold, timed, aloud. Tune N and the bar per lab. -->
- [ ] You go scenario → working solution in < [blank] min **without** the hints.
- [ ] You give the 90-second talk track out loud **without notes**.
- [ ] You answer all 3 curveballs **without freezing**.
- [ ] You self-grade ≥ <bar>/<max> on **two** attempts running.
> Any unchecked box is your next rep. Repeat — or move up a tier — until all are checked.
