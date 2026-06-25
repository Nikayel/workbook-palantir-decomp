Status: Ready — work through all parts in order

# Google PM Lab 03 — Estimation
## How Many YouTube Videos Are Uploaded Every Minute? (Tier 2)

**Tier:** 2 — blanks throughout. Work your own numbers before checking the model.

**Before you start:** Set a timer for 20 minutes. This is an estimation lab — shorter and more focused than the product sense or metrics labs. Google APM tests estimation not because the answer matters, but because the method signals structured thinking, stated assumptions, and calibrated sense-checking.

---

## Milestones

- [ ] M1 · Decomposed — broke "videos uploaded per minute" into estimable sub-problems
- [ ] M2 · Estimated — made reasonable assumptions for each sub-problem (stated out loud)
- [ ] M3 · Calculated — arrived at a final number
- [ ] M4 · Sense-checked — verified against at least one reference point
- [ ] M5 · Defended — curveballs answered
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Part 0 — Forethought

**Scenario:** Your Google APM interviewer says:

> "How many YouTube videos are uploaded every minute? You have 20 minutes. Show your work."

**The actual answer:** ~500 hours of video per minute. At an average of ~10 minutes per video, that's approximately 3,000 videos per minute. Your goal is not to hit this number exactly — your goal is to be within one order of magnitude (between 300 and 30,000) with a defensible method.

**What the interviewer is evaluating:**
1. Do you decompose before estimating (or just throw out a number)?
2. Do you state your assumptions explicitly?
3. Do you round intelligently (not calculating to 3 decimal places)?
4. Do you sense-check your answer against a reference point?
5. Can you adapt if the interviewer challenges an assumption?

**Target time:** 20 minutes total:
- 2 min — clarify and state your decomposition plan
- 10 min — work through the estimation (Parts 1–3)
- 3 min — sense-check
- 5 min — curveballs

**Confidence rating before starting (circle one):** 1 — 2 — 3 — 4 — 5

**What I want to get right this session:** [blank]

---

## Part 1 — Clarifying Questions

*Even in estimation, clarify the definition before estimating. 1-2 questions, fast.*

**Q1: "Are we estimating videos currently uploaded per minute as of today, or the upload rate growth trend?"**

*Your assumption:* [blank — state which you'll estimate and why]

**Q2: "Are we including all video lengths (10-second clips, live streams, full-length films) or just standard uploads?"**

*Your assumption:* [blank — state what you'll include and how you'll handle the mix]

*Note on clarification discipline:* In an estimation question, you have < 2 minutes for clarification. The interviewer wants you in the numbers. Don't spend 5 minutes clarifying — state an assumption and move.

---

## Part 2 — Decomposition Model

*Work through this yourself first. Fill in every blank. Then check the model at the bottom of Part 3.*

**Your decomposition path:**

```
Videos uploaded per minute
= (Total active YouTube creators) × (Upload frequency per creator per month)
  ÷ (Minutes per month)
```

**Step 1 — Total active YouTube creators:**

World internet users: ~5 billion
% who use YouTube: ~40% → [blank] billion YouTube users
% of YouTube users who have EVER uploaded a video: ~[blank]%
→ Lifetime uploaders: ~[blank] million

% of lifetime uploaders who uploaded in the last 30 days (active creators): ~[blank]%
→ Active creators: ~[blank] million

*State your assumptions for each percentage:* [blank]

**Step 2 — Upload frequency per active creator per month:**

Creator tiers (rough breakdown):
- Hobbyist (vast majority, ~90%): uploads ~[blank] video(s) per month
- Semi-pro (~9%): uploads ~[blank] videos per month
- Professional/large channels (~1%): uploads ~[blank] videos per month

Weighted average uploads per active creator per month: ~[blank]

*State your reasoning for the weighted average:* [blank]

**Step 3 — Calculate total uploads per month:**

Total active creators × Weighted average uploads/month
= [blank] million × [blank]
= [blank] million uploads per month

**Step 4 — Convert to per-minute rate:**

Minutes per month = 30 days × 24 hours × 60 minutes = [blank] minutes/month

Videos per minute = [blank] million ÷ [blank] minutes ≈ [blank] videos/minute

**Your final answer:** ~[blank] videos uploaded per minute

---

## Part 3 — Model Decomposition (Compare After Completing Part 2)

*Compare after you've filled in Part 2 yourself. The goal is to calibrate, not to memorize.*

```
STEP 1 — ACTIVE CREATORS:
World internet users: 5B
YouTube users (40%): 2B
% who ever uploaded: ~5% → 100M lifetime uploaders
% active (uploaded last 30 days): ~20% → 20M active creators

STEP 2 — UPLOAD FREQUENCY:
Hobbyist (90% of creators, 18M): 1 video/month → 18M uploads
Semi-pro (9%, 1.8M): 4 videos/month → 7.2M uploads
Pro/channels (1%, 200K): 15 videos/month → 3M uploads
Total: ~28M uploads/month
Weighted average: ~28M / 20M creators = ~1.4 videos/creator/month

STEP 3 — TOTAL:
20M creators × 1.4 videos/month = 28M uploads/month

STEP 4 — PER MINUTE:
30 × 24 × 60 = 43,200 minutes/month
28,000,000 ÷ 43,200 ≈ 648 videos/minute
```

**Model answer: ~650 videos/minute**

**Sense check:** The reported figure is ~500 hours of video per minute. At an average video length of ~10 minutes, that's 500 × 60 / 10 = 3,000 videos/minute. Our estimate of 650 is off by roughly 5×. That's less than one order of magnitude — acceptable for a Fermi estimation.

**Where the model estimate is likely off:**
- Active creator % may be higher (YouTube Shorts creators, who upload very short clips, inflate the count significantly)
- The "semi-pro" upload frequency is likely much higher for Shorts creators (who may upload daily)
- YouTube Shorts (launched 2021) now makes up a significant portion of upload volume — our model didn't separate Shorts from long-form

---

## Part 4 — Estimation Hygiene Rules

*Fill in the blanks from your own understanding. These are the disciplines that separate a strong estimation from a weak one.*

**Rule 1: Always state your assumptions.**
Why? [blank]

*What to address:* The interviewer can't evaluate your reasoning if they can't see your assumptions. "I'm assuming 5% of YouTube users have ever uploaded a video — which might seem low, but the vast majority of viewers have never created content. I'd revise this upward if we're including Shorts uploads, which have a much lower barrier." Stating assumptions also makes it easy to recover if one is challenged: "You think the active creator % is higher? Let me recalculate with 10% instead of 5% and see how that changes the output."

**Rule 2: Round aggressively — don't calculate to 3 decimal places.**
Why? [blank]

*What to address:* You're doing Fermi estimation, not financial modeling. 28 million / 43,200 ≈ 650. You do not say "648.1." You say "roughly 650, call it ~700 to be conservative." False precision signals that you don't understand the uncertainty in the estimate. Every input to a Fermi estimation has a wide confidence interval — the output precision should match.

**Rule 3: Sense-check against reference points.**
What reference points should an APM candidate have memorized? [blank]

*Key reference points for tech interviews:*
- YouTube: ~500 hours of video uploaded per minute (widely reported)
- World population: ~8 billion
- US population: ~330 million
- Internet users globally: ~5 billion
- US smartphone users: ~270 million
- Average person's lifespan: ~75 years
- Days in a year: 365 (use 400 for rounding)
- Minutes per year: ~500,000 (525,600 precise, round to 500K)

**Rule 4: If your answer is off by 10× from the reference, re-examine the biggest assumption.**
What do you do? [blank]

*What to address:* Don't just shrug. Say: "My estimate was 650 videos/minute, the reference is ~3,000. That's a 5× gap. Let me revisit my biggest assumption — active creator count. If I increase active creators from 20M to 100M (accounting for Shorts creators, which I omitted), the estimate becomes 3,000/minute. That's actually a better fit, and it makes sense: YouTube Shorts launched in 2021 and dramatically lowered the barrier to upload, likely 5× the pre-Shorts creator count." This is what the interviewer wants to see — not the right answer, but the right process when you're wrong.

---

## Part 5 — System Reasoning

*These are the follow-up questions the interviewer would ask.*

**Q1: What's the biggest source of uncertainty in your estimate?**

[blank — your answer]

*What to address:* The biggest uncertainty is the treatment of YouTube Shorts. Short-form creators who upload daily Shorts are a completely different behavior pattern from long-form creators who upload weekly. Our model assumed a single "creator" category with a weighted average. In reality, the bimodal distribution (Shorts creators vs long-form creators) means a weighted average understates the upload volume. In a real estimation, you'd build a two-track model: one for Shorts, one for long-form.

**Q2: Does "videos per minute" tell you anything useful about YouTube's business?**

[blank — your answer]

*What to address:* Not directly — it's a supply-side metric. What matters for the business is: (a) how much of the supply gets watched (content utilization rate), (b) how much of the watched content is monetizable (monetized Watch Time), and (c) whether the supply is growing fast enough relative to demand. A platform drowning in unmonetizable content (spam, low-quality Shorts) could have a very high upload rate but a declining business.

---

## Part 6 — Interview Simulation (Curveballs)

### Curveball 1

**Interviewer:** "Now estimate the total storage YouTube uses for all videos ever uploaded."

**Your answer:** [blank — work through it using the same decomposition discipline]

*Approach:*
1. Total videos ever uploaded: YouTube launched in 2005. At an average historical rate of ~300 videos/minute (lower in early years, higher now), over ~20 years: 300 × 43,200 min/month × 12 months × 20 years = ~3 billion videos. (Round to 3B.)
2. Average video length: mix of long-form (15 min) and Shorts (30 sec). Weighted average: ~5 minutes per video across all time.
3. Storage per minute of video: HD video at 1080p ≈ 1 GB/hour ≈ 17 MB/minute. SD archival ≈ 5 MB/minute. With multiple quality tiers (144p through 4K), YouTube stores ~8 copies of each video. Total: ~50 MB/minute of original video × 8 versions = ~400 MB per minute of video.
4. Total storage: 3B videos × 5 min × 400 MB/min ÷ 1,000 (MB to GB) ÷ 1,000 (GB to TB) = 6,000 Exabytes? That seems too high. Re-check: 3B × 5 min = 15B minutes × 400 MB = 6 × 10^15 MB = 6 × 10^9 GB = 6 exabytes. That's more plausible. (Reported estimates: YouTube ~1 exabyte. Our estimate is off by 6×. Where? Likely multiple compression generations and lower average quality than assumed.)

---

### Curveball 2

**Interviewer:** "What if I told you the real answer is 500 hours per minute — roughly 3,000 videos per minute. Where was your estimate off?"

**Your answer:** [blank]

*What to address:*
- "My estimate of 650 videos/minute is about 5× below the reported figure. The most likely source of error is my active creator count. I estimated 20M active creators, but YouTube has disclosed ~50M active channels and the Shorts format dramatically lowered the upload barrier. If I revise to 100M active creators — including all Shorts creators — and use a higher average upload frequency (3 videos/month, accounting for daily Shorts uploaders), I get: 100M × 3 / 43,200 = ~7,000 videos/min. That overshoots slightly — but splitting the difference suggests my creator count was the key variable. I'd also note that my model excluded spam and automated uploads, which likely contribute several hundred videos per minute."

---

### Curveball 3

**Interviewer:** "Estimate how much it costs Google to store 1 minute of YouTube video for 10 years."

**Your answer:** [blank]

*Approach:*
- Cost to store 1 GB for 1 year in cloud storage: ~$0.02/GB/month × 12 = ~$0.24/GB/year. Google's actual cost is lower (they own the infrastructure), estimate $0.05/GB/year internally.
- 1 minute of video stored in 8 quality tiers: ~400 MB = 0.4 GB
- Cost per year: 0.4 GB × $0.05 = $0.02/year
- Cost for 10 years: $0.20
- So it costs Google approximately 20 cents to store 1 minute of video for 10 years. (This is consistent with publicly discussed storage economics — cloud storage is very cheap at scale.)

---

## Part 7 — PM Rubric

*Self-grade after completing the lab. Score as a Google APM interviewer would.*

| Dimension | 5 — Strong | 3 — Adequate | 1 — Weak | Your Score |
|---|---|---|---|---|
| Structure | Decomposed into estimable sub-problems before estimating; used a logical path (creators × frequency ÷ time) | Decomposed partially; some sub-problems estimated, some guessed | Gave one number with no decomposition | __ /5 |
| User empathy | Recognized different creator tiers (hobbyist vs pro) have wildly different upload frequencies; didn't treat all creators as identical | Named creator tiers but used a single average without weighting | Didn't distinguish creator types | __ /5 |
| Prioritization | Identified the biggest source of uncertainty (Shorts creators) and addressed it proactively | Named uncertainty but didn't revise the estimate | Didn't acknowledge uncertainty | __ /5 |
| Metrics literacy — Estimation rigor | Stated all assumptions explicitly; rounded intelligently; sense-checked against reference point; recovered from 5× gap by identifying the assumption to revise | Stated most assumptions; sense-checked but didn't recover when off | Gave a number, no assumptions stated, no sense-check | __ /5 |
| Communication | Narrated reasoning step by step; clear what each number represents; said "call it ~700" not "648.14" | Communicated adequately but occasionally lost the thread | Interviewer couldn't follow the reasoning | __ /5 |
| Creativity | Named Shorts as a structural change that inflates upload volume; recognized spam/automated uploads as a category | Named Shorts or automated uploads but didn't quantify | No awareness of non-standard upload patterns | __ /5 |
| Handling ambiguity | Clarified definitions in < 2 minutes and moved immediately to estimation; didn't wait for perfect information | Clarified but took too long; or didn't clarify and made an error because of it | Got stuck on what "video" means and couldn't start | __ /5 |

**Total: __ / 35**

---

## Reflection

**What was your final estimate and how far off was it from the ~3,000 videos/minute reference?** [blank]

**Which assumption drove the biggest gap?** [blank]

**How quickly did you move from clarifying questions to decomposition?** [blank]

---

## You're Ready When...

- You complete the full estimation (Parts 0–4) in under 15 minutes without model answers
- You state every assumption out loud before using the number
- You sense-check your answer against the reference point unprompted
- When you find your estimate is 5× off, you immediately identify which assumption to revise (not just acknowledge the gap)
- You self-grade ≥ 28/35 on two separate attempts

**Next labs:** See Google TPM or Meta PM tracks for continued prep.

---

*Google PM Lab 03 · Tier 2 · v1.0*
