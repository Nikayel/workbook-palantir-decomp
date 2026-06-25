# Company Pack — Uber

## 1. Snapshot
| Program | For | Length / timeline |
|---|---|---|
| **SWE Intern** | students returning to school | ~12 wk (Jun–Aug) |
| **UberSTAR** | 1st/2nd-years + underrepresented | early pipeline (India-documented) |
| **PM Intern** | students | ~12 wk |
| **APM** | new grads (2 yr / 3 rotations) — **also a 12-wk internship** | bootcamp + global research trip (~4 cities) |
| **Data Science Intern** | students | ~12 wk |
> Apps open early Sept, close ~mid-Nov, rolling; apply early–mid Oct. 2026 APM deadline ~Sep 26.

## 2. Culture & values (hiring signal)
Eight **cultural norms** (post-2017 reset by Khosrowshahi, employee-voted): *We build globally, we live locally · We are customer obsessed · We celebrate differences · We do the right thing (.Period) · We act like owners · We persevere · We value ideas over hierarchy · We make big bold bets.* The reset itself is load-bearing — behavioral signal emphasizes **ethics + ownership + customer obsession** (a deliberate break from the old "always be hustlin'" era).

## 3. What's distinctive
- **Marketplace / real-world systems thinking** — Uber is a multi-sided, global, physical-world marketplace. Reason in those terms (supply vs demand vs bottom line), not abstractly.
- **PM bar is notably quantitative** (metric definition, diagnosing metric changes, A/B), often assessed in a round with a **data scientist**.

## 4. Assessment artifacts to replicate
- **OA = CodeSignal GCA** (and/or HackerRank) — ~3–4 Q, ~70 min, LC-medium, cutoff ~700–725 (old scale; now 200–600). *(Uber intern = GCA, NOT the Industry Coding Framework — flag.)*
- **SWE:** phone screen (1 coding) → onsite "Superday" ~4×45 min (coding / system design for grads / behavioral). Code must be **runnable, edge-case-tested, Uber-flavored** (routing/pricing/geospatial).
- **PM:** analytical round with a **data scientist**; a lead-PM case; the **JAM session** (prompt ~24 h in advance, ideate with 2–3 employees).
- **TPM (TPgM):** ~60-min distributed **system-design** round + cross-functional execution, often a **~1-week take-home case** presented to a panel.

## 5. Role tracks
**SWE.** Algorithmic + **practical Uber-domain**. Over-index: intervals + heaps, graphs + Dijkstra/shortest-path, sliding window/deque (moving averages), binary search on answer, topological sort, **data-structure design — LRU, rate limiter, hit counters with expiry**. Grads add system design + values. Languages: any (Java/Go/C++/Python common).
**PM / APM.** Two-sided **marketplace metrics**, experimentation/causal thinking, estimation ("how many drivers in the SF Bay Area?").
**Technical PM (TPgM).** Distributed system-design + dependency/risk + take-home case.

## 6. Lab build list
- SWE *workbooks*: `01` **practical Uber-domain** routing/dispatch lab (Tier 1) · `02` **rate-limiter / hit-counter-with-expiry design-a-DS** lab (Tier 2) · `03` ownership/"do the right thing" behavioral (Tier 2) · `04` **timed mock-OA (CodeSignal GCA-style)** (Tier 3). Sliding-window/graph pattern prep → shared **DSA drill kit**, *not* workbooks.
- PM/APM: `01` **two-sided marketplace metric** lab (Tier 1) · `02` JAM-session ideation (Tier 2, 24-h-prompt format) · `03` metric-drop root-cause (Tier 2).
- Technical PM: `01` distributed system-design-lite (Tier 2) · `02` take-home case (Tier 3).

## 7. Authenticity notes
Real surfaces: Rides, Eats, Freight, driver/rider apps, pricing/ETA/dispatch. Always frame as **supply (drivers) vs demand (riders) vs Uber's bottom line**. Model the 8 norms (esp. "do the right thing" + "act like owners") in behavioral keys. **Context:** heavy internal AI adoption (~95% engineers use AI monthly); AI/ML exposure flagged as a plus.

## 8. Sources & confidence
SWE deep-dive + PM/TPM + company briefs; uber.com/careers, Cultural Norms PDF, Exponent, igotanoffer, interviewquery. **Confidence:** high on 8 norms + marketplace emphasis + GCA OA; **medium** on intern round counts (Exponent/getsmartresume, not official).
