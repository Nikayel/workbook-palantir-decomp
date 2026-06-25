# Amazon PM Lab 01 — Flashcards

10 cards. Study until each answer comes in < 5 seconds.

---

## Card 01 — PR-FAQ Structure

**Q:** Name the 3 sections of an Amazon PR-FAQ and what each accomplishes.

**A:**

**Section 1: Press Release**
Structured narrative (~1 page) written as if the product already launched. Contains:
- Headline (customer benefit, no jargon, one sentence)
- Dateline
- Opening paragraph (who benefits and how)
- Problem paragraph (the pain before this product)
- Solution paragraph (what it does, customer perspective)
- Quote: Amazon spokesperson
- Quote: Customer
- Closing (how to access it)

Purpose: Forces the team to agree on what they're building and for whom before a line of code is written. If you can't write a press release that's exciting, the product probably isn't worth building.

**Section 2: Customer FAQ**
5–10 questions a real customer would ask. Addresses concerns about trust, accuracy, cost, and opt-out. Written in plain English, as if responding to an actual customer email.

Purpose: Reveals product gaps. If you can't answer "what if it's wrong?" without corporate hedging, you haven't designed for that failure mode.

**Section 3: Internal FAQ**
3–8 questions from Legal, Engineering, Finance, or other internal stakeholders. Addresses business risks, technical feasibility, and regulatory compliance.

Purpose: Surfaces the hard decisions that customer FAQ doesn't. "How does this interact with our existing products?" "What's our rollback plan?" "What's the launch gate metric?"

---

## Card 02 — Working Backwards Order

**Q:** What does "Working Backwards" mean, and what is the order of operations?

**A:**

Working Backwards means starting from the desired customer experience and working back to what you need to build — NOT starting from what you have and figuring out what customers want.

**Order:**
1. Define the customer (specific segment, specific pain)
2. Write the press release (future state: what is their life like after your product?)
3. Write the FAQ (what questions do they have? What could go wrong?)
4. Define success metrics (how will you know it worked?)
5. THEN define requirements and build

**Working Forwards (wrong):** "We have a machine learning model. What can we do with it?" → Feature hunt. Usually produces features that are technically interesting but not customer-valuable.

**Working Backwards (Amazon way):** "What does a household manager need to not run out of toilet paper again?" → PR-FAQ → build the model that serves that specific need.

**Bar Raiser signal:** If your press release could be equally true of a different product, you didn't start from the customer specifically enough. "Better household management" is too vague. "You won't run out of toilet paper at 11pm anymore" is specific.

---

## Card 03 — Bar Raiser Role (PM Version)

**Q:** What does a Bar Raiser look for specifically in a PM candidate?

**A:**

The Bar Raiser is looking for LP evidence that is:
- **Specific** (not "I improved metrics" but "I drove a 15% increase in DAU by removing 3 friction points in the onboarding flow")
- **Customer-first** (decisions trace back to LP1, not to internal politics or career progression)
- **Quantified** (you know your numbers; you know your north star metric; you know your launch gate)
- **Honest about failure** (you can name a time you were wrong, what you learned, and how it changed your approach)

**PM-specific Bar Raiser questions:**
- "Why this customer? What evidence do you have that this is the right segment?"
- "Your press release says X — what's the riskiest assumption in that sentence?"
- "How would you know, 90 days post-launch, that this worked?"
- "What would cause you to recommend killing this feature?"

**The answer "it performed below our success metric" is not enough.** The Bar Raiser wants: "If 90-day retention for this feature fell below 40%, OR if the false positive rate exceeded 10%, OR if customer trust scores for Alexa dropped by >5% in the treatment group, I would recommend a pause and root cause analysis before relaunching."

---

## Card 04 — LP Customer Obsession Behavioral Signal

**Q:** What is the behavioral signal for Customer Obsession (LP 1) in a PM interview?

**A:**

Customer Obsession does NOT mean:
- Building what customers say they want
- Making the customer happy in the short term
- Adding features customers request

Customer Obsession DOES mean:
- Understanding the underlying problem better than the customer articulates it
- Making hard tradeoffs in FAVOR of the customer even at short-term cost to the business
- Building for long-term customer trust, not short-term metrics

**Behavioral signal in PR-FAQ:**
- Headline leads with customer benefit, not feature name
- The problem paragraph describes real customer pain (specific, visceral)
- Q&A for "will I be auto-charged" is unambiguous: no auto-charges ever without confirmation
- Internal FAQ acknowledges the business risk of prioritizing customer trust over conversion rate

**Bar Raiser prompt:** "Tell me about a time you made a product decision that hurt short-term metrics but was the right thing for the customer."

---

## Card 05 — GDPR Consent Trigger

**Q:** Under GDPR, when does analyzing customer purchase history for proactive suggestions require explicit opt-in consent?

**A:**

GDPR (General Data Protection Regulation) applies to EU citizens regardless of where the company is based.

**The trigger:** Proactive, AI-driven analysis of personal data (purchase history) for purposes beyond the original transaction requires a legal basis. The two most common bases:

1. **Legitimate interest (Art. 6(1)(f)):** Amazon could argue that using purchase history for better service is a legitimate interest. But for proactive suggestions that feel "unsolicited," this is legally risky — regulators may view it as marketing, which requires consent.

2. **Consent (Art. 6(1)(a)):** Explicit opt-in from the customer. The cleanest approach for a feature that uses personal data for proactive suggestions.

**For this feature:** EU customers require an explicit opt-in screen: "Allow Alexa to use your Amazon order history to suggest reorders? [Yes, allow] [No, thanks]." The opt-out must be equally easy — one step, not buried in settings.

**PM action:** Flag to Legal early. Do not assume legitimate interest covers it. Design the opt-in UI as a launch requirement, not a post-launch enhancement.

---

## Card 06 — False Positive Tolerance in ML Product Decisions

**Q:** How do you decide the acceptable false positive rate for an ML feature at launch?

**A:**

**Framework: What is the cost of a false positive to the customer?**

Low-cost FP (dismissible, no impact): Higher tolerance acceptable.
Example: "You might be running low on paper towels" — customer dismisses in 2 seconds. Cost: minor inconvenience. Tolerance: 15–20% FP may be acceptable.

High-cost FP (auto-charge, major disruption, trust damage): Lower tolerance required.
Example: Alexa auto-orders the wrong item — customer sees an unexpected charge. Cost: financial impact + trust damage. Tolerance: < 5%.

**For this feature:**
- Suggestion with customer confirmation required → FP cost is low (dismiss in 1 tap)
- Auto-order without confirmation → FP cost is high (unexpected charge)
- Design must require confirmation → shifts FP tolerance from <5% to potentially 15%

**Launch gate formula:**
Set threshold based on comparable notification products. If notification opt-out rate spikes above X% when FP rate is Y%, Y is your ceiling.

**Common anchor:** Research shows push notification opt-out rates spike when error rates exceed ~10%. Set 10% as your launch gate, with intent to drive to <5% by 6 months post-launch.

---

## Card 07 — Lead with Customer Pain, Not the Feature

**Q:** What is the difference between a feature-first and customer-first PR-FAQ headline? Give an example of each.

**A:**

**Feature-first (wrong):**
"Amazon Launches Alexa Proactive Reorder — AI-Powered System Predicts When You'll Run Out of Household Items"

Problems: Leads with company name and feature name. "AI-Powered" is jargon. "Predicts when you'll run out" is interesting but not the benefit.

**Customer-first (correct):**
"Households That Use Alexa Will Never Run Out of Toilet Paper Again"

Why it works: Opens with the customer (households) and the outcome (never run out). No jargon. No company name. The feature is implicit in the outcome.

**Even better:**
"The Moment You Realize You're Out of Dish Soap Is Now the Moment Alexa Already Handled It"

Why it works: Visceral. Specific. Tells a story in one sentence. Makes the problem and solution tangible before any explanation.

**Test:** Read your headline to someone who doesn't work at Amazon. If they understand the benefit without follow-up questions, it's customer-first. If they ask "what is this actually?" — rewrite it.

---

## Card 08 — Amazon Writing Culture (6-Pager vs. Deck)

**Q:** What is the Amazon 6-pager, and why does Amazon use it instead of slide decks?

**A:**

**The 6-pager** is a ~6-page narrative document used in Amazon meetings instead of a slide deck. At the start of every major meeting, participants silently read the document (typically 15–30 minutes of reading time). Discussion follows.

**Format:** Narrative prose, not bullets. Data and charts are embedded in the narrative, not presented separately. Appendix for supporting data.

**Why not slides:**
1. Slides allow vague language to hide behind visuals. A sentence in a 6-pager must be complete and defensible. "Q3 performance was strong" fails in a 6-pager — you must say what it means.
2. Presenters control the pace of a slide deck — readers control the pace of a 6-pager. Each reader can examine a claim at their own depth.
3. 6-pagers require the author to think more rigorously before the meeting, reducing time wasted on poorly-thought-through proposals.

**PR-FAQ vs 6-pager:** PR-FAQ is specifically for new product/feature decisions (before building). 6-pager is broader — used for strategy proposals, retrospectives, org design, etc.

**PM implication:** If you join Amazon, you will write 6-pagers. Practice writing in complete, precise sentences with supporting data. Every claim must be defensible.

---

## Card 09 — Bias for Action in Product Scope

**Q:** How does "Bias for Action" (LP 9) apply to product scoping, and what is the wrong interpretation?

**A:**

**Wrong interpretation:** "Bias for Action means ship fast and fix bugs later." This leads to launching features that damage customer trust and require costly fixes.

**Correct interpretation:** "Many decisions and actions are reversible and do not need extensive study. We value calculated risk taking." The key word is CALCULATED.

**In product scoping, Bias for Action means:**
1. Define the smallest scope that delivers real value to a real customer
2. Ship that scope with high quality and a clear way to measure success
3. Learn from real-world data faster than you could from continued analysis
4. Use a staged rollout (1% → 10% → 100%) to de-risk the launch while still moving

**For the Alexa reorder feature:**
Wrong (Bias for Action misapplied): Launch with 15% FP rate because "we'll fix it later"
Right (Bias for Action correctly applied): Launch to 1% of opt-in volunteers, get 90 days of real-world FP data, gate expansion on reaching <10% FP

**What Bias for Action is NOT:**
- Skipping user research because it takes time
- Launching without a rollback plan
- Ignoring GDPR because getting Legal review takes too long

---

## Card 10 — "Would a 10-Year-Old Customer Understand This Headline?"

**Q:** What does the "10-year-old test" for PR-FAQ headlines check, and why does it matter?

**A:**

**The test:** Read your press release headline to a 10-year-old. Can they tell you (1) who benefits and (2) what changes for them?

**Why it matters:** Amazon's most-used services (Prime, Alexa, AWS) have customers across age, income, and education ranges. If your headline requires industry knowledge to understand, you've already narrowed your customer unnecessarily.

**The deeper reason:** If YOU can't explain the benefit in simple language, you probably don't understand it clearly enough yet. Complexity in a headline is usually a symptom of unclear thinking, not a sophisticated product.

**Examples:**

"Alexa's new ML-powered proactive consumable replenishment system leverages purchase history telemetry to predict household inventory depletion events" → Fails the test. 10-year-old cannot understand. You cannot explain it simply because you haven't distilled it yet.

"Alexa will tell you before you run out of toilet paper" → Passes the test. Clear benefit, specific item, zero jargon.

**Bar Raiser application:** The Bar Raiser will often ask "explain this to me like I'm not a PM." If you can't simplify without losing the essence, your product thinking is still abstract. Simplicity is the sign of clear thinking.
