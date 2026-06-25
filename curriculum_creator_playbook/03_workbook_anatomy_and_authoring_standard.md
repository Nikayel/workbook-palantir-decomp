# 03 · Workbook Anatomy & Authoring Standard

> **Audience:** the curriculum creator (you).
> **Purpose:** the single source of truth for *how a workbook is built*. If `02` is the science, this is the spec. Follow it so every lab — across PM, Technical PM, and SWE, across all 10 companies — looks and behaves consistently. Consistency is itself a learning feature (Principle 12: inconsistent depth breaks transfer).

This standard is a **perfected** version of the existing Palantir v1 labs (`/labs/`). It keeps what worked (the 6-part decomposition flow, the Question/Assumption pairing, the self-grade rubric) and fixes what didn't (uneven depth, no fading, thin feedback, no metadata, SWE-only, single-company). See `10_v1_audit_and_gap_analysis.md` for the full before/after.

---

## 1. The unit of work: a **Lab**

A **lab** is one self-contained practice instrument simulating **one interview moment**, sized for **45–75 minutes** of focused work. A lab is a **folder**, not a file. Every lab folder MUST contain this file set:

```
labs/<NN>_<slug>/
├── meta.yml              # machine-readable metadata (see §5)
├── README.md             # orientation + time plan + the interview moment it simulates
├── workbook.md           # THE learner-facing fill-in-the-blank instrument (the core)
├── starter.<ext>         # code/artifact scaffold with TODOs (SWE & Technical PM; optional for PM)
├── tests.<ext>           # runnable tests / acceptance checks (SWE & Technical PM)
├── reference_solution.<ext>  # the model implementation (revealed only after attempt)
├── solution_reasoning.md # answer key: model answers + strong-vs-weak + tradeoffs + failure modes
└── flashcards.md         # 8–15 generative spaced-repetition cards
```

- **PM labs** usually drop `starter`/`tests`/`reference_solution` and instead carry an `artifacts/` folder (e.g., a PR-FAQ template, a metric tree, a written-memo prompt). They keep `workbook.md`, `solution_reasoning.md`, `flashcards.md`.
- **Technical PM** and **SWE** labs keep the full set; "code" for a Technical PM may be an API spec (`openapi.yaml`), a SQL file, or a data-model file rather than an algorithm.
- Never ship a lab missing `workbook.md`, `solution_reasoning.md`, or `flashcards.md`. Those three carry the pedagogy.

---

## 2. The canonical lab structure (8 parts)

Every `workbook.md` follows this 8-part spine. Parts 0 and 7 are **new vs v1** (forethought + reflection) and are mandatory — they carry the metacognition layer (Principle 9). Parts map to Bloom levels (Principle 2) so each lab climbs to the top half.

| Part | Name | Bloom | Mandatory? | What it does |
|---|---|---|---|---|
| **0** | Forethought box | — | ✅ | goal, time-box, confidence prediction (1–5) |
| **1** | Scenario + clarifying questions | Analyze | ✅ | authentic ambiguous prompt; Question **paired with** Assumption |
| **2** | Decomposition | Analyze | ✅ | users, current workflow, bottleneck, entities, state transitions |
| **3** | System / contract design | Create | ✅ | IO contract / API / data model + design decisions + tradeoff table |
| **4** | Build (code / artifact) | Apply | role-dependent | implement against `starter` + run `tests`; or write the artifact (PR-FAQ, memo) |
| **5** | Reasoning write-up | Evaluate | ✅ | why this MVP, what breaks, what to audit, riskiest assumption |
| **6** | Interview simulation | Evaluate | ✅ | 90-second talk track + 3 curveballs |
| **7** | Self-grade + reflection | Evaluate | ✅ | analytic rubric, then "lowest row → next action" |

### Part-by-part authoring rules

**Part 0 — Forethought box.** 3 lines: a one-sentence goal, a target minutes figure, and "Confidence before starting (1–5): ___". Keeps the learner in the self-regulation loop.

**Part 1 — Scenario + clarifying questions.**
- The scenario is **2–6 sentences of authentic mess** (a real operational problem with at least one nasty data/constraint wrinkle). No toy abstractions.
- Use the **Question/Assumption pairing** — the v1 innovation we keep and enforce everywhere. Each prompt category (Goal, Users, Data, Constraints, Scale) gets a `Question: [blank]` immediately followed by `Assumption: [blank]`. This trains the candidate to never freeze: ask *and* assume in one breath.
- Include a collapsible `<details>` **Small hint** for early-tier labs only.

**Part 2 — Decomposition.** Five sub-blanks with **tutorial annotations** (the parenthetical coaching v1 added — keep it): Current workflow → Bottleneck → Core entities (nouns/tables, not properties) → State transitions (DB lifecycle, not UI flow). The annotation prevents the most common novice errors (listing properties as entities; confusing UI flow with state machine).

**Part 3 — System / contract design.**
- An **Input/Output contract table** (parameter, type, description) — concrete function signature or JSON payload, never abstract concepts.
- 2–4 **named design decisions** specific to this lab's operational reality (e.g., "Concurrency boundary," "Fallback behavior," "Idempotency").
- A **tradeoff table**: Decision | Option A | Option B | Choice | Why.

**Part 4 — Build.** Points the learner at `starter.<ext>`; lists the TODOs and the **edge cases to handle**. For PM labs this becomes "write the artifact" (a PR-FAQ, a metric definition, a written memo) with a structure prompt.

**Part 5 — Reasoning write-up.** The articulation step (Principle 6). Fixed prompt set: why these entities / why this workflow / why this MVP / what you would NOT build first / what breaks if data is stale / what needs audit / what needs permissions / real-time vs batch / simplest version that still helps / riskiest assumption.

**Part 6 — Interview simulation.** A 90-second talk-track scaffold (use `templates/`), then **exactly 3 curveballs** — each an *out-loud* response prompt that injects a desirable difficulty (delayed data, an override, a total-failure case). Curveballs are where the lab works at the edge of ability (Principle 5).

**Part 7 — Self-grade + reflection.** The analytic rubric (§6) followed by three reflection lines: "One thing I did well / One thing I missed / One thing I'll improve next lab," plus "Lowest rubric row → my next action."

---

## 3. The three fade tiers (the fill-in-the-blank engine)

Every lab is authored at **one** of three scaffolding tiers. A *course* moves learners from Tier 1 → Tier 3 (Principles 3–4). You decide a lab's tier in `meta.yml` (`tier: 1|2|3`) and author the blanks accordingly.

| Tier | Name | % pre-filled | Worked example? | Hints | Use for |
|---|---|---|---|---|---|
| **1** | Worked / Tutorial | 60–80% | Full annotated model shown inline | Generous | first 1–3 labs of a track |
| **2** | Completion | 30–60% | Partial; load-bearing parts blanked | Collapsible | middle of a track |
| **3** | Blank / Mock | 0–15% | None; rubric only | None | last 2–3 labs (full mock) |

**Backward fading is the default:** blank the *last* steps first. E.g., a Tier-2 lab gives the entities and workflow (early steps) and blanks the state transitions, tradeoff table, and edge cases (later steps).

**Authoring a faded blank.** Use the literal token `[blank]` for a fill-in (v1 used this; keep it — it renders cleanly and is greppable). For a *completion* blank, pre-fill the surrounding structure and leave only the load-bearing cell empty. One new concept per blank.

**Hint discipline.** Hints live in collapsible `<details><summary>…</summary>` blocks so they never leak into the learner's field of view before they attempt (Principle 3, anti-leakage). Tier-3 labs have no hints.

**Hide-hints / parallel version.** For learners who out-grow a tier, ship a `workbook.blank.md` parallel that strips the worked example — cheaper than re-authoring. Note it in `meta.yml` (`has_blank_variant: true`).

---

## 4. The blank & reveal conventions

- **Fill-in token:** `[blank]` (not markdown underscores — v1 migrated away from `____` for UX; do not regress).
- **Reveal-after-attempt:** model answers and reference solutions live in **separate files** (`solution_reasoning.md`, `reference_solution.*`) or in collapsible `<details>` blocks marked `🔒 Open only after you attempt`. Never put a model answer adjacent-and-visible to its blank.
- **Tables with blanks:** keep the header row and one example row filled; blank the practice rows.

---

## 5. `meta.yml` — the metadata standard (new vs v1)

Every lab carries machine-readable metadata so the catalog, study plans, and coverage matrix (`07`) can be generated and audited. Minimum schema:

```yaml
id: meta_03_notification_ranking
title: "Rank the Notifications Feed"
company: meta            # one of the 10, or "generic"
role: pm                 # pm | technical_pm | swe
interview_moment: "Meta product-sense + execution screen"
tier: 2                  # 1 worked | 2 completion | 3 blank/mock
difficulty: medium       # intro | easy | medium | hard | mock
est_minutes: 60
primary_skill: "metric selection under ambiguity"
secondary_skills: ["user segmentation", "tradeoff articulation"]
bloom_top: evaluate      # highest level the lab reaches
language: none           # python | node | sql | none (PM)
has_blank_variant: false
prereqs: ["meta_01_product_sense_intro"]
sources: ["see solution_reasoning.md"]
status: draft            # draft | review | published
```

`company`, `role`, `tier`, `difficulty`, and `primary_skill` are **required** — they drive the coverage matrix in `07`.

---

## 6. The rubric standard (analytic, countable)

Every lab self-grades on a **fixed analytic rubric**. Keep the v1 ten-dimension SWE rubric as the base; **swap dimensions per role** (see role tables below). Each row scores **1–5**, but the level descriptors must be **behavioral and countable**, not adjectives (Principle 8).

**Bad (do not author):** `Clarifying questions: __/5` with no descriptors.
**Good (author this):**

```
Clarifying questions ( /5)
  5 — 4+ questions, each paired with an explicit assumption tied to a design decision
  3 — 2–3 questions, some assumptions stated, loosely tied to design
  1 — 0–1 questions, jumps to a solution without scoping
```

Ship **one annotated exemplar per level** in `solution_reasoning.md` (the weak/adequate/strong calibration set). A learner must be able to self-place reliably without an instructor.

---

## 7. The answer-key standard (`solution_reasoning.md`)

This file is the **feedback engine** (Principle 7). It MUST contain, in order:

1. **Clarifying-questions answer key** — the model Question+Assumption for each category.
2. **Why this design** — entities, workflow, API/algorithm, MVP, each with a one-line *why*.
3. **Tradeoff table** (filled).
4. **Failure modes** — what breaks (stale data, concurrency, scale) + mitigation.
5. **How to explain it in 90 seconds** — a model talk track.
6. **Strong vs weak answer** — two contrasting answers with the *weak one annotated for why it's weak*. This is non-negotiable; it teaches the discrimination interviewers test.
7. **Curveball model responses** — a crisp model answer to each of Part 6's curveballs.
8. **Rubric exemplars** — one filled answer per rubric level (calibration).
9. **Sources** — where the interview-realism facts came from (cite the company pack).

---

## 8. The flashcards standard (`flashcards.md`)

8–15 cards per lab. Each card:
- Has a **generative cue** (free recall), never multiple-choice with a visible answer.
- Covers a **reusable primitive** (a decomposition heuristic, an API error case, a complexity fact, an LP, a metric definition) — not a lab-specific trivia detail.
- Is tagged with the spacing cadence note at the top of the file: *"Review day 1 → 3 → 7 → 14; reset to day 1 on a miss."*

---

## 9. Role adaptations of the skeleton

The 8-part spine is constant; the **content of Parts 3–4** and the **rubric dimensions** flex by role. Author from the matching role guide (`04`/`05`/`06`) + company pack.

### PM lab
- **Part 3** becomes *product design*: user segment → pain → solution set → prioritization (RICE/CIRCLES) → success metric (North Star + guardrail).
- **Part 4** becomes *write the artifact*: a product brief, a PR-FAQ (Amazon), a written memo (Stripe), a metric tree, or an A/B test design.
- **Rubric rows:** Structure · User empathy · Prioritization · Metrics literacy · Creativity · Communication · Handling ambiguity.

### Technical PM lab
- **Part 3** becomes *API/data/system-design-lite*: resource model, endpoints, idempotency/pagination/auth, data schema, batch-vs-streaming, the "what happens when a user clicks…" flow.
- **Part 4** becomes *produce the technical artifact*: an `openapi.yaml`, a data model, a SQL query, or a written technical tradeoff memo. **No production algorithm coding** — Technical PM is fluency, not implementation.
- **Rubric rows:** Technical fluency · Architecture tradeoffs (cost/latency/reliability) · Build-vs-buy reasoning · Scale/reliability reasoning · Communicates with engineers · Translates to non-technical · Handling ambiguity.

### SWE lab
- **Part 3** is the IO contract / data-structure design; **Part 4** is real coding against `tests`.
- **Two SWE lab styles** (pick per company — see `06`):
  - **Algorithmic** (Google/Meta/Microsoft/Amazon/Nvidia): one well-scoped DSA problem, narrate + optimize + test.
  - **Codebase / practical** (Stripe/Palantir/Uber/Atlassian): the **CodeSignal Industry-Coding-Framework template** — one project-style problem in **4 progressive levels** (L1 design+basic functions → L2 core logic+edge cases → L3 refactor/encapsulate → L4 extend without breaking earlier levels), or a **bug-squash** (failing test in an unfamiliar repo) or **integration** (ship a feature against a provided API).
- **Rubric rows:** Communication (think-aloud) · Problem solving (multiple approaches + Big-O) · Correctness · Code quality/readability · Testing & edge cases · Debugging/self-correction · Time management.

---

## 10. Naming, difficulty tags, and house conventions

- **Folder name:** `<NN>_<company>_<slug>` e.g. `03_stripe_idempotent_payments`. `NN` is the intended course order.
- **Difficulty ladder (fixed vocabulary):** `intro` → `easy` → `medium` → `hard` → `mock`. Tier and difficulty are related but distinct (a Tier-3 *blank* lab can still be `medium` difficulty).
- **Languages:** Python (default for SWE algorithmic + Palantir), Node.js (APIs/integration), SQL (data labs). Pick the company-authentic language (e.g., C++ for Nvidia systems labs, Swift for an Apple iOS lab) — see company packs.
- **Voice:** second person, imperative, coach-like. Short sentences. No hype. Mirror the existing labs' tone.
- **Every claim about an interview ("Stripe bans AI assistants," "Amazon scores LPs") must trace to a company pack**, which traces to a source. Do not invent interview facts.

---

## 11. File-by-file authoring spec (quick reference)

| File | Must contain | Reveal timing |
|---|---|---|
| `meta.yml` | full schema (§5) | n/a |
| `README.md` | interview-moment framing, 2hr/full/deep time plan, how-to-use | up front |
| `workbook.md` | the 8 parts at the lab's tier; `[blank]`s; collapsible hints | up front |
| `starter.<ext>` | docstring w/ pre-coding questions + **Expected Input Schema** + TODO list | up front |
| `tests.<ext>` | runnable acceptance tests incl. edge cases | up front (run to check) |
| `reference_solution.<ext>` | clean idiomatic model implementation | 🔒 after attempt |
| `solution_reasoning.md` | the 9-part answer key (§7) | 🔒 after attempt |
| `flashcards.md` | 8–15 generative cards + cadence note | after lab, then spaced |

> **The keystone rule:** a learner with no instructor must be able to (a) attempt every part, (b) get specific feedback on every part, and (c) know exactly what to do next. If any of the three fails, the lab is not done.
