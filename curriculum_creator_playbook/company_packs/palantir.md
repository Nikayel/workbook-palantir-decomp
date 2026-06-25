# Company Pack — Palantir

> This is the company the existing v1 workbook already targets. Its **decomposition round is the crown jewel** of this whole curriculum and the model for the SWE codebase style. Promote the existing `/labs/` to this pack (bring them to the `08` QA bar).

## 1. Snapshot
| Program | For | Length / timeline |
|---|---|---|
| **FDSE Intern** (Forward Deployed Software Engineer) | students returning to school; the signature role | ~12 wk, May–Sep, **4 start dates** |
| **SWE / Core Intern** (Foundry, Gotham, Apollo, AIP) | students | ~12 wk |
| **Accelerate** | sophomores/juniors earlier in their journey | 10–12 wk, NY/DC |
| **Meritocracy Fellowship** | graduating **high-school** seniors (no degree) | ~5 mo (Aug–Dec), $5,400/mo, SAT≥1460/ACT≥33 |
> Apps open ~fall (Oct), fill before Nov. Intern comp famously ~$10k/mo.

## 2. Culture & values (hiring signal)
**Mission-driven** (Western government/defense/intel + large commercial) · the **Forward Deployed mindset** (embed with the customer, build in their mess) · **problem decomposition** as *the* core competency · ownership/agency/raw intelligence/"best idea wins" · **anti-pedigree** hiring (de-emphasize resume/school).

## 3. What's distinctive
- **Problem decomposition under ambiguity is THE differentiator** across every role: take a vague real-world prompt → stakeholders/users → **data model/entities ("ontology": objects-properties-links)** → workflows → MVP sequence → tradeoffs, **out loud**.
- **Palantir has no classic PM.** The "PM-like" analog is **FDSE / Deployment Strategist** — prep those, not a Meta/Google APM loop.

## 4. Assessment artifacts to replicate
- **The Decomposition interview (hallmark)** — ~60-min CodePair on a vague problem with no scope ("design a taxi-dispatch system," "hospital patient-record management," "chess from scratch"). **Not meant to be solved — meant to be decomposed.** Discover requirements by asking; define entities/ontology + API contracts + workflows; prioritize + tradeoffs + V1. *FDSE "system design" = a **data pipeline** (ingestion → cleaning/normalization → ontology → UI), NOT load-balancers.* → **This is exactly the existing `labs/*/workbook.md` format.**
- **HackerRank OA** — 3–5 implementation-heavy "mini-projects" (multi-part), often a coding problem + a **SQL query** + an **API integration** task; clean code, complex logic, edge cases (empty/dupes/extremes). Sometimes a **"Learning Round"** (learn a new API on the fly). → the existing `exact_reported_problems/mock_oa/` is the model.
- Practical coding screens: string parsing, HashMaps, arrays, 2048-style; **mix standard + very non-standard** (pure LeetCode insufficient).

## 5. Role tracks
**SWE / FDSE.** **Codebase / practical style** — decomposition + practical data manipulation + SQL/API. This is the spine of the whole repo.
**PM.** No classic PM track → route to FDSE/Deployment-Strategist decomposition + mission/customer empathy.
**Technical PM.** The decomposition round *is* the technical-product test (ontology/data-pipeline). No separate track.

## 6. Lab build list
- SWE/FDSE: `01`–`06` the existing decomposition labs, brought to standard (Tier 1→3 across the set) · `07` **SQL window/sessionization** lab · `08` **API pagination/CRUD** lab · `09` **HackerRank mini-project OA** (Tier 3, timed) · `10` **90-min mock OA** (existing) (Tier 3). All decomposition / practical / SQL / API — **the exemplar of "SWE workbook = system-building."** Pure DSA appears only *inside* the mock OA, never as a standalone workbook.
- Deployment Strategist / "PM": `01` decomposition with a customer-outcome framing (Tier 1) · `02` ontology data-model lab (Tier 2).

## 7. Authenticity notes
Real surfaces: Foundry, Gotham, Apollo, AIP (and "ontology" language). Frame scenarios as **messy operational problems** (disaster relief, supply chain, 911 dispatch — the existing labs are perfect). Always require **assumptions stated out loud** and **prioritization to a V1**. Mission framing is a genuine filter — model bought-in, mission-aware reasoning.

## 8. Sources & confidence
PM/TPM/SWE + company briefs; palantir.com careers, blog.palantir.com, coditioning/prepfully/techinterview decomposition guides, interviewing.io. **Confidence:** high on the decomposition round (the most consistent signal across sources); **medium** on >90% conversion (anecdotal) and exact 2026 cycle structure.
