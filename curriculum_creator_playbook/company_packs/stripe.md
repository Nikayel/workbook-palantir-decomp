# Company Pack — Stripe

> Stripe carries **two** signature artifacts central to this curriculum: the **codebase-style SWE interview** (integration + bug-squash) and the **writing-first culture** (the load-bearing PM/Technical-PM signal). Make these the flagship Stripe labs.

## 1. Snapshot
| Program | For | Length / timeline |
|---|---|---|
| **Software Engineer, Intern (Summer)** | ≥2 yrs university, prior multi-person/OSS project, BS/MS/PhD CS/math | 12 (some 16) wk; real shipped projects; a "**hiring audition**" |
> Apps open early Sept, close ~mid-Nov, rolling. ~1–2% acceptance (~100–150 spots). PM/Technical-PM intern data is sparse — proxy from FT.

## 2. Culture & values (hiring signal)
Operating Principles: *We haven't won yet · Move with urgency and focus · Think rigorously · Trust and amplify · Users first / "really, really, really care" · Create with craft and beauty · Global optimization · micro-pessimist, macro-optimist.* **The defining fact: Stripe is a writing-first company** — memos/RFCs over decks, narrative pre-reads instead of PowerPoint, weekly written updates instead of standups. **Writing is the #1 hiring signal across every role.**

## 3. What's distinctive
- **Writing.** Practice **Stripe-style memos**: short declarative sentences, descriptive headings, surfaced tradeoffs, second-order/user-impact reasoning, zero fluff. This is load-bearing, not a nice-to-have.
- **Practical engineering, not algorithm trivia** (SWE). No whiteboard, no LeetCode tricks.

## 4. Assessment artifacts to replicate
- **Integration round (flagship SWE artifact):** dropped into an unfamiliar/private codebase with a **provided API/SDK + docs**; ship a small working feature in ~45–60 min with **full internet access** (search docs, **not AI**). Patterns: parse JSON → structured data → transform; clone a repo, call an API, store the response; implement a feature against a payments-style API and surface specific fields. **Graded on a working change + clean production code, NOT Big-O.**
- **Debugging round ("Bug Squash"):** a pinned version of a real OSS library with a **failing test or open issue**; fix in ~45–60 min. Classic bugs: missing dir-vs-file path check; missing AST visitor for a node type; a **race condition** (lost update from an unguarded read-modify-write). **A clear, well-reasoned diagnosis often counts more than a finished fix.**
- **Intern OA:** ~60-min HackerRank, **one implementation-heavy problem in ~3 progressive sub-parts** (solve part 1 to unlock 2) — implementation/OOP/data-handling, not DP/graph puzzles.
- **Writing exercise (PM / Technical PM):** a **written take-home memo** modeled on Stripe's internal style; connect adoption metrics to **second-order user impact** (trust, long-term retention), not just topline revenue.
- Tools: **CoderPad** (code), **Whimsical** (design). Loop 4–6 ×45–60 min, virtual.

## 5. Role tracks
**SWE.** **Codebase / practical style** — integration + bug-squash + the 3-part implementation OA. Weight code quality, testing, debugging, and **diagnosis** highly. Reward humility/seeks-feedback.
**PM.** Take-home **written memo** + product sense framed as fast, intentional UX/direction decisions. Developer/payments technical depth.
**Technical PM.** The **highest API/developer bar of the 10.** Technical screens ~entirely **API design + system architecture**: resource modeling, **idempotency** (idempotency keys, safe retries), **financial invariants** (double-entry ledgers, debits = credits), **backward-compatible/extensible API versioning** "for the next 10 years." Write it up as a Stripe memo.

## 6. Lab build list
- SWE *workbooks*: `01` **integration lab** (ship a feature vs a payments-style API in a provided repo, ICF spine) (Tier 1→2) · `02` **bug-squash lab** (failing test in an unfamiliar repo, incl. a **race condition**; rubric rewards diagnosis) (Tier 2) · `03` 3-part progressive implementation OA (Tier 2) · `04` humility/collaboration behavioral (Tier 2). All codebase/system-building — Stripe has **no pure-DSA round**, so no DSA-drill dependency here.
- PM: `01` **written product memo** (Tier 1 worked → Tier 2) · `02` developer-product sense case (Tier 2).
- Technical PM: `01` **idempotent payments API design** + **double-entry ledger invariants** + **10-yr versioning**, written as a memo (**flagship Technical-PM lab**) (Tier 1→2) · `02` webhook + pagination design (Tier 2).

## 7. Authenticity notes
Real surfaces: Payments, Billing, Connect, Radar, Issuing, the Stripe API/docs. **Study Stripe's actual API docs** and mirror their resource model. Every PM/TPM deliverable is a **written memo**; grade writing explicitly (a "Writing clarity & rigor" rubric row). **AI assistants are prohibited in interviews** (web/doc search allowed) — your labs should permit doc search but the rubric should reward the learner's own reasoning. 2025 "AI-enabled builder" hiring theme.

## 8. Sources & confidence
SWE + PM/TPM + company briefs; stripe.com/jobs (culture/university), tryexponent, coditioning bug-squash, codinginterview, igotanoffer, joinleland, slab writing-culture. **Confidence:** high on integration/bug-squash/writing culture + AI ban (multi-source); **medium** on intern OA specifics; **low** on PM-intern variant (FT proxy).
