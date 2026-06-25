# Flashcards — Meta PM Lab 01: Product Sense

*10 cards for spaced repetition. Study 24–48 hours after completing the workbook.*

---

## Card 1 — Segment-First Before Solutioning

**Q:** Why must you segment a user cohort before proposing any product solution? What is the failure mode if you skip it?

**A:** Segmentation reveals that a demographic label ("18-34") contains multiple distinct behavioral profiles with different pain points. A solution that fits one sub-segment may actively antagonize another.

**Example failure:** Designing a TikTok-style short-form feed for "18-34 Groups users" alienates the 28-34 parent cohort who uses Groups for neighborhood coordination and wants depth, not entertainment. The 22-year-old college student might love it. If you treat them as one segment, you ship a solution that helps one sub-segment and hurts another.

**The correct move:** Before proposing anything, ask "who within this cohort is most affected and why?" Identify the sub-segment with the highest lapse rate, the sharpest behavioral insight, and the most addressable pain. Then design for that sub-segment first.

**Meta-specific note:** Meta interviewers explicitly look for whether candidates resist the urge to immediately propose features. The strongest candidates spend the first 10 minutes on diagnosis. The weakest candidates propose features in the first 60 seconds.

---

## Card 2 — RICE Scoring Formula

**Q:** Spell out the RICE formula, what each letter stands for, and explain why you divide by Effort instead of subtracting it.

**A:** **RICE = (Reach × Impact × Confidence) / Effort**

- **Reach:** Number of users affected per quarter (or as a % of target segment). Uses your best estimate.
- **Impact:** How significantly does this move the target metric per user affected? Standardized scale: 0.25 = minimal, 0.5 = low, 1 = medium, 2 = high, 3 = massive.
- **Confidence:** How confident are you in your Reach and Impact estimates? Typically 0–100%, expressed as a decimal. "I'm 80% confident" = 0.8 confidence multiplier.
- **Effort:** Person-months to design, build, and ship. Typically 1 person-month = 1 engineer for 1 month; scale as needed.

**Why divide, not subtract?** Dividing by Effort creates a rate: "impact per unit cost." Subtracting Effort would create a surplus: "impact minus cost." The rate is dimensionally correct for prioritization — a feature with Reach=5, Impact=3, Confidence=2, Effort=1 (RICE=30) is better than one with Reach=5, Impact=3, Confidence=2, Effort=6 (RICE=5), and the ratio captures this correctly. Subtraction would give 9 and 4 — similar in the wrong direction.

---

## Card 3 — Network Effects in Re-Engagement

**Q:** You're designing a feature to re-engage lapsed Facebook Groups users. How do network effects complicate the A/B test design?

**A:** In a social product, a user's experience depends on who else is in the network — not just on what features they see. This creates **network interference** in A/B tests:

**The problem:** If you assign 50% of users to treatment (see the new digest) and 50% to control (don't), treatment users who return to Groups will interact with control users in those Groups. Their increased activity may improve the Groups experience for control users — elevating the control group's metrics. Result: you underestimate the true treatment effect.

**Mitigation strategies:**
1. **Cluster-level randomization:** Assign treatment/control at the Group level, not the individual level. Users in treatment Groups see the digest AND interact primarily with other treatment users. Contamination is reduced.
2. **Ego-network randomization:** Assign treatment based on a user's friend graph cluster. Users in the same friend cluster are assigned to the same arm.
3. **Geographic randomization:** Treatment in certain cities/regions; control in others. Interaction between arms is minimized by geography.

**The honest answer in an interview:** "A/B tests in social networks can underestimate treatment effects due to network interference. I'd use cluster-level randomization — assign by Group, not by individual user — to reduce contamination."

---

## Card 4 — NSM vs Guardrail Metric (Meta Context)

**Q:** For a Facebook Groups re-engagement feature, define a North Star Metric and a guardrail metric. Explain how they're different and why you need both.

**A:** **North Star Metric (NSM):** Measures whether the feature achieved its primary goal. For Groups re-engagement: "% of lapsed 18-34 users who make at least 1 active contribution (post, comment, or substantive react) in any Group within 30 days of exposure to the feature."

Why this NSM: It measures active re-engagement (contribution), not passive re-engagement (viewing). A lapsed user who reads the digest but never returns to Groups is not re-engaged. The NSM must measure the outcome we care about, not the activity.

**Guardrail metric:** The metric that would KILL the launch if it moved negatively, even if the NSM looks good. For Groups re-engagement: "Notification opt-out rate among 18-34 users receiving the digest" AND "report/harassment rate on Group content surfaced in the digest."

Why these guardrails: A 5% re-engagement lift isn't worth it if it comes at the cost of: (a) users permanently opting out of all notifications (a one-way door that permanently reduces our ability to reach them), or (b) surfacing harmful content to lapsed users who then report more harassment (a safety harm that overrides the engagement gain).

**The key distinction:** NSM tells you if it's working. Guardrail tells you if it's safe to scale.

---

## Card 5 — A/B Test Interference in Social Networks

**Q:** Describe 3 forms of network interference that can contaminate an A/B test in a social product like Facebook Groups.

**A:**
1. **Direct interaction:** Treatment users interact with control users in shared Groups. Treatment users who return to Groups post more content, which control users in the same Group see — improving the control group's experience and understating the treatment effect.

2. **Notification spillover:** If a treatment user receives a digest notification and shares the Group content with a control user (e.g., "hey, check out this post") via Messenger, the control user gets indirect exposure to the treatment.

3. **Creator supply effect:** If treatment users returning to Groups post more content, creators in those Groups may produce more content in response to increased engagement signals. This improves the Group's content quality for all members, including control users.

**Mitigation:** Cluster-level randomization (at Group level) reduces #1 and #3. #2 is harder to eliminate but is typically a small effect. Always acknowledge network interference in your A/B test design when presenting to a Meta PM interviewer — it shows product sophistication.

---

## Card 6 — Meta's "Move Fast" in PM Context

**Q:** A VP at Meta asks you to ship a feature in 2 weeks. Your A/B test needs 4 weeks for statistical significance. What does "Move Fast" actually mean in this context?

**A:** "Move Fast" at Meta does NOT mean "skip the A/B test." It means "find the fastest path to a reliable signal." Options:

**Option 1 — Sequential testing with guardrails:** Ship to 1% of users on day 1. Monitor safety guardrails (harassment rate, opt-out rate) daily — these are faster to measure than the re-engagement NSM. If guardrails are clean by day 7, expand to 5%. The NSM signal may not be significant yet, but you're moving and it's safe.

**Option 2 — High-frequency cohort:** Test on a sub-segment that uses Groups daily (not all 18-34 users) — you'll accumulate data points faster and reach significance sooner.

**Option 3 — Large-scale early launch:** Launch to 20% of users immediately (instead of the planned 5%). Larger sample → faster significance. Tradeoff: higher blast radius if something goes wrong.

**What "Move Fast" is NOT:** Shipping to 100% of users without a control group because the VP wants it done. That eliminates the ability to measure causal effect and roll back cleanly. Frame this to the VP as: "Moving fast means I can give you a guardrail-verified signal in 2 weeks and a significance-backed result in 4. Shipping to 100% means we never know if it worked, and we can't isolate any problems that emerge."

---

## Card 7 — Guardrail Examples for Social Products

**Q:** Name 4 guardrail metrics that are commonly used in social product launches. For each, explain what it protects against.

**A:**
1. **Harassment/report rate:** Protects against a feature that increases user engagement by surfacing inflammatory content. If users report more content or block more users after a feature launch, engagement is being driven by conflict — not value.

2. **Notification opt-out rate:** Protects against sending notifications that users perceive as spam. If opt-out rate rises sharply, you've permanently reduced your ability to communicate with those users. Notification trust is a long-term asset.

3. **Account deletion / deactivation rate:** Protects against features that drive users off the platform entirely. If a feature launch correlates with a spike in account deletions (especially among the target cohort), the feature is causing harm severe enough to drive exit.

4. **Content removal rate (by moderators):** Protects against a feature that surfaces or amplifies content that requires moderation action. If content removal requests spike after launch, the feature is creating a moderation burden that signals a safety problem.

---

## Card 8 — "Build Awesome Things" in Product Decisions

**Q:** Meta's value "Build Awesome Things" often creates tension with safety and quality constraints. How do you navigate this tension as a PM?

**A:** "Build Awesome Things" means building products that are genuinely excellent for users at scale — not just impressive or technically novel. The tension arises when "awesome" is interpreted as "fast, bold, growth-maximizing" regardless of quality or safety.

**The navigation framework:**
1. **Awesome ≠ max engagement.** A feature that drives a 5% Groups post increase via controversy is not awesome — it's harmful. Awesome means users feel good about using it over time.
2. **Awesome requires trust.** A notification product that gets opted out at high rates is the opposite of awesome — it depletes user trust in the platform's communications. The guardrail protects the conditions that make awesomeness sustainable.
3. **Awesome means it's right for the user, not just good for the metric.** "The LLM generates conversation starters that drive posts" is a metric win. "The LLM generates conversation starters that feel fake and users discover they're being manipulated" is the opposite of awesome — even if posts are up.

**Practical answer in an interview:** "I interpret 'Build Awesome Things' as building things that are genuinely excellent for users at Meta's scale — which means they're also safe and trustworthy. The guardrail metrics protect our ability to keep building awesome things long-term."

---

## Card 9 — Data-Driven vs. Intuition Tradeoff

**Q:** Your A/B test shows 5% re-engagement lift. Your intuition says users found the digest annoying. Do you trust the data or your intuition? How do you resolve the conflict?

**A:** Neither blindly. The right answer is to investigate why your intuition and the data diverge.

**Possible explanations for the conflict:**
1. **The data is measuring the wrong thing.** 5% re-engagement lift means users returned to Groups — but what did they do when they got there? If they returned, scrolled for 10 seconds, and left, that's a different outcome from re-engagement that sticks. Check the retention metric 7 days and 30 days after the initial re-engagement.
2. **The N is too small.** If the sample is small, 5% might not be statistically significant — and your intuition might be picking up signal from qualitative feedback that the quantitative data is too underpowered to capture yet.
3. **The annoyed users opted out.** If annoyed users opted out of the digest, they self-selected out of the test. The remaining treatment users who stayed opted in are the satisfied ones — biasing the metric upward. Check opt-out rate first.

**Resolution:** Run a follow-up qualitative study (user interviews, post-digest survey) to understand whether the re-engagement is high-quality or surface-level. Let the qualitative evidence speak to your intuition and the quantitative data speak to the metric. If both align (data says 5% lift, qualitative says users love it), launch. If they diverge (data says 5% lift, qualitative says users are annoyed), investigate before launching.

---

## Card 10 — When a 5%/3% Safety Tradeoff Is Worth It

**Q:** A product change drives a 5% increase in Group posts AND a 3% increase in harassment reports. Walk through the complete decision framework for whether to launch.

**A:**
**Step 1 — Understand the denominator.** At Meta's scale, 3% more harassment reports might be tens of millions of additional reports per year. Absolute scale matters, not just percentage.

**Step 2 — Investigate the mechanism.** Is the harassment rate constant (3% of all posts get reported, now there are 5% more posts) or is the harassment RATE increasing (a higher % of posts are being reported)? If it's the former — same rate, more volume — your feature didn't cause more harm per unit of activity. If it's the latter — a higher % of posts are now reported — your feature is causing qualitatively worse content.

**Step 3 — Check the guardrail definition.** If your pre-set guardrail was "harassment rate must not increase by more than X percentage points," check whether 3% exceeds X. If it does: pause the launch. The guardrail exists precisely for this moment — to prevent rationalizing safety harms away.

**Step 4 — Fix the root cause before relaunching.** If harassment is driven by the First Contribution Amplifier boosting posts to larger audiences (more reach = more trolls), fix the amplifier (cap the boost to users who are already Group members, not all viewers) and retest.

**The honest answer:** "A 5%/3% tradeoff at Meta's scale is not acceptable without investigating the mechanism. I'd pause the launch, investigate whether the harassment rate is constant or increasing, fix the root cause if the rate is increasing, and only relaunch when the fix is in place."

---

*10 cards · Meta PM Lab 01 · Review 24–48 hrs after completing workbook*
