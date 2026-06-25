# 07 · Production Plan & Counts — "How many to create, in what order"

> **Audience:** the curriculum creator.
> **Purpose:** the build plan. How many labs, of which types, for which company/role, in what order, and how they assemble into a learner's course. This is your project tracker.

---

## 1. The unit math

The catalog is a 3-axis space: **10 companies × 3 roles × N lab types**. A naïve 10×3×6 = 180 is the wrong target — three corrections keep it realistic:

1. **Not every company supports every role.** Palantir has **no classic PM** (route to FDSE/decomposition). Google & Meta have **no separate Technical-PM track** (fold into PM/SWE). Apple PM ≈ EPM; Nvidia PM is technical-only. Mark these "fold" cells.
2. **Some labs are shared/generic** (estimation, core DSA patterns, a behavioral-STAR template) — author once, skin lightly. The existing `/dsa_patterns/` is a generic SWE bank you reuse across companies.
3. **Tier the build** — ship a high-value MVP first, then fill out.

---

## 2. Recommended lab count per company × role

Each cell is "labs to author for a complete track." `—` = fold into another track (don't build standalone). Counts include the tier mix in §3.

| Company | SWE | PM | Technical PM | Company total |
|---|---|---|---|---|
| Google | 3 | 4 | 2 (fold-lite) | 9 |
| Meta | 4 | 4 | — (fold into PM) | 8 |
| Amazon | 4 | 3 | 2 | 9 |
| Microsoft | 4 | 3 | 2 | 9 |
| Apple | 4 | 2 | 2 (EPM) | 8 |
| Palantir | 6 | — (→FDSE) | — (→decomp) | 6 |
| Nvidia | 4 | — | 2 | 6 |
| Uber | 4 | 3 | 2 | 9 |
| Stripe | 3 | 2 | 2 | 7 |
| Atlassian | 4 | 3 | 2 | 9 |
| **Role totals** | **40** | **24** | **16** | **≈ 80 company-specific labs** |

Plus a **shared/generic bank** (reused across companies, ~20 labs):
- ~8 generic **DSA-pattern** labs (the existing `/dsa_patterns/`, brought to standard).
- ~3 generic **estimation/market-sizing** labs (PM).
- ~3 generic **SQL** + ~2 generic **API/data** labs (the existing `/api_sql_data/`).
- ~2 generic **behavioral-STAR** templates (skin per company's values/LP).
- ~2 generic **system-design-lite** labs (Technical PM).

**Grand total target: ~100 labs** (80 company-specific + ~20 shared). That is the *full* curriculum; you do **not** build it all at once — see the roadmap.

---

## 3. Tier mix within a track (the difficulty curve)

For any company×role track, distribute tiers so the learner climbs worked → blank (Principle 3). A typical **4-lab track**:

| Slot | Tier | Difficulty | Role of the lab |
|---|---|---|---|
| Lab 1 | **Tier 1 (worked)** | intro/easy | model the skill fully; "I do" |
| Lab 2 | **Tier 2 (completion)** | medium | core practice; "we do" |
| Lab 3 | **Tier 2 (completion)** | medium | the company-signature artifact |
| Lab 4 | **Tier 3 (blank/mock)** | hard/mock | timed, unscaffolded; "you do alone" |

A 6-lab track (Palantir SWE) adds two more Tier-2 labs (SQL, API). A 2–3-lab track gets 1 worked + 1–2 completion, and shares a Tier-3 mock with the SWE track.

---

## 4. Build roadmap (do it in this order)

### Phase 0 — Foundations (before any company labs)
- [ ] This playbook (done).
- [ ] The 9 **authoring templates** in `templates/`.
- [ ] The **3 gold-standard samples** (PM, Technical PM, SWE) in `gold_standard_samples/` — your clone-me references.
- [ ] Bring **Palantir** (the existing `/labs/` etc.) up to the `08` standard (it's already 80% there). This validates the standard on real content.

### Phase 1 — The MVP (~30 labs): one strong track per company, signature-first
Build the **single highest-signal track** per company plus its signature artifact. This gives a learner *something excellent* for every company fast.
- [ ] Amazon: LP-STAR + PR-FAQ + 1 SWE algorithmic + Work-Simulation lab.
- [ ] Stripe: integration + bug-squash + Technical-PM idempotent-payments memo.
- [ ] Palantir: decomposition set (from Phase 0) + mock OA.
- [ ] Meta: 2-medium speed drill + Jedi behavioral + product-sense.
- [ ] Google: plain-doc algorithmic + product-sense + Googleyness behavioral.
- [ ] Atlassian: Values lab + craft/LLD coding.
- [ ] Uber: marketplace-metrics PM + routing SWE.
- [ ] Microsoft: LLD + growth-mindset behavioral.
- [ ] Nvidia: pointers/memory C++ lab + HW-SW Technical-PM.
- [ ] Apple: teardown/improve PM + practical DSA.

### Phase 2 — Depth (~70 labs): complete every track to the §2 counts
Fill out each company×role to the recommended count and full tier curve. Interleave companies (don't finish one company before starting the next — Principle 11 at the *catalog* level keeps your difficulty calibration honest).

### Phase 3 — Polish & maintenance
- [ ] Cross-company calibration pass (a Tier-2 medium at Google ≈ a Tier-2 medium at Uber).
- [ ] Cumulative flashcard deck across the whole catalog.
- [ ] Re-verify every company pack's facts each recruiting cycle (dates, OA cutoffs, AI policy).

---

## 5. How labs assemble into a learner's course

A learner picks a **(company, role)** and gets a sequenced course. Provide three study plans per track (mirror the existing repo's 7-day/14-day pattern):

- **Sprint (1 week):** Tier-1 lab → 2 Tier-2 labs → Tier-3 mock; flashcards daily.
- **Standard (2–4 weeks):** the full track at 2–4 labs/week + the shared DSA/estimation bank + spaced flashcards (day 1/3/7/14).
- **Deep (4–8 weeks):** the full track + a second company's track interleaved + repeat the Tier-3 mocks on a strict timer, recording 90-second talk-tracks.

Per `02`: ~12–20 labs over 4–8 weeks is the healthy dosage; the last 2–3 labs of any course are near-blank, full-length mocks.

---

## 6. Definition of "company track complete"
A company×role track is **done** when:
- [ ] Lab count meets §2.
- [ ] Tier curve runs worked → completion → blank/mock (§3).
- [ ] The **company-signature artifact** lab exists (PR-FAQ / integration / decomposition / Values / Jedi / marketplace / etc.).
- [ ] Every lab passes the `08` QA checklist.
- [ ] A learner can complete the track with **no instructor** (the keystone rule, `03` §11).
- [ ] The company pack's facts were re-verified this recruiting cycle.
