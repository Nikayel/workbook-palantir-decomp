# 09 · Style Guide & Conventions

> **Audience:** the curriculum creator.
> **Purpose:** the house style so 100 labs by different hands read as one product. Consistency is a learning feature (Principle 12).

---

## Voice & tone
- **Second person, imperative, coach-like.** "Pause. Do not design yet." "State an assumption and move on."
- **Short sentences. No hype.** No "amazing/powerful/revolutionary." Mirror the existing `/labs/` tone.
- **Respect the learner's time** — every line either instructs, prompts, or gives feedback. Cut throat-clearing.
- **Be honest about the interview.** If a company's intern process is undocumented, say so in the lab's sources; don't fabricate confidence.

## Markdown conventions
- **Headings:** `#` lab title, `##` parts, `###` sub-sections. One `#` per file.
- **Fill-in token:** `[blank]` (never `____`). Greppable, renders cleanly.
- **Hints & reveals:** collapsible `<details><summary>…</summary>…</details>`. Mark post-attempt reveals `🔒 Open only after you attempt`.
- **Tables** for any contract, rubric, or tradeoff (Input/Output, Decision/A/B/Choice/Why). Never prose where a table fits.
- **Code fences** with a language tag (```python, ```sql, ```js, ```yaml).
- **Tutorial annotations** in italics inside parentheses: *(Tutorial: list the object name like 'Incident', not properties like 'address'.)*
- **Callouts** with `>` blockquotes for golden rules and keystone reminders.

## Naming
- **Lab folder:** `<NN>_<company>_<slug>` — e.g. `03_stripe_idempotent_payments`. `NN` = course order, zero-padded.
- **Company packs:** `company_packs/<company>.md`, lowercase.
- **Slugs:** lowercase, underscore-separated, descriptive (`bug_squash_race_condition`, not `lab3`).
- **Languages/extensions:** `.py` (Python — SWE/Palantir default), `.js` (Node/APIs), `.sql` (data), `.swift`/`.cpp` where company-authentic, `.yaml` (API/meta).

## The fixed vocabularies (don't invent new terms)
- **Tier:** `1` worked · `2` completion · `3` blank/mock.
- **Difficulty:** `intro` · `easy` · `medium` · `hard` · `mock`.
- **Role:** `pm` · `technical_pm` · `swe`.
- **Status:** `draft` · `review` · `published`.
- **Bloom top:** `analyze` · `evaluate` · `create` (a lab must reach one of these).

## Sources & citations
- Every interview-realism claim **traces to a company pack**, which lists its sources and a **confidence flag**.
- In a lab, cite at the bottom of `solution_reasoning.md`: "Interview-realism per `company_packs/<company>.md` (last verified: <cycle>)."
- **Flag uncertainty inline** ("intern process sparse; FT loop used as proxy"). Never launder a proxy into a fact.
- Treat percentages (conversion, acceptance, OA cutoffs) as **directional**, never guarantees.

## Accessibility & inclusivity
- Don't assume a degree/pedigree (Palantir's anti-pedigree ethos is a good north star). Scenarios should be solvable from skills, not insider knowledge.
- Avoid culture-bound idioms in scenarios; interns are global.
- Keep reading level plain; define jargon on first use (idempotency, ontology, NSM).
- Alt-text any images/diagrams; prefer ASCII/Mermaid diagrams that render in plain text.

## Authenticity rules (the realism contract)
- Use the company's **real product surfaces** (from the pack) — Search/Maps for Google, Payments/Billing for Stripe, Foundry/ontology for Palantir.
- Use the company's **real values language** in behavioral labs (LPs for Amazon, the 5 values for Atlassian, growth mindset for Microsoft) — but teach learners to *demonstrate*, not recite.
- Use the **company-authentic OA/round format** (plain-doc for Google, integration/bug-squash for Stripe, decomposition for Palantir, Codility for Microsoft).
- Pick the **company-authentic language** (C++ for Nvidia systems, Swift for Apple iOS).

## What good vs bad looks like (quick contrasts)
- **Rubric row.** ✅ "Strong (5): 4+ questions, each paired with an explicit assumption tied to a design decision." ❌ "Good: asks good questions."
- **Scenario.** ✅ "Responder GPS pings are delayed up to 5 minutes and occasionally drop." ❌ "You have some location data."
- **Behavioral key.** ✅ models "I" + quantified outcome + reflection. ❌ "we shipped a great feature."
- **Blank placement.** ✅ model answer in `solution_reasoning.md`. ❌ model answer in a visible line under the blank.
