# Flashcards — Google PM Lab 03: Estimation

*8 cards for spaced repetition. Study 24–48 hours after completing the workbook.*

---

## Card 1 — Estimation Decomposition Pattern

**Q:** What is the standard decomposition pattern for a supply-side estimation question like "how many X happen per minute"?

**A:** Supply-side per-minute estimation = (Population × Participation rate × Activity frequency) ÷ Time unit

For YouTube uploads specifically:
```
Videos/minute = (Total active creators) × (Uploads/creator/month) ÷ (Minutes/month)
```

The key discipline is to decompose each factor into estimable pieces before putting a number to any of them. Never estimate the whole in one shot. The decomposition forces you to expose every assumption — which is exactly what the interviewer is evaluating.

**The two-track variant:** When a population has bimodal behavior (e.g., Shorts creators vs long-form creators), build two separate tracks and sum them. A single weighted average across a bimodal distribution will be systematically wrong.

---

## Card 2 — Rounding Discipline

**Q:** Why should you round aggressively in a Fermi estimation? Give an example of good vs. bad rounding.

**A:** You should round aggressively because every input to a Fermi estimation has a confidence interval of ±50-200%. Calculating to 3 decimal places implies precision you don't have — and signals to the interviewer that you don't understand the uncertainty in your own inputs.

**Bad rounding:** "20 million creators × 1.4 videos/month ÷ 43,200 minutes/month = 648.1 videos/minute."

**Good rounding:** "20 million creators × about 1.5 videos/month ÷ about 40,000 minutes/month ≈ 750. Call it 700 videos/minute to be conservative."

The good version: (a) rounds inputs to friendly numbers, (b) does easy mental math, (c) adjusts the final answer conservatively to account for overestimation bias. It also communicates confidence — "call it 700" signals that you know this is an estimate, not a calculation.

---

## Card 3 — Reference Points Every APM Should Know

**Q:** List 8 reference points an APM candidate should have memorized for estimation questions.

**A:**
1. **YouTube upload rate:** ~500 hours of video per minute; ~3,000 videos per minute at ~10 min avg length.
2. **World population:** ~8 billion.
3. **US population:** ~330 million.
4. **World internet users:** ~5 billion.
5. **US smartphone users:** ~270 million.
6. **Days in a year:** 365 (use 360 or 400 for rounding).
7. **Minutes in a month:** 30 × 24 × 60 = 43,200. Round to 40,000.
8. **Minutes in a year:** ~525,000. Round to 500,000.

Bonus for storage questions:
- 1 hour of HD video (1080p): ~1 GB
- Cloud storage cost: ~$0.02/GB/month at public rates; ~$0.005/GB/month at hyperscaler internal cost.

---

## Card 4 — Order of Magnitude Thinking

**Q:** Your estimate is 650 videos/minute and the true answer is 3,000. Are you "wrong"? How should you think about this gap in an interview?

**A:** You're not wrong in the meaningful sense. 650 vs. 3,000 is less than one order of magnitude (10×). In Fermi estimation, being within one order of magnitude (i.e., within 10×) is the success criterion, not hitting the exact number.

However, a 5× gap is worth investigating if you have time. The correct response:
"My estimate of ~650 is about 5× below the reported ~3,000. Let me identify which assumption is most likely causing this gap. The biggest assumption is active creator count — I used 20M, but YouTube has disclosed 50M+ active channels. If I triple that to 60M and also increase upload frequency to account for daily Shorts uploaders, I get: 60M × 3/month ÷ 43,200 = ~4,000. That brackets the reference figure. The main thing I missed was the Shorts format changing the upload behavior of the creator base."

The meta-point: the interviewer wants to see you reason toward the gap, not just acknowledge it.

---

## Card 5 — When Your Estimate Is Off by 10×

**Q:** Your Fermi estimate is off by 10× from the reference. What's the systematic process for finding the error?

**A:** 10× errors in Fermi estimation almost always come from ONE misestimated assumption, not from multiple small errors compounding. Find the assumption, fix it.

**Process:**
1. List all assumptions you made (this is why you state them explicitly — so you can find the error).
2. Identify the assumption with the widest confidence interval. This is usually a penetration rate or a population count.
3. Ask: "What value of this assumption would give me the reference answer?"
4. Ask: "Is that value plausible? What would I need to believe about the world for that to be true?"

**Example:** At 650 vs 3,000, the gap factor is ~5×. Active creator count was 20M. The number that closes the gap: 100M active creators. Is 100M plausible? Yes — YouTube Shorts has lowered the creation barrier dramatically. That's a plausible world. Conclusion: the Shorts cohort was the missing variable.

---

## Card 6 — Google APM Estimation Evaluation Criteria

**Q:** What specifically do Google APM interviewers evaluate in an estimation question? List 5 criteria.

**A:**
1. **Decomposition quality:** Did you break the problem into estimable sub-problems, or did you estimate the whole in one shot? Decomposition is the primary signal.
2. **Assumption transparency:** Did you state every assumption explicitly, or did you use numbers that appeared from nowhere?
3. **Rounding discipline:** Did you round appropriately and avoid false precision? Did you adjust conservatively at the end?
4. **Sense-checking:** Did you verify your answer against a reference point without being prompted? This shows calibration.
5. **Recovery behavior:** When your estimate was wrong, did you diagnose which assumption to revise and recalculate? Or did you just accept the gap?

The interviewer is NOT evaluating: whether you hit the right number, how fast you did the math, or whether you used their preferred decomposition structure.

---

## Card 7 — Stated Assumptions Beat Accurate Answers

**Q:** Why does "stated assumptions, wrong answer" score better than "right answer, no assumptions stated" in a Google APM estimation interview?

**A:** Because the interview is testing your reasoning process, not your ability to remember statistics. If you state your assumptions, the interviewer can follow your logic, challenge a specific assumption, and see how you recover. That's a conversation — which is what a PM interview is.

If you give the right answer without showing your work, the interviewer doesn't know if you:
- Remembered the answer from reading a blog post
- Got lucky with a guess
- Actually understand the structure of the problem

Stated assumptions also show intellectual honesty. "I'm assuming 5% of YouTube users have ever uploaded — I don't know this for certain but I think the vast majority of viewers are passive" is a Googleyness signal. It's the kind of rigorous, humble reasoning Google values.

**Practical tip:** Say "I'm assuming..." before every number you use in the estimation. Make it automatic.

---

## Card 8 — Storage Cost Estimation

**Q:** Estimate the cost to store 1 hour of HD video for 1 year using a first-principles approach.

**A:**
- 1 hour of 1080p HD video ≈ 1 GB (after compression; raw would be much higher)
- YouTube stores multiple quality tiers per video (144p, 360p, 720p, 1080p, 1440p, 4K, and audio-only for some users) ≈ 5-8 copies total
- Total storage per hour of original HD video: ~1 GB × 7 = ~7 GB (the higher-quality versions are larger than the 1 GB baseline, but lower-quality versions are smaller; 7 GB is a reasonable weighted total)
- Cloud storage cost (public rate): ~$0.02/GB/month = $0.24/GB/year
- Google's internal cost (they own the data centers): estimate $0.005/GB/month = $0.06/GB/year
- Cost per hour of video per year at Google internal rate: 7 GB × $0.06 = ~$0.42/year
- Over 10 years: ~$4.20 per hour of video

Cross-check: 1 minute of video at $0.07/year × 10 years = $0.70. Consistent with ~$0.20-$1.00 range discussed in cloud economics contexts.

---

*8 cards · Google PM Lab 03 · Review 24–48 hrs after completing workbook*
