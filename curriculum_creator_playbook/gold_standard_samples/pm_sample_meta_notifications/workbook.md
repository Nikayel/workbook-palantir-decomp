Status: Spec incomplete — fill in all blank fields before writing the brief

# Scenario
Meta's **notifications** have become noisy. A heavy user can get 40+ notifications a day across Facebook, Instagram, and Threads — birthdays, "people you may know," group activity, reactions. Engagement with notifications is falling and some users are turning them **off entirely**, which is a long-term threat (a user with notifications off is much harder to bring back). You're the PM. **What would you build to make the notifications feed valuable again — for billions of users?** Then prove it with a metric and an experiment.

> Deliverable is a **brief + metric tree + A/B design**, not code. You're scored on structure, user empathy, prioritization, metrics literacy, and communication.

## 🪜 Milestones — check them off as you go
This track ships a **brief + metric tree + A/B design, not code** — so M4 is "artifact complete & self-checked against the model."
- [ ] M1 · Scoped — clarifying questions + assumptions written
- [ ] M2 · Segmented — the bleeding user segment + the bottleneck named
- [ ] M3 · Designed — a prioritized cut + a North Star **and a guardrail**
- [ ] M4 · Built — `artifacts/metric_tree_and_brief.md` filled **and** the A/B design written
- [ ] M5 · Defended — survived all 3 curveballs out loud
- [ ] M6 · Ready — self-graded ≥ 28/35

# Part 0: Forethought
Goal (one sentence): Make notifications feel worth keeping on — raise value per notification, not volume.
Target time: 70 minutes
Confidence before starting (1–5): [blank]

# Part 1: Clarifying questions
Goal:
> Are we optimizing engagement, retention, or notification opt-in rate?
Question: [blank]
Assumption: I'll assume the real goal is **protecting long-term retention** by stopping opt-outs — not maximizing clicks (which can backfire).

Users:
> Which surface and which segment hurts most — heavy users drowning, or light users who get too little?
Question: [blank]
Assumption: I'll assume **heavy users drowning in low-value notifications** are the bleeding segment.

Data:
> What signals do we have per notification (type, predicted relevance, recency, sender affinity)?
Question: [blank]
Assumption: I'll assume we have per-notification **type, sender-affinity, and a relevance prediction**.

Constraints:
> Any rule we can't break (e.g., security/safety notifications must always go through)?
Question: [blank]
Assumption: I'll assume **safety/security notifications bypass ranking** and always deliver.

Scale:
> Billions of users, many locales — does the solution need to be ML-ranked vs rules?
Question: [blank]
Assumption: I'll assume we start with a **simple ranked+bundled** approach before heavy ML.

# Part 2: Decomposition (segment & map)
Primary segment + their job-to-be-done:
*(Worked example:)* Heavy users want to **not miss the few things they care about** without scrolling 40 items.

Current workflow:
1. Every event emits a notification.
2. They're shown reverse-chronologically.
3. The signal (a close friend's reply) is buried under noise (a stranger's group post).

Bottleneck:
1. [blank — reverse-chron ordering with no relevance ranking or bundling]

Core entities:
1. Notification
2. User
3. Signal (relevance/affinity/recency features)

> 🚩 Checkpoint M2 · Segmented — you should now have **heavy users opting out** as the bleeding segment and **reverse-chron ordering with no relevance ranking** as the bottleneck. Stuck? Ask which segment's behaviour is the hardest to reverse.

# Part 3: Product design + success metric
## Pains (name 2–3 real ones for the segment)
1. [blank]
2. [blank]

## Solution set (ideate, then CUT)
| Idea | What it does | Reach | Impact | Confidence | Effort | RICE-ish call |
|---|---|---|---|---|---|---|
| Rank by relevance | order by predicted value, not time | high | high | med | med | [blank] |
| Bundle low-value types | "5 people reacted…" digest | high | med | high | low | [blank] |
| Smart frequency cap | cap low-value/day | high | med | med | low | [blank] |
| Per-type controls | granular opt-in UI | med | med | high | med | [blank] |

**The explicit cut (required):** I would build [blank] first and intentionally NOT build [blank] yet, because [blank].

## Success metric
North Star: [blank — e.g. "7-day notification-driven *meaningful* sessions per user," not raw CTR]
Guardrail(s): [blank — e.g. notification opt-out rate must not rise; total sends must not balloon]
Counter-metric to watch: [blank — gaming/over-bundling hiding important items]

> 🚩 Checkpoint M3 · Designed — you've made an **explicit cut** (built X first, NOT Y) and chosen a **North Star + a guardrail that can veto launch**. Stuck? If your metric is raw CTR, redo it — CTR rises even as users opt out.

# Part 4: Produce the artifacts
1. Fill `artifacts/metric_tree_and_brief.md` (the metric tree + a ≤200-word brief).
2. **A/B test design** here:
> Hypothesis: [blank]
> Unit of randomization: [blank — user]
> Primary metric + guardrails: [blank]
> Minimum run / what would make you ship or kill: [blank]

# Part 5: Reasoning write-up
Why this segment first? [blank]
Why this North Star instead of raw CTR? [blank]
Why is bundling+ranking the right MVP? [blank]
What would you NOT build first? [blank]
What breaks if the relevance model is wrong? [blank]
What's the riskiest assumption? [blank]

# Part 6: Interview simulation
## 90-second talk track
"The real problem isn't too many notifications, it's too few *valuable* ones, so I'd optimize value-per-notification for heavy users… [blank]"

## Curveballs (answer out loud)
Curveball 1: Ranking lifts CTR but opt-outs also rise. Ship it?
Your response: [blank]

Curveball 2: Engineering says true ML ranking is a quarter away. What ships next week?
Your response: [blank]

Curveball 3: Leadership wants to add an AI "summary of your day" notification. How would you evaluate it?
Your response: [blank]

# Part 7: Self-grade + reflection
Score 1–5 (PM rubric from `rubric_bank.md`).

Structure: __/5
User empathy: __/5
Prioritization: __/5
Metrics literacy: __/5
Communication: __/5
Creativity: __/5
Handling ambiguity: __/5

Total: __ / 35

One thing I did well: [blank]
One thing I missed: [blank]
Confidence now (1–5): [blank]   ← compare to your Part 0 prediction.
Lowest rubric row → my next action: [blank]

## ✅ You're ready when…
- [ ] You go prompt → a prioritized solution + metric in **< 25 min** without the hints.
- [ ] You give the 90-second talk track out loud without notes.
- [ ] You answer all 3 curveballs without freezing — especially "CTR up, opt-outs up: ship?"
- [ ] You self-grade ≥ 28/35 on **two** attempts running.
> Any unchecked box is your next rep. Re-run cold and timed until all four are checked.
