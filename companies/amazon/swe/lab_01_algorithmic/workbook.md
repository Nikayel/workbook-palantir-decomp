Status: Ready — work through all parts in order

# Amazon SWE Lab 01 — Work-Simulation Inbox Triage
## LP Inbox Lab (Tier 2 — Completion)

**Role:** SWE | **Tier:** 2 (structure provided, substance is yours to fill in) | **Est. time:** 50 min | **Difficulty:** Medium

---

## Scenario

You're a software engineer on the Amazon Prime team, three months into the job. You log into your laptop Monday morning and find a backlog of messages that arrived over the weekend. You have 50 minutes to process them before your 10am standup.

Each message requires you to read it, decide on the best response or action, and record which Leadership Principle guided your decision. Your responses are scored against Amazon's Leadership Principles — not by correctness in the technical sense, but by whether they reflect the LP-driven decision-making framework Amazon uses to evaluate all employees.

This is not a coding lab. It tests LP awareness in practical SWE scenarios.

**The clock is running. Go.**

---

## Milestones

- [ ] M1 · LP mapped — can name all 16 LPs from memory (or from your list) before starting the inbox
- [ ] M2 · Inbox processed — worked through all 12 scenarios, selected and recorded a response for each
- [ ] M3 · LP linked — each response explicitly linked to 1-2 LPs with behavioral reasoning ("I chose A because LP X means... and in this context that looks like...")
- [ ] M4 · STAR prepared — drafted one STAR story per distinct scenario type that arose in the inbox
- [ ] M5 · Defended — explained 3 counter-intuitive LP choices (e.g., why "Disagree and Commit" is NOT the same as compliant silence, or why "Dive Deep" is not "perfectionism")
- [ ] M6 · Ready — self-graded ≥ 28/35 on two separate attempts

---

## Part 1 — LP Warm-Up

**Before opening the inbox, do this cold.**

"Without looking at any list, write down as many of the 16 Amazon Leadership Principles as you can. Then check against the answer below."

Your list (fill in):
1. [blank]
2. [blank]
3. [blank]
4. [blank]
5. [blank]
6. [blank]
7. [blank]
8. [blank]
9. [blank]
10. [blank]
11. [blank]
12. [blank]
13. [blank]
14. [blank]
15. [blank]
16. [blank]

**The 16 Amazon Leadership Principles (check your answers):**
1. Customer Obsession
2. Ownership
3. Invent and Simplify
4. Are Right, A Lot
5. Learn and Be Curious
6. Hire and Develop the Best
7. Insist on the Highest Standards
8. Think Big
9. Bias for Action
10. Frugality
11. Earn Trust
12. Dive Deep
13. Have Backbone; Disagree and Commit
14. Deliver Results
15. Strive to be Earth's Best Employer
16. Success and Scale Bring Broad Responsibility

How many did you get? Score: __ / 16

**Checkpoint M1:** Check the box if you attempted this cold before peeking.

---

## Part 2 — LP Framework for SWE

*The 4 most load-bearing LPs for SWE candidates in both OA and interviews. Fill in what each LP actually means in code behavior — not the abstract phrase, but the specific action it drives.*

**Customer Obsession** — "Leaders start with the customer and work backwards."
In code decisions, this looks like: [blank]

*Model answer:* Choosing a simpler API surface even if the implementation is harder. Writing tests that simulate user behavior, not implementation details. Raising a concern about a feature that works technically but will confuse users. Advocating for performance improvements that affect user-facing latency, even if backend metrics look fine.

**Ownership** — "Leaders are owners. They act on behalf of the entire company, beyond just their own team."
When a bug is found, Ownership looks like: [blank]

*Model answer:* Filing a clear bug report with reproduction steps, severity assessment, and immediate mitigation (not just flagging it and moving on). Not saying "that's the other team's code." Checking whether the same bug exists in related systems. Staying through the incident even if your shift ended.

**Dive Deep** — "Leaders operate at all levels, stay connected to the details."
In a testing and debugging context, Dive Deep looks like: [blank]

*Model answer:* Not accepting "it works on my machine." Running the bug under the exact same conditions as production. Reading the stack trace all the way to the root cause, not stopping at the first plausible explanation. Writing a regression test that pins the exact failure condition before fixing.

**Deliver Results** — "Leaders focus on the key inputs and deliver with the right quality and in a timely fashion."
In scope decisions, Deliver Results affects choices in this way: [blank]

*Model answer:* Knowing which features are MVP and which are nice-to-have — and cutting the latter under time pressure without being asked. Communicating deadline risk early enough that the team can adjust. Not letting perfect be the enemy of shipped. Choosing a testable, complete subset over a speculative, large one.

---

## Part 3 — Inbox: 12 Scenarios

*For each scenario: select the best response (A, B, or C), name the primary LP, and write 1-2 sentences explaining the LP-to-behavior link. There is always a best answer, though the differences are sometimes subtle.*

---

### Scenario 1 — The Load Bug

Your manager asked you to ship a feature by Friday. It's Tuesday afternoon. You discover that the current implementation will fail under load > 1,000 concurrent users due to a race condition you introduced. The demo on Thursday uses 500 users max. The real rollout is 50,000 users on Monday.

**Options:**
A) Raise the issue now, propose a fix, and risk missing Friday's demo deadline
B) Ship Friday, file a ticket for the load issue after the demo, and don't mention it to your manager
C) Stay late Tuesday and Wednesday, fix the architecture silently, and ship on time without mentioning the delay risk

Best response: [blank]

LP: [blank]

Reasoning: [blank]

*Model answer:* A. Ownership — raising the issue before it becomes a production incident IS the ownership behavior. "Acting on behalf of the whole company" means you cannot knowingly ship a defect that will fail in production. B violates Insist on the Highest Standards AND Earn Trust. C is better than B (you fix it) but violates Earn Trust — your manager cannot make a good decision about the Thursday demo without knowing the risk. LP-driven behavior: communicate the risk AND the fix plan simultaneously.

---

### Scenario 2 — The Senior Engineer's PR

A colleague's PR has a subtle race condition you spotted in review. You've re-read the code three times and are confident the bug exists. They are a senior engineer with 8 years at Amazon, and they push back in the review thread: "You're overthinking this — it's not a race condition."

**Options:**
A) Defer to their seniority and approve the PR
B) Escalate to your manager before responding
C) Write a test case that reproduces the race condition and share it in the PR thread

Best response: [blank]

LP: [blank]

Reasoning: [blank]

*Model answer:* C. Have Backbone; Disagree and Commit — but the "disagree" phase here requires evidence, not assertion. Writing a test that reproduces the race condition is backbone backed by data. It respects the senior engineer by letting the code speak rather than asserting authority. A violates Have Backbone. B violates Earn Trust (escalating before doing the work to prove your point makes you look like you're avoiding a difficult conversation). LP note: backbone without evidence is stubbornness; backbone with evidence is engineering rigor.

---

### Scenario 3 — The Ambiguous Spec

Your tech lead left a Slack message Friday at 6pm: "Build the user export feature by Wednesday." There is no design doc, no API spec, and no ticket. It's Monday morning. Your lead is in Tokyo and won't be online for 6 hours.

**Options:**
A) Wait for your lead to come online before starting anything
B) Write a design doc with your best interpretation of the scope, send it to your lead now, and start on the parts you're confident about
C) Build the full feature as you imagine it and show it to your lead Wednesday

Best response: [blank]

LP: [blank]

Reasoning: [blank]

*Model answer:* B. Bias for Action — "Many decisions and actions are reversible and do not need extensive study." Starting the parts you're confident about (e.g., setting up the scaffolding, reviewing the user data model) while simultaneously documenting your interpretation and sending it for review is the high-agency move. A is too passive. C risks building the wrong thing for two days. The design doc is not "studying too long" — it takes 30 minutes and de-risks the Wednesday deadline significantly.

---

### Scenario 4 — The Cost-Aware Design

You are designing a new service that needs to store 10M user records. You could use DynamoDB (simple, fully managed, ~$500/month for this load) or build a custom Redis cluster (more complex, requires ops, ~$80/month). Your manager says "don't over-engineer it" but also "we're watching costs."

**Options:**
A) Use DynamoDB because it's simpler and your time is worth more than $420/month
B) Build the Redis cluster because $5,040/year in savings is meaningful at scale
C) Propose both options to your manager with total cost of ownership (including engineering time) and let them decide

Best response: [blank]

LP: [blank]

Reasoning: [blank]

*Model answer:* C, with an LP pull: this is a Frugality situation ("accomplish more with less") but it also invokes Are Right, A Lot (you need data to know if you're right) and Earn Trust (your manager said "I'm watching costs" — presenting them with a real tradeoff earns trust more than unilaterally picking one). If pushed to choose without manager input: A, because Frugality does NOT mean always choose the cheapest option — it means being resourceful. Engineering time at $200/hr means 2 hours/month of ops time wipes out the Redis savings. Frugality requires calculating total cost, not just cloud spend.

---

### Scenario 5 — The Slow Feature

While implementing a new feature, you discover that the existing database query it depends on takes 800ms for users with > 500 orders (about 12% of Prime users). The feature works correctly but will be slow for a significant minority. The deadline is Thursday.

**Options:**
A) Ship it — the feature works. File a ticket to optimize the query later.
B) Delay the feature until you can optimize the query.
C) Ship the feature but add a metric that alerts when p95 latency exceeds 500ms, and commit to fixing the query in the next sprint.

Best response: [blank]

LP: [blank]

Reasoning: [blank]

*Model answer:* C. Customer Obsession + Deliver Results in tension. C threads the needle: you deliver on schedule, but you are not ignoring the customer experience (adding the metric and the explicit commitment). A without the metric violates Customer Obsession — you are knowingly degrading the experience for 12% of Prime users without any plan to detect or address it. B violates Deliver Results unless the deadline was set knowing the query was an issue. The metric is the LP-aware move: it shows you internalized the customer impact and created accountability.

---

### Scenario 6 — The Junior Developer

A junior engineer on your team is stuck on a bug for 3 hours. You could fix it for them in 10 minutes. Their approach is inefficient and the code quality is low. You have your own work to do.

**Options:**
A) Fix it for them directly — it's faster and you're both behind
B) Ask them to explain the bug to you, then guide them to the fix with questions, then review the final code with feedback on quality
C) Tell them to check Stack Overflow and come back if still stuck

Best response: [blank]

LP: [blank]

Reasoning: [blank]

*Model answer:* B. Hire and Develop the Best — "Leaders are always looking for ways to raise the performance bar." Teaching the debugging process and giving code quality feedback IS the Amazon behavior, even under time pressure. A is efficient but does not develop the junior engineer — next week they have the same problem and you spend 10 more minutes. C is dismissive. B costs you 30 minutes but builds the team's capability. This is an explicit LP trade-off: short-term output vs. long-term team quality. Amazon scores this as B.

---

### Scenario 7 — The Small Feature with Big Implications

You're implementing a "share cart" feature — users can send a link that lets a friend see their current shopping cart. An edge case: the cart can contain items from the user's wish list, which they may not want to share publicly. No one has flagged this.

**Options:**
A) Implement as specced — the product team didn't ask you to handle wish list privacy
B) Implement as specced and add a comment in the PR noting the potential privacy leak for the product team to decide
C) Pause implementation, file a design note about the wish list privacy edge case, get product team alignment, then implement

Best response: [blank]

LP: [blank]

Reasoning: [blank]

*Model answer:* C. Success and Scale Bring Broad Responsibility — "We must be humble and thoughtful about the secondary effects of our actions." A privacy leak in a share feature is not a minor edge case — it violates customer trust and potentially regulations (GDPR, CCPA if in scope). B is better than A (at least you flagged it) but "adding a comment" is insufficient for a live privacy issue — it could ship without anyone reading the comment. C pauses velocity for safety, which is the LP-aligned choice. This LP is specifically about not letting scale and success blind you to the harm you can cause.

---

### Scenario 8 — The New Technology

Your team's principal engineer proposes migrating from the existing Python service to a Rust microservice for performance. You have no Rust experience. The project timeline is 8 weeks. You will be the primary implementer.

**Options:**
A) Push back on the proposal — you don't know Rust and 8 weeks is not enough time to learn and deliver
B) Accept the project, immediately start learning Rust in parallel with current work, and flag risks to your manager within the first week
C) Accept the project silently and figure it out as you go

Best response: [blank]

LP: [blank]

Reasoning: [blank]

*Model answer:* B. Learn and Be Curious — "Leaders are never done learning and always seek to improve." B is the Amazon behavior: you take the challenge, you invest in learning, AND you are transparent about the risk (flagging early). A can be right if you genuinely believe 8 weeks is unrealistic — Have Backbone applies. But the LP-aligned instinct is to try and learn, not to refuse based on unfamiliarity. C is the worst choice: taking on risk without surfacing it violates Earn Trust and Ownership. The LP distinction between B and C: "flag risks early" is the critical behavior.

---

### Scenario 9 — The Design Decision You Disagree With

Your team voted 4-1 to use a shared database approach instead of your proposed event-sourcing architecture. You believe the shared database will cause scaling problems in 18 months. The decision is now final.

**Options:**
A) Continue to advocate for event sourcing — this is too important to let go
B) Accept the decision and implement the shared database approach with the same care and quality you would have given event sourcing
C) Implement it but do it half-heartedly since you think it's the wrong call

Best response: [blank]

LP: [blank]

Reasoning: [blank]

*Model answer:* B. Have Backbone; Disagree and Commit — "Once a decision is determined, commit wholly." The distinction: "Disagree and Commit" means you made your case (backbone), the team decided, and now you execute with full commitment (commit). A violates Disagree and Commit — relitigating a settled decision undermines team trust. C violates Insist on the Highest Standards. B is exactly the LP: you may still believe you were right, and you may revisit the decision if new evidence emerges in 18 months, but right now you build the shared database at full quality. Common misconception: people think "Commit" means "agree you were wrong." It does not. It means "execute as if you proposed this."

---

### Scenario 10 — The Performance Data

You and a colleague each built a candidate implementation of the same service. Benchmarks show your implementation is 15% faster. In the design review meeting, your colleague presents their version first and does not show the benchmark comparison.

**Options:**
A) Present your benchmark data immediately and recommend your implementation
B) Wait until after the meeting to share the data privately with your manager
C) Ask your colleague in the meeting: "Can we also look at the benchmark comparison between the two implementations before deciding?"

Best response: [blank]

LP: [blank]

Reasoning: [blank]

*Model answer:* C. Are Right, A Lot + Earn Trust in combination. C presents the data in the right venue (the design review meeting, where the decision is being made) without being adversarial. A is right on the LP but the framing matters — immediately "recommending your implementation" may come across as poaching. C invites comparison rather than asserting superiority. B is too passive — waiting until after the meeting means the decision may be made without the data. LP note: Are Right, A Lot is not about being right in an argument; it is about ensuring decisions are made with the best available data.

---

### Scenario 11 — The Bar Raiser Feedback

You're in a debrief after a candidate interview. You gave the candidate a "Strong Hire." Two other interviewers gave "No Hire." The Bar Raiser agrees with the No Hires. You are asked if you want to change your vote.

**Options:**
A) Change your vote to No Hire to reach consensus
B) Maintain your Strong Hire with a clear explanation of the specific behaviors that led to that rating
C) Abstain — you've presented your view, the group can decide

Best response: [blank]

LP: [blank]

Reasoning: [blank]

*Model answer:* B. Have Backbone; Disagree and Commit — but also Hire and Develop the Best. The Bar Raiser process is designed to surface dissent, not suppress it. If you saw behaviors that genuinely meet the bar, changing your vote under social pressure violates Have Backbone. B requires you to articulate specifically what you saw: "The candidate gave a specific example in the leadership dimension that showed X behavior. I'm maintaining Strong Hire based on that." If the Bar Raiser and other interviewers have compelling counter-evidence you hadn't considered, updating your vote is correct — that is "updating with evidence," not "caving to pressure." The distinction is critical.

---

### Scenario 12 — The Ethical Edge Case

You are asked to implement a feature that personalizes Prime recommendations for users aged 12-17. The algorithm uses behavioral data to surface items with high purchase probability. You have personal concerns about the ethics of behavioral targeting for minors.

**Options:**
A) Implement the feature as requested — it's legal and you were asked to do it
B) Raise the concern with your manager and the product team, document the conversation, and implement if directed after the conversation
C) Refuse to implement it until the ethics review board signs off

Best response: [blank]

LP: [blank]

Reasoning: [blank]

*Model answer:* B. Success and Scale Bring Broad Responsibility — "We will be scrutinized for our impact on society." The LP asks you to be "thoughtful about the secondary effects of our actions." Raising the concern is the LP-aligned move — you are not refusing (that would be premature without more information) and you are not silently complying (that would abdicate responsibility). Documenting the conversation protects you, the team, and the product. If the answer after the conversation is "we've considered this, here's our mitigation, proceed," then B leads to implementation. If the answer reveals a real problem, your flag may have prevented a regulatory incident. A is incomplete because it skips the "thoughtful" requirement. C overcorrects — refusing work before raising the concern skips the collaborative step.

**Checkpoint M2:** Check the box above when you have a recorded response and LP for all 12 scenarios.

---

## Part 4 — STAR Story Bank

*For each scenario type that appeared in the inbox, draft one STAR story from your own experience. If you don't have a real example, draft a plausible one from a project you worked on. The goal is to have a story ready, not to invent facts.*

**Scenario types to cover:**

| Type | LP | Your STAR story |
|---|---|---|
| Raised a difficult issue early | Ownership / Earn Trust | [blank] |
| Disagreed with a senior person and held your ground | Have Backbone | [blank] |
| Made a decision under ambiguity without waiting | Bias for Action | [blank] |
| Optimized for the right cost — not always the cheapest | Frugality | [blank] |
| Taught or mentored someone instead of solving for them | Hire and Develop | [blank] |
| Raised an ethical or privacy concern proactively | Success and Scale | [blank] |
| Committed fully to a decision you disagreed with | Disagree and Commit | [blank] |

**STAR format reminder:**
- **S** — Situation: 1-2 sentences of context. What was the setting?
- **T** — Task: What was your specific responsibility? Say "I", not "we."
- **A** — Action: What did YOU do specifically? This is 60% of the story. Be concrete.
- **R** — Result: What happened? Quantify if possible. What was the measurable outcome?

**Common STAR mistakes:**
- Saying "we" throughout — the interviewer is assessing YOU, not your team.
- A result like "the project succeeded" — this is not a result. "Latency dropped from 800ms to 200ms, and the feature launched on schedule" is a result.
- A story that is all Situation with no Action — front-loading context at the expense of what you actually did.

**Checkpoint M4:** Check the box when you have at least 4 STAR stories drafted.

---

## Part 5 — LP Reasoning: The Hard Questions

*Answer these without looking at the LP list. These probe nuance, not recall.*

**Q1: Which LP pair is most commonly confused with each other, and why?**
[blank]

*Model answer:* Have Backbone; Disagree and Commit is most commonly confused with Earn Trust. People assume "backbone" means being combative, and "earn trust" means always agreeing to keep the peace. The reality: backbone without respect is stubbornness; Earn Trust without backbone is sycophancy. They are complementary — you disagree with evidence and respect (earning trust in the process), and you commit fully after the decision (also earning trust). The confusion appears in interviews when candidates describe "I disagreed" stories as Earn Trust stories, or vice versa.

**Q2: What is the difference between "Deliver Results" and "Bias for Action"?**
[blank]

*Model answer:* Bias for Action is about the START of work — moving quickly under ambiguity, not over-analyzing, making reversible decisions fast. Deliver Results is about the END — ensuring the thing you started actually ships, with the right quality, on time. You can have Bias for Action without Deliver Results (you move fast but nothing ships). You can have Deliver Results without Bias for Action (you eventually deliver but it took twice as long as it should have because you waited for perfect information). They operate at different points in the timeline of work.

**Q3: How does "Dive Deep" show up in a code review context?**
[blank]

*Model answer:* Dive Deep in code review means: not approving code you don't understand, asking questions about specific lines rather than leaving high-level "looks good" comments, running the code locally to verify behavior rather than trusting the description, and catching edge cases in tests (or asking for them). It is the opposite of rubber-stamping. The failure mode is: "this engineer is too senior to need my review," which violates Dive Deep. "Leaders stay connected to the details" means senior people are MORE rigorous in review, not less.

**Q4: Why is "Insist on the Highest Standards" NOT the same as perfectionism?**
[blank]

*Model answer:* Insist on the Highest Standards is calibrated to what "high" means in the specific context — a one-off script has different quality standards than a customer-facing API. Perfectionism is uncalibrated — it applies the same infinite-quality bar to every output, which violates Deliver Results. The LP says "relentlessly high standards" but it also implies knowing WHAT you are being rigorous about. High standards on correctness and testing; flexibility on which font to use in an internal doc. Perfectionism conflates these.

**Checkpoint M5:** Check the box when you can explain the Disagree and Commit / Earn Trust confusion and the Deliver Results / Bias for Action difference verbally, without notes.

---

## Part 6 — Curveballs

### Curveball 1 — A/B Test with an Unexpected Signal

**Your A/B test shows a 2% lift in click-through rate on a new product recommendation module. But users are spending 15% less time on the page overall. Product wants to ship. What LP guides your recommendation?**

**Your answer:** [blank]

*Things to address:*
- Customer Obsession — "work backwards from the customer." A 15% reduction in time on page may indicate users are finding what they want faster (positive) or finding the page less engaging (negative). The click-through lift alone does not tell you which.
- Dive Deep — what does "time on page" mean in this context? Is it a good or bad signal? You need to understand the root before recommending.
- Are Right, A Lot — you need more data before you can be confident you're right. What does the full funnel look like? Did conversion increase?
- Recommendation: do not ship on click-through alone. Run a secondary analysis on downstream conversion and user satisfaction signals. Present the ambiguity to product. This is Customer Obsession in practice: you are not satisfied with a metric that could be masking user harm.

---

### Curveball 2 — The Ethically Questionable Feature

**You're asked to work on a feature that enables geo-targeted advertising to users under 16. You think this is ethically questionable. What do you do, step by step?**

**Your answer:** [blank]

*Things to address:*
- Success and Scale Bring Broad Responsibility — this LP directly applies. You are not just an implementer; you are accountable for the downstream impact.
- Step 1: Understand the full context before reacting. Is there a legal review? Is this feature regulated in your markets?
- Step 2: Raise the concern explicitly with your manager and the product team. "I have concerns about this feature's impact on users under 16. Has this gone through legal and ethics review?" This is backbone.
- Step 3: If the answer is yes and the concerns are addressed, implement. Disagree and Commit.
- Step 4: If the answer is "we haven't thought about it," pause until it goes through the appropriate review. This is not obstruction — it is responsibility.
- What you do NOT do: implement silently (violates Success and Scale) or refuse without raising concerns first (violates the collaborative process).

---

### Curveball 3 — Bar Raiser Asks About Failure

**"Tell me about a time you failed. Be specific." What LP does a strong answer demonstrate, and what makes the answer strong?**

**Your answer:** [blank]

*Things to address:*
- The LP is Learn and Be Curious — "leaders are never done learning." A strong failure story demonstrates that you learned something durable from the failure, not that you have some kind of character flaw.
- A strong answer structure: (1) what the failure was, specifically and without minimizing — say "I" not "we"; (2) why it happened — your specific decisions that contributed; (3) what you did to recover; (4) what you changed about how you work as a result; (5) evidence that the change stuck.
- What makes it weak: vague failures ("I worked too hard and burned out"), failures that are clearly actually successes ("I failed to ship the feature in two weeks but we shipped it in three"), or failures with no lasting behavioral change.
- What makes it strong: a real mistake with real consequences, owned without excuse, with a specific behavioral change that you can demonstrate is still in effect. The Bar Raiser is looking for self-awareness and intellectual honesty, not for you to be perfect.

---

## Part 7 — Behavioral Rubric

*Self-grade after completing all 12 inbox scenarios and the STAR bank. Score yourself as the Bar Raiser would after reading your write-ups cold.*

| Dimension | 5 | 3 | 1 | Your Score |
|---|---|---|---|---|
| LP recall | Named 14-16 LPs correctly from memory in Part 1 | Named 10-13 | Named < 10 | __ /5 |
| LP-to-behavior mapping | Linked each scenario to the specific LP with a behavioral explanation ("this LP means X; in this context that looks like Y") | Named the LP but explained it abstractly or without connecting to the scenario | Wrong LP or no explanation given | __ /5 |
| Nuance — LP tensions | Named at least 2 LP tensions explicitly (e.g., Bias for Action vs. Deliver Results, Backbone vs. Earn Trust) in your scenario explanations | Named 1 tension | No tensions identified — treated each LP as isolated | __ /5 |
| STAR quality | Stories have specific quantified results, "I" language throughout, clear behavioral Action section that is ≥ 60% of the story | Stories present but vague — "we" language, unclear results, no numbers | Generic stories or no stories drafted | __ /5 |
| Ethical reasoning | Identified the stakeholder at risk, named the relevant LP, described the trade-off, and named the action (scenarios 7, 12, curveballs) | Named the LP but was vague about the trade-off or the specific action | Did not identify the ethical dimension or defaulted to "just follow instructions" | __ /5 |
| Communication / structure | Each response is concise (2-4 sentences), structured (response → LP → reason), and LP is visible in the reasoning — not stated as an afterthought | Understandable but wandering; LP is named but not used to explain the choice | Responses are long paragraphs without structure; LP mentioned in passing or not at all | __ /5 |
| Time management | Processed all 12 scenarios with LP and reasoning in < 50 min | Processed 9-11 scenarios | Processed < 9 scenarios in 50 min | __ /5 |

**Total: __ / 35**

---

## You're Ready When...

- You score 14/16 on LP recall in Part 1 without looking
- You can defend your answer for Scenarios 2, 9, and 11 (the three most commonly mishandled) without notes
- You have at least 4 STAR stories drafted, each with a quantified result and "I" language
- You can explain Disagree and Commit vs. Earn Trust without confusing them
- You self-grade ≥ 28/35 on two separate attempts

**What to do if you scored below 24/35:** Go back to the 16 LPs and write a one-sentence behavioral definition for each from a SWE context. Not the Amazon phrase — the behavior. Then redo the inbox.

**Next lab:** [→ Lab 02: Design-a-DS](../lab_02_design_ds/workbook.md)

---

*Amazon SWE Lab 01 · Tier 2 (Completion) · Work-Simulation LP Inbox · v2.0*
