# 10 · v1 Audit & Gap Analysis — "What we have, and why it isn't perfect yet"

> **Audience:** the curriculum creator.
> **Purpose:** an honest assessment of the existing Palantir workbook (the repo this playbook lives in), what to **keep**, what to **fix**, and how the new authoring standard (`03`) closes each gap. The user's instinct — *"i think its not perfect"* — is correct: the bones are good, but depth is uneven and it's single-company, single-role.

---

## What v1 is
A **Palantir FDSE/SWE** interview-prep workbook with genuinely good structure:
- `labs/` — 8 decomposition labs, each with `README.md`, `workbook.md`, `starter.py`, `tests.py`, `reference_solution.py`, `solution_reasoning.md`.
- `dsa_patterns/` — 8 pattern folders with a README + starter.
- `api_sql_data/` — SQL and API labs.
- `exact_reported_problems/` — reported scenarios + a 90-min mock OA.
- `templates/`, `drills/` — fill-in-the-blank templates and flashcards.

---

## What's STRONG — keep and propagate (these become the standard)

1. **The 6-part decomposition `workbook.md`** (`labs/lab_01_911_dispatch/workbook.md`) is excellent pedagogy: clarifying questions → decomposition → system/API contract → coding → reasoning → interview simulation → self-grade. We keep it and extend it to **8 parts** (adding forethought + reflection).
2. **The Question/Assumption pairing** (Part 1) is the workbook's best idea — it trains candidates to ask *and* assume so they never freeze. **Enforce it everywhere.**
3. **Tutorial annotations** (the parentheticals like *"Do NOT list properties like 'address' here, just the object name"*) pre-empt the most common novice errors. Keep them, especially in Tier-1 labs.
4. **`Expected Input Schema` in starter docstrings** (`labs/lab_01_911_dispatch/starter.py`) — concrete, removes ambiguity about the contract. Standardize it.
5. **`solution_reasoning.md` with a "Strong vs weak answer" section** (`labs/lab_01_911_dispatch/solution_reasoning.md`) — this is exactly the feedback discrimination learners need. Make it mandatory (`03` §7).
6. **Time-boxed READMEs** with 2hr/3hr/5hr paths — good self-regulation scaffolding.
7. **`[blank]` token** (migrated from underscores) renders cleanly and is greppable. Keep it.

---

## What's NOT PERFECT — the gaps, with evidence

| # | Gap | Evidence | Fix (standard) |
|---|---|---|---|
| G1 | **Single company, single role.** SWE/FDSE-only, Palantir-only. The whole point of this playbook is 10 companies × {PM, Technical PM, SWE}. | entire repo | `04`/`05`/`06` role guides + 10 company packs |
| G2 | **No fading.** Every lab is roughly the same blank-heavy tier; no worked→completion→blank progression, so novices hit "you do alone" with no "I do/we do." (Lab 1 was *partly* fixed — "Turn Lab 1 into a tutorial lab" — proving the need, but it's ad hoc.) | `labs/*/workbook.md` all similar depth | `03` §3 three-tier fade + `meta.yml tier` |
| G3 | **Inconsistent depth.** Some pieces are rich; others are 1–2 lines. `exact_reported_problems/access_control_tree/README.md` is literally *"Given org/resource tree, determine access via inheritance."* `api_sql_data/sql_labs/lab_1_response_metrics.sql` is just two comment lines. `labs/lab_08/workbook.md` collapses the self-grade to "Total: __ / 50" with no rubric rows. | cited files | `03` standard + `08` QA checklist (every lab gets the full file set) |
| G4 | **Thin feedback in places.** Drills are sparse: `drills/behavioral_prompts.md` is 5 generic prompts; `drills/decomp_flashcards.md` has 3 cards. No spacing cadence. | `drills/` | `03` §8 flashcards standard (8–15 generative cards + day-1/3/7/14 cadence) |
| G5 | **No metadata.** Nothing is machine-readable; you can't generate a coverage matrix or audit balance across companies/roles/tiers. | no `meta.yml` anywhere | `03` §5 `meta.yml` + `07` coverage matrix |
| G6 | **No forethought/reflection.** Labs open on the scenario and end on the rubric; the metacognition layer (goal/confidence prediction; lowest-row→next-action) is missing. | `workbook.md` Parts | `03` Parts 0 & 7 (mandatory) |
| G7 | **Rubric descriptors are uncountable.** `labs/lab_01/workbook.md` self-grade lists dimensions but no behavioral level descriptors, so self-placement is unreliable. | self-grade section | `03` §6 countable 1–5 descriptors + exemplars |
| G8 | **Thin/empty tests.** `labs/lab_01/tests.py` has a single `test_basic_filtering`; many edge cases the workbook *names* aren't tested. | `tests.py` | `08` checklist: tests must cover the edge cases the workbook lists |
| G9 | **No "codebase-style" SWE labs.** v1 has decomposition + algorithmic + SQL/API, but not the Stripe-style integration/bug-squash or the CodeSignal ICF 4-level format the user explicitly wants. | repo | `06` §3.1 codebase + the SWE gold-standard sample |
| G10 | **No authoring guidance at all.** There's no standard telling a *creator* how to build more of these consistently — which is the entire deliverable you're reading now. | repo | this playbook |

---

## Recommended disposition of existing v1 content

- **Promote** `labs/lab_01_911_dispatch/` to the canonical SWE-decomposition exemplar (it's already the most polished). Add `meta.yml`, Parts 0 & 7, countable rubric, fuller tests → it becomes a Tier-1 reference lab.
- **Re-skin** the 8 labs as the **Palantir** company pack's SWE/FDSE labs (they already are Palantir-flavored), and bring each up to the `08` QA bar.
- **Backfill** `dsa_patterns/` READMEs and `exact_reported_problems/` stubs to full labs (G3).
- **Expand** `drills/` to the flashcards standard (G4).
- **Do not** rewrite everything at once. Use the `07` production plan to sequence: standard first, then Palantir to-standard, then the other 9 companies.

> **Bottom line:** v1 is a strong *prototype of one lab type for one company*. This playbook turns it into a *repeatable system* for three roles across ten companies. Keep the soul (decomposition, Question/Assumption, strong-vs-weak); fix the consistency, the fading, the feedback depth, and the coverage.
