# 🏥 Drill 2: Hospital Patient Discharge & Readmission Prevention

**Interview difficulty:** ⭐⭐⭐⭐ (Hard)  
**Estimated time:** 45 minutes  
**Topics:** Multi-stakeholder workflows, clinical decision support, risk scoring, data quality

---

## The Prompt

> A large hospital network wants to reduce patient readmissions within 30 days. Currently, discharge decisions are made by doctors based on gut feel and hospital bed pressure. There's no systematic assessment of discharge risk, no structured follow-up planning, and no early warning system if patients start declining. You've been asked to design a system that:
>
> - Predicts readmission risk at discharge time
> - Recommends discharge conditions and follow-up actions
> - Alerts clinic staff if discharged patients show early warning signs
> - Tracks outcomes to improve the model
>
> The goal is to reduce 30-day readmission rates from 18% to <12% while maintaining patient autonomy.

---

## Phase 1: Stop and Think (5 minutes)

**Before reading anything, answer these:**

### 1. What are the key stakeholders?

```
Stakeholder 1: _______________________________
Stakeholder 2: _______________________________
Stakeholder 3: _______________________________
Stakeholder 4: _______________________________
```

### 2. What data would predict readmission?

```
Signal 1: _______________________________
Signal 2: _______________________________
Signal 3: _______________________________
Signal 4: _______________________________
Signal 5: _______________________________
```

### 3. What actions does a doctor need to take?

```
Action 1: _______________________________
Action 2: _______________________________
Action 3: _______________________________
```

---

## Phase 2: Clarifying Questions

**Question 1: What's the definition of readmission?**

_Expected answer:_

```
Any re-hospitalization within 30 days of discharge.
This is our outcome label.
Readmissions can be planned (e.g., surgery) or unplanned (e.g., complication).
We care about unplanned readmissions.
```

**Your understanding:**

```
_______________________________________
```

---

**Question 2: What data do we have?**

_Expected answer:_

```
- Clinical records: diagnosis, labs, medications, vital signs
- Social factors: age, living situation, social support
- Insurance: coverage type, past ER visits
- Outcome: readmitted or not (historical)

This is enough to build an initial model.
```

**Your thoughts:**

```
_______________________________________
```

---

**Question 3: Who are all the stakeholders?**

_Expected answer:_

```
Doctors: Make discharge decision
Nurses: Provide discharge instructions
Patients: Decide whether to follow instructions
Clinic staff: Monitor discharged patients
Hospital administrators: Track metrics, reduce costs
Insurers: Pay for readmissions
```

**Did you think of all six?**

```
_______________________________________
```

---

**Question 4: What happens if the system predicts high risk?**

_Expected answer:_

```
Option A: Doctor reviews, can override (system is advisory)
Option B: Automatic escalation (certain threshold triggers intervention)
Option C: Both (dashboard alert + automatic if very high risk)

Most hospitals choose: System suggests, doctor approves.
System confidence <80%: Doctor must review.
System confidence >95%: Could auto-escalate (need careful governance).
```

**Your approach:**

```
_______________________________________
```

---

## Phase 3: Expected Decomposition

### Users / Personas

**Persona 1: Doctor (Primary decision-maker)**

- Pain point: No systematic assessment; relies on gut feel; time-constrained
- Actions: Reviews risk score, decides discharge conditions, approves/overrides recommendation

**Persona 2: Nurse (Discharge executor)**

- Pain point: Unclear instructions; patient confusion; no follow-up
- Actions: Delivers discharge plan, reviews with patient, schedules follow-up

**Persona 3: Patient (Autonomous agent)**

- Pain point: Confused after discharge; unclear what to do; no support
- Actions: Follows instructions (or doesn't), seeks help if needed

**Persona 4: Clinic staff (Monitor post-discharge)**

- Pain point: No alerting; can't prevent readmission; reactive only
- Actions: Receives alerts, calls patient, escalates if needed

**Persona 5: Hospital administrator**

- Pain point: Can't predict readmission costs; reactive management
- Actions: Reviews metrics, adjusts staffing, identifies systemic issues

**Did you map all five?**

```
_______________________________________
```

---

### Current Workflow

```
Patient admitted
     ↓
Doctor treats patient
     ↓
Doctor decides discharge timing (gut feel)
     ↓
Nurse gives verbal discharge instructions
     ↓
Patient goes home (confused? clear? depends)
     ↓
Patient tries to follow instructions
     ↓
If complications: Patient goes to ER
     ↓
READMISSION (24–30 days later)
```

**Bottleneck:** No systematic assessment of risk. No structured follow-up. No early warning system. Readmission is reactive, not preventive.

**Solution fits:** Before discharge, assess risk. If high risk: recommend structured follow-up, early outpatient visit, home health, close monitoring.

**Did you identify this?**

```
_______________________________________
```

---

### Core Entities

| Entity               | Key Attributes                                                               |
| -------------------- | ---------------------------------------------------------------------------- |
| **Patient**          | id, age, gender, comorbidities, social_support, insurance                    |
| **Admission**        | id, patient_id, diagnosis, admission_date, severity, labs, medications       |
| **Discharge Plan**   | id, admission_id, recommendations, follow_up_date, post_discharge_monitoring |
| **Readmission Risk** | id, admission_id, risk_score, risk_factors, prediction_confidence            |
| **Alert**            | id, patient_id, alert_type, severity, created_at, resolved                   |

**Relationships:**

- Patient has_many Admissions
- Admission has_one DischargeContext, has_many Alerts
- DischargeContext is_based_on ReadmissionRisk

**Did you model all five?**

```
_______________________________________
```

---

### Readmission Risk Scoring

**Signals that predict 30-day readmission:**

```python
def predict_readmission_risk(admission):
  score = 0

  # Signal 1: Age & comorbidities (older + more conditions = higher risk)
  age_score = min(admission.age / 100 * 50, 50)  # Max 50 at age 100
  score += age_score

  # Signal 2: Admission severity (more severe = higher risk)
  severity_map = {"mild": 5, "moderate": 15, "severe": 30}
  score += severity_map[admission.severity]

  # Signal 3: Number of comorbidities
  score += admission.comorbidities_count * 3

  # Signal 4: Social support (no support = higher risk)
  social_support_map = {"strong": 0, "moderate": 10, "weak": 25}
  score += social_support_map[admission.social_support]

  # Signal 5: Insurance coverage (uninsured/underinsured = higher risk)
  if admission.uninsured:
    score += 20

  # Signal 6: Recent ER usage (frequent ER = higher risk)
  recent_er_visits = count_er_visits_last_90_days(admission.patient_id)
  score += min(recent_er_visits * 5, 25)

  # Signal 7: Medication adherence (from past admissions)
  adherence_rate = get_past_adherence(admission.patient_id)
  score += (1 - adherence_rate) * 15  # High adherence = low score

  total_score = min(score, 100)
  return total_score

def classify_risk(score):
  if score < 30: return "LOW"
  elif score < 60: return "MEDIUM"
  else: return "HIGH"
```

**Risk thresholds:**

- LOW (<30): Standard discharge, routine follow-up
- MEDIUM (30–60): Structured discharge, early follow-up visit
- HIGH (>60): Intensive support, home health, close monitoring

**Did you think of these signals?**

```
_______________________________________
```

---

### Discharge Plan Recommendations

**If LOW RISK:**

```
- Standard outpatient follow-up (3 weeks)
- Written discharge instructions
- Phone number for clinic
```

**If MEDIUM RISK:**

```
- Early follow-up visit (5–7 days)
- Home health nurse visit (within 48 hours)
- Phone check-in at 2 days
- Clear medication list
```

**If HIGH RISK:**

```
- Urgent follow-up visit (2–3 days)
- Home health daily for 1 week
- Phone check-ins at 1 day, 3 days, 7 days
- Case manager assignment
- Medication synchronization
- Mental health screening
```

**Did you stratify responses?**

```
_______________________________________
```

---

### Alerts & Monitoring

**Post-discharge, we monitor for early warning signs:**

```
Alert triggers:
1. Patient misses follow-up appointment → Call patient
2. Patient not picking up medications → Alert pharmacy
3. Vitals trending worse (from wearable/clinic) → Alert clinic
4. Patient calls hotline with concerning symptoms → Escalate
5. 10 days post-discharge with no contact → Pro-active call
```

**Who gets alerted?**

```
Clinic staff: First responder
Case manager: If patient high-risk
Doctor: If alert is urgent
```

**Did you design monitoring?**

```
_______________________________________
```

---

### APIs & Actions

**Action 1: Calculate Readmission Risk**

```
POST /api/v1/admissions/:id/risk-assessment
Input: {
  admission_id,
  patient_id,
  diagnosis,
  severity,
  age,
  comorbidities: [...],
  social_support,
  insurance_type
}
Output: {
  risk_score: 0-100,
  risk_level: "LOW" | "MEDIUM" | "HIGH",
  top_risk_factors: ["age", "comorbidities", "social_support"],
  confidence: 0.87,
  recommendations: [...]
}
```

**Action 2: Generate Discharge Plan**

```
POST /api/v1/admissions/:id/discharge-plan
Input: {
  admission_id,
  risk_level,
  patient_id
}
Output: {
  plan_id,
  recommendations: [...],
  follow_up_date,
  follow_up_type: "standard" | "intensive",
  monitoring_schedule: [...],
  medications: [...],
  discharge_instructions: string,
  case_manager_assigned: boolean
}
```

**Action 3: Record Post-Discharge Event**

```
POST /api/v1/patients/:id/events
Input: {
  patient_id,
  event_type: "appointment_missed" | "medication_not_filled" | "symptom_reported" | "er_visit",
  severity: "low" | "medium" | "high",
  details: string
}
Output: {
  event_id,
  alert_triggered: boolean,
  escalation_path: [...]
}
```

**Did you design these APIs?**

```
_______________________________________
```

---

### Edge Cases & Data Quality

**Edge case 1: Missing data (e.g., no social support info)**

```
Handling:
- Don't skip the patient
- Use conservative estimate (assume moderate support)
- Flag for manual review
- Log data quality issue
```

**Edge case 2: Patient refuses follow-up**

```
Handling:
- Document refusal
- Set alert for escalation
- Respect autonomy (don't force)
- Log for analysis (why do patients refuse?)
```

**Edge case 3: Prediction is wrong (low-risk patient readmitted)**

```
Handling:
- This is a false negative
- Log it for model retraining
- Understand root cause (was it unmeasurable? patient choice?)
- Iterate model quarterly
```

**Did you think of these?**

```
_______________________________________
```

---

### Security & Ethics

**Who can see what?**

```
Doctors: Full admission data, risk score, recommendations
Patients: Their own risk score (explained in simple terms), discharge plan
Clinic staff: Admitted patients' data, alerts
Admin: Aggregate metrics only (no individual patient data)
```

**Ethical concerns:**

```
1. Bias in data (historical data may over-predict for certain groups)
   → Audit for disparities; monitor outcomes by demographic
2. Feedback loop (model recommends close monitoring → drives readmission)
   → Track if recommendations are necessary or self-fulfilling
3. Patient autonomy (are we coercing discharge decisions?)
   → System is advisory; doctor + patient decide together
```

**Did you think about ethics?**

```
_______________________________________
```

---

### MVP (2 weeks)

```
✓ Risk scoring algorithm
✓ Doctors see risk score at discharge
✓ Structured discharge recommendations
✓ 7-day follow-up calls
✓ Manual alert creation
```

**NOT in MVP:**

```
✗ Automated alerts
✗ Home health integration
✗ Wearable/continuous monitoring
✗ ML model tuning
✗ Full post-discharge tracking
```

**Why?** Start with risk + human follow-up. Automation comes later after we validate effectiveness.

**Did you scope appropriately?**

```
_______________________________________
```

---

### Success Metrics

| Metric                       | Baseline | Target     |
| ---------------------------- | -------- | ---------- |
| 30-day readmission rate      | 18%      | <12%       |
| Doctor adoption              | 0%       | >80%       |
| Prediction accuracy          | N/A      | >80% (AUC) |
| Time to discharge plan       | 30 min   | <5 min     |
| Patient follow-up compliance | 60%      | >85%       |

**Did you define metrics?**

```
_______________________________________
```

---

## Interviewer Curveballs

### Curveball 1: "Your model has 15% false positives. Doctors ignore high-risk predictions."

_Response:_

```
This is a real problem: alert fatigue. If 15% of alerts are wrong,
doctors stop trusting the system.

Fix:
1. Improve model accuracy (more data, better features)
2. Explain predictions (why is this patient high-risk?)
3. Calibrate thresholds (reduce false positives, accept more false negatives)
4. Feedback loop (log doctor overrides, retrain model)

I'd reduce to <5% false positives by:
- Adding confidence intervals
- Requiring doctor review above 60% confidence
- Tuning thresholds to optimize precision (fewer false alarms)
```

**Your response:**

```
_______________________________________
```

---

### Curveball 2: "Certain demographics have worse outcomes in your system."

_Response:_

```
This is a bias issue. Possible causes:
1. Historical bias (model learned patterns from biased past data)
2. Different risk factors (social determinants not captured)
3. Different support systems (some groups have less access to care)

How I'd investigate:
- Audit predictions by demographic (age, gender, race, income)
- Check for disparities in readmission rates
- Analyze feature importance (does model over-weight certain factors?)
- Consult clinical teams: are there unmeasured risk factors?

Fix:
- Retrain model with fairness constraints
- Add social determinant features
- Regular monitoring and public reporting
```

**Your response:**

```
_______________________________________
```

---

## Scoring Yourself

| Dimension                  | You    | Notes                            |
| -------------------------- | ------ | -------------------------------- |
| **Ambiguity handling**     | \_\_/5 | Multi-stakeholder complexity     |
| **Workflow understanding** | \_\_/5 | Did you map pre/post-discharge?  |
| **Risk scoring**           | \_\_/5 | Signals, thresholds, calibration |
| **Data quality**           | \_\_/5 | Missing data, bias, monitoring   |
| **Ethics & fairness**      | \_\_/5 | Did you discuss equity?          |
| **Communication**          | \_\_/5 | Clarity on sensitive topic       |

**Total: \_\_/30**
