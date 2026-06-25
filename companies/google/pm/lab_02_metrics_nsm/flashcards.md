# Flashcards — Google PM Lab 02: Metrics / NSM

*10 cards for spaced repetition. Study 24–48 hours after completing the workbook.*

---

## Card 1 — Watch Time Metric Tree

**Q:** Decompose YouTube Watch Time into its constituent sub-metrics. What is the full metric tree?

**A:**
```
Watch Time (total)
= Sessions per day × Watch Time per session

Sessions per day
= DAU × Sessions per user per day

Watch Time per session
= Avg videos watched per session × Avg watch duration per video
```
The tree has two branches: session frequency (how often users open YouTube) and session depth (how much they watch per session). A 15% Watch Time drop is not a diagnosis — it's a symptom. You need to know which branch is driving it before you can hypothesize a cause. If sessions per day is flat and Watch Time per session is down 15%, the cause is something that cuts sessions short (autoplay broken, worse content recommendations, slower load times). If sessions per day is down 15% and Watch Time per session is flat, the cause is something that prevents users from opening the app at all (competitor, notification change, onboarding failure for new users).

---

## Card 2 — NSM vs Guardrail Metric

**Q:** Watch Time is YouTube's reported North Star Metric. Why might it actually be a proxy, and what would the true NSM be?

**A:** Watch Time is a proxy for user value and platform health, not the true business outcome. The true NSM depends on the business goal:
- If the goal is **Revenue**: NSM = Ad Revenue per user per month. Watch Time is a leading indicator, not the NSM itself.
- If the goal is **user satisfaction**: NSM = User-reported satisfaction with recommended content (a harder-to-measure outcome, but more directly tied to why users stay).
- If the goal is **creator ecosystem health**: NSM = Creator monthly active users who earn above a threshold.
Watch Time is used as the NSM because it's measurable and correlated with all three outcomes. But it can mislead: Watch Time can be high because users are watching autoplay videos they don't actually want (passive engagement, not active value). A guardrail for this: video completion rate. If Watch Time goes up but completion rate goes down, users are stopping videos mid-way — Watch Time increase is low-quality.

---

## Card 3 — Segmentation Before Hypothesizing

**Q:** Why must you segment a metric drop before forming hypotheses? What's the failure mode if you hypothesize first?

**A:** Segmentation narrows the search space. Without it, you have dozens of possible causes and no way to rank them. With it, the data eliminates all causes that don't match the segment where the drop is concentrated.

**The failure mode:** You anchor on a compelling narrative ("TikTok is eating our users") and spend the entire diagnosis chasing that hypothesis. Then you find the drop is entirely in mobile web users in Germany — and TikTok doesn't even rank in Germany for that age group. You've wasted 15 minutes and look like you don't know how to diagnose.

**Segmentation order (do them in this sequence):**
1. Geography (global or concentrated in a market?)
2. Device/platform (app vs mobile web vs desktop?)
3. User cohort (new vs retained? When did they join?)
4. Content type (which categories are down?)
5. Time (sudden drop on a date, or gradual over weeks?)

Each segmentation halves your hypothesis space. By segment 3, you usually know where to look.

---

## Card 4 — Three-Bucket Hypothesis Framework

**Q:** What are the three buckets for diagnosing a product metric drop, and what goes in each?

**A:**
- **Supply** (what's available): Content quality and quantity. Creator churn, upload volume decline, algorithm changes that deprioritize certain content types, moderation that removed large amounts of content.
- **Demand** (who's using it and why): User behavior changes. Seasonal effects, competitor pull (TikTok, Reels), cohort behavior shift, demographic changes in the user base, notifications changes reducing session triggers.
- **Platform** (how it's delivered): Technical and UX issues. Video load time regression, autoplay broken, recommendation algorithm bug, A/B test with unexpected side effect, CDN issues in a region.

**Why these three matter:** The investigation plan for each bucket is completely different. Supply issues require creator analytics and content moderation logs. Demand issues require behavioral panels and competitor data. Platform issues require engineering logs and feature deploy timestamps. Naming the bucket first tells your data scientist which data set to pull.

---

## Card 5 — Correlation vs. Causation in Metric Drops

**Q:** A PM says "TikTok launched a new feature on March 1st and our Watch Time dropped on March 3rd — TikTok caused it." What's wrong with this reasoning and how do you fix it?

**A:** This is a correlation claim. Two things happened close in time, but that doesn't establish causation. To confirm causation you need:

1. **Holdout group**: Did YouTube have a control group of users who weren't shown TikTok recommendations or content? (Probably not — but you could check if the Watch Time drop varied by country where TikTok has different market share.)
2. **Natural experiment**: Did YouTube's Watch Time drop in markets where TikTok isn't available (e.g., India where TikTok was banned)? If yes, TikTok isn't the cause.
3. **Mechanism check**: What's the specific causal chain? "TikTok launched short-form video → YouTube users opened TikTok instead → YouTube sessions per day dropped." Is there data showing sessions per day dropped? Or only Watch Time per session?

The correct response to the PM: "That's an interesting hypothesis. Let's check whether the drop appears in markets where TikTok isn't available. If the drop is global and uniform regardless of TikTok market penetration, we can rule out TikTok as the primary cause."

---

## Card 6 — How to Evaluate a "Our Feature Caused This" Claim

**Q:** A PM from another team says their feature launch 3 months ago might have caused a Watch Time drop. Walk through how you evaluate this claim.

**A:** Three-step evaluation:

**Step 1 — Timeline check:** Does the Watch Time drop start ON or AFTER the feature launch date? Pull the time series. If the drop started before the launch, the feature can't be the primary cause. If the drop coincides, it's a suspect.

**Step 2 — Holdout check:** Was the feature launched to 100% of users, or was there a staged rollout with a holdout group? If there's a holdout (users who didn't get the feature), compare Watch Time: holdout group vs. treatment group. If Watch Time is down equally in both groups, the feature didn't cause it. If Watch Time is significantly worse in the treatment group, that's causal evidence.

**Step 3 — Mechanism check:** Is there a plausible causal chain? "Our feature added a 'watch next' button that replaced autoplay" → "autoplay trigger rate dropped" → "Watch Time per session dropped." That's a plausible mechanism. "Our feature changed the color of the subscribe button" → "Watch Time dropped" is implausible without a mechanism.

If the PM can't articulate a mechanism, the correlation is probably coincidental.

---

## Card 7 — Seasonal Adjustment in Metrics

**Q:** A metric drops 15% quarter-over-quarter. How do you determine if this is seasonal vs. a real problem?

**A:** Compare the same quarter year-over-year, not just quarter-over-quarter. YouTube Watch Time has known seasonal patterns: it typically peaks in winter (Q4 — holiday breaks, less outdoor activity) and dips in summer (Q2/Q3 — school's out, more outdoor activity in many markets). A Q3 Watch Time drop vs. Q2 may simply be the summer slump, not a structural problem.

**How to adjust:**
1. Pull Watch Time for the same quarter in the prior 3 years.
2. Calculate the average seasonal adjustment for that quarter (e.g., Q3 is typically 8% lower than Q2).
3. Compare the current drop against the seasonal baseline. A 15% drop with an 8% seasonal expectation means the real anomalous drop is only 7% — still significant, but half as alarming.

**The failure mode:** Treating a seasonal dip as a crisis and launching a high-effort intervention that confuses the natural recovery with success. "We shipped Feature X and Watch Time recovered!" when it would have recovered anyway.

---

## Card 8 — Cross-App Measurement Challenges

**Q:** A VP asks: "How much of our Watch Time drop is explained by users switching to TikTok?" How would you actually measure this?

**A:** This is hard because YouTube doesn't have direct visibility into other apps' usage. Options:

1. **Panel data**: Subscribe to a third-party user panel service (Nielsen, Comscore, Sensor Tower) that surveys or passively measures app usage across a representative sample. These panels can show share of time spent across apps.
2. **Device usage data (Android)**: On Android, apps can request aggregate device usage stats (with user permission). If YouTube's Android app has permission, it could see that time in *other* apps increased when YouTube Watch Time dropped — a weak signal, not direct TikTok attribution.
3. **Survey**: Run a post-session survey for users who closed YouTube after < 2 minutes: "What are you doing instead?" Options: TikTok, Instagram Reels, going outside, other YouTube session (reopened), other.
4. **Causal inference proxy**: If TikTok is banned in Market A but not Market B, and Watch Time dropped in Market B but not Market A, that's a natural experiment supporting TikTok as a cause.

The honest answer: you can't directly measure this without panel data. You can build circumstantial evidence and triangulate.

---

## Card 9 — A/B Test Design for Metric Recovery

**Q:** You've identified that autoplay trigger rate dropped (causing Watch Time per session to fall). Design an A/B test to test a fix.

**A:**
- **Hypothesis**: Re-enabling autoplay for users where it was suppressed (by a UI change or settings default) will increase Watch Time per session.
- **Treatment**: Users for whom autoplay was suppressed by the recent change are reverted to autoplay-on by default.
- **Control**: Same segment of users continues with autoplay suppressed.
- **Segment**: Only users affected by the autoplay change (identified by the deploy date and device segment), not all users — otherwise you dilute the signal.
- **Primary metric (NSM)**: Watch Time per session.
- **Guardrail**: Autoplay opt-out rate. If restoring autoplay causes a spike in opt-outs, users are signaling they don't want it — forcing it back on will backfire long-term.
- **Duration**: 2 weeks minimum. Autoplay behavior changes within 1-2 sessions, so this is faster to test than a feature that requires habit formation.
- **Success threshold**: Watch Time per session in treatment ≥ 80% of pre-change baseline, with autoplay opt-out rate not increasing by more than 5%.

---

## Card 10 — Googleyness in Metrics Work

**Q:** What does "Googleyness" look like specifically in a metrics interview answer, as opposed to a product sense interview?

**A:** In a metrics interview, Googleyness shows up as:

1. **Intellectual rigor**: You don't accept a 15% Watch Time drop as a diagnosis — you treat it as a symptom and decompose it. You refuse to anchor on the first hypothesis and explicitly test it against data.

2. **Intellectual humility**: You say "I'd want to check the measurement methodology before concluding the drop is real — it's possible the measurement changed." You don't assume the data is correct until you've validated it.

3. **Collaborative framing**: You frame the investigation as a team problem. "I'd bring this to the data science team and say: here are my three hypotheses ranked by prior probability, here's what data pull would confirm each one, please start with hypothesis 1 and come back to me before pulling data for hypothesis 3."

4. **Comfort with ambiguity**: You don't need a definitive answer to move. "Based on available data, the most likely cause is X, with 60% confidence. Here's the action I'd take now to address X while we gather data to confirm. I'd revisit if the data comes back differently."

The failure mode: presenting a polished-sounding diagnosis without acknowledging what you don't know. Google values "I don't know — here's how I'd find out" over a confident wrong answer.

---

*10 cards · Google PM Lab 02 · Review 24–48 hrs after completing workbook*
