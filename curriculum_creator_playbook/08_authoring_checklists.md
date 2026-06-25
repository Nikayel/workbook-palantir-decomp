# 08 · Authoring Checklists

> **Audience:** the curriculum creator.
> **Purpose:** copy-paste checklists for every stage. If a checklist item fails, the work isn't done. These operationalize `02` (science), `03` (standard), and `07` (counts).

---

## A. Before you start a lab — Design checklist
- [ ] I picked a **(company, role, tier, difficulty)** and read the matching **company pack** + **role guide** (`04`/`05`/`06`).
- [ ] I named the **exact interview moment** this lab simulates (e.g., "Stripe integration round").
- [ ] I wrote **1 measurable objective per section** before drafting (backward design, Principle 1).
- [ ] I chose the **primary skill** this lab isolates (one weakness, Principle 5) and what it deliberately does *not* grade.
- [ ] I confirmed where this lab sits in the track's **tier curve** (`07` §3) so scaffolding matches expertise.

## B. While authoring — Content checklist (the learning-science gate)
- [ ] Lab reaches **Analyze/Evaluate/Create**, not just recall (Principle 2).
- [ ] Skill is taught across a **worked → completion → blank** fade appropriate to the tier (Principle 3). Backward fading: blank the *last* steps first.
- [ ] Scenario is **authentic and messy** (a real product surface + at least one nasty data/constraint wrinkle) (Principle 6).
- [ ] **Part 0 forethought box** (goal, time-box, confidence) and **Part 7 reflection** (lowest-row → next action) are present (Principle 9).
- [ ] **Part 1 uses the Question/Assumption pairing** for every category.
- [ ] **Part 2 has tutorial annotations** (Tier 1/2) preventing the common errors (properties-as-entities; UI-flow-as-state-machine).
- [ ] **Part 3** has a concrete IO/API/data contract (a table, not prose) + 2–4 named design decisions + a tradeoff table.
- [ ] **Part 4** points at a `starter`/artifact with TODOs and the **edge cases to handle**.
- [ ] **Part 6** has exactly **3 curveballs** that inject a desirable difficulty.
- [ ] Every **`[blank]`** has a model answer somewhere in `solution_reasoning.md`.
- [ ] **No answer leakage**: model answers/reference solution are in separate files or collapsible `🔒` blocks — never visible next to the blank (Principle 3/10).
- [ ] One **new concept per blank**; worked example and its blanks are physically adjacent.

## C. Feedback & assessment checklist
- [ ] **Analytic rubric** with **countable 1–5 descriptors** (behavioral, not adjectives) (Principle 8) — using the role's rubric rows (`04`/`05`/`06`).
- [ ] `solution_reasoning.md` contains all **9 required sections** (`03` §7), including a **strong-vs-weak answer with the weak one annotated for *why***.
- [ ] **One rubric exemplar per level** (weak/adequate/strong) for calibration.
- [ ] Every model answer **references the rubric row** it satisfies (feed-forward).
- [ ] Feedback is phrased as **next actions**, not verdicts.

## D. Code/artifact checklist (SWE & Technical PM)
- [ ] `starter` docstring has **pre-coding reflection questions + an Expected Input Schema + a TODO list**.
- [ ] `tests` cover **the edge cases the workbook names** (not just a happy path) — fixes v1 gap G8.
- [ ] `reference_solution` is **clean, idiomatic, and runnable**; it passes `tests`.
- [ ] For **codebase-style** labs: the repo/scaffold runs; the "ship a feature" or "fix the failing test" task is achievable in ~45–60 min; rubric weights code quality/testing/diagnosis (`06` §3).
- [ ] For **Technical PM**: the artifact is a **spec/memo/SQL/data-model**, not production algorithm code.
- [ ] Language is **company-authentic** (Swift/Apple-iOS, C++/Nvidia, Node/APIs, SQL/data).

## E. Spaced-repetition checklist
- [ ] `flashcards.md` has **8–15 generative cards** (free recall, no visible answers).
- [ ] Cards cover **reusable primitives**, not lab-trivia.
- [ ] The **cadence note** (day 1 → 3 → 7 → 14; reset on miss) is at the top.

## F. Metadata & consistency checklist
- [ ] `meta.yml` is complete (`03` §5); `company`, `role`, `tier`, `difficulty`, `primary_skill` set.
- [ ] Folder named `<NN>_<company>_<slug>`; difficulty from the fixed ladder (`intro/easy/medium/hard/mock`).
- [ ] Voice is second-person, imperative, no hype; matches existing labs.
- [ ] **Every interview claim traces to the company pack → a source.** No invented interview facts.
- [ ] Required file set present (`03` §1): never missing `workbook.md`, `solution_reasoning.md`, `flashcards.md`.

## G. Pre-publish QA checklist (the gate before `status: published`)
- [ ] A test learner (or you, cold) can **attempt every part, get specific feedback on every part, and know the next action** — the keystone rule (`03` §11).
- [ ] Difficulty is **calibrated** against a sibling lab of the same tier (cross-company).
- [ ] No section produces zero gradable evidence (cut it if so).
- [ ] Markdown renders cleanly (tables, `<details>`, code fences).
- [ ] Tests run green; reference solution runs.
- [ ] Sources/confidence flags are present and honest (don't over-claim intern specifics).
- [ ] `meta.yml status` flipped `draft → review → published`.

## H. Company-pack completion checklist (per company)
- [ ] All 8 pack sections filled (`company_packs/README.md` template).
- [ ] SWE **style** decided (algorithmic vs codebase) and justified.
- [ ] The **signature artifact** is identified and has a lab in the build list.
- [ ] Facts re-verified this recruiting cycle; dates/OA/AI-policy flagged if stale.

## I. Course-assembly checklist (per company×role track)
- [ ] Lab count meets `07` §2; tier curve runs worked → blank (`07` §3).
- [ ] Three study plans written (sprint/standard/deep).
- [ ] A **Tier-3 mock capstone** exists.
- [ ] A cumulative flashcard deck spans the track.
- [ ] "Definition of complete" (`07` §6) satisfied.

## J. Release checklist (catalog-level)
- [ ] Cross-company calibration pass done (same-tier labs feel equivalent).
- [ ] Top-level catalog/index regenerated from `meta.yml`.
- [ ] Each company pack carries a "last verified: <cycle>" date.
- [ ] Known gaps/uncertainties documented (don't hide them).
