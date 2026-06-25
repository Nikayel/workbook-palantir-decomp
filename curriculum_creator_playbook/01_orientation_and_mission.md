# 01 · Orientation & Mission

> **Read this first.** It tells you what you're building, the mental model, and how to navigate the rest of the playbook.

## Your mission
You are the **curriculum creator**. Your job is to author **hands-on practice workbooks** that interns use to prepare for **PM, Technical PM, and SWE internship interviews** at **10 companies** (Google, Meta, Amazon, Microsoft, Apple, Palantir, Nvidia, Uber, Stripe, Atlassian).

The workbooks are **deliberate-practice instruments** in the style pioneered by the existing Palantir labs in this repo — but **perfected and generalized**: a learner reads an ambiguous real-world scenario, writes clarifying questions, decomposes the problem, designs a contract, builds something against tests, defends tradeoffs, and self-grades — all without an instructor.

> **The one-sentence standard:** a learner with no instructor must be able to *attempt every part, get specific feedback on every part, and know exactly what to do next.* If a lab fails that, it isn't done.

## The mental model
- **Workbooks ≠ lectures.** Nobody *reads* these; they *perform* in them. Every page is an attempt or a piece of feedback.
- **You are not the source of truth on interviews — the company packs are.** They carry the researched facts and confidence flags. Author from them; never invent interview facts.
- **Fading is the engine.** Each skill is taught worked → completion → blank. A course walks a learner up that ramp.
- **The mess is the curriculum.** Authentic ambiguity is the transferable skill; don't sand it off.

## How the playbook is organized (file map)
| File | What it gives you | When you use it |
|---|---|---|
| `01_orientation_and_mission.md` | this — the map | first |
| `02_curriculum_design_principles.md` | the learning science (12 principles) | once, before authoring |
| `03_workbook_anatomy_and_authoring_standard.md` | the **how-to-build** spec (8-part lab, fade tiers, file set, rubric/answer-key standards) | every lab |
| `04_role_guide_pm.md` | PM track: rounds, frameworks, rubric, lab seeds | PM labs |
| `05_role_guide_technical_pm.md` | Technical-PM track: API/data/system-design-lite | TPM labs |
| `06_role_guide_swe.md` | SWE track: OA platforms, DSA map, **codebase style** | SWE labs |
| `07_production_plan_and_counts.md` | **how many** to build, in what order (coverage matrix + roadmap) | planning |
| `08_authoring_checklists.md` | copy-paste **checklists** for every stage | every lab + release |
| `09_style_guide_and_conventions.md` | house style, naming, vocabularies | every lab |
| `10_v1_audit_and_gap_analysis.md` | what the existing Palantir workbook gets right/wrong | context |
| `company_packs/*.md` | the **10 company fact packs** | every lab |
| `templates/*` | clone-me skeletons (workbook, rubric, answer key, meta, flashcards) | every lab |
| `gold_standard_samples/*` | **3 fully-worked example labs** (PM, TPM, SWE) | clone these |

## Your authoring workflow (the loop)
1. **Plan** — pick a `(company, role, tier, difficulty)`; open the **company pack** + **role guide** + check the **coverage matrix** (`07`).
2. **Clone** — copy the matching **gold-standard sample** (or `templates/` skeleton).
3. **Author** — fill the 8 parts at the right tier (`03`); pull realism from the company pack; pull the rubric rows from the role guide.
4. **Feedback** — write `solution_reasoning.md` (model + strong-vs-weak + exemplars) and `flashcards.md`.
5. **Check** — run the `08` checklists (Design → Content → Feedback → Code → Metadata → QA).
6. **Publish** — flip `meta.yml status` to `published`; add to the catalog.

## Quickstart (build your first lab today)
- New to the system? Read `02` and `03`, skim one **gold-standard sample**, then re-skin it to a different company using that company's pack. You'll have a publishable lab in one sitting.
- Building for a specific company? Open its pack, find the **signature artifact** (e.g., Amazon PR-FAQ, Stripe integration), and build that lab first — it's the highest-signal, most differentiated practice.

## Relationship to this repo
The existing `/labs`, `/dsa_patterns`, `/api_sql_data`, `/exact_reported_problems`, `/templates`, `/drills` are **v1** — a strong prototype of *one lab type for one company (Palantir, SWE)*. This playbook turns that into a **repeatable system for 3 roles × 10 companies**. See `10_v1_audit_and_gap_analysis.md` for exactly what to keep and what to fix.
