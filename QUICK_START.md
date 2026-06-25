# ⚡ Quick Start: How to Use the Interactive Curriculum

**This is NOT a reading assignment. You will WRITE answers and learn by doing.**

---

## 📋 What Changed?

### Old Format (Case Study):
- Read problem → Read expected solution → Compare

### New Format (Interactive Quiz-Style):
- Read problem → **You write answer in blanks** → Compare your work → Score yourself

---

## 🎯 Start Here: 15 Minutes

### Step 1: Open the Interactive Template (5 min)
```
templates/decomp_template_interactive.md
```

Read it. Notice:
- Sections 1–14 with guided prompts
- Blank lines with `_______` for YOUR answers
- Instructions like "Your answer:" before blanks
- NO complete answers (you fill them in)

### Step 2: Open the First Interactive Drill (10 min)
```
drills/01_911_dispatch_interactive.md
```

Scan through it. Notice:
- **Phase 1: Stop and Think** – Answer questions WITHOUT peeking
- **Phase 2: Reveal** – See expected clarifying questions
- **Phase 3: Study** – Read full decomposition
- **Phase 4: Score** – Use rubric to grade yourself

---

## 🔄 The Interactive Flow (for each drill)

### Phase 1: Stop & Think (5 min)
```
❌ DON'T read the solution yet
✅ DO answer "Stop and Think" section
✅ Write your clarifying questions
✅ List entities you'd define
✅ Explain your scoring logic
```

### Phase 2: Reveal (5 min)
```
✅ Now compare your questions to expected ones
✅ Did you miss something? Note it.
❌ Don't read full solution yet
```

### Phase 3: Study (20 min)
```
✅ Read the "Expected Decomposition" section
✅ See how they modeled users, workflow, data
✅ Understand their API design
✅ Learn the edge cases
```

### Phase 4: Self-Score (5 min)
```
✅ Use the rubric at the end
✅ Score yourself: Ambiguity (1–5), Workflow (1–5), etc.
✅ Calculate total score
```

### Phase 5: Code Exercise (30 min)
```
✅ Run the Python or JS code
✅ Implement the logic yourself
✅ Test with sample data
✅ Understand what's hard about real implementation
```

**Total: ~60–90 min per drill**

---

## 🗂️ File Organization

### Templates (Start with these)

| File | Use When |
|------|----------|
| `decomp_template_interactive.md` ⭐ | You're starting a new drill and need blanks to fill |
| `decomp_template.md` | You want to see a completed example |

### Drills (Interactive vs Reference)

| Drill | Interactive ⭐ | Reference |
|-------|---|---|
| 911 Dispatch | `01_911_dispatch_interactive.md` | `01_911_dispatch.md` |
| Hospital Discharge | `02_hospital_discharge_interactive.md` | `02_hospital_discharge.md` |
| Fraud Detection | `03_fraud_detection_interactive.md` | `03_fraud_detection.md` |

**Always start with the interactive version!**

---

## 📅 7-Day Plan (Using Interactive Versions)

### Day 1: Orientation (1.5 hours)
- [ ] Read this quick start (10 min)
- [ ] Open `templates/decomp_template_interactive.md`, scroll through (5 min)
- [ ] Open `drills/01_911_dispatch_interactive.md`, scan structure (5 min)
- [ ] Memorize talk track (20 min)
- [ ] Practice narrating aloud (15 min)

### Day 2: First Drill + Code (3 hours)
- [ ] Phase 1: Answer "Stop & Think" in `01_911_dispatch_interactive.md` (5 min)
- [ ] Phase 2–4: Read expected solution + score (30 min)
- [ ] Run `python/911_dispatch_sim.py` (15 min)
- [ ] Implement ranking logic (30 min)
- [ ] Discuss trade-offs (15 min)

### Day 3: Fraud Detection (3 hours)
- [ ] Phase 1–4: `03_fraud_detection_interactive.md` (45 min)
- [ ] Run `python/fraud_scoring.py` (45 min)
- [ ] Add new signals to the scoring (30 min)

### Day 4: Hospital Discharge (3 hours)
- [ ] Phase 1–4: `02_hospital_discharge_interactive.md` (50 min)
- [ ] Reflection: Multi-stakeholder complexity (30 min)
- [ ] Ethical considerations (20 min)

### Day 5: Repeat & Refine (3 hours)
- [ ] Pick one previous drill
- [ ] Timed 45 min to re-do it (Phase 1–4)
- [ ] Compare to solution (15 min)
- [ ] Record yourself explaining it (45 min)

### Day 6–7: JavaScript + Mock Interview (6 hours)
- [ ] Study `js/workflow_state_machine.js` (45 min)
- [ ] Implement a state machine (45 min)
- [ ] Mock interview with friend (90 min)

---

## ✅ Success Checklist

By end of Day 7, you should be able to:

- [ ] Fill in `decomp_template_interactive.md` without help in <60 min
- [ ] Answer 911 dispatch drill in <45 min
- [ ] Identify 5+ edge cases per problem
- [ ] Explain your scoring logic clearly
- [ ] Write a production-ready ranking algorithm
- [ ] Handle curveballs (scale, data quality, adoption) gracefully
- [ ] Narrate your design clearly under pressure
- [ ] Score yourself accurately using the rubric

---

## 🎤 When You Do the Real Interview

**Use the same flow:**

1. **Clarify** – Ask 8–12 questions (5–8 min)
2. **Map workflow** – Draw boxes and arrows (3–5 min)
3. **Define entities & state** – Propose core objects (3–5 min)
4. **Design MVP APIs** – Propose 3–4 key endpoints (5–7 min)
5. **Add logic** – Explain ranking/scoring heuristics (5–7 min)
6. **Handle edge cases** – Missing data, scale, conflicts (5–7 min)
7. **Security & metrics** – Permissions, monitoring (3–5 min)

**Total: ~40–45 minutes → 5 min buffer**

---

## 💡 Pro Tips

1. **Don't peek.** Fill in Phase 1 completely before reading Phase 3.
2. **Write on paper.** Typing is slower. Handwrite your answers.
3. **Narrate out loud.** Practice explaining your design. Awkward pauses matter.
4. **Time yourself.** Can you do it in 45 min? 30 min? Get faster.
5. **Record yourself.** You'll hear how you sound. Refine your pacing.
6. **Iterate code.** Don't just read the Python exercise. Modify it. Test edge cases.

---

## 🚀 Start Now

**Right now, literally do this:**

1. Open your terminal
2. Run: `cd /Users/nikayeljamal/Demo/PalantirPrepDecomp/palantir-decomp-practice`
3. Open `templates/decomp_template_interactive.md` in your editor
4. Read section 1 (Goal). Write your own answer in a blank section.
5. Go to `drills/01_911_dispatch_interactive.md`. Read the prompt.
6. Answer the "Stop & Think" section. Write for real. No peeking.

**You have 15 minutes. Go.**

---

_The best way to learn interview decomposition is to DO it, not read about it._
