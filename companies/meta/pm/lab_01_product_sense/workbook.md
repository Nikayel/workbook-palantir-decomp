Status: Ready — work through all parts in order

# Meta PM Lab 01 — Product Sense
## Facebook Groups Re-Engagement for 18-34 (Tier 1)

**Tier:** 1 (Worked) — ~60% pre-filled. Study the model structure carefully, understand every decision, then blank it and answer it yourself. The goal is to internalize Meta's Product Sense framework, not memorize the answers.

**Before you start:** Set a timer for 45 minutes. This lab simulates the Meta PM/RPM Product Sense round. You will NOT write code. Your artifact is a product brief with RICE scoring, a North Star Metric, and an A/B test design.

---

## Milestones

- [ ] M1 · Segmented — didn't treat "18-34" as monolithic; found a sub-segment with the highest pain
- [ ] M2 · Diagnosed — named the underlying behavior shift (not just "they use Instagram instead")
- [ ] M3 · Designed — 3 ideas with explicit RICE + one cut with rationale
- [ ] M4 · Metrics — NSM + guardrail + A/B design
- [ ] M5 · Defended — curveballs answered at billions scale
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Part 0 — Forethought

**Goal:** Recommend a specific, defensible product intervention to re-engage 18-34 year old Facebook Groups users, backed by user evidence, prioritized with RICE, and accompanied by a North Star Metric and A/B test design.

**Key Meta PM principle:** Meta interviewers evaluate your ability to think at the intersection of user psychology, product mechanics, and scale. "Users aged 18-34 prefer Instagram" is not a diagnosis — it's a symptom. The diagnosis lives in the WHY: what specific behavioral shift is happening, what's the friction in the current Groups product for this cohort, and what intervention most directly addresses it?

**Target time:** 45 minutes. Suggested breakdown:
- 3 min — clarifying questions
- 7 min — user decomposition + sub-segment selection (Parts 1–2)
- 10 min — 3 ideas + RICE scoring (Part 3)
- 10 min — metrics artifact (Part 4)
- 8 min — reasoning (Part 5)
- 7 min — curveballs (Part 6)

**Confidence rating before starting (circle one):** 1 — 2 — 3 — 4 — 5

**What I want to get right this session:** [blank]

---

## Part 1 — Clarifying Questions

*The scenario: Your Meta PM/RPM interviewer says:*

> "Facebook Groups is seeing declining engagement from users aged 18-34. Design a solution to re-engage this cohort."

**Model questions and rationale:**

**Q1: "Are we trying to re-engage lapsed users (bring back inactive users) or retain at-risk users (prevent further churn)?"**

Rationale: These require completely different interventions. Lapsed users need a reason to come back — a reactivation trigger. At-risk users need a reason to stay — a stickiness improvement. The diagnosis also differs: lapsed user churn is a historical signal; at-risk user behavior is observable in real-time.

*Assumption for this lab: We're targeting lapsed users — those who were active in Groups 6+ months ago but haven't posted, commented, or reacted in the last 60 days.*

**Q2: "Does 18-34 mean all users in that age range, or is there a specific sub-group — college students, young parents, creators — that the data suggests is driving the decline?"**

Rationale: "18-34" is not a behavioral segment. A 19-year-old college student's relationship with Facebook Groups is completely different from a 33-year-old parent's. Treating them as one segment will generate features that resonate with neither.

*Assumption: We'll investigate which sub-segment has the highest lapse rate, and design for the highest-pain sub-segment. We'll identify that in Part 2.*

**Q3: "How is 'engagement' defined here — posting, commenting, reacting, or Group membership? And are we looking at all Group types equally, or are some (interest-based, local, professional) more affected?"**

Rationale: A user who reacts to every post but never posts is engaged differently from a user who posted once and disappeared. The intervention design depends on which engagement type has declined. Similarly, a decline in local community Groups is a different problem from a decline in interest-based hobbyist Groups.

*Assumption: "Engagement" = any active contribution: posting, commenting, or reacting (views excluded). Group type: we'll look at all types but will segment in Part 2.*

**Q4: "Is this global or specific markets? What's the competitive landscape — Discord, Reddit, BeReal, Snapchat?"**

Rationale: The competitive threat for 18-34 year olds varies dramatically by market. In the US, Discord has largely taken the "niche community" use case from Groups. In India, Facebook still dominates community discussion. The intervention for a market-specific decline vs. a global decline is different.

*Assumption: We're focused on English-language markets (US, UK, Canada, Australia) where the competitive dynamic with Discord and Reddit is most significant.*

**Q5: "Is there any constraint on the solution — timeline, surface (Groups feed vs. notification vs. homepage), or technologies we can't use?"**

*Assumption: No hard constraints. We're designing for the long-term — we'll scope a V1 for 6-8 weeks shipping in the brief.*

**Checkpoint M1:** Check the box above once you've written your assumptions and can articulate what's different about 18-34 year olds vs. other cohorts BEFORE looking at Part 2.

---

## Part 2 — Decomposition

### Current Journey for an 18-34 User in Facebook Groups

*Map the journey step by step. Do this before proposing any solutions — you're looking for where 18-34 year olds specifically drop off.*

**Persona construction: who is the 18-34 user in Groups?**

18-34 breaks into at least three meaningfully different sub-segments:

| Sub-segment | Typical Groups they join | Why they joined | Why they lapse |
|---|---|---|---|
| College students (18-22) | Campus groups, class groups, club groups | Practical utility — schedule info, event invites | Graduate and leave campus; the Group becomes irrelevant |
| Young professionals (23-29) | Professional networking, hobby groups, local community | Discovery and identity | Discovery improves elsewhere (LinkedIn, TikTok For You); Groups feel like work |
| Young parents (28-34) | Parenting groups, neighborhood groups, school parent groups | Support and local community | Content quality degrades over time; too much off-topic noise |

**Highest-pain sub-segment:** Young professionals (23-29) — they joined Groups for identity and discovery, but the content they see in their Groups has low relevance to their current life stage. The Group they joined as a college anime fan now feels stale; they've grown beyond it but haven't left.

**Key behavioral insight:** The 18-34 cohort experiences "identity drift" — their interests and life stage change faster than their Group memberships do. They're members of Groups that no longer represent who they are. The product doesn't help them find better-fit Groups or refresh their membership portfolio.

**Current journey for young professional "Marcus," 26, Los Angeles:**

| Step | Action | What's working | What's broken / painful |
|---|---|---|---|
| 1. Discovery | Facebook suggests Groups based on interests and friends | Relevant Groups suggested at join time | Suggestions don't refresh as Marcus's interests evolve |
| 2. Joining | Marcus joins 3-5 Groups on a topic he's interested in | Low friction to join | No onboarding — Marcus doesn't know how to contribute or what the Group norms are |
| 3. First visit | Marcus sees the Group feed | He can see what's been posted | The first 3 posts are links to external articles, not discussion; he scrolls past |
| 4. First contribution attempt | Marcus tries to post a question | He can post | Post gets 0 responses in 24 hours — nobody engaged; Marcus feels ignored |
| 5. Return (or not) | Marcus checks back | — | Nothing has changed; no one responded; his post is buried |
| 6. Lapse | Marcus stops opening the Group | — | No re-engagement signal; Group continues posting; Marcus is invisible to the algorithm as disengaged |

**Bottleneck:** Step 4 — the failed first contribution. Marcus tried to engage and got no response. This is the highest-leverage intervention point: a first contribution that fails signals to Marcus that the Group is not worth his time. If the first contribution succeeds (even a small reaction or reply), Marcus is statistically more likely to return.

**Checkpoint M2:** Check the box once you've identified the specific sub-segment, the behavioral insight (identity drift), and the bottleneck step (failed first contribution).

---

## Part 3 — Prioritization and Feature Design

*Generate ideas that target the bottleneck. Score with RICE. Cut at least one.*

**RICE scoring guide:**
- **Reach:** % of 18-34 lapsed users affected per quarter. Score 1-5.
- **Impact:** How directly does this fix the bottleneck (failed first contribution)? Score 1-3.
- **Confidence:** Evidence quality for Reach and Impact. Score 1-3.
- **Effort:** Engineering person-months. Lower = higher RICE. Score 1-3 (1 = high effort, reduces RICE).
- **RICE = (Reach × Impact × Confidence) / Effort**

**Three ideas:**

**Idea 1: First Contribution Amplifier**
When a lapsed 18-34 user makes their first post in a Group after 60+ days of inactivity, temporarily boost the post's visibility in the Group feed (show it to 3× the normal number of active Group members for the first 6 hours). Goal: ensure at least one quality response, converting the silent return into a sticky re-engagement.

| Reach | Impact | Confidence | Effort | RICE |
|---|---|---|---|---|
| [blank — what % of lapsed users post when they do return?] | [blank] | [blank] | [blank] | [blank] |

*Model RICE:* Reach: 3 (only users who return AND post — maybe 20% of lapsed users who open Groups again); Impact: 3 (directly addresses the failed-first-contribution bottleneck); Confidence: 2 (we have evidence that "no response to first post" predicts lapse, but we'd need to A/B the boost); Effort: 2. RICE = (3×3×2)/2 = 9.

**Idea 2: Group Portfolio Health Score + Refresh Prompt**
Every 90 days, proactively surface a "Your Groups have been quiet" card on the Facebook homepage for users who haven't engaged in 30+ days. The card shows: (a) which Groups they're in, (b) how active each has been, (c) suggested replacement Groups in similar categories where members their age are more active. Let them swap Groups in one tap.

| Reach | Impact | Confidence | Effort | RICE |
|---|---|---|---|---|
| [blank] | [blank] | [blank] | [blank] | [blank] |

*Model RICE:* Reach: 5 (all lapsed users — proactive card requires no action to trigger); Impact: 2 (addresses identity drift, but doesn't directly fix the first-contribution problem); Confidence: 2 (we're confident lapsed users have stale Group portfolios; we're less sure they'll swap); Effort: 3 (requires a new matching algorithm for "age-peer-active" Groups). RICE = (5×2×2)/3 = 6.7.

**Idea 3: Weekly Group Digest with Personalized Hook**
For lapsed 18-34 users, send a weekly email or in-app notification: "Here's what's happening in [Top Group] this week." But instead of showing the most recent posts (which may be low quality), use engagement signals to surface the post most likely to resonate with that specific user — based on their past reactions and the types of content they engaged with most. Add a low-friction reply button directly from the notification.

| Reach | Impact | Confidence | Effort | RICE |
|---|---|---|---|---|
| [blank] | [blank] | [blank] | [blank] | [blank] |

*Model RICE:* Reach: 5 (all lapsed users receive the notification); Impact: 2 (gets users back to Groups, but they still face the first-contribution barrier on return); Confidence: 3 (personalized digests have strong evidence in email marketing; Meta already has this infra); Effort: 1 (high effort — ML personalization + notification system changes). RICE = (5×2×3)/1 = 30. **Highest RICE by far.**

**Your cut:**
I am cutting [blank] because [blank].

*Model cut:* "I'm cutting the Group Portfolio Health Score feature. While it addresses the identity drift insight well, it solves for Group discovery rather than Group stickiness. Discovery is the wrong intervention for a lapsed user — they already know how to find Groups. The core problem is that the Groups they're in don't give them a reason to contribute. Fixing discovery doesn't fix contribution quality. I'd revisit this in V2 as a complementary feature once the first-contribution and re-engagement problems are solved."

**Your recommended feature:** [blank]

*Model recommendation:* "I recommend the Weekly Group Digest with Personalized Hook as the primary bet. It has the highest RICE, it creates a low-friction re-entry point for lapsed users (react from the notification, no need to navigate to Groups), and Meta already has the ML personalization and notification infrastructure to build it without a large net-new engineering investment. The First Contribution Amplifier is my V2 recommendation — once we've re-engaged lapsed users via the digest, the amplifier ensures their first contribution sticks."

**Checkpoint M3:** Check the box once you've completed the RICE table, cut one feature with explicit reasoning, and named your recommendation.

---

## Part 4 — Product Brief (PM Artifact)

**Feature name:** [blank]

*Model:* "Groups Re-Engagement Digest"

---

**Problem:**
[blank — 2-3 sentences: who, pain, why now]

*Model:* "Facebook Groups engagement from users aged 18-34 has declined, driven primarily by lapsed users who joined Groups for identity and community but received no compelling reason to return after their initial contributions went unacknowledged. The current Groups experience does not proactively surface relevant content to lapsed users, and it relies on these users to self-initiate re-engagement — a behavioral barrier that most lapsed users don't overcome. With short-form social content platforms capturing the daily attention of this cohort, the window to re-engage lapsed Group users before they permanently exit is narrowing."

---

**Solution:**
[blank — 2-3 sentences: what, how]

*Model:* "A weekly personalized digest notification (email and/or in-app) that surfaces the single highest-relevance post from each of the user's active Groups, selected by a personalization model trained on the user's historical engagement patterns. The notification includes a low-friction inline reply option so the user can contribute without navigating to Groups first. For the first 4 weeks after a lapsed user re-engages via the digest, the First Contribution Amplifier boosts their post visibility to ensure at least one quality response."

---

**North Star Metric:**
[blank — one metric directly measuring whether lapsed users re-engage]

*Model:* "% of lapsed 18-34 Group users who make at least 1 active contribution (post, comment, or substantive react) in any Group within 30 days of receiving the digest — measured as a 30-day rolling average."

*Why this NSM:* It measures the specific behavior we're trying to restore (active contribution), not passive re-engagement (opening the notification or viewing the Group feed). A lapsed user who views the Group but doesn't contribute is not re-engaged — they're just browsing. The 30-day window captures re-engagement without requiring habit formation (which takes longer to measure).

---

**Guardrail metric:**
[blank — metric that would veto launch if it moved negatively]

*Model:* "Notification opt-out rate among 18-34 users who receive the digest. If this rises more than 10 percentage points above the control group's opt-out rate, it signals that the digest is perceived as spam rather than value — a harm to the long-term relationship that overrides the short-term re-engagement gain. A second guardrail: report/block rate on Group content surfaced in the digest (if we're showing users more content, we must not be showing them more harmful content)."

---

**A/B test design:**
[blank — who, what, how long, success criteria]

*Model:* "Treatment group: 15% of lapsed 18-34 Group users (no active contribution in 60+ days) who are opted into notifications. Control group: 15% of the same segment who receive no digest notification. Matching on: account age, Group membership count, prior engagement level. Test duration: 6 weeks (long enough for 6 digest cycles and to measure 30-day re-engagement). Declare success if: (1) re-engagement rate in treatment ≥ 5 percentage points above control, AND (2) notification opt-out rate in treatment ≤ control + 10 points, AND (3) report rate on surfaced content does not increase."

*A/B design note — network effects:* In social products, A/B tests are complicated by network effects — treatment users who return to Groups will interact with control users, potentially improving control users' Groups experiences (and understating the true treatment effect). Mitigation: assign treatment/control at the Group cluster level, not at the individual user level, so treatment users interact primarily with other treatment users.

**Checkpoint M4:** Check the box once all 5 brief fields are completed in your own words.

---

## Part 5 — System Reasoning

**Q1: Why focus on "failed first contribution" as the bottleneck rather than "wrong Group discovery"?**

[blank — your answer]

*Model:* "Discovery gets you to a Group. Contribution keeps you there. If Marcus joins the right Group but still gets zero responses to his first post, he'll still lapse — the Group will feel as dead as the wrong one. The bottleneck is the first contribution loop, not the discovery funnel. We know this because our data (hypothetically) shows that users who get a response to their first post within 24 hours have a 4× higher 30-day retention rate than those who don't. That's the highest-leverage intervention point."

**Q2: How does this feature work at Meta's scale — billions of users, hundreds of millions of Groups?**

[blank — your answer]

*Model:* "At Meta's scale, the personalization model needs to run inference for potentially 100M+ lapsed users per week. The key constraints: (a) The model must be fast enough to generate recommendations in batch (not real-time per request) — you run it Sunday night, serve the results Monday morning. (b) The content to surface must be safe — no harassment, no misinformation, no low-quality engagement-bait. Content safety scoring must run on every candidate post before it's eligible for the digest. (c) The notification infra must handle peak send volume without creating a spike in back-end traffic when users click through simultaneously. Use staggered send windows (Monday 8-10am in the user's time zone) rather than batch-sending all at once."

**Q3: What's the riskiest assumption in your brief?**

[blank — your answer]

*Model:* "The riskiest assumption is that lapsed users WANT to return to Groups, and that a well-timed, relevant notification is enough to overcome inertia. The alternative hypothesis: lapsed users have actively chosen to spend their time elsewhere (Discord, TikTok, IRL activities) and no notification will bring them back to a product they've consciously de-prioritized. The A/B test will tell us this — if the re-engagement rate is low even with the personalized digest (< 2 percentage points above control), we should consider whether the Groups product itself needs a more fundamental redesign rather than a re-engagement notification."

---

## Part 6 — Interview Simulation (Curveballs)

### Curveball 1 — Safety Tradeoff

**Interviewer:** "Your feature shows a 5% increase in Group posts but a 3% increase in reports of harassment. Do you launch?"

**Your answer:** [blank]

*Things to address:*
- This is the Meta PM's most common tension: engagement vs. safety. Meta's internal principle is that "safety trumps growth" — so a 3% increase in harassment reports is not an acceptable cost for a 5% post increase, at scale.
- At Meta's scale: 3% increase in harassment reports across billions of Groups means tens of millions more harassment reports per year. That's not a rounding error — it's a safety crisis.
- However, investigate the mechanism before declaring failure: is the harassment coming from the boosted posts (i.e., our amplifier is boosting harassing content) or from general Group activity increase (more posts = more surface area for harassment at a constant rate)? If the harassment rate is constant (same % of posts get reported) and only total posts went up, the feature is not CAUSING more harm — it's just surfacing more of what already existed.
- Decision: pause the launch, investigate the mechanism, and fix it before relaunching. Do not launch with known harassment rate increase without understanding the cause.

---

### Curveball 2 — AI/LLM Tradeoff

**Interviewer:** "Meta's AI team wants to add LLM-generated conversation starters to Groups. You think it'll feel fake. How do you evaluate it?"

**Your answer:** [blank]

*Things to address:*
- "It'll feel fake" is a hypothesis, not a data point. Evaluate it empirically before making a recommendation.
- Framework: (1) User testing: show a mix of real human conversation starters and LLM-generated ones to users without labeling them. Do they rate the LLM ones as lower quality? (2) Engagement metrics: if LLM conversation starters do drive posts and replies, does the engagement feel coerced (users reply once and then lapse) or genuine (users return)? (3) Disclosure: does Meta need to disclose that conversation starters are AI-generated? This is a policy and legal question as much as a product question.
- The risk is not that LLM conversation starters feel fake — it's that if users discover they're interacting with AI-generated content and feel deceived, the reputational damage to Facebook Groups is worse than the engagement gain. Transparency is the safeguard: label AI-generated starters clearly.
- Recommendation: A/B test with full disclosure. If engagement holds even when users know it's AI-generated, launch with disclosure. If disclosure tanks engagement, that tells you users don't want AI-generated content in Groups — and the answer is no.

---

### Curveball 3 — Timeline Pressure

**Interviewer:** "A VP wants this shipped in 2 weeks. Your A/B test needs 4 weeks for statistical significance. What do you do?"

**Your answer:** [blank]

*Things to address:*
- This is a classic PM tension: stakeholder pressure vs. data integrity. "Move Fast" at Meta doesn't mean "skip the A/B test" — it means "design a faster path to a signal."
- Options:
  1. **Sequential A/B with early stopping**: Ship the feature and monitor the primary metric daily. If the effect is large enough (say, 15+ percentage points re-engagement lift vs. control) by day 14, you have enough signal to decide even without 4-week statistical significance. If the effect is small, you need 4 weeks.
  2. **Narrower test scope**: Run the test on a higher-frequency segment (users who open Facebook daily but not Groups) — a group that gives you more data points per day, shortening the time to significance.
  3. **Staged launch with guard rails**: Ship to 1% of users in week 1, monitor safety metrics (harassment rate, opt-out rate) as guardrails. If guardrails are clean, expand to 5% in week 2. The re-engagement metric may not be significant yet, but safety signals give you confidence to continue.
- What you DON'T do: launch to 100% without a test because a VP is impatient. Frame this to the VP as: "I can give you a 1% signal in 2 weeks that tells us whether this is safe to scale, and a 10% signal in 4 weeks that tells us whether it's working. Shipping to 100% at 2 weeks means we can't isolate the effect if something goes wrong."

---

## Part 7 — PM Rubric

*Self-grade after completing the lab. Score as a Meta PM/RPM interviewer would.*

| Dimension | 5 — Strong | 3 — Adequate | 1 — Weak | Your Score |
|---|---|---|---|---|
| Structure | Segment → diagnose → RICE → NSM → A/B in order; never proposed features before finding the bottleneck | Followed the framework mostly but proposed features before completing the journey map | No clear structure; immediately brainstormed features when asked to "design a solution" | __ /5 |
| User empathy | Broke 18-34 into sub-segments with different behaviors; found the specific behavioral insight (identity drift, failed first contribution) that explains the lapse | Named sub-segments but treated them as similar; pain was generic ("they prefer short-form video") | No sub-segmentation; treated 18-34 as monolithic | __ /5 |
| Prioritization | RICE-scored 3 features; cut one with explicit reasoning; named the V2 sequencing for the cut feature | Scored features but didn't cut; or cut without reasoning | Listed features without prioritization | __ /5 |
| Metrics literacy | NSM measures active contribution (not passive re-engagement); guardrail explicitly includes harassment rate; A/B design addresses network interference risk | Named NSM and guardrail but without operationalizing them | Named "engagement" as both the NSM and the thing being measured | __ /5 |
| Communication | Articulated the identity drift insight clearly; adapted explanation for the safety curveball without becoming defensive | Communicated adequately; the reasoning was followable but required effort | Hard to follow; interviewer would not be confident in the recommendation | __ /5 |
| Creativity | Named "identity drift" as the underlying behavioral insight — not the obvious "they use TikTok instead"; proposed first-contribution amplifier as a mechanism | Proposed a reasonable feature (digest or notification) but didn't identify why the core problem is first-contribution failure | Proposed obvious features ("make Groups more visual," "add a TikTok-like feed") without diagnosing the problem | __ /5 |
| Handling ambiguity | Defined "lapsed," "engagement," and "18-34 sub-segments" independently; made explicit assumptions about market and scope; moved forward on the VP's 2-week timeline without shutting down or capitulating | Clarified when asked but needed prompting; handled the timeline curveball by just saying "we need 4 weeks" without offering alternatives | Got stuck defining terms; couldn't navigate the VP timeline without a clear answer | __ /5 |

**Total: __ / 35**

---

## You're Ready When...

- You complete the full brief (Parts 0–6) in under 40 minutes without model answers
- You name "identity drift" and "failed first contribution" (or equivalent behavioral insights) before the model
- You answer Curveball 1 (5% posts / 3% harassment) without immediately saying "don't launch" — you investigate the mechanism first
- You handle the VP's 2-week ask with the sequential/guardrail alternative without capitulating or refusing
- You self-grade ≥ 28/35 on two separate attempts

**Next lab:** [→ Meta PM Lab 02: Jedi Behavioral](../lab_02_jedi_behavioral/workbook.md)

---

*Meta PM Lab 01 · Tier 1 (Worked) · v1.0*
