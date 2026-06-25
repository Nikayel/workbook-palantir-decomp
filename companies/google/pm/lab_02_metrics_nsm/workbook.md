Status: Ready — work through all parts in order

# Google PM Lab 02 — Metrics / North Star Metric
## YouTube Watch Time Drop (-15%) — Diagnosis (Tier 2)

**Tier:** 2 — blanks throughout, model answers locked. Work through every part before comparing.

**Before you start:** Set a timer for 45 minutes. This lab simulates the Google APM metrics round — the second pillar alongside Product Sense. You will NOT write code. Your artifact is a diagnosis memo and an investigation plan.

---

## Milestones

- [ ] M1 · Framed — segmented the drop before hypothesizing (geography? device? content type? user cohort?)
- [ ] M2 · Hypothesized — named 3 buckets: supply (content), demand (users), platform (bugs/UX)
- [ ] M3 · Metrics mapped — named the metric tree under Watch Time
- [ ] M4 · Root-caused — narrowed to most likely cause with reasoning
- [ ] M5 · Defended — curveballs answered
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Part 0 — Forethought

**Scenario:** Your Google APM interviewer says:

> "YouTube is seeing a 15% drop in Watch Time over the last quarter. Walk me through how you'd diagnose this and what you'd do about it."

**What makes this hard:** A 15% drop in Watch Time is a board-level number. If you jump straight to hypotheses ("maybe users switched to TikTok"), you'll get cut off. Google APM interviewers want to see that you segment first, hypothesize second, and diagnose third. Most candidates fail by skipping the segmentation step entirely.

**Target time:** 45 minutes. Suggested breakdown:
- 3 min — clarifying questions
- 7 min — metric tree decomposition
- 10 min — hypothesis tree
- 10 min — investigation plan
- 8 min — reasoning write-up
- 7 min — curveballs

**Confidence rating before starting (circle one):** 1 — 2 — 3 — 4 — 5

**What I want to get right this session:** [blank]

---

## Part 1 — Clarifying Questions

*Before diagnosing anything, clarify the shape of the problem. These questions are what separate a PM who can navigate ambiguity from one who can't.*

**Q1 (Goal): "Is Watch Time the North Star Metric here, or is it a proxy for something else — like Revenue, user satisfaction, or creator health?"**

Rationale: Watch Time is a leading indicator. If the NSM is Revenue and Watch Time is down 15% but Revenue is flat, the diagnosis changes completely. If the NSM is creator health and Watch Time is down but creator uploads are up, then users are failing to discover content — a different problem than creator churn.

*Write your assumption:* [blank]

**Q2 (Users): "Is this Watch Time across all users, or is it segmented? Specifically — are new user cohorts and retained user cohorts both down, or is the drop concentrated?"**

Rationale: New user Watch Time dropping means onboarding or content recommendation for new users is broken. Retained user Watch Time dropping means the platform has failed existing users — a stickiness problem.

*Write your assumption:* [blank]

**Q3 (Data): "Are we looking at total Watch Time, per-user Watch Time, or per-session Watch Time? And how was it measured — in-app signals or server-side?"**

Rationale: These are different numbers with different causes. Total Watch Time can drop if DAU dropped. Per-session Watch Time dropping means each session is shorter — a different root cause. Measurement discrepancy (in-app vs server) can itself explain a reported drop.

*Write your assumption:* [blank]

**Q4 (Constraints): "Is this a sudden drop (an event happened — a bug, a policy change, a competitor launch) or a gradual decline that's been trending for quarters?"**

Rationale: Sudden drops are almost always incidents — a bug, an algorithm change, a bad policy rollout. Gradual declines are structural — behavior shifts, competitor growth, content quality erosion.

*Write your assumption:* [blank]

**Q5 (Scale): "Is this global, or concentrated in specific regions or markets?"**

Rationale: A drop in India (YouTube's largest market by users) is a different problem from a drop in the US (YouTube's largest market by revenue). Regional drops often have local causes (data cost, local competitor, mobile data policy change).

*Write your assumption:* [blank]

**Checkpoint M1:** Check the box above once you've answered all 5 questions with your own assumptions, BEFORE moving to the metric tree.

---

## Part 2 — Metric Tree Decomposition

*Decompose Watch Time into estimable sub-metrics. The goal is to find which branch of the tree explains the 15% drop. Do this before hypothesizing causes — the data tells you where to look.*

**Watch Time = [fill in the first decomposition]**

```
Watch Time (total)
= Sessions per day × Watch Time per session

Sessions per day
= DAU × Sessions per user per day

Watch Time per session
= Avg videos watched per session × Avg watch duration per video
```

**Fill in: Which branch would you investigate first, and why?**

Branch 1: Sessions per day [blank — higher DAU means more Watch Time potential; if DAU is flat and Watch Time is down, the problem is in session depth]

Branch 2: Watch Time per session [blank — if users are opening YouTube but watching less per session, something in the content or UX is cutting sessions short]

**Your answer — which branch first and why:** [blank]

*Key principle: Never hypothesize before you've segmented the metric tree. Segmentation narrows your search space from "anything" to "this branch." You go from 15% drop to "the drop is entirely in Watch Time per session, not in session count" — which eliminates half your hypothesis tree immediately.*

**Checkpoint M2:** Check the box once you've completed the metric tree and named which branch you'd investigate first.

---

## Part 3 — Hypothesis Tree

*Now hypothesize. Three buckets: supply (content quality), demand (user behavior), platform (technical/UX). Every hypothesis gets a metric that could confirm or deny it.*

```
Watch Time drop (−15%)
├── Supply: less or worse content available
│   ├── Creator churn
│   │   Metric: creator uploads per week, 12-week trend
│   │   Confirms if: uploads down ≥ 10% in same period
│   ├── Content quality degradation
│   │   Metric: avg video completion rate (played to > 80%)
│   │   Confirms if: completion rate down quarter-over-quarter
│   └── Algorithm deprioritized high-engagement content types
│       Metric: impressions and Watch Time by content category (gaming, vlogs, tutorials, news)
│       Confirms if: one category's impressions collapsed with a timestamp matching the drop
│
├── Demand: fewer or less engaged users
│   ├── Seasonal effect
│   │   Metric: year-over-year Watch Time for the same quarter
│   │   Confirms if: same quarter last year also showed a dip (summer slump, etc.)
│   ├── Competitor pull (TikTok, Reels, Shorts)
│   │   Metric: cross-app usage panel data (if available); alternatively, survey data on self-reported app switching
│   │   Confirms if: cohorts who joined post-2022 (peak TikTok growth) show higher Watch Time decline
│   └── New user cohort behavior shift
│       Metric: Watch Time segmented by user account creation date
│       Confirms if: users who joined in the last 12 months watch significantly less than users who joined 3 years ago at the same tenure point
│
└── Platform: bugs, UX changes, or infrastructure issues
    ├── Video load time increased
    │   Metric: p50 and p95 video start time, error rate
    │   Confirms if: start time increased ≥ 200ms in the same period
    ├── Autoplay broken or suppressed
    │   Metric: % of sessions where autoplay triggered the next video
    │   Confirms if: autoplay trigger rate dropped in the same quarter
    └── [blank — name a third platform hypothesis]
        Metric: [blank]
        Confirms if: [blank]
```

**Most likely hypothesis (your pick after reviewing the tree):** [blank]

**Reasoning:** [blank — why do you rank this one highest? What would the data show to confirm it?]

**Checkpoint M3:** Check the box once you've completed the full hypothesis tree including your third platform hypothesis and your most-likely pick.

---

## Part 4 — Investigation Plan

*Write this as a 3-step plan you'd share with your data scientist. Be specific enough that they could actually execute it.*

**Step 1 — Pull the segmented data:**

"First, I want a breakdown of Watch Time by [blank] — I need to know whether the drop is uniform across all segments or concentrated. Specifically, pull: Watch Time by [geography / device / user tenure / content type / new vs. retained user]. If the drop is uniform, that suggests a platform-wide issue. If it's concentrated in one segment, that tells us where to look."

*Your answer — what specific data cut do you pull first:* [blank]

**Step 2 — Segment and isolate:**

"Once I have the first cut, I'll apply a second segmentation: [blank]. I want to cross-tabulate the segment where the drop is largest with the timeline to find a change point — did the drop start suddenly (a date) or gradually (a trend)? A sudden change point usually maps to an event: an algorithm change, a bug deploy, a policy enforcement date."

*Your answer — what second segmentation and why:* [blank]

**Step 3 — A/B test or holdback if the cause is confirmed:**

"If we confirm the root cause is [blank], the next step is [blank]. Specifically: [design a concrete test or holdback — not vague 'test and learn']. We'd measure: [specific metric movement required to confirm the fix works]."

*Your answer — specific test design based on your most-likely hypothesis:* [blank]

**Checkpoint M4:** Check the box once you've written all three investigation steps in your own words.

---

## Part 5 — System Reasoning

*These are the follow-up questions the interviewer would ask a strong APM candidate.*

**Q1: Why segment before hypothesizing? What's the failure mode if you skip it?**

[blank — your answer]

*What to address:* If you hypothesize before segmenting, you anchor too early. You might spend 20 minutes investigating a competitor thesis ("TikTok took our users") only to find that the drop is entirely from mobile web users in a country where TikTok isn't available — making your hypothesis irrelevant. Segmentation first narrows the search space and prevents anchoring bias.

**Q2: Watch Time is a lagging indicator. What leading indicators would you monitor to catch this earlier next time?**

[blank — your answer]

*What to address:* Leading indicators of Watch Time decline include: video completion rate (early signal of content quality drop), autoplay trigger rate (early signal of session depth), weekly active creators (early signal of supply), new user 7-day Watch Time (early signal of onboarding quality). If you had dashboards on these, a 15% Watch Time drop wouldn't be a surprise — you'd have seen the leading indicators move 4-6 weeks earlier.

**Q3: How do you avoid a "correlation is causation" mistake in this diagnosis?**

[blank — your answer]

*What to address:* A common mistake: TikTok launched a new feature the same week Watch Time dropped, so "TikTok caused our Watch Time drop." This is correlation, not causation. To confirm causation you need: (a) a holdback group that was NOT exposed to the hypothesized cause, OR (b) a natural experiment (the feature was rolled out in some geographies but not others). Correlation narrows suspects; holdbacks and natural experiments confirm.

---

## Part 6 — Interview Simulation (Curveballs)

### Curveball 1

**Interviewer:** "Watch Time is down 15% but Revenue is up 3% in the same quarter. Does your diagnosis change?"

**Your answer:** [blank]

*Things to address:*
- If Revenue is up while Watch Time is down, it means YouTube is monetizing each unit of Watch Time more efficiently — higher ad loads per video, better targeting, higher CPM content performing better.
- Diagnosis implication: this changes the severity assessment. If the business goal is Revenue, a 15% Watch Time drop with a 3% Revenue increase might actually be acceptable (trading low-monetization Watch Time for high-monetization Watch Time).
- However, Watch Time is still a leading indicator of long-term platform health. Declining Watch Time that hasn't yet affected Revenue is a warning signal, not a green light. The question becomes: is this a healthy mix shift, or an early sign of structural engagement erosion that will eventually hit Revenue?
- What you'd investigate: breakdown of Revenue by CPM category. If high-CPM content (brand-safe, established creators) Watch Time is holding and low-CPM content (long-tail, user-generated) is down — that's a healthy mix shift. If all categories are down, Revenue is borrowing against future engagement.

---

### Curveball 2

**Interviewer:** "Your data shows the entire 15% drop is from mobile web users — not the app. What does that tell you?"

**Your answer:** [blank]

*Things to address:*
- Mobile web YouTube is a different product surface from the app. Users on mobile web are often: (1) users who were sent a link and watched without opening the app, or (2) users in markets where data is expensive (mobile web uses less data), or (3) users who never downloaded the app.
- A mobile web-specific drop narrows the root cause dramatically: it eliminates creator churn, content quality, and competitor behavior as primary causes (those would affect app users too). What's left: a platform/UX issue specific to mobile web (e.g., a JS change that broke autoplay on mobile Safari), a policy change that affected mobile web differently (GDPR cookie consent popups reducing Watch Time in Europe), or a test that inadvertently went to mobile web users only.
- Action: pull mobile web session logs from the quarter and look for any deploy that coincides with the drop start date.

---

### Curveball 3

**Interviewer:** "A PM from another team says their feature launch 3 months ago might have caused this drop. How do you evaluate that claim?"

**Your answer:** [blank]

*Things to address:*
- This is the "attribution dispute" scenario — common in large organizations. Don't dismiss it (that's politics), and don't accept it uncritically (that's lazy).
- Framework: (1) Timeline check — does the Watch Time drop start on or after the feature launch date, or before? If before, the feature can't be the primary cause. (2) Holdout check — did the feature launch to all users, or was there a staged rollout? If staged, compare Watch Time in the holdout group (didn't get the feature) vs. the treatment group (got the feature). (3) Mechanism check — what's the plausible causal chain? How would THIS feature reduce Watch Time? "We added a feedback button and users now have a way to skip content they don't like" is plausible. "We changed the settings menu layout" is not plausible.
- What you'd say: "Let's pull the holdout data from your launch. If Watch Time in the holdout group is flat while the treatment group is down, that's strong evidence your feature is contributing. If both groups are down equally, your feature isn't the cause — something else is."

---

## Part 7 — PM Rubric

*Self-grade after completing the lab. Score as a Google APM interviewer would.*

| Dimension | 5 — Strong | 3 — Adequate | 1 — Weak | Your Score |
|---|---|---|---|---|
| Structure | Segmented before hypothesizing; used the metric tree to narrow the search space; moved from data to hypothesis to investigation plan in order | Followed the framework mostly but jumped to hypotheses before fully segmenting | Jumped to "TikTok stole our users" without any data pull or segmentation | __ /5 |
| User empathy | Recognized that different user cohorts (new vs. retained) have different Watch Time drivers; didn't treat "YouTube users" as monolithic | Named user segments but didn't analyze them differently | No user segmentation; treated all users the same | __ /5 |
| Prioritization | Named 3 buckets (supply/demand/platform), ranked hypotheses with explicit reasoning, identified most-likely cause before going to investigation | Named hypotheses but didn't rank them; or ranked without reasoning | Listed every possible cause without any prioritization | __ /5 |
| Metrics literacy | Decomposed Watch Time into a metric tree; named leading indicators that would catch this drop earlier; distinguished correlation from causation in investigation plan | Named the metric tree but didn't use it to narrow hypotheses; or confused correlation with causation | Named "Watch Time" as the metric to track Watch Time drop (circular) | __ /5 |
| Communication | Articulated each step of the diagnosis process clearly; could explain the plan to a non-technical stakeholder | Communicated adequately but occasionally over-indexed on jargon | Diagnosis was unclear or incomplete; interviewer would not be able to follow the reasoning | __ /5 |
| Creativity | Named a non-obvious root cause (e.g., measurement discrepancy, autoplay rate, mobile web-specific bug) alongside the obvious ones | Named only obvious hypotheses (TikTok, content quality) | Named one hypothesis and didn't explore further | __ /5 |
| Handling ambiguity | Clarified the shape of the drop (which metric definition, which segment, sudden vs gradual) before diving in; made explicit assumptions; moved forward without waiting to be prompted | Clarified when asked but needed the interviewer to prompt for segmentation | Got stuck or didn't clarify; dove into the wrong problem | __ /5 |

**Total: __ / 35**

---

## Reflection

**What part of the diagnosis did you do well?** [blank]

**Where did you anchor too early or skip segmentation?** [blank]

**Which curveball was hardest and why?** [blank]

---

## You're Ready When...

- You complete the full diagnosis (Parts 0–6) in under 40 minutes without model answers
- You segment the metric tree before naming any hypothesis
- You answer Curveball 1 (Revenue up while Watch Time down) without getting confused about what the business goal actually is
- You correctly explain the holdout group approach in Curveball 3
- You self-grade ≥ 28/35 on two separate attempts

**Next lab:** [→ PM Lab 03: Estimation — YouTube Videos Uploaded Per Minute](../lab_03_estimation/workbook.md)

---

*Google PM Lab 02 · Tier 2 · v1.0*
