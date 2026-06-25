# 02 · Curriculum Design Principles

> **Audience:** the curriculum creator (you).
> **Purpose:** the evidence base behind *why* our workbooks are shaped the way they are. Read this once before you author anything. Every rule in `03_workbook_anatomy_and_authoring_standard.md` traces back to a principle here.

Our workbooks are **deliberate-practice instruments**, not lecture notes. A learner does not read them — they *perform* in them: writing clarifying questions, decomposing an ambiguous prompt, designing an API, coding against tests, defending tradeoffs, and self-grading. Everything below is in service of making that performance transfer to a real interview room.

The twelve principles are grouped into four jobs: **(A) Aim** the practice, **(B) Scaffold** it, **(C) Feed it back**, **(D) Sequence** it.

---

## A. AIM THE PRACTICE

### 1. Backward design — start from the interview moment
**Principle.** Understanding by Design (Wiggins & McTighe) plans in reverse: *desired result → acceptable evidence → learning activity*. You design the assessment **before** the activity, so every exercise earns its place by producing evidence of a target skill.

**Apply to our workbooks.**
- Open every lab spec by naming the **exact interview moment it simulates** (e.g., "Palantir decomposition round," "Stripe integration round," "Meta product-sense screen"). That moment is the desired result.
- Write objectives as **observable performances**, not topics. ✅ "Convert an ambiguous prompt into 4–6 scoped clarifying questions, each paired with a stated assumption." ❌ "Understand requirements gathering."
- If a section produces **no gradable evidence** of a named objective, cut it or convert it into one that does.

### 2. Bloom's ladder — every lab must climb to the top half
**Principle.** Revised Bloom (Anderson & Krathwohl): *Remember → Understand → Apply → Analyze → Evaluate → Create*. Interview performance lives in **Analyze/Evaluate/Create**; recognition (Remember/Understand) is only a warm-up.

**Apply to our workbooks.** Map each lab section to a level and make sure the lab reaches the top half:

| Bloom level | Verb | Where it lives in our lab |
|---|---|---|
| Remember | list, state | warm-up flashcards |
| Understand | explain, classify | "why ask about scale before designing?" |
| Apply | implement, use | the coding step / API contract |
| Analyze | differentiate, decompose | workflow + bottleneck + entity modeling |
| Evaluate | critique, justify, defend | curveballs + tradeoff table + self-grade |
| Create | design, construct | the end-to-end system + state machine |

❌ Don't stack three recall sections and call it practice — that builds recognition, not readiness.

---

## B. SCAFFOLD THE PRACTICE

### 3. Cognitive load & the fading sequence — *this is our fill-in-the-blank engine*
**Principle.** Sweller's Cognitive Load Theory: novices learn more from **studying worked examples** than from unaided problem-solving (the *worked-example effect*). But this **reverses** as skill grows (the *expertise-reversal effect*) — full worked examples become redundant, even harmful, for advanced learners. The fix is **guidance fading**: fully-worked → partially-completed → fully-blank.

**Apply to our workbooks.** This is the single most important design decision we make. Every skill is taught across a **three-tier fade**:

- **Tier 1 — Worked (I do).** A complete, annotated model of the artifact, with the expert's internal monologue shown.
- **Tier 2 — Completion (we do).** 50–70% pre-filled; the **load-bearing** parts are blanked (e.g., entities and workflow given, state transitions and error cases blank).
- **Tier 3 — Blank (you do).** The learner produces the whole artifact; only the rubric remains as support.

Rules:
- **Backward fading is the default** — remove the *last* steps first (give the setup, make them finish), then earlier steps as competence grows.
- **Match scaffolding to expertise, not convenience.** Do not hand a lab-8 learner the same heavy template you gave at lab 1 — that triggers expertise reversal. Provide a **"hide hints" / faded parallel** version.
- **One new concept per blank.** Keep the worked example and its blanks physically adjacent (avoid split-attention).

### 4. Gradual release of responsibility — never skip "we do"
**Principle.** GRR (Pearson & Gallagher; Fisher & Frey): *Focus (I do) → Guided (we do) → Collaborative (you do together) → Independent (you do alone)*. The most common scaffolding failure is **jumping from "I do" straight to "you do alone."**

**Apply to our workbooks.**
- Map the fade in Principle 3 onto GRR: worked example = I do; completion problem = we do; blank artifact = you do.
- Across a **course**, front-load fully-modeled labs; make later labs near-blank.
- When you model, **narrate the thinking, not just the answer** ("I'm asking about volume because it changes whether we shard"). Modeling expert reasoning is the point.

### 5. Deliberate practice — one weakness per rep, at the edge of ability
**Principle.** Ericsson: improvement comes from **well-defined tasks targeting a specific weakness, immediate feedback, and repetition just beyond current ability** — not from hours logged. Comfortable repetition produces an "OK plateau."

**Apply to our workbooks.**
- **Isolate the skill.** A lab targeting clarifying-question quality should not also grade code style — split focus muddies the feedback signal.
- **Sequence reps at rising difficulty:** clear domain → ambiguous scope → conflicting requirements.
- If learners pass a lab on the first try without strain, it's too easy: add a curveball or raise the ambiguity.

### 6. Authenticity & cognitive apprenticeship — keep the mess
**Principle.** Collins, Brown & Holum: skills transfer when practiced in **authentic, realistic contexts** through *modeling → coaching → scaffolding → articulation → reflection*. Sanding off ambiguity to make grading easy destroys the transferable skill.

**Apply to our workbooks.**
- Use **real-world-shaped scenarios** with real constraints and real messiness (delayed GPS, duplicate events, partial data). The mess *is* the curriculum.
- Require **articulation** — the "write your system-design reasoning" and "90-second talk track" steps force learners to externalize thinking, where misconceptions surface.
- Make the worked example an **apprenticeship**: show the expert's monologue, not a polished final answer that appears by magic.

---

## C. FEED IT BACK

### 7. Feedback & answer keys — timely, specific, criterion-tied
**Principle.** Hattie & Timperley: effective feedback answers **"Where am I going? How am I going? Where to next?"** and must be specific, timely, and tied to explicit criteria. Praise/score alone has near-zero learning value.

**Apply to our workbooks.**
- Provide a **model answer for every blank**, revealed **immediately after** the attempt (timeliness matters most while the attempt is fresh).
- Include **strong-vs-weak comparison answers**, and annotate *why* the weak one is weak ("guesses scale instead of asking" → "states an assumption and asks"). This teaches the discrimination interviewers test for.
- Every model answer should **reference the rubric row** it satisfies, closing the feed-forward loop.
- Phrase guidance as **next actions** ("add an error case for duplicate IDs"), not verdicts.

### 8. Analytic rubrics & self-grading — countable level boundaries
**Principle.** For self-study, **analytic rubrics beat holistic ones** — they tell the learner *which dimension* failed. A holistic "2/4" signals something is wrong but not what.

**Apply to our workbooks.**
- **One observable trait per rubric row**, with 3–4 levels described by **behavior, not adjectives**. ✅ "Strong (3): 4+ questions, each paired with an explicit assumption tied to a design decision." ❌ "Good: asks good questions."
- Make level boundaries **concrete and countable** so a learner can self-place reliably.
- **Calibrate** with one annotated exemplar per level (an actual filled-in answer at weak / adequate / strong) — the self-study substitute for inter-rater training.
- Keep rubrics to **4–10 rows**; collapsing distinct skills into one row or exploding into 20 rows both hurt.

### 9. Metacognition for self-directed learners — forethought and reflection on *every* lab
**Principle.** Zimmerman's self-regulated learning cycles through *forethought (goal/plan) → performance (monitor) → self-reflection (evaluate/adapt)*. These skills are teachable with structured prompts.

**Apply to our workbooks.**
- Open each lab with a **forethought box**: a time-box, a stated goal, and a confidence prediction (1–5).
- Close each lab with a **reflection tied to the next action**: "Which rubric row scored lowest? What will you do differently next lab?"
- Don't rely on a single end-of-course "reflect on your learning" — attach short prompts to *each* lab.

---

## D. SEQUENCE IT

### 10. Retrieval practice & spacing — the only two "high-utility" techniques
**Principle.** Roediger & Karpicke: self-testing retained ~80% after a week vs ~34% for rereading. Dunlosky et al. rated **practice testing and distributed practice** the two highest-utility study techniques. Retrieval works best **repeated and spaced at expanding intervals**.

**Apply to our workbooks.**
- Attach **8–15 flashcards per lab** covering reusable primitives (decomposition checklist, common API error cases, complexity facts).
- Specify a **review cadence**: day 1 → day 3 → day 7 → day 14 (roughly doubling); reset an item to a 1-day interval on a failed recall.
- Every flashcard cue must require **generation (free recall)**, not recognition. ❌ No multiple-choice with the answer visible.

### 11. Interleaving & desirable difficulties — block briefly, then mix
**Principle.** Bjork: conditions that *slow* acquisition often *improve* retention and transfer ("desirable difficulties"). **Interleaving** (ABC/ABC) beats **blocking** (AAA/BBB) on delayed tests because it forces learners to *discriminate* between problem types — exactly the real-interview demand. Caveat: very-low-prior-knowledge learners need a short initial block first.

**Apply to our workbooks.**
- **Block-then-interleave** at the course level: first few labs isolate one skill with heavy scaffolding, then mix lab types (a PM-scoping prompt, a SWE data-modeling prompt, a TPM tradeoff prompt) so learners practice *choosing the approach*.
- Engineer difficulty via **spacing, retrieval, and blank-percentage** — not by writing confusing instructions (that's an *undesirable* difficulty).

### 12. Avoid the common authoring failure modes
**Principle + fix** (the table you should re-read before shipping any lab):

| Failure mode | Why it hurts | Fix (principle) |
|---|---|---|
| Too easy / passes first try | no edge-of-ability strain | add curveballs, raise ambiguity (5, 11) |
| No feedback loop | learner can't see the gap | model + strong/weak answers, revealed after attempt (7) |
| Unclear objectives | activities yield no usable evidence | backward-design every step (1) |
| Inconsistent depth across labs | erratic difficulty breaks transfer | standardize the skeleton; map to Bloom (2) |
| Answer leakage | model visible before attempt kills retrieval | collapsible/after-the-attempt reveal (3, 10) |
| Uniform scaffolding | expertise reversal for advanced learners | fade guidance across the course (3) |
| Holistic-only self-grade | learner can't locate the weakness | analytic rubric, countable boundaries (8) |
| Recall-heavy, no synthesis | builds recognition, not performance | ensure each lab reaches Evaluate/Create (2) |

---

## The learning-science checklist for any lab
Before a lab leaves your desk, it must satisfy all of these (re-stated as a checklist in `08_authoring_checklists.md`):

- [ ] Named after the real interview moment it simulates (1)
- [ ] Has 1 measurable objective per section (1)
- [ ] Reaches Analyze/Evaluate/Create, not just recall (2)
- [ ] Skill taught across a worked → completion → blank fade (3, 4)
- [ ] Targets one weakness at the edge of ability (5)
- [ ] Uses an authentic, messy scenario (6)
- [ ] Every blank has a model answer + a strong-vs-weak contrast, revealed after the attempt (7)
- [ ] Analytic rubric with countable level boundaries + exemplars (8)
- [ ] Opens with forethought, closes with reflection→next action (9)
- [ ] Ships with 8–15 generative flashcards + a spacing cadence (10)
- [ ] Designed to be interleaved with other lab types (11)

---

## Recommended dosage (grounded in the above)
- **One lab:** target **45–75 min** of focused work (longer "deep" path optional).
- **A course:** **12–20 labs over 4–8 weeks**, at **2–4 labs/week** (~1 hr each) with review time — this respects spacing better than cramming.
- **Difficulty curve:** monotonic rise in ambiguity and blank-percentage; reserve the **last 2–3 labs as near-blank, full-length mock interviews** (the transfer test the whole course was backward-designed from).
- **A parallel spacing layer:** a cumulative flashcard deck reviewed at expanding intervals across the whole course.

---

## Sources
- **Backward design / UbD:** UCF Backward Design; ASCD UbD White Paper; UIC Backward Design.
- **Bloom's (revised):** Anderson & Krathwohl 2001; Valamis; Colorado College.
- **Cognitive load / worked examples / fading:** Sweller; *Worked-example effect* (Wikipedia); ASU "Fading and Feedback in Problem-Solving"; NSW CESE CLT report.
- **Gradual Release of Responsibility:** Pearson & Gallagher; Fisher & Frey; ODU GRR.
- **Deliberate practice:** Ericsson; Frontiers in Psychology 2019; Product Talk glossary.
- **Cognitive apprenticeship:** Collins, Brown & Holum.
- **Feedback:** Hattie & Timperley, *The Power of Feedback*; Melbourne CSHE; Duke Kunshan CTL.
- **Rubrics:** NC State rubric best-practices; Novak (holistic/single-point/analytic).
- **Metacognition / SRL:** Zimmerman; Frontiers 2017 SRL review.
- **Retrieval & spacing:** Roediger & Karpicke 2006; Dunlosky et al. 2013 (AFT); Univ. of York spaced repetition.
- **Interleaving / desirable difficulties:** Bjork & Bjork; Firth systematic review (Wiley).

*(Full URLs in `/scratchpad/research/` research briefs; most primary pages 403 automated fetches, so claims rest on search extracts of the cited sources + established literature.)*
