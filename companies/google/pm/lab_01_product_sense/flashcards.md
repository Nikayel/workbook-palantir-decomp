# Flashcards — Google PM Lab 01: Product Sense

*10 cards for spaced repetition. Study 24–48 hours after completing the workbook.*

---

## Card 1 — Product Sense Framework

**Q:** What is the 6-step product sense framework you should use for any "improve X" question in a Google APM interview?

**A:**
1. **Clarify** — narrow the problem space: which users, what "improve" means, what business goal this serves.
2. **Segment** — pick a specific user persona with a concrete pain point. Do not say "all users."
3. **Map the journey** — trace the user's current experience step by step to find the bottleneck. Do not jump to solutions.
4. **Ideate** — generate 3+ feature ideas that specifically target the bottleneck you found.
5. **Prioritize** — score the ideas with RICE (or Impact/Effort), explicitly cut at least one, name your primary recommendation.
6. **Measure** — define an NSM that measures the outcome (not activity), a guardrail metric with a threshold, and an A/B test outline.
Never skip step 3. The bottleneck identification is where most APM candidates earn or lose points.

---

## Card 2 — NSM vs Guardrail

**Q:** What is the difference between a North Star Metric and a guardrail metric? Give one example of each for a feature improvement to Google Maps.

**A:**
- **North Star Metric (NSM):** Measures whether the feature achieved its primary goal — the outcome you care about. It should be user-facing and tied to value delivered. Example: "% of commuters who complete their habitual route without switching to another navigation app (7-day rolling average)." This measures the outcome (app retention during commute), not the activity (feature open rate).
- **Guardrail metric:** The metric that would make you KILL the launch if it moved in the wrong direction, even if the NSM looks good. It protects against unintended harm. Example: "Post-commute stress rating (1–5 survey)." If a feature that's supposed to reduce anxiety actually makes users more stressed, the guardrail catches it.
Rule: the guardrail should measure something the NSM can't — often a qualitative or safety-related dimension that the main metric could mask.

---

## Card 3 — RICE Scoring

**Q:** Explain the RICE framework in one sentence each for each component. Why do you divide by effort instead of subtracting it?

**A:**
- **Reach:** How many target users are affected per unit time? (Users affected per month, or % of your segment.)
- **Impact:** How much does this move the needle per user affected? Use a standardized scale (e.g., 0.25 = minimal, 0.5 = low, 1 = medium, 2 = high, 3 = massive).
- **Confidence:** How sure are you about your Reach and Impact estimates? (0–100% or 1–3 scale.) This is the "epistemic discount."
- **Effort:** Person-months to ship the feature end-to-end.
- **RICE = (Reach × Impact × Confidence) / Effort.**
Dividing by effort forces you to ask "is this worth it relative to the cost?" Subtracting effort would let a very high-reach feature with enormous effort still look good. Division normalizes: doubling effort cuts RICE in half, regardless of reach.

---

## Card 4 — User Segmentation Heuristic

**Q:** An APM interviewer asks "how would you improve Google Search?" You start by segmenting users. Name 3 strong segmentation axes and explain which ones you should choose from.

**A:** Strong segmentation axes for product sense questions:
1. **Use case / job-to-be-done:** "Users who are researching purchases" vs. "users doing quick fact lookups" vs. "users navigating to local businesses." Different jobs have completely different pain points.
2. **Frequency / engagement tier:** Heavy daily users vs. occasional users vs. brand-new users. A heavy user's pain is often different from a new user's pain.
3. **Platform / context:** Mobile-first users vs. desktop users; urban vs. rural; languages other than English.
Avoid segmenting by demographics alone (age, gender) unless the problem is explicitly demographic. Job-to-be-done segmentation almost always produces sharper insights. Choose the segment where the bottleneck is most acute and most addressable.

---

## Card 5 — Googleyness in Product Answers

**Q:** What does Googleyness look like concretely in a product sense interview answer? Give 3 specific behaviors.

**A:**
1. **Saying "I don't know" when you don't know, then reasoning forward.** "I don't have data on commuter app-switching rates, but I'd hypothesize it's high because of Citymapper's growth in London — and I'd validate this with a diary study before shipping." This is intellectually honest and shows you know how to test assumptions.
2. **Being open to the interviewer redirecting.** When the interviewer says "interesting — but what about drivers?", respond with "that's a good push — let me think about whether my bottleneck analysis changes for drivers." Don't defend your first answer rigidly.
3. **Making your reasoning explicit at every step.** Don't just say "I'd prioritize Feature A." Say "I'm prioritizing Feature A because it has the highest RICE and directly targets the bottleneck I found in Step 3. Feature B is a close second and I'd sequence it in v2." The reasoning is what the interviewer (and HC) are evaluating.

---

## Card 6 — A/B Test Design Essentials

**Q:** What are the 5 elements of a well-designed A/B test for a product feature? Give a concrete example for the Departure Optimizer feature.

**A:**
1. **Who is in treatment vs. control?** Be specific about the segment. "10% of daily commuters who used transit navigation ≥ 5 days in the past 30 days" — not "10% of all Maps users."
2. **What is the treatment?** The feature the treatment group sees. "Departure Optimizer panel on Maps home screen."
3. **What is the control?** What the control group sees. "Current Maps home screen with no panel." (NOT a different feature — a neutral baseline.)
4. **How long does the test run?** Long enough for users to encounter the feature multiple times and for seasonal effects to wash out. For a commute feature: at least 4 weeks (20 commuting sessions per user).
5. **What movement in the NSM declares success?** Be specific with a threshold. "No-app-switch rate improves ≥ 5 percentage points in treatment vs. control, AND guardrail metric does not decline by more than 0.2 stars."

---

## Card 7 — "Improve X" Framing

**Q:** The biggest mistake candidates make when asked to "improve X" is proposing features before finding the problem. How do you avoid this? Give the exact phrase you say out loud to buy time and signal the right behavior.

**A:** The exact phrase: "Before I propose anything, I want to make sure I understand the user and the problem clearly — can I take a few minutes to map out the current experience?" Then: "Let me pick a specific user segment [state segment], trace their current journey [step through it], and identify where the biggest bottleneck is. I'll hold off on feature ideas until I've found the bottleneck." This signals to the interviewer that you know product sense means finding the right problem, not generating solutions. Most candidates start generating solutions in the first 60 seconds. Waiting 5 minutes to do it earns disproportionate credit.

---

## Card 8 — Cutting Features Explicitly

**Q:** Why is explicitly cutting a feature (saying "I'm not choosing this one, and here's why") important in a Google APM interview?

**A:** Cutting demonstrates three things: (1) **Prioritization judgment** — you understand that resources are finite and every feature has an opportunity cost. Saying "all three are worth building" signals poor judgment. (2) **Intellectual honesty** — you're not just presenting your best ideas; you're showing you can evaluate and dismiss your own ideas. This is a Googleyness signal. (3) **Defensibility** — cutting with a reason makes your recommendation more defensible. If the interviewer asks "why not Feature B?", you already have a crisp answer. The cut must come with a reason, not just a declaration. "I'm cutting Feature B because its engineering effort is 3× higher than Feature A for similar projected impact — that's a RICE penalty I can't justify at this stage."

---

## Card 9 — Second-Order Effects

**Q:** What is a "second-order effect" in product decision-making, and why should you mention one when proposing a feature?

**A:** A second-order effect is a downstream consequence of a feature that wasn't the primary intent — often a risk or an unintended behavior that emerges after launch. Mentioning one signals systems thinking and Googleyness. Example for Departure Optimizer: "The first-order effect is reduced anxiety and fewer app switches. The second-order effect I'd watch: if users learn they can leave 10 minutes later and still arrive on time, they may shift their departure windows collectively — which could change peak demand patterns on transit in ways that undermine the accuracy of our own predictions (a feedback loop). I'd monitor departure-time distributions in the treatment group as a secondary signal." Naming a second-order effect shows you think beyond the feature's happy path.

---

## Card 10 — Interviewer-Adapting Communication Style

**Q:** In a Google APM interview, how should you adapt your communication style if the interviewer is: (a) nodding and quiet, (b) interrupting with follow-up questions, or (c) asking "can you be more specific?"

**A:**
- **(a) Nodding and quiet:** They're letting you drive. This is a trust signal — don't fill the silence with filler. Continue your structure methodically and check in every few minutes: "I'm moving to prioritization now — does that make sense before I go there?"
- **(b) Interrupting with follow-ups:** They're engaged and want to go deeper. Don't resist — follow their thread, answer the sub-question, then say "to return to where I was..." This is collaborative problem-solving, which scores Googleyness points.
- **(c) "Can you be more specific?":** You're being too abstract. Ground immediately in a concrete example: instead of "users who want faster commutes," say "specifically Priya — she leaves at 8:15am, takes the Jubilee line, and switches to Citymapper at Victoria because Maps doesn't show platform-specific delays." Specific beats abstract every time in a Google interview.

---

*10 cards · Google PM Lab 01 · Review 24–48 hrs after completing workbook*
