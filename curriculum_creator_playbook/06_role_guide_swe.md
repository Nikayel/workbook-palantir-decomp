# 06 · Role Guide — Software Engineer (SWE) Intern

> **Audience:** the curriculum creator.
> **Purpose:** how to author the SWE track, including the **"codebase / practical" style** the user specifically asked about (Stripe integration & bug-squash, Palantir decomposition, the CodeSignal Industry-Coding-Framework). Pair with the company pack and `03`.

The existing Palantir labs (`/labs/`, `/dsa_patterns/`, `/api_sql_data/`, `/exact_reported_problems/`) are your v1 SWE material. This guide generalizes them to 10 companies.

> **North-star decision for the SWE track: the workbook format is for *building and evolving systems*, not for grinding DSA.** The 8-part decomposition arc earns its keep only when there is ambiguity to scope, entities to model, and tradeoffs to defend — i.e. **codebase / decomposition / practical / low-level-debugging / design-a-data-structure** work. A pure algorithm puzzle ("two-pointer max subarray") has none of that, and instant-judge platforms (LeetCode / NeetCode / HackerRank) drill patterns far better than a markdown file can.
>
> **So, for SWE:**
> - **Author *workbooks* for system-building** — codebase rounds, decomposition, design-a-data-structure/LLD, low-level debugging. These are the differentiated, high-signal labs (and the ones the user explicitly wants).
> - **Handle pure DSA as *drills*, never as 8-part workbooks** — a pattern map (§2) → curated external problem sets → a spaced flashcard per pattern → one timed mock-OA *assessment*.
> - Interns still face DSA online assessments at most companies, so DSA still matters — it just lives in a lighter modality. The **mock-OA capstone** is the only place pure DSA appears in this curriculum, and it's a Tier-3 *test*, not a teaching workbook.

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

## 2. DSA: the *drill* map (a grind list, NOT a workbook source)

~87% of questions map to ~10–12 patterns. Interns skew **easy–medium**. **Do not turn these into decomposition workbooks** — point learners at curated LeetCode/NeetCode sets, attach one spaced flashcard per pattern (pattern → when-to-use → complexity), and let the timed mock-OA (§9) be the only place they appear *inside* this curriculum. The one exception is the **last row** — *design-a-data-structure* — which graduates into a real workbook (it's mini-system-building, §3.3):

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

## 3. The SWE workbook styles (all are system-building)

Every SWE *workbook* is one of these four system-building types. (Pure DSA is a **drill**, per §2 — it is deliberately not on this list.) Pick the style from the company pack.

### 3.1 Codebase / practical — *the primary SWE workbook*
The learner works **inside an existing/unfamiliar repo** against tests, **ships a feature** or **fixes a bug** — no whiteboard, no abstract puzzle. The flagship style for **Stripe, Palantir, Uber, Atlassian**, and the right default whenever a company's round is practical.

### 3.2 Decomposition — *the Palantir-style workbook*
A vague, unscoped real-world problem the learner **decomposes** out loud (stakeholders → entities/ontology → API contract → workflows → MVP → tradeoffs). The existing `/labs/` are the gold v1 example. **This is the SWE format that most embodies the whole workbook idea** — and the strongest argument for why interns benefit from a workbook at all.

### 3.3 Design-a-data-structure / LLD — *the gray-zone DSA that IS a workbook*
LRU cache, rate limiter, hit-counter-with-expiry, min-stack, "design an A/B-test class," a notification system, a parking lot. These are mini-systems with a contract, state, and edge cases — so the 8-part arc fits. **This is how the "DSA-flavored" companies (Google/Meta/Microsoft/Amazon) still get real workbooks** without turning two-pointer puzzles into workbooks.

### 3.4 Low-level / debugging — *the Nvidia/Apple-systems workbook*
Find the bug in a 250-line C program; implement a primitive (thread-safe queue, `shared_ptr` with refcount, `malloc`); reason about pointers/memory/concurrency. System-building at the systems layer.

The canonical spine for 3.1–3.3 is the **CodeSignal Industry Coding Framework (ICF/ICA)** — build practical labs on this 4-level model even when the company doesn't literally use CodeSignal:

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

The SWE *workbooks* per company (**not** pure-DSA — that's the shared drill kit):
- 1–2 **system-building** labs in the company's style (§3): codebase/practical, decomposition, design-a-DS/LLD, or low-level/debugging.
- 1 **SQL or API/data** lab where relevant (Palantir, Uber, Stripe, Technical-PM overlap).
- 1 **behavioral/values** lab skinned to the company (§6).
- 1 **timed mock-OA** capstone (Tier-3) — the *only* place pure DSA appears, and it's an assessment, not a teaching workbook. The existing `/exact_reported_problems/mock_oa/` is the template.

Plus, authored **once and shared** (not per company, not a workbook): the **DSA drill kit** — the §2 pattern map → curated LeetCode/NeetCode sets → a spaced flashcard per pattern. Interns grind this alongside the workbooks; most "algorithmic" prep lives here, not in a workbook.

**Style-by-company cheat sheet (the *workbook* style; DSA is always a drill on top):** Google = design-a-DS + ambiguity-narration + mock · Meta = CodeSignal-ICF multi-stage (codebase) + AI-enabled + mock · Microsoft = **LLD/OOD** ("design an A/B-test class") + mock · Amazon = **Work-Simulation + design-a-DS** + mock · Nvidia = **low-level/debugging + implement-a-primitive** (C++) · Stripe = **codebase (integration + bug-squash)** · Palantir = **decomposition + HackerRank mini-projects + SQL/API** · Uber = **practical domain (routing/pricing/geo) + rate-limiter design-a-DS** · Atlassian = **craft/LLD + write-your-own-tests** · Apple = **practical/domain (iOS, embedded "implement malloc")**. Every company also gets a behavioral/values lab + the shared DSA drill kit.
