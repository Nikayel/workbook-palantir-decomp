# Atlassian — Interview Prep START HERE

Status: Ready — work through all parts in order

---

## Snapshot

**Roles:** SWE Intern (Early Careers), Graduate Engineer, Grad++ (post-grad accelerated track), Associate Product Manager (APM)

**Hemispheric Timing:**
- US cycle: May – August (apply Oct–Jan)
- AU cycle: Nov – February (apply May–Aug)
- Graduate programs open ~6 months before start

**Offices hiring interns/grads:** San Francisco, New York, Austin, Sydney, Amsterdam, Bengaluru

---

## Culture — The 5 Values (verbatim)

Memorize these word for word. They appear in the Values interview as named gates.

1. **"Open company, no bullshit"** — Transparency over politics. Say what you mean. Share context broadly, even when it's uncomfortable.
2. **"Build with heart and balance"** — Care deeply about the work AND about your own sustainability. Neither burnout nor indifference.
3. **"Don't #@!% the customer"** — The customer's experience is non-negotiable. Data integrity, reliability, and honesty about failures matter.
4. **"Play, as a team"** — Win collectively, not individually. Credit flows outward, friction flows inward.
5. **"Be the change you seek."** — Don't wait for permission. If something is broken, own fixing it.

**Team Anywhere:** Atlassian is permanently distributed. No return-to-office mandate. This affects how they evaluate communication: async-first, written clarity, and trust are table stakes.

---

## What's Distinctive About Atlassian Interviews

### The Values Interview is a Hard Gate

This is a **standalone, scored** interview — not a culture-fit add-on tacked onto the end of a coding round. It is given by a trained interviewer who has a rubric. A "No" from the values interview **cannot be overridden** by strong technical performance.

You need a **STAR story for each of the 5 values**, mapped explicitly. "I had a conflict with a teammate" is not enough — you need to name the value and explain why your behavior embodied it.

### Craft Over Flawless Syntax

Atlassian interviewers are trained to reward:
- **Voluntarily writing tests** — if you add tests that weren't asked for, that is a positive signal
- **Reading code before writing** — jumping straight to fixing without understanding is penalized
- **Communicating tradeoffs** — saying "I'm choosing this approach because..." is valued over silent coding

### "No Brilliant Jerks" Is Real Policy

Atlassian's values are operationalized in performance reviews and promotion decisions, not just hiring. Someone who is technically exceptional but violates "Play, as a team" or "Open company, no bullshit" will not pass interviews and will not be promoted.

---

## Assessment Pipeline

| Stage | Format | Notes |
|---|---|---|
| Application | Resume + cover | No OA auto-trigger; humans review for grads |
| HackerRank OA | 2–4 questions, Easy–Medium, 60–90 min | Not always required; depends on volume |
| "World of Atlassian" SJT | Situational judgment test | Values alignment disguised as scenarios |
| Karat technical screen | Live coding, 45–60 min, external panel | Bug fix + implement + extend pattern |
| Loop (onsite/virtual) | 4 rounds | See below |

### Loop Rounds
1. **Craft Coding** — live implementation, often in an unfamiliar repo. Voluntary tests rewarded.
2. **Code Design / LLD** — design a mini-system (notification, permission system, workflow engine). OOD principles evaluated.
3. **Values Interview** — STAR stories mapped to all 5 values. Scored independently.
4. **Hiring Manager** — domain fit, motivation, career vision.

---

## Lab Menu

### SWE Labs (craft/LLD style)

| Lab | Style | Tier | Description |
|---|---|---|---|
| Lab 01 | Craft coding + write-your-own-tests | Tier 1 | Karat-style: read buggy Jira module, write failing tests, fix bugs, voluntarily add more tests |
| Lab 02 | LLD notification system | Tier 2 | Code Design round: Observer pattern, Open/Closed Principle, extensible channel design |
| Lab 03 | Values interview STAR | Tier 1 | Prepare 5 mapped STAR stories, one per value, with specific behavioral markers |
| Lab 04 | World of Atlassian SJT prep | Tier 2 | Practice the situational judgment scenarios; learn to identify which value each scenario tests |

### PM Labs

| Lab | Style | Tier | Description |
|---|---|---|---|
| Lab 01 | Experimentation / A-B + KPI lab | Tier 2 | Design an A/B test for a Jira feature; define primary + guardrail metrics |
| Lab 02 | Values-mapped product case | Tier 2 | Product case where decisions must be explicitly linked to Atlassian values |
| Lab 03 | Values panel | Tier 1 | Shared with SWE Lab 03 — same STAR structure, PM-flavored scenarios |

### TPM Labs

| Lab | Style | Tier | Description |
|---|---|---|---|
| Lab 01 | 48-hour execution take-home | Tier 3 | Program plan for a complex cross-team delivery; risk register + dependency map |
| Lab 02 | KPI / SQL reasoning | Tier 2 | Atlassian data engineering questions; define what "sprint health" means in SQL |

---

## Before You Start

1. **Memorize all 5 values verbatim.** Not paraphrased — exact phrasing matters because the interviewer is scoring against exact criteria.
2. **Have a STAR story for EACH value** — one story per value, ready to deliver in 2–3 minutes. Practice out loud, not just in your head.
3. **Know that "no brilliant jerks" is a real gate.** If you are technically strong but communicate dismissively or avoid accountability in your stories, you will not pass.
4. **Practice reading code before touching it.** In the Karat screen, 5 minutes of quiet reading before writing any tests is correct behavior — not slow behavior.
5. **Understand Team Anywhere context.** You may be asked about async communication, documentation habits, or how you work with people you rarely see in person. Have concrete answers.

---

## Quick Reference: Values → Behaviors in Interviews

| Value | What it looks like in a coding interview | What it looks like in a STAR story |
|---|---|---|
| Open company, no bullshit | Say when you're unsure; don't fake confidence | Story about sharing uncomfortable truth or calling out a problem |
| Build with heart and balance | Show you care about code quality without obsessing | Story about quality vs speed tradeoff where you found balance |
| Don't #@!% the customer | Notice data integrity bugs even when not in scope | Story where you caught a customer-impacting issue and acted |
| Play, as a team | Credit others; ask clarifying questions; don't solo sprint | Story about enabling teammates or sharing a win |
| Be the change you seek | Voluntarily add tests; raise issues proactively | Story about fixing something without being asked |
