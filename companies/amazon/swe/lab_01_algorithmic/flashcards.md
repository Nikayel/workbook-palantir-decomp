# Flashcards — Amazon SWE Lab 01: Work-Simulation LP Inbox Triage

*10 cards for spaced repetition. Study these 24–48 hours after completing the workbook. Cover the answer and try to recall it before reading.*

---

## Card 1 — The 16 Leadership Principles (Group 1: Customer + Ownership + Invention + Judgment)

**Q:** Name the first four Amazon Leadership Principles and give one specific SWE behavior that demonstrates each.

**A:**
1. **Customer Obsession** — "Leaders start with the customer and work backwards."
   SWE behavior: Choosing a simpler API surface even if the backend implementation is harder, because users find the complex API confusing.

2. **Ownership** — "Leaders are owners and act on behalf of the entire company."
   SWE behavior: Finding a bug in someone else's code during review and filing a complete bug report with reproduction steps and severity — not just flagging it and moving on.

3. **Invent and Simplify** — "Leaders expect and require innovation and simplification from their teams."
   SWE behavior: Replacing a 500-line custom parser with a 30-line use of an existing library, then writing tests to verify behavioral equivalence.

4. **Are Right, A Lot** — "Leaders are right a lot. They have strong judgment and good instincts."
   SWE behavior: Pushing back on a design decision with a benchmark, not an opinion. Updating your position when better data arrives — even if it contradicts your earlier judgment.

---

## Card 2 — The 16 Leadership Principles (Group 2: Learning + Hiring + Standards + Thinking)

**Q:** Name LPs 5 through 8 and give one specific SWE behavior for each.

**A:**
5. **Learn and Be Curious** — "Leaders are never done learning and always seek to improve themselves."
   SWE behavior: Spending 2 hours reading the RFC for a protocol you are implementing rather than guessing at the edge cases.

6. **Hire and Develop the Best** — "Leaders raise the performance bar with every hire and every interaction."
   SWE behavior: In a code review, explaining WHY a pattern is better — not just marking it wrong — turning the review into a teaching moment for the author.

7. **Insist on the Highest Standards** — "Leaders have relentlessly high standards."
   SWE behavior: Rejecting a PR that works correctly but has no test coverage for edge cases, even when the team is under deadline pressure.

8. **Think Big** — "Leaders create and communicate a bold direction that inspires results."
   SWE behavior: Proposing that a single-team internal script could be turned into a platform for the whole org, and writing the one-pager design doc unprompted.

---

## Card 3 — The 16 Leadership Principles (Group 3: Action + Frugality + Trust + Depth)

**Q:** Name LPs 9 through 12 and give one specific SWE behavior for each.

**A:**
9. **Bias for Action** — "Speed matters. Many decisions and actions are reversible and do not need extensive study."
   SWE behavior: Launching a 1% traffic experiment to validate a hypothesis in 2 hours rather than spending three weeks in design review for a decision that can be reversed.

10. **Frugality** — "Accomplish more with less. Constraints breed resourcefulness, self-sufficiency, and invention."
    SWE behavior: Using a managed database that costs $500/month instead of building a custom data store that would consume 3 weeks of engineering time — because the total cost of ownership of the custom solution is higher.

11. **Earn Trust** — "Leaders listen attentively, speak candidly, and treat others respectfully."
    SWE behavior: Writing a post-incident report that names your own mistake specifically, describes its blast radius, and states exactly what you changed — not a vague "improved team communication."

12. **Dive Deep** — "Leaders operate at all levels, stay connected to the details, audit frequently."
    SWE behavior: Reading the stack trace all the way to the root cause rather than stopping at the first plausible explanation. Running the bug under production conditions before declaring it fixed.

---

## Card 4 — The 16 Leadership Principles (Group 4: Backbone + Results + Employer + Scale)

**Q:** Name LPs 13 through 16 and give one specific SWE behavior for each.

**A:**
13. **Have Backbone; Disagree and Commit** — "Leaders are obligated to respectfully challenge decisions they disagree with, even when doing so is uncomfortable."
    SWE behavior: Writing a test case that reproduces a race condition you spotted in a senior engineer's PR, sharing it in the PR thread, and maintaining the objection until the evidence is acknowledged — not deferring to seniority.

14. **Deliver Results** — "Leaders focus on the key inputs for their business and deliver them with the right quality and in a timely fashion."
    SWE behavior: Cutting a non-critical feature from the sprint scope to ship the core feature on time, proactively notifying the PM rather than waiting to be told you are behind.

15. **Strive to be Earth's Best Employer** — "Leaders work every day to create a safer, more productive, higher performing, more diverse, and more just work environment."
    SWE behavior: Noticing that a newer team member's ideas are being talked over in design review and explicitly inviting them to finish their thought.

16. **Success and Scale Bring Broad Responsibility** — "We must be humble and thoughtful about the secondary effects of our actions."
    SWE behavior: Raising a privacy concern about a feature that is legally compliant but that could expose user behavioral data to third parties — raising it before implementation, not after.

---

## Card 5 — The Four Load-Bearing LPs for SWE Candidates

**Q:** Which four LPs are most commonly evaluated in Amazon SWE Work Simulations and behavioral interviews? Why these four specifically?

**A:** Customer Obsession, Ownership, Dive Deep, and Deliver Results.

**Why these four:** They map directly to the core SWE behaviors that distinguish strong from weak candidates:

- **Customer Obsession:** Do you make decisions that serve users, or decisions that serve your own convenience or the speed of implementation?
- **Ownership:** When something goes wrong, do you act like it is your problem regardless of whose code or system it is?
- **Dive Deep:** Do you understand your system at the detail level, or do you accept "it works" without knowing why — until it doesn't?
- **Deliver Results:** Do you ship things, or do you spin in planning, refinement, and stakeholder alignment indefinitely?

The other LPs matter too, but these four appear in nearly every Work Simulation scenario and every SWE behavioral loop. If you can only internalize four LPs in depth before an Amazon interview, make it these four.

---

## Card 6 — Bar Raiser Role and Veto

**Q:** What is the Bar Raiser in Amazon's hiring process, what authority do they have, and how should this affect how you prepare?

**A:** The Bar Raiser is a specially trained Amazon employee from a different team who joins the interview loop as an independent evaluator. They are not the hiring manager and have no interest in filling the headcount.

**Authority:** The Bar Raiser has effective veto power. If the Bar Raiser votes No Hire, the candidate does not receive an offer — even if the rest of the loop is unanimously positive. This asymmetry is intentional and designed to prevent teams from "lowering the bar" under pressure to hire quickly.

**What they evaluate:** Whether the candidate would raise the average performance bar of the team they are joining — not "good enough to do the job" but "better than the bottom 50% of current employees at this level." They probe specifically for LP specificity in STAR stories and for candidates who say "we" instead of "I."

**Preparation implications:**
- Have STAR stories with quantified results and "I" language ready for failure, backbone, ownership, and dive-deep scenarios.
- The Bar Raiser will ask the most uncomfortable question in your loop — often about a genuine failure or a time you disagreed with a direction. They are testing self-awareness and intellectual honesty, not perfection.
- Generic LP mentions ("I always think about the customer") fail. Specific behavioral evidence ("I re-ran the benchmark after the senior engineer pushed back, found it supported my original position, and shared the results") passes.

---

## Card 7 — LP Tension Examples (Bias for Action vs Think Big; Backbone vs Earn Trust)

**Q:** Name two common LP tension pairs that appear in SWE scenarios. For each pair, describe how they pull in opposite directions and how Amazon expects you to resolve it.

**A:**

**Bias for Action vs. Think Big:**
- Tension: Bias for Action says "make reversible decisions fast, stop over-analyzing." Think Big says "consider the broader system implications, don't optimize locally at the expense of the bigger picture."
- Resolution: use reversibility as the decision rule. Reversible actions (a feature flag, a 1% experiment, a local refactor) → Bias for Action wins, move fast. Irreversible or hard-to-undo actions (a database schema, a public API contract, an architectural choice that will touch 10 teams) → Think Big wins, take time to consider second-order effects.
- SWE example: ship an MVP behind a flag immediately (Bias for Action), but design the public API contract carefully in a design review (Think Big), because changing an API contract after customers depend on it is extremely costly.

**Have Backbone; Disagree and Commit vs. Earn Trust:**
- Tension: Backbone says "challenge decisions you disagree with, even upward, even when it's uncomfortable." Earn Trust says "listen attentively, treat people respectfully, be aware of your own biases."
- Resolution: Backbone requires evidence and respect simultaneously. Earn Trust requires candor, not compliance. The two LPs are complementary, not opposed. You disagree WITH EVIDENCE (which builds trust by demonstrating rigor). You commit fully AFTER THE DECISION (which also builds trust by demonstrating reliability). A candidate who defers to avoid conflict fails Backbone. A candidate who keeps pushing after the decision fails Earn Trust.

---

## Card 8 — STAR Structure with "I" Language and Quantified Results

**Q:** What are the four STAR components? What is the most common failure mode in each, and how do you fix it?

**A:**

**Situation:** 1–2 sentences of context. What was the setting, what was at stake, what was the scale?
- Common failure: too much context. Five sentences of backstory before anything happens.
- Fix: assume the interviewer is smart. State the minimum needed to understand why the task was hard.

**Task:** Your specific responsibility. Must say "I", not "we."
- Common failure: "Our team needed to reduce the p99 latency."
- Fix: "I was responsible for identifying and fixing the root cause of the 3× latency regression that was blocking the November launch."

**Action:** What you specifically did. This is 60% of the story. Be concrete — name the specific decision, the specific tool, the specific obstacle.
- Common failure: "I worked with the team to investigate and resolve the issue."
- Fix: "I profiled the production traffic replay and found a missing index on the orders table. I wrote the migration, tested it against a production-scale dataset in staging, and deployed with a canary that monitored write latency. When the index increased write latency by 8%, I rolled back and proposed a read-through caching layer instead."

**Result:** Quantified outcome. What changed? What did you learn? What stuck?
- Common failure: "the project was a success" or "my manager was happy."
- Fix: "P99 latency dropped from 800ms to 120ms, shipping the November launch on time. The profiling workflow I used is now the team standard for latency investigations."

Quantification rule: if you cannot find an exact number, use a direction and a reasonable estimate. "Roughly 40% fewer support tickets" beats "significantly fewer support tickets" which beats "fewer support tickets."

---

## Card 9 — Disagree and Commit: Meaning and Misreadings

**Q:** What does "Disagree and Commit" actually mean? Name two common misreadings and explain why each is wrong.

**A:** Disagree and Commit means: when you disagree with a decision, you make your position known clearly and with supporting evidence (disagree). Once the decision is made through the proper process, you execute it with full effort, as if you had proposed it yourself (commit).

**Misreading 1: "Commit means I was wrong."**
Wrong. Committing to a decision does not mean accepting that you were wrong or that you agree with the outcome. You may still believe your original position was better. The LP asks you to execute the team's decision at full quality regardless. Your belief about the architecture does not change your quality of implementation.

**Misreading 2: "Disagree means I keep raising the issue until I get my way."**
Wrong. The "disagree" phase happens ONCE — before the decision is made. Once the decision is made, the disagree phase is over. Continuing to relitigate a settled decision is not backbone; it is a failure to commit and a violation of Earn Trust. If material new evidence arrives after the decision (e.g., the architecture you warned about begins failing at the predicted load 6 months later), you can re-open the discussion with that new data — that is not relitigating, it is new information.

**Misreading 3: "Commit means visible compliance, private resistance."**
Wrong. "Commit wholly" is explicit in the LP. Half-hearted implementation that "technically follows" the decision while avoiding the spirit of it violates both Disagree and Commit and Insist on the Highest Standards. The Bar Raiser will probe for this: "How did you implement the decision after you lost the argument?" is a standard probe for full vs. superficial commitment.

---

## Card 10 — Amazon Writing Culture as a Signal in Work Simulation

**Q:** Amazon is known for a writing culture (6-page narratives over slides, PR/FAQ documents). How does this appear in the SWE OA Work Simulation, and what writing behaviors earn higher scores?

**A:** Amazon's writing culture reflects the belief that clarity of writing reflects clarity of thinking. Verbal fluency can mask fuzzy reasoning; structured writing cannot.

In the Work Simulation, this surfaces as:
- Scenarios that present written messages and ask you to select or draft responses.
- Scoring that rewards: responses that are short, lead with the decision, and make the LP reasoning visible in the logic — not tacked on at the end as a label.

Writing behaviors that earn higher Work Simulation scores:

1. **Lead with the decision.** "I'll raise this issue with my manager now, before the Thursday demo." Not: "There are several things to consider here, including the deadline, the technical risk, and the team dynamics..."

2. **Name the LP in the reasoning, not as a tag.** "Shipping a known load defect violates Insist on the Highest Standards, so I'll raise it now even if it risks the demo." Not: "I'd raise the issue (LP: Insist on the Highest Standards)."

3. **Quantify or specify when possible.** "The race condition will fail at > 1,000 concurrent users. Our production rollout is 50,000." Not: "There is a scalability concern."

4. **No padding.** The word "various" is a red flag. "Several stakeholders" means you haven't identified them. Name them or don't cite them.

The Work Simulation scorer reads responses the way a Bar Raiser reads a STAR story — looking for specificity, first-person agency, and LP reasoning that is behavioral (describes an action) rather than philosophical (describes a value).

---

*10 cards · Amazon SWE Lab 01 · Work-Simulation LP Inbox Triage · Review 24–48 hrs after completing workbook*
