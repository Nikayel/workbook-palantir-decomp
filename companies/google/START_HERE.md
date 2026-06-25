# Google — Interview Prep Entry Point

Welcome to the Google company workbook. Read this page fully before opening any lab. It will save you time and prevent the most common preparation mistakes.

---

## Google Snapshot

**Roles covered in this workbook:**
- **SWE** — Software Engineer (new grad L3 and experienced L4+)
- **APM** — Associate Product Manager (university program)
- **TPM** — Technical Program Manager (note: Google does not have a separate TPM interview track at all levels — see TPM note below)

**Culture signals Google scores on:**
- **GCA (General Cognitive Ability):** Your ability to reason through a novel problem, not just your recall of known solutions. Interviewers score how you think, not just whether you land the right answer. Narrating your process is mandatory.
- **RRK (Role-Related Knowledge):** Technical or domain knowledge directly relevant to the role. For SWE: algorithms, data structures, system design. For APM: product strategy, metrics, user research instincts.
- **Googleyness:** A culture-fit signal that assesses comfort with ambiguity, intellectual humility, collaborative problem-solving, and a bias to action. This signal can veto an otherwise strong candidate — a great coder with poor Googleyness scores can be declined by Hiring Committee.

**Hiring Committee:** At Google, the final hire/no-hire decision is made by a Hiring Committee (HC), not the interviewers. Interviewers submit independent written packets. HC reads the packets and votes. This means your written artifact (the code, the design doc, the product brief) matters as much as the verbal performance — HC only sees the packet, not you.

---

## What's Distinctive About Google Interviews

**Reasoning aloud beats landing the optimal answer.** An interviewer who sees you arrive at a suboptimal solution while clearly articulating your tradeoffs will score you higher than a candidate who silently produces the optimal solution. GCA is scored on the process.

**Googleyness can veto.** If you come across as arrogant, unwilling to be corrected, or resistant to collaboration, a strong technical score won't save you. Actively invite the interviewer to redirect you: "Does that approach make sense, or would you push me a different direction?"

**Plain-doc coding.** Google SWE phone screens are conducted in a plain Google Doc — no syntax highlighting, no autocomplete, no bracket matching. This is intentional. The interviewers want to see how you think, not how well you use an IDE. Practice writing code in a plain text editor.

**No run button.** You cannot execute code during the interview. You must walk through test cases manually, out loud. "Let me trace through this with the input [1,5],[2,6]..." is the correct behavior.

**APM vs SWE vs TPM:**
- APM interviews emphasize product sense, user empathy, and metrics — plus a "leadership" round. There is no coding round.
- SWE interviews are 2×45 minute coding screens (phone) plus 4–5 onsite rounds (coding, system design, behavioral, Googleyness).
- Google TPM interviews vary significantly by team. Some teams run a lighter system design + program management track. Others run near-SWE-level technical screens. Check your specific team's recruiter notes. The TPM labs in this workbook target a "system-design-lite + technical tradeoffs" format.

---

## Interview Format at a Glance

| Stage | Format | Duration | What's Scored |
|---|---|---|---|
| Phone screen (SWE) | 1–2 rounds, plain Google Doc coding | 45 min each | GCA, RRK (algorithmic) |
| Phone screen (APM) | Behavioral + product sense | 30–45 min | Googleyness, product sense |
| Onsite — SWE | 4–5 rounds (coding × 2–3, system design × 1, behavioral × 1) | 45 min each | GCA, RRK, Googleyness |
| Onsite — APM | 4–5 rounds (product sense, leadership, analytical, Googleyness) | 45–60 min | All four signals |
| Team match | After HC approval, recruiter connects you with teams | Varies | Mostly fit |
| Hiring Committee | HC reviews packet, votes | N/A | Holistic across all signals |

---

## Lab Menu

### SWE Track (est. 4–5 hrs total)

| Lab | Topic | Tier | Time | Link |
|---|---|---|---|---|
| Lab 01 | Algorithmic — Meeting Rooms | Tier 1 (worked) | 45 min | [→ Open](swe/lab_01_algorithmic/workbook.md) |
| Lab 02 | Graph/Grid — Number of Islands | Tier 2 (completion) | 50 min | [→ Open](swe/lab_02_graph_grid/workbook.md) |
| Lab 03 | Mock Phone Screen — Anagram Pairs | Tier 3 (blank mock) | 45 min | [→ Open](swe/lab_03_mock_screen/workbook.md) |

### PM Track (est. 5–6 hrs total)

| Lab | Topic | Tier | Time | Link |
|---|---|---|---|---|
| Lab 01 | Product Sense — Improve Google Maps | Tier 1 (worked) | 45 min | [→ Open](pm/lab_01_product_sense/workbook.md) |
| Lab 02 | Metrics / NSM — YouTube Watch Time | Tier 2 (completion) | 45 min | [→ Open](pm/lab_02_metrics_nsm/workbook.md) |
| Lab 03 | Estimation — Gmail Storage Costs | Tier 2 (completion) | 30 min | [→ Open](pm/lab_03_estimation/workbook.md) |
| Lab 04 | Googleyness Behavioral | Tier 2 (completion) | 30 min | [→ Open](pm/lab_04_googleyness_behavioral/workbook.md) |

### TPM Track (est. 3–4 hrs total)

| Lab | Topic | Tier | Time | Link |
|---|---|---|---|---|
| Lab 01 | System-Design-Lite — URL Shortener | Tier 2 (completion) | 50 min | [→ Open](tpm/lab_01_system_design_lite/workbook.md) |
| Lab 02 | Technical Tradeoff Explainer | Tier 2 (completion) | 40 min | [→ Open](tpm/lab_02_technical_tradeoff/workbook.md) |

---

## Before You Start — Checklist

Work through this before opening Lab 01. Items marked [BLOCKER] will actively hurt your performance if you skip them.

- [ ] [BLOCKER] **Know your role.** Are you applying for SWE, APM, or TPM? The tracks are distinct. Do not do the SWE labs if you're interviewing for APM — you'll practice the wrong muscles.
- [ ] [BLOCKER] **Practice coding in a plain text editor.** Open TextEdit (Mac) or Notepad (Windows) — not VS Code, not an IDE, not a REPL. Write a 10-line Python function from scratch. You need to be comfortable with no autocomplete before your phone screen.
- [ ] Review what GCA means in practice: it is scored on how clearly you narrate your reasoning, not on whether you arrive at the optimal solution first try.
- [ ] Understand Googleyness signals: intellectual humility (you can be wrong and update), curiosity (you ask genuine questions), collaboration (you invite the interviewer in), comfort with ambiguity (you don't freeze when the problem is underspecified).
- [ ] If you're targeting APM, read up on the Google APM program timeline (applications open in fall, interviews in winter/spring). The APM track in this workbook assumes you're in an active interview cycle.
- [ ] If you're targeting TPM, ask your recruiter whether your specific team runs a technical coding screen. Some do; most don't. The TPM track here assumes no coding, but covers system-design-lite and technical communication.

---

## Estimated Time Commitment

| Track | Total Lab Hours | Recommended Spacing |
|---|---|---|
| SWE | 4–5 hrs | 1 lab per day, 3 days minimum |
| PM | 5–6 hrs | 1 lab per day, 4 days minimum |
| TPM | 3–4 hrs | 1 lab every 1.5 days |

Do not try to complete multiple labs in a single sitting, especially the Tier 3 mock. Each lab requires genuine recall, not just recognition — spacing your practice by 24+ hours is what makes it stick.

---

## Navigation

- [Root workbook index](../../START_HERE.md)
- SWE Lab 01 → [Meeting Rooms](swe/lab_01_algorithmic/workbook.md)
- PM Lab 01 → [Improve Google Maps](pm/lab_01_product_sense/workbook.md)
- TPM Lab 01 → [System Design Lite](tpm/lab_01_system_design_lite/workbook.md)

---

*Google · Version 1.0 · 2026-06*
