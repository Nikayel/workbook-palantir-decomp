# Google PM Lab 01 — Product Sense
## Improve Google Maps for Commuters (Tier 1 — Worked)

**Tier:** 1 (Worked) — ~60% pre-filled. Study the model structure and reasoning carefully, understand every decision, then blank it and answer it yourself. The goal is to internalize the framework, not memorize the answers.

**Before you start:** Set a timer for 45 minutes. This lab simulates a Google APM Product Sense interview. You will NOT write code — your artifact is a product brief and a prioritized feature list.

---

## Milestones

- [ ] M1 · Framed — named a specific user segment and their #1 pain point before proposing any solution
- [ ] M2 · Decomposed — mapped the current user journey and identified the specific bottleneck
- [ ] M3 · Prioritized — generated 3+ ideas, explicitly ranked them, and cut at least one with a stated reason
- [ ] M4 · Artifact — completed the brief with a North Star Metric, guardrail metric, and A/B test outline
- [ ] M5 · Defended — answered all 3 curveballs without pivoting away from your chosen recommendation
- [ ] M6 · Ready — self-graded ≥ 28/35 on two separate attempts

---

## Part 0 — Forethought

**Goal:** Recommend a specific, defensible improvement to Google Maps for commuters, backed by user evidence, prioritized with a scoring framework, and accompanied by a success metric.

**Key APM interview principle:** Google APM interviewers are NOT looking for a single "correct" answer. They're evaluating your structure, your user empathy, your ability to prioritize under constraint, and your comfort with tradeoffs. A well-reasoned case for an imperfect idea beats a vague case for an "obvious" idea.

**Target time:** 45 minutes. Suggested breakdown:
- 3 min — clarifying questions
- 7 min — user segment + journey mapping (Parts 1–2)
- 10 min — ideation + RICE scoring (Part 3)
- 10 min — brief artifact (Part 4)
- 8 min — reasoning write-up (Part 5)
- 7 min — curveballs (Part 6)

**Confidence rating before starting (circle one):** 1 — 2 — 3 — 4 — 5

**What I want to get right this session:** [blank]

---

## Part 1 — Clarifying Questions

*The scenario: Your Google APM interviewer says:*

> "How would you improve Google Maps for commuters?"

*This is intentionally vague. Clarify before proposing anything.*

**Model questions and rationale:**

**Q1: "Who are we optimizing for — all commuters globally, or a specific mode of transit or geography?"**
Rationale: "Commuter" includes car, bus, subway, bike, and walk. A feature for drivers is useless for subway riders. Narrowing the persona lets you go deeper.
*Assumption for this lab: We're focusing on daily urban commuters who use a mix of transit modes (e.g., walk → subway → walk) in a dense city like New York, London, or Tokyo.*

**Q2: "What does 'improve' mean — increase reliability, reduce commute time, reduce cognitive load, or something else?"**
Rationale: "Improve" is the most under-specified word in an APM interview. If you don't define it, you'll generate features that point in different directions.
*Assumption: We define "improve" as reducing anxiety and cognitive load during the commute — not just reducing time.*

**Q3: "Are we optimizing for a specific business goal, like increasing DAUs, revenue, or market share vs. Waze/Apple Maps?"**
Rationale: Business context changes the prioritization. A feature that's great for users but doesn't help DAUs might not get greenlit.
*Assumption: Primary goal is increasing daily active usage of Maps by commuters who currently switch to other apps (especially Waze and Citymapper) mid-commute.*

**Q4: "Is there any constraint on the solution — API access, platform (Android/iOS/web), or user data availability?"**
Rationale: A real PM needs to know what's buildable. Constraints are part of the brief.
*Assumption: No technical constraints stated — we're free to propose anything that's feasible for Google's engineering teams.*

**Checkpoint M1:** Check the box above once you've framed the problem with at least 2 clarifying questions and written your assumptions.

---

## Part 2 — Decomposition

### User Journey for the Urban Multi-Mode Commuter

*Map the current experience step by step. Do this before proposing any solutions — you're looking for the bottleneck, not brainstorming features yet.*

**Persona:** Priya, 28, marketing manager in London. Commutes 45 minutes each way: 10 min walk + 25 min Tube + 10 min walk. Uses Google Maps to plan the route, then often switches to Citymapper when the route changes.

**Current journey:**

| Step | Action | What's working | What's broken / painful |
|---|---|---|---|
| 1. Plan | Opens Maps 10 min before leaving | Quick route suggestion | Route doesn't factor in current Tube disruptions proactively |
| 2. Depart | Leaves home following Maps walking directions | Works well | Doesn't know if she should delay departure to avoid a delayed train |
| 3. En route (walking) | Maps navigation | Works well | Rerouting alerts are rare and late |
| 4. Platform | Waiting for train | N/A (Maps passive) | No push notification if her specific train is delayed; she checks Tube status app separately |
| 5. En route (transit) | Maps shows progress | Works adequately | If she needs to switch routes mid-ride due to an incident, Maps re-calculates slowly |
| 6. Arrive + walk | Final walking directions | Works well | Doesn't suggest "leave now vs. leave in 10 min" to optimize arrival time |

**Bottleneck:** [blank — fill in: where is the biggest pain, and why?]

*Model answer to compare:* The biggest bottleneck is Step 4 and the transition between Steps 2 and 3: the app doesn't proactively alert Priya to disruptions that affect HER specific route, and doesn't tell her whether to leave now or wait. She has to switch apps or check manually. The anxiety this creates — "am I going to be late?" — is the core pain, not the route itself.

**Core user pain:** [blank — one sentence]

*Model answer:* Priya doesn't know when to leave or whether her route is reliable until it's too late to change plans.

**Primary persona's #1 Job-to-be-Done:** [blank]

*Model answer:* "Help me arrive on time without having to think about it."

**Checkpoint M2:** Check the box once you've identified the bottleneck and named the primary pain point. Do not generate features yet.

---

## Part 3 — Prioritization and Feature Design

### 3 Feature Ideas

*Generate ideas that target the bottleneck identified in Part 2. Then score them with RICE. You MUST cut at least one idea with an explicit reason.*

**RICE scoring guide:**
- **Reach:** How many of our target users (daily commuters on multi-mode routes) does this affect? Score 1–5 (5 = all of them).
- **Impact:** How much does this improve the core pain (commute anxiety / switching apps)? Score 1–3 (3 = directly eliminates it).
- **Confidence:** How confident are we in Reach and Impact estimates? Score 1–3 (3 = strong evidence).
- **Effort:** Engineering effort in person-months. Lower effort = higher RICE score. Score 1 = very high effort (reduces RICE).
- **RICE = (Reach × Impact × Confidence) / Effort**

| Feature | Description | Reach | Impact | Confidence | Effort | RICE | Cut? |
|---|---|---|---|---|---|---|---|
| **Proactive Departure Alerts** | Push notification 20–30 min before user's habitual commute time: "Leave now — your usual route is delayed. Alternative: Bus 94 (5 min longer but more reliable today)." | [blank] | [blank] | [blank] | [blank] | [blank] | [blank] |
| **Live Commute Confidence Score** | During navigation, show a small real-time indicator: "87% chance of on-time arrival." Updates every 2 min based on live transit data. If it drops below 70%, proactively suggest reroute. | [blank] | [blank] | [blank] | [blank] | [blank] | [blank] |
| **Leave-Now vs. Leave-Later Decision Panel** | On the Maps home screen during commute window, show: "Leave now: arrive 8:47am · Wait 10 min: avoid platform crowding, arrive 8:53am." | [blank] | [blank] | [blank] | [blank] | [blank] | [blank] |

*Model RICE scoring for reference (fill in your own first):*

| Feature | Reach | Impact | Confidence | Effort | RICE |
|---|---|---|---|---|---|
| Proactive Departure Alerts | 4 | 3 | 2 | 2 | 12 |
| Live Confidence Score | 3 | 2 | 2 | 3 | 4 |
| Leave-Now vs. Later Panel | 4 | 3 | 2 | 1 | 24 |

**Your cut and reason:**

I am cutting [blank] because [blank].

*Model cut:* "I'm cutting the Live Confidence Score. While it's interesting, it adds information but doesn't directly reduce anxiety — it might actually increase it if users watch the score drop. It's also lower RICE due to high engineering effort for real-time probabilistic modeling. I'd revisit it as a v2 enhancement once the core alert system is proven."

**Your recommended feature:** [blank]

*Model recommendation:* "I recommend the Leave-Now vs. Leave-Later Decision Panel as the primary bet. It has the highest RICE, directly addresses the core pain (Priya doesn't know when to leave), and requires relatively lower engineering lift compared to real-time probabilistic modeling. Departure Alerts is a close second and I'd sequence it in v2."

**Checkpoint M3:** Check the box once you've completed the RICE table, cut at least one feature with a reason, and named your recommendation.

---

## Part 4 — Product Brief (PM Artifact)

*Write this as if you're submitting it to your PM lead for a go/no-go review. Be specific.*

---

**Feature name:** [blank]

*Model:* "Commute Departure Optimizer"

---

**Problem:**
[blank — 2–3 sentences: who is affected, what pain, why now]

*Model:* "Daily urban commuters on multi-mode transit routes (walk + transit + walk) experience high anxiety about departure timing because Google Maps does not tell them when to leave relative to live transit disruptions. This causes users to switch to competing apps (Citymapper, Waze) that offer proactive departure guidance. With urban commuting recovering post-pandemic, this is a high-frequency use case that Maps is under-serving."

---

**Solution:**
[blank — 2–3 sentences: what it does, how it works at a high level]

*Model:* "A departure timing panel on the Maps home screen that appears 30 minutes before a user's habitual commute window. The panel shows two or three departure options (now, +10 min, +20 min) with predicted arrival time and crowding level for each. It sources data from real-time transit feeds, Maps historical commute data, and Google's existing transit prediction models."

---

**Success metric (North Star Metric):**
[blank — one metric that directly measures whether this feature solved the problem]

*Model:* "% of commuters who complete their habitual route end-to-end using only Google Maps (no app switching), measured as a 7-day rolling average per user."

*Why this NSM:* It directly measures whether we've eliminated the reason users switch to Citymapper. Time saved and ETA accuracy are leading indicators; no-switch rate is the outcome we care about.

---

**Anti-metric (guardrail):**
[blank — the metric that would make you kill the launch if it moved negatively]

*Model:* "Average commuter stress rating (captured via post-commute prompt: 'How was your commute? 1–5'). If this drops by more than 0.2 stars after launch, we investigate and pause rollout. A feature designed to reduce anxiety that actually increases it is worse than no feature."

---

**A/B test design:**
[blank — who sees the treatment, what's the control, how long do you run it, and what movement in the NSM declares success]

*Model:* "Treatment group: 10% of daily urban commuters (users who used Maps navigation on transit routes ≥ 5 days in the past 30 days) see the Departure Optimizer panel. Control group: 10% matched users see the current Maps home screen with no panel. Run for 4 weeks (to capture 20+ commuting sessions per user). Declare success if: (1) no-app-switch rate improves ≥ 5 percentage points in treatment vs. control, AND (2) guardrail metric (stress rating) does not decline by more than 0.2 stars."

---

**Checkpoint M4:** Check the box once all 5 brief fields are filled in with your own words.

---

## Part 5 — System Reasoning

*Answer these in writing. These are the follow-up questions an APM interviewer or a PM lead would ask.*

**Q1: Why this user segment (urban multi-mode commuters) and not, say, drivers or cyclists?**
[blank — your answer]

*Model:* "Multi-mode commuters have the highest anxiety because their route has multiple handoffs — each one is a point where a disruption cascades into a bigger delay. A driver can reroute fluidly; a subway rider is committed once they board. Citymapper and Transit already own this segment better than Maps does, so this is a market share recovery opportunity. Cyclists are a smaller segment and the intervention is different (bike infrastructure varies too much)."

**Q2: Why prioritize the Leave-Now vs. Leave-Later Panel over Proactive Departure Alerts?**
[blank — your answer]

*Model:* "Both are strong. The panel wins on effort — it surfaces information we already have (live transit, historical commute data) in a decision-support format rather than requiring a new prediction model. Alerts require computing a 'should I notify now?' trigger which is more ML-intensive. I'd ship the panel first, validate that users engage with it, and then add proactive alerts once we know the decision-support format resonates."

**Q3: What is the riskiest assumption in your brief?**
[blank — your answer]

*Model:* "The riskiest assumption is that users WANT to be nudged about departure timing. Some users may find the panel intrusive ('I already know when I leave'). There's also a risk of alert fatigue if the recommendations are frequently wrong. The A/B test guardrail addresses this — if we see users dismissing the panel or stress scores drop, that's the signal to reconsider."

**Q4: What would make you kill the launch (beyond the guardrail metric)?**
[blank — your answer]

*Model:* "Three things: (1) If the model's 'on-time' predictions are wrong > 20% of the time in the first week, the feature does more harm than good — we should pull it immediately and fix the prediction quality. (2) If we see a spike in support tickets or app store reviews mentioning 'wrong departure time,' that's qualitative signal to act on even if the NSM looks fine. (3) If transit agency partners push back on the use of their real-time data in this context, we'd have a legal and partnership risk."

---

## Part 6 — Interview Simulation

### 90-Second Narration

*Set a timer for 90 seconds. Without looking at your notes, narrate your complete product recommendation as if you're pitching it to the interviewer. Cover: user segment, core pain, your recommendation, the NSM, and the one thing you'd measure.*

[blank — your narration notes or reflection afterward]

---

### Curveball 1 — Scale

**Interviewer:** "Google Maps has over 1 billion users. How does your feature scale internationally? Does 'Leave-Now vs. Leave-Later' work the same way in Lagos as in London?"

**Your answer:** [blank]

*Things to address:*
- Transit data quality varies dramatically. London TfL has excellent real-time data; Lagos does not. The feature's value is directly tied to data quality.
- Localization: departure timing norms are cultural. In some cities, transit is so unreliable that advice "leave now" is meaningless.
- Strategy: roll out to cities with mature real-time transit data feeds first (London, New York, Tokyo, Berlin, Singapore). Build a data quality score per city and use it as a launch gate.
- Long-term: invest in transit data partnerships in emerging markets to expand the feature's reach.

---

### Curveball 2 — Conflicting Metrics

**Interviewer:** "Your A/B test results come in. ETA accuracy improved by 3% and the no-switch rate improved by 4 percentage points. But the post-commute stress rating dropped by 0.3 stars (below your 0.2-star guardrail). What do you do?"

**Your answer:** [blank]

*Things to address:*
- The guardrail was set for a reason — a drop of 0.3 stars means the guardrail is breached. You should pause the rollout, not declare victory.
- Investigate: is the stress increase correlated with accurate or inaccurate recommendations? ("The panel said leave now and I arrived on time" vs "The panel said leave now and the train was cancelled anyway.")
- Possible cause: the feature is highlighting problems users weren't previously aware of, increasing perceived anxiety even if objective outcomes improved.
- Next steps: qualitative research (user interviews) to understand the stress driver, then iterate. Don't override the guardrail with a narrative — the guardrail exists to prevent exactly this.

---

### Curveball 3 — Scope Expansion

**Interviewer:** "A VP wants to add a shopping feature to Maps — nearby deals and ads integrated into the navigation flow. How do you evaluate it?"

**Your answer:** [blank]

*Things to address:*
- This is a classic "shiny object from leadership" PM scenario. Your job is to evaluate it rigorously, not just say yes or no.
- Framework: (1) Does it serve the user's JTBD while navigating? (2) Does it add to or detract from the core navigation experience? (3) What's the business model — ads? affiliate? (4) Competitive: Google already shows business pins and promoted places; this is an extension, not a new concept.
- Red flags: distracted driving if the feature triggers during active navigation. Any feature that increases distraction during navigation is a safety issue and a liability.
- Recommendation structure: "I'd evaluate this as a navigation-complete moment feature — show deals only after the user has arrived at their destination or parked, not during active turn-by-turn. That addresses the safety concern and still captures the monetization opportunity."

---

## Part 7 — PM Rubric

*Self-grade after completing the lab. Score as an APM interviewer would.*

| Dimension | 5 — Strong | 3 — Adequate | 1 — Weak | Your Score |
|---|---|---|---|---|
| Structure | Clear framework throughout: clarify → segment → bottleneck → ideas → prioritize → NSM → A/B; never jumped ahead | Followed the framework mostly but skipped or merged steps | No clear structure; jumped from "improve Maps" to feature proposals without framing | __ /5 |
| User empathy | Named a specific persona with a concrete pain point; used the journey map to find the bottleneck before ideating | Named a user type but pain was generic ("users want faster commutes") | No specific user mentioned; proposed features without a user problem | __ /5 |
| Prioritization | Scored 3 features with RICE (or equivalent); explicitly cut at least 1 with a stated reason; picked a primary recommendation | Scored features but didn't cut; or cut without reasoning | Listed features without prioritization; no recommendation | __ /5 |
| Metrics literacy | Defined an NSM that measures the outcome (not activity); defined a guardrail metric with a threshold; described an A/B test with success criteria | Named an NSM and guardrail but without precise definitions or thresholds | Named "user satisfaction" or "engagement" as metrics without operationalizing them | __ /5 |
| Communication | Spoke clearly and concisely; adapted the explanation to the audience; no jargon without definition | Communicated adequately but occasionally lost the thread or over-explained | Rambled; interviewer would not understand the recommendation | __ /5 |
| Creativity | Proposed a non-obvious feature (e.g., decision panel rather than generic "add more info") that targets the specific bottleneck | Proposed a reasonable feature but obvious (e.g., "improve ETA accuracy") | Proposed features with no connection to the identified bottleneck | __ /5 |
| Handling ambiguity | Defined the user segment and success metric independently without waiting for the interviewer to narrow things down; made explicit assumptions | Clarified when asked but waited for prompts; didn't make assumptions independently | Got stuck when the problem was vague; needed extensive guidance to proceed | __ /5 |

**Total: __ / 35**

---

## You're Ready When...

- You complete the full brief (Parts 0–6) in under 40 minutes without referencing the model answers
- Your NSM directly measures the outcome you care about (not a proxy)
- You answer Curveball 2 (the conflicting metrics scenario) without overriding the guardrail with a narrative
- You self-grade ≥ 28/35 on two separate attempts

**Next lab:** [→ PM Lab 02: Metrics/NSM — YouTube Watch Time](../lab_02_metrics_nsm/workbook.md)

---

*Google PM Lab 01 · Tier 1 (Worked) · v1.0*
