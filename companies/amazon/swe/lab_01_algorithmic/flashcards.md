# Amazon SWE Lab 01 — Flashcards

10 cards. Study until each answer comes in < 5 seconds.

---

## Card 01 — Binary Search on Answer Template

**Q:** Write the binary search on answer template from memory.

**A:**
```python
def solve(inputs, k):
    def can_finish(limit):
        # Check: given this limit, can k workers (or units) handle all inputs?
        # Return True if feasible, False if not
        ...

    lo = [minimum possible answer]   # e.g., max(inputs) for makespan problems
    hi = [maximum possible answer]   # e.g., sum(inputs) for 1-worker case

    while lo < hi:
        mid = (lo + hi) // 2
        if can_finish(mid):
            hi = mid       # mid is feasible — try lower
        else:
            lo = mid + 1   # mid is too low — need more

    return lo
```

**When to use:** "Minimize the maximum" or "find the smallest X such that Y is possible." The feasibility check must be monotone: if X works, X+1 also works.

---

## Card 02 — Dijkstra Time Complexity

**Q:** What is Dijkstra's time complexity with a binary heap, and what does each term come from?

**A:**

**O((V + E) log V)**

- **V log V**: Each of the V nodes is popped from the heap at most once. Each pop is O(log V) for a binary heap.
- **E log V**: Each of the E edges causes at most one push to the heap. Each push is O(log V).
- Combined: O((V + E) log V).

**With Fibonacci heap:** O(E + V log V) — better when E >> V. Rarely used in practice due to implementation complexity.

**BFS comparison:** O(V + E) — same traversal cost but no heap. Works for unweighted graphs only.

**When V and E are similar order:** O(E log V) is the dominant term.

---

## Card 03 — When to Binary Search vs Greedy

**Q:** How do you decide between binary search on answer vs a direct greedy algorithm?

**A:**

**Use binary search on answer when:**
- The answer is a numeric range (time, capacity, size)
- Feasibility is monotone: if X works, X+1 also works
- Computing feasibility for a fixed X is straightforward (usually O(n) or O(n log n))
- Direct calculation of the optimal value is non-obvious

**Use greedy when:**
- Local optimal choice leads to global optimum (provable exchange argument)
- The answer has a direct formula (e.g., if tasks are splittable: answer = ceil(total_work / k))
- Greedy gives O(n log n) and binary search would give O(n log n) anyway — greedy is simpler

**Distinguishing signal:** If you find yourself wanting to try "what if the answer is X?" — that's the binary search framing. If you find yourself wanting to build the answer up incrementally — that's greedy.

---

## Card 04 — Which LPs Show in SWE Code

**Q:** Name 4 Leadership Principles that a SWE can demonstrate through code and explain how.

**A:**

| LP | How it shows in SWE code |
|---|---|
| **Dive Deep (LP 12)** | Testing edge cases (k > n, empty input, disconnected graph). Staying connected to details means not declaring "done" without testing boundary conditions. |
| **Insist on the Highest Standards (LP 7)** | Code readability, naming, no magic numbers. Comments that explain WHY, not what. A Bar Raiser can read your code and understand your thinking. |
| **Bias for Action (LP 9)** | Attempting a brute force first, then optimizing. Not paralyzed by "what if it's not optimal" — write something that works, then improve. |
| **Invent and Simplify (LP 3)** | Choosing a simpler algorithm when it's sufficient. Not over-engineering. Using O(n) when O(n log n) isn't needed. |

**Pro move:** In an Amazon interview, name the LP when you make a decision: "I'm going to write the brute force first — Bias for Action — then we can optimize once we have something working."

---

## Card 05 — Bar Raiser Role

**Q:** What is the Bar Raiser's job, and how does it differ from a standard interviewer?

**A:**

The Bar Raiser is a trained, certified Amazon employee (often from a different team) who participates in every interview loop. Their job:

1. **Independent assessment:** They evaluate independently of the hiring team. If the team wants to hire and the Bar Raiser says "no hire," the candidate does not get an offer.

2. **Hold the bar:** They assess whether the candidate would raise the average quality of the team — not just "is this person good enough," but "is this person better than the bottom 50% of current employees at this level?"

3. **LP depth:** Bar Raisers are trained to probe LP stories for specifics. Generic STAR answers fail. "I worked on a project" = fail. "I identified a 40% latency spike on the payment service, traced it to a database query, proposed a caching layer, and deployed it in 48 hours — improving p99 latency from 800ms to 120ms" = Bar Raiser-level specificity.

4. **Veto authority:** The only person in the loop who can unilaterally block a hire.

---

## Card 06 — Work Simulation Scoring on LPs

**Q:** How is Amazon's Work Simulation (inbox triage) scored, and what is the key insight for doing well?

**A:**

The Work Simulation presents scenarios as emails/messages from stakeholders. You choose how to respond from multiple options. Each scenario maps to 1–2 Leadership Principles.

**Scoring:** Your response is scored on how well it aligns with the LP the scenario tests. The "correct" answer is the one that most clearly demonstrates the target LP.

**Key insight:** The correct answer is NOT necessarily the most efficient answer or the nicest answer. It's the answer that demonstrates the specific LP being tested. Examples:

- Scenario about customer complaint → Customer Obsession response (prioritize customer, even at short-term cost)
- Scenario about peer disagreement → Have Backbone response (respectfully push back, provide evidence, commit after decision)
- Scenario about missing data before a decision → Dive Deep response (get the data, don't guess)

**Preparation:** Before the OA, read through all 16 LPs and internalize the defining behavior for each. When you see a scenario, ask: "Which LP is this testing?" Then choose the answer that best exemplifies that LP — even if it's the harder or less comfortable option.

---

## Card 07 — Amazon OA Format

**Q:** What are the 3 components of the Amazon SWE OA, and how much time is allotted for each?

**A:**

| Component | Time | Format |
|---|---|---|
| Coding problems | ~70 min | 2 medium LeetCode-style problems in a code editor with test cases |
| Work Simulation | ~35 min | Inbox triage — choose response from multiple-choice options for ~8–10 email scenarios |
| Work Style Assessment | ~15 min | Self-report personality/work preferences; used for calibration, not pass/fail |

**Total:** ~2 hours

**Strategy:**
1. Coding first (most heavily weighted). Don't start WS until coding is submitted.
2. For each coding problem: read, identify pattern, brute force in words, optimize, code, test.
3. For WS: go with your gut on LP alignment. Overthinking is not rewarded.
4. Work Style Assessment: there are no "right" answers. Be authentic — inconsistent responses (trying to game it) are detected.

---

## Card 08 — STAR Structure for LP Stories

**Q:** Write out the STAR structure with Amazon-specific guidance for each component.

**A:**

**S — Situation (1–2 sentences)**
Set the context. Team size, company stage, what was at stake. Be specific about scale.
Bad: "I was working on a big project."
Good: "I was leading backend development for a 3-person team building Amazon's internal supplier onboarding tool, handling 500 new suppliers per week."

**T — Task (1 sentence)**
What were YOU specifically responsible for? Not "we" — "I."
Bad: "We needed to reduce latency."
Good: "I was responsible for identifying and fixing the root cause of a 3x latency regression that was blocking the November launch."

**A — Action (3–5 sentences, most important)**
What YOU did. Specific steps. Obstacles you overcame. Evidence you were driving, not following.
Bad: "I worked with the team to find the problem and fix it."
Good: "I ran a profiling session and traced the spike to a missing database index. I proposed adding the index, wrote the migration script, tested it in staging against production-scale data, and deployed with monitoring. When the index degraded write performance by 8%, I rolled back and proposed a caching layer instead."

**R — Result (1–3 sentences)**
Quantified outcome. What changed? What did you learn?
Bad: "The latency improved."
Good: "P99 latency dropped from 800ms to 120ms. The launch shipped on time. I documented the profiling workflow and it's now standard practice for the team."

---

## Card 09 — "Invent and Simplify" in Code

**Q:** What does "Invent and Simplify" look like in a SWE interview, and what is its opposite?

**A:**

**Invent and Simplify (LP 3)** in code means:
- Choosing the simplest algorithm that meets the requirements
- Not over-engineering for hypothetical future needs
- Recognizing when O(n log n) is overkill and O(n) is sufficient
- Writing readable, maintainable code over clever-but-unreadable code

**Examples:**
- Using a dict instead of a Trie when there's no prefix query
- Using BFS instead of Dijkstra for an unweighted graph
- Writing a single loop instead of three map/filter chains

**Its opposite:** Premature optimization. Building infrastructure for problems you don't have. Adding abstraction layers that don't reduce complexity.

**Interview signal:** When you choose your algorithm, say: "I'm using a hash map here — simpler than a Trie, and since we don't need prefix queries, it's sufficient. Invent and Simplify." This explicitly demonstrates LP awareness.

---

## Card 10 — k-Worker Scheduling Pattern

**Q:** Describe the k-worker scheduling pattern and its two common formulations.

**A:**

The k-worker scheduling (parallel processing) pattern appears frequently in Amazon OAs. It has two common formulations:

**Formulation 1: Minimize makespan (minimum time to complete all tasks)**
- Binary search on T
- can_finish(T): use greedy assignment (sort tasks descending, assign to least-loaded worker using min-heap)
- lo = max(tasks), hi = sum(tasks)
- Time: O(n log(sum) × n log k)

**Formulation 2: Minimize workers needed (given time budget T, what's the min k?)**
- Direct formula: workers_needed = sum(ceil(task / T) for task in tasks)
- No binary search needed — one pass

**Formulation 3: Minimize time to process all tasks where each task goes to exactly one worker, workers work in parallel**
- If workers are identical and tasks indivisible: binary search on T, greedy assignment
- If tasks are splittable: answer = ceil(sum(tasks) / k) — just division

**Key insight:** Always clarify which formulation you're solving before you code. "Minimize makespan" vs "minimize workers needed" vs "splittable tasks" are three different problems with different solutions.
