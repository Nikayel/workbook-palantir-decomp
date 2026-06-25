# 06 · Role Guide — Software Engineer (SWE) Intern

> **Audience:** the curriculum creator.
> **Purpose:** how to author the SWE track, including the **"codebase / practical" style** the user specifically asked about (Stripe integration & bug-squash, Palantir decomposition, the CodeSignal Industry-Coding-Framework). Pair with the company pack and `03`.

The existing Palantir labs (`/labs/`, `/dsa_patterns/`, `/api_sql_data/`, `/exact_reported_problems/`) are your v1 SWE material. This guide generalizes them to 10 companies and two distinct lab styles.

---

## 1. The SWE-intern loop and OA platforms

Flow: application → recruiter screen → **OA** → 1–2 technical screens (45–60 min, 1–2 coding problems each) → sometimes a behavioral/values round → offer → **team match**. Interns get **fewer rounds and little/no system design** vs full-time.

Know the OA platforms cold — your labs should mimic the **scoring model**, not just the problem:

| Platform | Format | Scoring model (mimic this) | Who uses it |
|---|---|---|---|
| **HackerRank** | auto-graded coding | **% of hidden test cases passed** (partial credit); weighted cases possible; plagiarism + tab-proctoring; "Proctor Mode" (Apr 2025) AI-monitors | Palantir, Stripe (intern), Atlassian, Nvidia |
| **Codility** | auto-graded | **correctness + performance** (Big-O on large data — a correct brute force that TLEs loses the perf points) | Microsoft |
| **CodeSignal GCA** | 70 min, 4 Qs increasing difficulty | shareable score on the **200–600 scale** (the old 300–850 is **deprecated** — don't print it); ~475+ advances many firms, 540+ top; proctored, **AI + logic-search banned** | Uber (GCA) |
| **CodeSignal ICA** | 90 min, 1 project, 4 levels | test-driven; **see §3 — the codebase-style template** | Capital One; the canonical practical template |
| **Karat** | ~60 min human screen | live coding + domain Qs, rubric-scored | Atlassian phone screen |
| **Amazon (own)** | Coding (2 Qs, ~70–90 min) **+ Work Simulation (~50 min, LP-scored inbox) + Work Style Assessment** | correctness + efficiency **+ Leadership-Principle behavior** | Amazon |

Concrete intern loops worth replicating: **Google** = 2×45-min coding in a *plain Google Doc* (no autocomplete) + team match, no system design. **Meta** = CodeSignal multi-stage OA → one ~45-min CoderPad round of 2 medium problems (speed matters). **Microsoft** = Codility (2 Qs, 90 min) → Superday of 2–3×45-min.

---

## 2. DSA topic map (intern difficulty)

~87% of questions map to ~10–12 patterns. Interns skew **easy–medium**. Cover these (the existing `/dsa_patterns/` folder already seeds most):

| Pattern | Intern difficulty | Note |
|---|---|---|
| Arrays & hashing | easy–med | **most common**; hashmap O(1) |
| Two pointers | easy–med | sorted-array / palindrome |
| Sliding window | medium | subarray/substring — high freq |
| Stack / queue | easy–med | valid parens, monotonic |
| Strings / parsing | easy–med | very common in OAs |
| Linked lists | easy–med | reversal, cycle |
| Trees | medium | traversal, BST, recursion |
| Graphs (BFS/DFS) | medium | grid/island common |
| Heaps / PQ | medium | top-K, merge-K |
| Intervals | medium | merge/overlap |
| Binary search | easy–med | on arrays **and on the answer space** |
| Recursion / backtracking | med–hard | permutations, subsets |
| Basic DP | med | 1-D (climbing stairs, coin change); hard DP rare for interns |
| Design-a-data-structure | medium | **LRU cache, min-stack** — bridges to LLD |

---

## 3. The two SWE lab styles — and when to use each

This is the most important authoring decision for SWE. **Pick a style per company.**

### Style A — Algorithmic
One well-scoped DSA problem; the learner narrates approach, optimizes Big-O, and tests edge cases. This is the classic `/labs/` + `/dsa_patterns/` format. Use for: **Google, Meta, Microsoft, Amazon, Nvidia** (Nvidia with a low-level/C++/CUDA skin — see pack).

### Style B — Codebase / practical (the "if asked by those companies" style)
The learner works **inside an existing/unfamiliar repo** against tests, **ships a feature** or **fixes a bug** — no whiteboard, no abstract puzzle. Use for: **Stripe, Palantir, Uber, Atlassian** (Atlassian's craft/LLD rounds are philosophically aligned).

**The canonical codebase template is the CodeSignal Industry Coding Framework (ICF/ICA).** Build practical labs on this 4-level spine even when the target company doesn't literally use CodeSignal — it's the cleanest model of real feature work:

> **ICF spine (90 min, one project, NOT meant to be finished):**
> - **L1 — Initial design & basic functions (~10–15 min):** define the data model + a small API surface + basic tests.
> - **L2 — Data processing & core logic:** larger transformations, edge cases, more tests.
> - **L3 — Refactoring & encapsulation:** extract modules, apply OOP/design patterns, raise coverage. *This level separates engineers who can **evolve** code from those who only write fresh code — most interns never practice it.*
> - **L4 — Extending design & final features:** add features + cross-cutting concerns (error handling, config) **without breaking earlier levels** (backward compatibility).
> Each level **extends the same problem** → reuse, encapsulate, refactor. Open IDE, test-driven, scored on tests passing.

**Company-specific practical formats to replicate:**
- **Stripe — Integration round:** drop the learner into an unfamiliar repo with a **provided API/SDK + docs**; ship a small working feature in ~45–60 min with **full internet access** (search docs, *not* AI). Graded on a **working change + clean production code (naming, modularity, edge handling)**, not Big-O. Example tasks: parse JSON files → structured data → transform; call a payments-style API and surface specific fields.
- **Stripe — Bug-squash / Bug-bash:** a pinned version of a real OSS library with a **failing test or open issue**; investigate & fix in ~45–60 min. Classic bugs: a missing dir-vs-file path check; a missing AST visitor for a node type; a **race condition** (lost update from an unguarded read-modify-write). **A clear, well-reasoned diagnosis often counts more than a completed fix** — build the rubric to reward diagnosis.
- **Palantir — Decomposition:** ~60-min collaborative session on a **vague, real-world problem with no defined scope** ("design a taxi-dispatch system," "hospital patient-record management"). The learner discovers requirements, defines **entities/ontology (objects-properties-links)**, **API contracts**, workflows, then prioritizes + reasons about tradeoffs + V1. **Not meant to be solved** — it's meant to be *decomposed* out loud. FDSE "system design" = a **data pipeline** (ingestion → cleaning/normalization → ontology → UI), **not** load-balancers. This is exactly what the existing `/labs/` workbook.md trains — it's your gold v1 example.
- **Palantir — HackerRank OA:** 3–5 implementation-heavy "mini-projects" (multi-part, each building on the prior); may include a coding problem + a **SQL query** + an **API integration** task. The existing `/exact_reported_problems/mock_oa/` is the model.

---

## 4. System design for interns

Usually **absent or light**. Where it appears for interns/new-grads it's **LLD/OOD** (design a parking lot, a library, a notification system; "design a data structure" like LRU), **not** distributed HLD. Don't author distributed-systems labs for the intern SWE track except as an optional stretch — and even then, frame Technical-PM-style (`05`). Atlassian and Uber new-grad loops are the main places LLD shows up.

---

## 5. SQL / API / data labs

Keep and generalize the existing `/api_sql_data/`:
- **SQL** — window functions, sessionization, latest-status-per-group, fraud alerts. Core for Palantir FDSE, Uber, Atlassian, and all Technical-PM tracks.
- **API** — pagination/cursoring, CRUD with idempotency, consuming a paginated upstream. Core for Stripe and Technical-PM.

---

## 6. Behavioral / values rounds (yes, even for SWE interns)

Several companies score behavior heavily for SWE interns — author a values lab per company:
- **Amazon** — LP-mapped STAR is **woven through every round**; ~25% of candidates who clear the technical bar are still rejected on behavioral. Build an LP-STAR lab (2+ stories per high-frequency LP).
- **Meta** — the **"Jedi" round** (resolving conflict, growing continuously, embracing ambiguity, driving results, communicating).
- **Atlassian** — the standalone **Values interview** (a hard gate, often run by someone outside the team).
- **Microsoft** — **growth-mindset**-framed STAR in every round.
- **Nvidia** — light, anchored to **Intellectual Honesty** (admit gaps, don't bluff).

---

## 7. The rubric (use these rows in SWE labs)

| Dimension | Strong | Weak |
|---|---|---|
| **Communication (think-aloud)** | clarifies, states assumptions, narrates tradeoffs | silent solving, unexplained jumps |
| **Problem solving** | systematic, multiple approaches, states+optimizes Big-O | brute force, can't reason about complexity |
| **Correctness** | clean, correct, idiomatic | buggy, fights the language |
| **Code quality / readability** | good names, modular | messy, poor naming |
| **Testing & edge cases** | tests normal + corner, self-corrects | declares "done" untested |
| **Debugging** | finds & fixes own bugs calmly | needs interviewer to find bugs |
| **Time management** | finishes the core in the window | over-invests in one part |

For **codebase-style** labs, weight **Code quality**, **Testing**, and **Debugging** higher, and add a **"works against the provided tests/ API"** row. For **bug-squash** labs, add a **"diagnosis quality"** row that can score full marks even without a complete fix.

---

## 8. Common intern mistakes → bake into strong-vs-weak keys

Jump to code without clarifying; not testing / ignoring edge cases (empty/null/single); silent problem-solving; brute force with no optimization; poor variable names; poor time management; **panicking on hints** (incorporating a hint calmly is a positive signal — model that).

---

## 9. What to build for the SWE track (counts in `07`)

Per company, roughly:
- 2–3 **algorithmic** labs on the patterns that company over-indexes (see pack), at rising tiers.
- 1 **codebase/practical** lab **if the company uses that style** (Stripe, Palantir, Uber, Atlassian) — these are the highest-value, most differentiated SWE labs and the ones the user explicitly wants.
- 1 **SQL or API/data** lab where relevant (Palantir, Uber, Stripe, Technical-PM overlap).
- 1 **behavioral/values** lab skinned to the company (§6).
- 1 **mock** (Tier-3, full-length, timed) capstone — e.g., a Palantir-style 90-minute mock OA (the existing `/exact_reported_problems/mock_oa/` is the template).

**Style-by-company cheat sheet:** Google = algorithmic (plain-doc) · Meta = algorithmic (speed) · Microsoft = algorithmic + LLD · Amazon = algorithmic + Work-Simulation/LP · Nvidia = algorithmic with **C++/pointers/CUDA/systems** skin · Stripe = **codebase (integration + bug-squash)** · Palantir = **codebase (decomposition + HackerRank mini-projects + SQL/API)** · Uber = algorithmic + **practical Uber-domain** (routing/pricing/geo) + LLD for grads · Atlassian = algorithmic + **craft/LLD + write-your-own-tests**.
