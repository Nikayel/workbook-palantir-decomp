Status: Ready — work through all parts in order

# Amazon PM Lab 01 — PR-FAQ: Alexa Proactive Reorder Suggestions

**Role:** PM | **Tier:** 1 (structure provided — you fill the content) | **Est. time:** 60 min | **Difficulty:** Medium | **Format:** Working Backwards PR-FAQ

---

## Scenario

You're in an Amazon PM interview. The interviewer puts a scenario on the table: "Write a PR-FAQ for a new Amazon feature — Alexa can now proactively suggest reorders for household consumables before you run out, based on your order history and predicted usage. You have 60 minutes. Begin."

The room is quiet. There are no slides. There is no whiteboard. There is a blank document. You are expected to write a Press Release and a set of FAQs that are clear enough for a non-technical VP to read, and specific enough for an engineer to begin building from. The Bar Raiser is watching.

Start from the customer. Not from the feature.

---

## Milestones

- [ ] M1 · Customer first — identified the specific customer and their pain before writing any product copy
- [ ] M2 · Press release written — headline + 5 paragraphs following Working Backwards format
- [ ] M3 · FAQ written — 5 customer Q&As + 3 internal Q&As
- [ ] M4 · LP check — named which LP drove each major product decision in the PR-FAQ
- [ ] M5 · Defended — curveball 1 (Bar Raiser rewrite), curveball 2 (GDPR), curveball 3 (15% false positive rate) answered
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Part 0: Forethought

**Goal:** Write a customer-first PR-FAQ that would pass a Bar Raiser review — meaning it starts with the customer's problem (not the feature), uses plain English (not Amazon jargon), and surfaces the hardest tradeoffs (not just the happy path).

**Target time:** 60 min
- 5 min: Customer research / Who is this for?
- 5 min: Clarifying questions (below)
- 10 min: Press release draft
- 10 min: FAQ draft
- 10 min: LP mapping
- 10 min: Curveball prep
- 10 min: Revise and tighten

**Confidence (1–5):** ___

**What does a Bar Raiser reject first?**
Most PR-FAQs fail because they start with "We are excited to announce..." — a company-first, feature-first frame. The Bar Raiser will say: "Who is the customer? What is their problem today? Rewrite from there." Your draft must open with a specific customer in a specific painful situation.

---

## Part 1: Clarifying Questions — Working Backwards

Working Backwards means the first question is never "what do we build?" It is always "who is the customer, and what is their problem?" Answer these before writing a single word of product copy.

**Category: Goal — What is the customer's problem BEFORE Alexa involvement?**
Question: What is the actual frustration this customer experiences? Is it forgetting to buy items, running out unexpectedly, or the cognitive load of tracking household inventory?
Assumption: The primary pain is unexpected stockouts — the customer runs out of a consumable (toilet paper, dish soap, paper towels) at an inconvenient time. Secondary pain: the cognitive overhead of manually tracking and reordering.

<details>
<summary>Hint</summary>
The problem statement says "proactive reorder" but that's the solution, not the problem. The problem is: people run out of things they use every day. The disruption is real — running out of toilet paper is an emergency. Running out of coffee filters ruins a morning. Define the problem this specifically. A vague problem ("people forget to buy things") leads to a vague feature. A specific problem ("households with 2+ people using consumables with variable usage rates frequently run out before they realize they need to reorder") leads to a scoped, testable feature.
</details>

**Category: Users — Who is the customer?**
Question: Is this for all Alexa users, or a specific segment? A Prime subscriber with an established order history? An elderly user on a fixed income? A household manager tracking 20+ consumables?
Assumption: Primary customer segment is Prime members with ≥ 6 months of Amazon order history who have purchased household consumables at least 3 times. They are likely household managers (any adult responsible for keeping a home stocked) with moderate to high consumption of replenishable goods. Secondary segment: elderly users who benefit from proactive assistance but may need extra trust-building around consent.

<details>
<summary>Hint</summary>
Narrowing the customer segment sharpens the product. "All Alexa users" is not a customer — it's everyone, which means you can't design for them specifically. A PM who can name a specific segment with specific behaviors scores higher. The Bar Raiser will ask: "What's your target NPS for this segment? How will you know you got this right?" You need a specific customer to answer that.
</details>

**Category: Data — What data does Amazon have, and what are the risks?**
Question: What order data is available? Amazon purchase history only, or also Subscribe & Save subscription patterns, Alexa shopping list data, and third-party usage signals?
Assumption: We have Amazon order history (purchase frequency, item, quantity) and Subscribe & Save patterns. We do NOT have third-party grocery data (unless Prime membership unlocks this). We do NOT have actual consumption rates — we infer them from order intervals. The model's error rate is unknown at launch — we'll define an acceptable threshold.

<details>
<summary>Hint</summary>
This is where the Bar Raiser will push: "You said you'll infer consumption from order intervals. But order intervals are noisy — someone might have bought in bulk, or changed brands, or stopped using the item. How does your model handle that?" If you didn't think about data quality, you'll be caught flat-footed. Think about what the data does NOT tell you, not just what it does tell you.
</details>

**Category: Constraints — Privacy, consent, and opt-out**
Question: Does analyzing purchase history for proactive suggestions require explicit consent under GDPR, CCPA, or Amazon's internal privacy policies?
Assumption: In the EU, proactive use of purchase history for suggestions likely requires opt-in consent under GDPR's legitimate interest or consent basis — we will treat this as requiring explicit opt-in for EU customers. In the US, we can default opt-in with a clear opt-out mechanism prominently surfaced. The PR-FAQ will specify the opt-in/opt-out mechanism, and Legal must review before launch.

<details>
<summary>Hint</summary>
Do NOT ignore this. A PM who launches a privacy-impacting feature without flagging GDPR implications will fail the Bar Raiser round. The Bar Raiser will ask: "Did Legal review this? What's the consent model?" A good PM names the risk, explains the mitigation, and defines what "launch-ready from a privacy standpoint" looks like. You don't need to be a lawyer — you need to know that the risk exists and that Legal is in the loop.
</details>

**Category: Scale — How many users and what's the error tolerance?**
Question: How many Alexa households would this affect at launch? What is the acceptable false positive rate (suggesting reorder when the user still has plenty) before customers opt out or lose trust?
Assumption: Alexa has ~100M active devices globally (estimate). US-only launch: ~50M devices. Eligible households (Prime + order history): ~30M. False positive tolerance: we will define a 10% false positive rate as the maximum acceptable at launch, measured by "user dismissed the suggestion without purchasing within 2 weeks." Above 10%, the feature reduces trust in Alexa and may increase opt-outs.

<details>
<summary>Hint</summary>
Scale questions are also business questions. "100M devices" sounds impressive — but if your false positive rate is 20%, you annoy 20M households. That's a brand problem, not a feature win. Define your error tolerance before launch, not after. The Bar Raiser will ask: "How did you arrive at 10% as the threshold?" Your answer: "Based on comparable notification products, >10% FP rate correlates with a 15% increase in notification opt-out rate. We set 10% to stay below that inflection point."
</details>

---

## Checkpoint M1 — Customer First

Mark M1 complete when: you can complete this sentence in one specific, non-jargon sentence:

"The customer we are solving for is ___ who experiences the problem of ___, which currently causes them to ___."

Write it here:
___

---

## Part 2: Working Backwards Decomposition

Before writing the press release, map the customer journey and the product logic.

### Current State — Broken Customer Journey

A household manager discovers they've run out of dishwasher pods on a Monday night when the dinner dishes are piling up. They search Amazon on their phone, find their usual brand, and order it — but it won't arrive until Wednesday. The disruption was avoidable: they've been ordering this brand every 30 days for 2 years. Nobody warned them. Nobody noticed the pattern.

Write the version of this frustration for your specific customer segment:
___

### The "Imagine" Moment

"Imagine you wake up on a Saturday morning and Alexa says: 'Good morning. You typically run out of paper towels around this time — should I reorder your usual brand for Prime same-day delivery?'"

Write the "imagine" moment for your version of the feature:
___

### Core Entities

| Entity | Description | Key attributes |
|---|---|---|
| Customer profile | Prime member with order history | Historical purchase frequency, preferred brands, household size (inferred) |
| Consumable item | A replenishable household product | ASIN, average consumption rate, brand, substitute availability |
| Reorder suggestion | The proactive Alexa prompt | Item, predicted run-out date, suggested quantity, suggested price |
| Subscription preference | Customer's consent and opt-in state | Opt-in status, preferred suggestion timing (morning/evening), blacklisted items |

### State Transitions

```
Customer purchase event → Model updates consumption rate estimate
                        ↓
                  Predicted run-out date computed
                        ↓
              [7 days before predicted run-out]
                        ↓
              Alexa proactive suggestion surfaced
                        ↓
         ┌─────────────────────────────────────┐
         ↓                                     ↓
  Customer accepts                    Customer dismisses
         ↓                                     ↓
   Order placed                    Model notes: longer interval
   Delivery scheduled              Suggestion threshold adjusted
```

---

## Checkpoint M2 — Approach Ready

Mark M2 complete when: the "imagine" moment and the broken customer journey are both written in plain English, no jargon, no Amazon buzzwords.

---

## Part 3: PR-FAQ — Contract

The PR-FAQ is your product's contract. It defines what you are committing to, for whom, and why. Every word is intentional. Write your draft in the template below.

```
PRESS RELEASE

[HEADLINE]
One sentence. Lead with the customer benefit, not the feature name. No jargon.
No "we are excited to announce." No "leveraging AI." No "seamless experience."

Draft:
___


SEATTLE, WA — [Date]

[OPENING PARAGRAPH — 3–5 sentences]
Who benefits? How does their life change? Write this as if it already happened.
Lead with the customer, not Amazon.

Draft:
___


[PROBLEM PARAGRAPH — 3–5 sentences]
The pain that existed before this feature. Be specific. Use real language.
"Running out of dish soap at 11pm and having to run to a gas station" beats
"household consumable management friction."

Draft:
___


[SOLUTION PARAGRAPH — 3–5 sentences]
What Alexa now does, from the customer's perspective. Focus on the experience,
not the technology. Customers do not care that it uses machine learning.
They care that they never run out of paper towels.

Draft:
___


[QUOTE: Amazon spokesperson]
What does this mean for customers at scale? Make it specific — not "we are committed
to customer satisfaction" but "this is what we believe shopping should feel like."

Draft:
"_______________________________________" said [Name], [Title].


[QUOTE: Customer]
A real, specific customer reaction. Not "this is amazing!" but something that shows
the feature solved a real problem in a real life.

Draft:
"_______________________________________" said [Name], [City, State].


[CLOSING — 2–3 sentences]
How do customers get access? What action do they take? Where do they learn more?

Draft:
___
```

---

## FAQ — Customer Q&As

Write your answers. The questions are given (they are the most predictable customer concerns — not having them answered in a PR-FAQ is a gap a Bar Raiser will note).

**Q1: Will Alexa automatically charge me for reorders without my permission?**
A1:
___

<details>
<summary>Hint</summary>
This is the #1 customer trust concern. Your answer must be unambiguous: no auto-charges without explicit confirmation. The design must reflect this — Alexa asks, customer confirms, then order is placed. If the feature auto-places orders, you've lost the trust of every customer who sees an unexpected charge. This decision maps to LP1 (Customer Obsession) — customer trust over conversion rate.
</details>

**Q2: Is Amazon watching and analyzing my purchase history without my knowledge?**
A2:
___

<details>
<summary>Hint</summary>
Transparency is the answer here. Amazon has always used purchase history for recommendations — this feature extends that to proactive suggestions. The customer-friendly framing: "We use the same purchase history you've always trusted us with, to save you the step of reordering yourself. You can see exactly what data we use in your privacy settings, and you can opt out at any time." Do not be defensive. Be transparent and specific.
</details>

**Q3: What if the suggestion is wrong — I already bought this item somewhere else?**
A3:
___

<details>
<summary>Hint</summary>
The model will be wrong sometimes. The customer-friendly design: they see the suggestion and can dismiss it with one tap or voice command. Dismissal is free (no friction). And: dismissal trains the model — "the customer dismissed this, suggesting they're not running out, or they bought elsewhere." Over time the suggestions improve. Your answer should make clear that a wrong suggestion has zero cost to the customer.
</details>

**Q4:** [Write your own — predict the next most likely customer concern]
Q4:
___
A4:
___

<details>
<summary>Hint</summary>
Strong candidates for Q4: "How do I turn this off?" (opt-out mechanism), "Does this work for all items or only some?" (scope), "Can I set a budget limit so Alexa doesn't suggest expensive items?" (financial control), "What if I'm out of town and don't need a delivery?" (context awareness). Pick the one most relevant to your customer segment.
</details>

**Q5:** [Write your own — pick a trust, privacy, or accuracy concern]
Q5:
___
A5:
___

---

## FAQ — Internal Q&As

These are for your team, engineering, and the Bar Raiser. They must show that you've thought through the business and technical tradeoffs, not just the customer experience.

**Q1: How does this feature interact with Subscribe & Save?**
A1:
___

<details>
<summary>Hint</summary>
Subscribe & Save (S&S) is Amazon's existing subscription product for consumables. The risk: if customers use this new feature instead of S&S, you cannibalize a recurring revenue stream. The opportunity: this feature might convert non-S&S customers to S&S by surfacing the option at the moment of suggestion. Your answer should: acknowledge the cannibalization risk, propose a metric to track it, and argue that customer value (never running out) is the right north star even if it temporarily shifts S&S rates.
</details>

**Q2: What is the model accuracy threshold required before launching to all US customers?**
A2:
___

<details>
<summary>Hint</summary>
This is a Dive Deep question. Don't say "the model needs to be good enough." Name a specific threshold (e.g., "false positive rate ≤ 10% and false negative rate ≤ 15%") and explain how you'd measure it in a holdout test before launch. Also: define your launch criteria for expanding beyond the initial cohort. "If FP rate is ≤ 10% at 90 days with 100K users, we expand to 1M users" is a specific, testable launch gate.
</details>

**Q3: How do we handle customer complaints about unwanted suggestions?**
A3:
___

<details>
<summary>Hint</summary>
Your answer should cover: (1) the customer-facing resolution path (easy opt-out, single-item blacklist, "don't suggest this category"), (2) the team-facing escalation path (when does a surge in complaints trigger a feature review?), and (3) the metric that would cause an emergency rollback ("if customer complaint rate exceeds X% or Trust & Safety flags this as a brand risk, we pause the feature globally"). This is Ownership + Highest Standards combined.
</details>

---

## Checkpoint M3 — FAQ Complete

Mark M3 complete when: all 5 customer Q&As and all 3 internal Q&As have answers that are specific, non-jargon, and address the real concern (not a PR-sanitized version of it).

---

## Part 4: LP Mapping

This section is the difference between a PM candidate and an Amazon PM candidate. Every major product decision in your PR-FAQ should be traceable to a Leadership Principle.

**LP 1 — Customer Obsession:**
Which specific decision in your PR-FAQ reflects this LP? (Hint: it's probably the one where you chose customer trust over conversion rate.)
___

**LP 3 — Invent and Simplify:**
Where in the feature did you simplify the customer experience? Did you remove a step, a form, a decision?
___

**LP 4 — Are Right, A Lot:**
What data would you need to prove that your customer hypothesis (the specific pain you identified) is correct? What would change your mind?
___

**LP 9 — Bias for Action:**
What would you cut from scope to ship a v1 faster, while still solving the core customer problem?
___

**LP 12 — Dive Deep:**
What is the metric you would monitor daily in the first 30 days post-launch that would tell you the feature is working?
___

**LP 13 — Have Backbone:**
If engineering told you the model would need 6 more months to hit the false positive threshold you set, and business leadership wanted to launch anyway with a higher FP rate, what would you do?
___

<details>
<summary>Hint: LP 13</summary>
The Bar Raiser answer is not "I would defer to leadership." The Bar Raiser answer is: "I would present the data showing that a 20% FP rate correlates with a 15% increase in notification opt-out, which reduces the long-term value of this product. I would propose a phased launch to 1% of users to gather real-world FP data, with a clear gate before broader rollout. I would commit to the decision once it's made, but I would ensure leadership made it with full information."
</details>

---

## Part 5: Reasoning — 10 WHY Questions

**1. Why does Amazon use PR-FAQ format instead of a product spec or a slide deck?**
___

**2. What does "Working Backwards" mean, and why does it produce better products than "Working Forwards"?**
___

**3. Why does the PR-FAQ have a Press Release AND FAQs — what does each accomplish?**
___

**4. What would a Bar Raiser challenge first in your current draft?**
___

**5. What is the riskiest assumption in your press release?**
___

**6. Why should the headline lead with customer benefit, not feature name?**
___

**7. How does writing the PR-FAQ before building the product change what gets built?**
___

**8. What metric would tell you, 90 days post-launch, that this feature is succeeding?**
___

**9. If the feature has a 15% false positive rate at launch, is that acceptable? What's your argument in both directions?**
___

**10. What is the Subscribe & Save cannibalization risk, and how would you measure it?**
___

---

## Part 6: Interview Simulation

### 90-Second Talk Track

"Before I write anything, I want to anchor on the customer. The customer we are solving for is a Prime member who manages a household, who has experienced the disruption of running out of an everyday consumable — toilet paper, dish soap, paper towels — at an inconvenient time. The pain is real, frequent, and avoidable.

My press release will open with that customer's experience — not with Alexa's capabilities. The headline will name the benefit to the customer in plain English. The first paragraph will describe how their life changes, not how the technology works.

My FAQ will address the questions customers will actually have: will I be auto-charged, is Amazon watching me, what if the suggestion is wrong. And my internal FAQ will address the questions the Bar Raiser will have: how does this interact with Subscribe & Save, what's our launch gate, what's our rollback plan.

Let me start writing."

### Curveballs

**Curveball 1:** "The Bar Raiser says your PR-FAQ leads with the feature, not the customer. Fix it live."

Instructions: Open your draft. Rewrite the headline and opening paragraph in under 3 minutes. Read it aloud before and after. What changed?

<details>
<summary>Hint</summary>
Before: "Amazon today announced Alexa Proactive Reorder, a new AI-powered feature that automatically detects when you're running low on household consumables."

After: "For the millions of households that have ever run out of toilet paper at the worst possible moment, Amazon's Alexa can now predict when you're running low and ask if you want to reorder — before you're caught out."

The difference: before = feature-first, company-first. After = customer problem-first, benefit-in-plain-English. The feature is still named, but it's introduced as the solution to a named problem, not as the announcement itself.
</details>

Write your before and after headline:
Before: ___
After: ___

**Curveball 2:** "Your Q4 answer says we'll use order history — Legal says that triggers GDPR consent requirements in EU. What now?"

Instructions: Give a structured answer covering: (1) what you do NOW (not later), (2) what changes in the product design, and (3) how this affects the launch timeline.

<details>
<summary>Hint</summary>
NOW: Thank Legal. This is exactly the kind of early-stage flag that prevents a launch crisis.

Product design change: EU launch requires explicit opt-in (not opt-out). Add an opt-in screen to the Alexa app that clearly explains: "Alexa will use your Amazon order history to suggest reorders. You can opt out anytime in Settings." This screen is the consent mechanism.

Launch timeline: US launch can proceed with opt-out model. EU launch is delayed until opt-in flow is designed, implemented, reviewed by Legal, and tested. Give a realistic estimate: "EU launch slips ~6 weeks for consent flow implementation and Legal review."

LP alignment: This is Earn Trust (LP 11) — you are prioritizing long-term customer trust over a faster launch date.
</details>

___

**Curveball 3:** "The model has a 15% false positive rate — it suggests reorder when the user still has plenty. Is that acceptable to launch?"

Instructions: Argue both sides (60 seconds each), then give your recommendation with a decision framework.

<details>
<summary>Hint</summary>
FOR launching at 15% FP: The feature still works for 85% of suggestions. Early adopters are more tolerant. Real-world data from launch will improve the model faster than lab testing. Bias for Action (LP 9) — ship and learn.

AGAINST launching at 15% FP: For every 10 suggestions, 1.5 are wrong. That's the equivalent of a friend who gives you bad advice 15% of the time — you start ignoring them. Customer trust is not easily recovered. If trust in Alexa drops, the collateral damage extends beyond this feature.

Recommendation: Do not launch to all US customers at 15%. But don't wait for perfection either. Launch to a 1% cohort (opt-in volunteers who know the model is in beta). Use 90 days of real-world data to drive FP below 10%. Then expand. This is "Bias for Action" applied smartly — you're not waiting for a perfect model; you're using a staged launch to improve it with real data while protecting brand trust.
</details>

___

---

## Part 7: Self-Grade + Reflection

### PM Rubric

| Dimension | 1 | 2 | 3 | 4 | 5 | Score |
|---|---|---|---|---|---|---|
| **Structure** | No clear format | Some structure, inconsistent | PR-FAQ format recognizable | PR-FAQ complete, logical flow | PR-FAQ is model Amazon Working Backwards: customer → problem → solution → specifics | ___ |
| **User empathy** | Wrote about features, not customers | Named a customer type | Named a specific segment with a specific pain | Pain is vivid and specific; "imagine" moment resonates | Pain is so specific that the reader feels it; quotes are authentic, not PR-polish | ___ |
| **Prioritization** | Tried to solve everything | Scoped vaguely | Named one scope cut | Justified scope cut with customer reasoning | Named v1 scope with clear rationale; what's deferred and why is explicit | ___ |
| **Metrics literacy** | No metrics | Vague metrics ("improve NPS") | Named a north star metric | North star + launch gate metric with threshold | Full metric stack: north star, guardrail, launch gate, rollback trigger — all with specific numbers | ___ |
| **Communication** | Jargon-heavy, passive voice | Readable with effort | Clear, mostly plain English | Clear, concise, no jargon | Each sentence earns its place; a 10-year-old could understand the headline | ___ |
| **Creativity** | Feature copy, no insight | One interesting angle | Identified a non-obvious user need | Non-obvious need + non-obvious solution | Reframed the problem in a way that changed what should be built | ___ |
| **Handling ambiguity** | Required full spec before starting | Needed significant clarification | Named assumptions, proceeded | Proceeded with explicit assumptions, flagged risks | Operated from customer problem alone; named every assumption; knew when to ask vs. decide | ___ |

**Writing Quality Row (Amazon-specific)**

| Dimension | 1 | 2 | 3 | 4 | 5 | Score |
|---|---|---|---|---|---|---|
| **Writing quality** | Buzzword-heavy; passive; vague | Readable, some jargon | Clear sentences, plain English | Short sentences, no jargon, real tradeoffs surfaced | Stripe-level clarity: precise, no fluff, every word intentional; a VP could approve the headline without a meeting | ___ |

**Total: ___ / 40**

### Reflection

Which section was hardest to write?

___

What did the Bar Raiser curveball expose in your draft?

___

What would you cut from v1 if you had to ship in half the time?

___

What would your north star metric be, and why?

___

### Ready-When Checklist

- [ ] My headline leads with the customer benefit, not the feature name, and contains no jargon
- [ ] My opening paragraph describes how the customer's life changes, not what the technology does
- [ ] Every Q&A in the customer FAQ addresses the real concern (not the sanitized version)
- [ ] I can name which LP drove each major product decision in my PR-FAQ
- [ ] I have a specific model accuracy threshold for launch (with reasoning for the number)
- [ ] I can handle the GDPR curveball with a structured 3-part answer (now / design change / timeline)
- [ ] I can argue both sides of the 15% FP rate question and give a clear recommendation
- [ ] My writing quality passes the "would a 10-year-old understand this headline" test
