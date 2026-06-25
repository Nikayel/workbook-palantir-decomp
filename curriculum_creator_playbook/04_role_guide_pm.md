# 04 · Role Guide — Product Manager (PM) Intern

> **Audience:** the curriculum creator.
> **Purpose:** everything you need to author PM-track labs — what the interview tests, the frameworks to drill, the question archetypes to mine for lab seeds, the rubric, and the mistakes to bake into your strong-vs-weak answer keys. Pair this with the relevant **company pack** for the company skin, and with `03` for the lab structure.

> **Honesty flag for authors:** companies publish *full-time* PM loops, not intern loops. Several intern processes (Apple, Palantir, Nvidia, Stripe PM) are sparse/undocumented; those company packs lean on the FT loop as a proxy and say so. Don't over-claim intern specifics.

---

## 1. What the PM-intern interview tests

A typical funnel: resume → recruiter screen (30–45 min) → 1–2 video screens → an onsite "loop" of 3–5 interviews (often virtual). Intern loops are **shorter** than full-time (e.g., Nvidia interns are reportedly phone-only). Nearly every question maps to one of these round types:

| Round | Tests | A "good answer" looks like | Lab style to build |
|---|---|---|---|
| **Product Design / Sense** | creativity + user empathy on an ambiguous space | clarify goal → pick a segment → name real pains → ideate → **prioritize** → define a success metric | "Design X for Y" lab |
| **Analytical / Metrics** | choosing & interpreting data, defining success | NSM + guardrail/counter-metrics; tradeoffs; experiment design | "measure success of Z" / "set the NSM" lab |
| **Estimation / Market sizing** | structured quant under uncertainty | explicit structure, stated round-number assumptions, top-down *or* bottom-up chosen deliberately, sanity check | "size the market for…" lab |
| **Product Strategy / GTM** | market/competitive thinking, business sense | attractiveness, competition, fit, financials, risks → a recommendation with a "so what" | "should company enter market?" lab |
| **Execution / Root-cause** | diagnosing a metric drop, getting things done | MECE internal-vs-external split, hypothesis elimination, narrow to a funnel step, propose a fix | "metric dropped 20% — diagnose" lab |
| **Behavioral / Leadership** | leadership, conflict, drive ("fit") | STAR with **"I"** (not "we"), quantified outcomes, a reflection | values/behavioral lab (company-skinned) |
| **Technical / SQL** (some) | engineering fluency | reason about systems/APIs/tradeoffs; basic SQL | → route to the Technical PM guide (`05`) |

**2025–2026 trend to reflect:** an **AI product-sense** pillar is emerging — e.g., Meta added a round where you get a product prompt then *vibe-code a prototype* on a Llama chatbot. Build at least one "design + prototype an AI feature" lab.

---

## 2. The frameworks to drill (and how to turn each into a lab)

Teach the **structure invisibly** — a recurring interviewer complaint is candidates *reciting* a framework name, which reads as junior. Your labs should make the learner *use* the structure, then your answer key shows the strong version naming nothing.

| Framework | What it's for | How to build a lab prompt around it |
|---|---|---|
| **CIRCLES** (Comprehend, Identify customer, Report needs, Cut/prioritize, List solutions, Evaluate tradeoffs, Summarize) | product design | a "Design X for Y" prompt with each heading as a faded blank; score whether **prioritization precedes ideation** |
| **Design thinking** (Empathize→Define→Ideate→Prototype→Test) | user-centred design | hand the learner a persona + journey map; ask them to mark the **highest-pain step** before solutioning |
| **AARRR** (Acquisition/Activation/Retention/Revenue/Referral) | growth/funnel | map a feature's funnel to each A; find the leaking stage |
| **HEART + GSM** (Happiness/Engagement/Adoption/Retention/Task-success; Goals-Signals-Metrics) | UX quality | pick 2 HEART signals + their goal/signal/metric |
| **North Star + guardrails** | steering metric | "propose a NSM for [product] + 2 guardrails" |
| **RICE / ICE / MoSCoW / Kano** | prioritization | give 6 features + rough reach/impact; score with RICE, then re-bucket with MoSCoW |
| **Market sizing** (top-down vs bottom-up; mnemonic **SCALE**) | estimation | require the learner to solve the *same* prompt **both ways** and reconcile |
| **Root-cause / 5 Whys** (define metric precisely → MECE internal/external → eliminate → drill to funnel step) | execution | "metric dropped 20% — list clarifying questions first, then a MECE tree, then narrow" |
| **GTM** (market attractiveness, competition, capabilities, financials, risks) | strategy | force a recommendation + risks; **ban the words "SWOT"/"Porter"** in the answer |

---

## 3. Question archetypes (lab seeds)

Mine these for scenarios. Always **re-skin** to a company's real product surface (see company packs) so the practice is authentic (Principle 6).

- **Design / sense:** "Design Spotify for children." "Design a smart water bottle." "Improve [Apple Watch / Teams / Maps] retention." "What would you build for billions of users at Meta?" "Pick your favorite product and improve it."
- **Estimation:** "Size the US toothbrush market." "How many coffees are sold in NYC per day?" "Estimate annual revenue of London hair salons."
- **Analytical / metrics:** "How would you measure the success of feature Z?" "Set up an A/B test for this feature." "Uber: how does a change affect supply (drivers) vs demand (riders) vs the bottom line?"
- **Execution / root-cause:** "First-time order completions dropped 20% — diagnose." "DAUs fell week-over-week with no launch — why?" "Three features, one sprint — prioritize."
- **Strategy / GTM:** "Take [product] to a new country." "Should [company] enter [adjacent market]?"
- **Behavioral:** "Led without authority / handled conflict / made a data-driven decision / failed." "Why product, and why this company?"

---

## 4. The rubric dimensions (use these rows in PM labs)

Interviewers consistently score these. Author each as a **countable** 1–5 row (`03` §6).

| Dimension | Strong (5) | Weak/median (1–2) |
|---|---|---|
| **Structure** | visible roadmap, MECE buckets | rambling list, no signposting |
| **User empathy** | names a segment + real pain points | designs from personal preference |
| **Prioritization** | explicit cut with rationale | treats all ideas as equal |
| **Metrics literacy** | NSM + guardrails, tradeoffs | vanity metrics, can't define success |
| **Communication** | concise, adapts to interviewer | jargon, framework-name-dropping |
| **Creativity** | non-obvious, differentiated ideas | generic "me-too" features |
| **Handling ambiguity** | clarifies, states assumptions, moves | freezes or over-asks before starting |

---

## 5. Common mistakes → bake these into every strong-vs-weak answer key

The "weak" answer in `solution_reasoning.md` should *demonstrate* one of these so the learner sees the discrimination:
- **Jumping to solutions** before defining the problem/user (the #1 cited mistake).
- **No structure / rambling.**
- **Forgetting the user** or failing to tie back to a business goal.
- **Mechanically reciting a framework** ("First I'll use CIRCLES…") — reads as robotic.
- **No success metric** — can't say how you'd measure it.
- **No tradeoffs/constraints** — "perfect" solutions with no tough call.
- **"We" instead of "I,"** unquantified results, rehearsed-sounding behavioral answers.

---

## 6. What to build for the PM track

See `07_production_plan_and_counts.md` for exact counts. In short, a complete PM track per company is roughly:
- 1 **product-design/sense** lab (Tier 1 worked → company product surface)
- 1 **metrics/analytical** lab
- 1 **estimation** lab (often shareable/generic, lightly skinned)
- 1 **execution/root-cause** lab
- 1 **behavioral/values** lab (company-skinned to its values/LP)
- 1 company-signature artifact lab where it exists (Amazon **PR-FAQ**, Uber **JAM/marketplace case**, Stripe **written memo**, Atlassian **values panel**) — these are the highest-value, most differentiated labs.
- Strategy/GTM is optional for interns; include 1 generic if you have room.

**Company skins (see company packs for detail):** Google → product sense + Googleyness + light system design; Meta → data-driven execution + "build for billions" + AI-prototype; Amazon → PR-FAQ + Working-Backwards + LP-mapped STAR; Microsoft → structured design *without naming frameworks*; Apple → teardown/improve an iconic product; Uber → two-sided-marketplace metrics + JAM; Atlassian → values panel + B2B SaaS; Stripe → written memo + developer/payments depth; Nvidia → technical/GPU-domain product sense; Palantir → there is no classic PM — route to FDSE/decomposition (see SWE guide + Palantir pack).
