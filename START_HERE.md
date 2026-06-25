# Interview Prep Workbook — Start Here

## What is this?

A structured, company-specific interview prep system for software engineering, PM, and technical PM roles at 10 top tech companies. Each workbook is a self-contained interactive exercise you fill in, code, and grade yourself — simulating a real interview from first principles.

This is not a passive resource. You do not read it — you work it. Every lab has a scenario, a structured problem, fill-in blanks, code cells, and a self-graded rubric. The goal is deliberate practice: same kind of muscle-building repetition that separates candidates who "studied" from candidates who are ready.

---

## Pick Your Company

| Company | Roles | Labs | Entry Point |
|---|---|---|---|
| Palantir | SWE / FDSE | 8 labs | [→ Start](companies/palantir/START_HERE.md) |
| Google | SWE · PM · TPM | 9 labs | [→ Start](companies/google/START_HERE.md) |
| Meta | SWE · PM | 8 labs | [→ Start](companies/meta/START_HERE.md) |
| Amazon | SWE · PM · TPM | 9 labs | [→ Start](companies/amazon/START_HERE.md) |
| Microsoft | SWE · PM · TPM | 9 labs | [→ Start](companies/microsoft/START_HERE.md) |
| Stripe | SWE · PM · TPM | 7 labs | [→ Start](companies/stripe/START_HERE.md) |
| Uber | SWE · PM · TPM | 9 labs | [→ Start](companies/uber/START_HERE.md) |
| Atlassian | SWE · PM · TPM | 9 labs | [→ Start](companies/atlassian/START_HERE.md) |
| Apple | SWE · PM · EPM | 8 labs | [→ Start](companies/apple/START_HERE.md) |
| Nvidia | SWE · TPM | 6 labs | [→ Start](companies/nvidia/START_HERE.md) |

---

## Recommended Path If You're New Here

If you've never used this system before, follow this sequence:

1. **Start with Palantir Lab 01 (911 Dispatch).** It's the most fully scaffolded lab in the system — Tier 1 worked, every blank pre-filled, every choice explained. Read it like a worked example first, then blank it and redo it from memory.
2. **Do Labs 01–03 of your primary target company.** Once you've seen the format once, apply it to the company you're actually interviewing at.
3. **Attempt a Tier 3 mock before your interview.** The blank mock (Lab 03 of each SWE track, or the last PM lab) is the real test. If you can finish cold, in under 60 minutes, without opening the worked labs — you're ready.

If you have a specific company interview coming up in less than a week, skip step 1 and go directly to that company's entry point. All entry points include a "Before You Start" checklist.

---

## How Each Workbook Works

Every lab (workbook.md) is divided into 7 parts that mirror the structure of a real interview:

| Part | Name | What It Is |
|---|---|---|
| Part 0 | Forethought | Goal, time target, confidence rating before you start |
| Part 1 | Clarifying Questions | What you'd ask the interviewer before writing a line of code |
| Part 2 | Decomposition | How you break the problem apart (brute force → optimized) |
| Part 3 | Contract | Exact input/output spec and edge cases, signed before coding |
| Part 4 | Code / Artifact | The implementation (SWE: Python/Go/Java) or document (PM: brief, NSM, A/B) |
| Part 5 | Reasoning Write-Up | Explain your choices in prose — the "why" behind the "what" |
| Part 6 | Interview Simulation | 90-second narration + 3 curveball questions |
| Part 7 | Rubric | 7-dimension self-grade, 5 points per dimension, 35 total |

You work through parts 0–6, then self-grade with Part 7. Then you check off the milestones.

---

## The Tier System

Each lab has a tier that controls how much scaffolding you get. Progress through tiers in order.

**Tier 1 (Worked):** About 60% pre-filled. The model solution is shown, explained, and annotated. You study the model, understand each decision, then blank it and re-implement from scratch. Use Tier 1 to build the mental model the first time.

**Tier 2 (Completion):** The structure and contract are provided. The key load-bearing parts — the algorithm choice, the state management, the metric definition — are left blank for you to fill. You can't just copy-paste; you have to supply the substance. Use Tier 2 to practice under partial pressure.

**Tier 3 (Blank Mock):** Almost completely blank. Section headers only. Rubric at the bottom. No hints, no starter code, no example walkthrough. This is the real interview simulation. If you need to look anything up, the prep isn't done yet. Use Tier 3 as your final readiness gate.

The recommended progression for any track is: do all Tier 1 labs first, then Tier 2, then attempt Tier 3.

---

## The Milestone System

Every lab has 6 milestones (M1–M6) that gate your progress through the lab:

| Milestone | What It Marks | Gate? |
|---|---|---|
| M1 | Clarified — asked at least 2 substantive questions before coding | Soft |
| M2 | Approached — explained brute force AND optimized approach before typing | Soft |
| M3 | Coded — working implementation written (even if not optimal) | Soft |
| M4 | Tested — ran at least 3 test cases including at least 1 edge case | **Hard gate** |
| M5 | Optimized — stated time and space complexity, named any tradeoffs | Soft |
| M6 | Ready — self-graded ≥ threshold on two separate attempts | Final |

M4 is a hard gate: do not move to Part 5 or 6 until you have checked off M4. Skipping testing is the #1 mistake candidates make in real interviews, and this system forces you to build the habit.

Check each milestone as a checkbox before moving to the next section. The milestones for each lab are listed at the top of the workbook.

---

## File Structure of Each Company Folder

```
companies/
  google/
    START_HERE.md         ← entry point for Google (start here)
    swe/
      lab_01_algorithmic/
        workbook.md       ← the interactive lab (fill this in)
        meta.yml          ← machine-readable lab metadata
        flashcards.md     ← 10 review cards for spaced repetition
      lab_02_graph_grid/
        workbook.md
        meta.yml
        flashcards.md
      lab_03_mock_screen/
        workbook.md
        meta.yml
        flashcards.md
    pm/
      lab_01_product_sense/
        workbook.md
        meta.yml
        flashcards.md
      ...
```

Every company follows the same structure. The entry point (START_HERE.md) for each company explains that company's specific interview format, the signals they score on, and any company-specific quirks you need to know before starting the labs.

---

## How to Use This Workbook — Concrete Instructions

**Step 1.** Open the company's START_HERE.md. Read the entire page. It's short. Don't skip it — the "Before You Start" checklist has things you'll miss if you dive straight into a lab.

**Step 2.** Open Lab 01 of your role track. Read Part 0, then set a timer for the estimated time.

**Step 3.** Work through Parts 1–6 with the timer running. For SWE labs: actually write the code in a plain text editor (not an IDE). For PM labs: actually write the brief in your own words — don't just fill in single words.

**Step 4.** When the timer goes off, finish the sentence you're on and stop. Note your stopping point.

**Step 5.** Self-grade using Part 7. Be honest. Score yourself as an interviewer would, not as someone who knows what they were trying to do.

**Step 6.** Check off milestones based on what you actually did, not what you intended to do. If you didn't test before moving on, M4 is unchecked.

**Step 7.** Wait 24 hours. Redo the lab. Your second score is your real score. Your first attempt is calibration; your second is readiness.

**Step 8.** Move to the next lab only when you've self-graded ≥ the threshold on two consecutive attempts.

---

## You're Ready When...

- You complete a Tier 3 lab cold (no hints, no peeking, no referencing earlier labs) in under 60 minutes
- You self-grade ≥ 35/50 on the final rubric
- You answer all 3 curveballs without freezing or saying "I don't know"
- You can narrate your reasoning clearly enough that someone who couldn't see your screen would understand what you're building and why

If you hit all four of those markers, you're ready for the real thing.

---

*Last updated: 2026-06 · Version 1.0*
