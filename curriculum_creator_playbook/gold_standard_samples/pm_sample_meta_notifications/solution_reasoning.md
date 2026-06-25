# Solution Reasoning — Rank the Notifications Feed

> 🔒 Open only after you attempt the workbook.

## 0. Clarifying-questions answer key
- **Goal** — protect long-term retention by stopping opt-outs; *not* maximizing raw CTR (which can backfire).
- **Users** — heavy users drowning in low-value notifications are the bleeding segment.
- **Data** — per-notification type, sender-affinity, relevance prediction.
- **Constraints** — safety/security notifications bypass ranking and always deliver.
- **Scale** — start rules/ranking + bundling before heavy ML; billions of users, many locales.

## 1. Why this design
- **Reframe the problem:** it's not "too many notifications," it's "too few *valuable* ones." Optimizing value-per-notification (not volume, not CTR) is the insight that separates a strong answer.
- **Segment first:** heavy users opting out is the near-irreversible leak; fix them first.
- **MVP = relevance ranking + bundling** of low-value types, with a **bypass list** for safety. Cheap, shippable, reversible.
- **North Star = meaningful notification-driven sessions per WAU**, with **opt-out rate as a hard guardrail** and a **counter-metric** for over-bundling hiding important items.

## 2. The explicit cut (the thing weak answers skip)
Build **ranking + bundling** first; do **NOT** build granular per-type controls or full ML ranking yet — they're higher effort and the bundling+ranking MVP captures most of the value while we learn. Naming what you *won't* build is half the score.

## 3. Failure modes
- **Relevance model wrong** → important items buried. *Mitigation:* the safety bypass list + the opt-out guardrail + a "see all / recent" escape hatch.
- **Over-bundling** hides time-sensitive items. *Mitigation:* counter-metric + don't bundle high-affinity senders.
- **CTR goes up, opt-outs go up** → you optimized the wrong thing. *Mitigation:* opt-out is a guardrail that can *block* launch even if CTR rises.

## 4. Model 90-second talk track
"The real problem isn't volume, it's value — heavy users get 40 notifications and the one that matters is buried, so they turn notifications off, which is nearly irreversible. I'd rank by predicted relevance and bundle low-value types, while letting safety notifications bypass ranking. I'd steer by meaningful notification-driven sessions per weekly user, with opt-out rate as a hard guardrail so we don't trade long-term trust for short-term clicks. I'd ship behind an A/B test and only launch if the North Star rises with opt-outs flat or down."

## 5. Strong vs weak answer
- **Weak:** "Add an AI feed that shows the most-clicked notifications first, and measure CTR." *Why it's weak:* optimizes **CTR** (a vanity metric that rises even as users get annoyed and opt out), no segment, no explicit cut, no guardrail, and jumps to "AI" without naming the user pain. It also can't say what it would *not* build.
- **Strong:** the reference — reframes to value-per-notification, picks the bleeding segment, makes an explicit RICE cut, chooses a North Star **with a guardrail that can veto launch**, and designs the A/B test. *Why it's strong:* it's user-first, prioritized, and metrically honest — exactly Meta's product-sense + execution bar.

## 6. Curveball model responses
- **CTR up but opt-outs up → ship?** No. Opt-out is the guardrail; a rise means we're extracting short-term clicks at the cost of long-term retention. Hold and investigate which notification types drive the opt-outs.
- **ML is a quarter away → ship next week?** A rules-based MVP: bundle the obvious low-value types and cap their frequency; that captures much of the value with no model. Learn, then invest in ML.
- **Evaluate an AI "summary of your day" →** define the user value first (does it reduce opens of low-value items?), then a guardrail (it must not *replace* a time-sensitive notification), then an A/B with the same North Star. Don't ship because it's "AI"; ship because it moves the metric without hurting the guardrail.

## 7. Rubric exemplars
- **Weak (1–2):** optimizes CTR; no segment; "add AI"; no cut; no guardrail.
- **Adequate (3):** picks a segment, ranks notifications, names a metric, but no guardrail and a soft cut.
- **Strong (5):** reframes to value-per-notification, explicit RICE cut, North Star **+ guardrail that can block launch**, clean A/B, articulates the relevance-model risk.

## 8. Key takeaways / reusable primitives
- **Optimize the right metric:** CTR is a vanity metric; pair any engagement metric with a **guardrail** (here, opt-out rate) that can veto a launch.
- **Always make an explicit cut** — name what you won't build and why.
- **Reframe volume problems as value problems.**
- **Start rules, earn ML.** A rules MVP de-risks the model investment.

## 9. Sources
Meta's Product Sense + data-driven Execution pillars, "build for billions," and metric-guardrail discipline per `company_packs/meta.md` and `04_role_guide_pm.md`. Last verified: 2026 summer.
