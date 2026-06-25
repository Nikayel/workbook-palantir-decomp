# Drill 2: Hospital Patient Discharge Workflow

**Interview difficulty:** ⭐⭐⭐ (Medium-Hard)  
**Estimated time:** 45 minutes  
**Topics:** Workflow optimization, multi-actor coordination, state machines, resource planning

---

## The Prompt

> A large hospital is struggling with patient discharge delays. Patients are medically ready to leave, but discharge takes 4–8 hours due to poor coordination between doctors, nurses, pharmacists, insurance verification teams, and transportation. On average, a bed stays occupied 3–5 hours after the patient is cleared for discharge, blocking new admissions and reducing hospital revenue. Design a system to automate and streamline the discharge workflow so that patients leave within 1 hour of being cleared medically.

---

## Clarifying Questions (Select the most important ones)

1. **What is "medically ready"? Who decides?** (Doctor needs to sign off)
2. **How many patients per day go through discharge?** (50–200 depending on hospital size)
3. **What are the actual blockers today?** (Insurance verification, meds not ready, transportation not arranged, paperwork lost)
4. **Can you automate insurance verification?** (Partially; some cases need human review)
5. **Do patients need to wait for transportation, or can they leave on their own?** (Depends on patient condition)
6. **How many actors are involved?** (Doctor, nurse, pharmacist, insurance clerk, transport coordinator, patient/family)
7. **Is the system for hospital staff or patients or both?** (Primarily staff; patient gets notifications)
8. **What's the success metric?** (Time from medical clearance to patient out the door)

---

## Expected Decomposition (Abbreviated)

### Users

- **Doctor** – Signs discharge order
- **Nurse** – Prepares patient, confirms readiness
- **Pharmacist** – Prepares discharge medications
- **Insurance Clerk** – Verifies coverage, gets pre-authorization
- **Transport Coordinator** – Arranges ride home
- **Patient/Family** – Waits for discharge, receives paperwork

### Current Workflow

```
Doctor → Discharge order (paper or email)
         ↓
Nurse → Confirms patient ready (checks vitals, prepares meds request)
         ↓
Pharmacist → Fills meds, labels them (1–2 hours!)
              ↓
              Insurance verification (can be slow)
              ↓
              Transport arranged
              ↓
              Patient waits for all steps
              ↓
              Paperwork compiled
              ↓
              Patient discharged
```

**Bottleneck:** No parallelization. Each step waits for previous. Insurance and pharmacy are sequential, not parallel.

### Proposed Workflow (MVP)

```
Doctor signs discharge order
    ↓
System triggers 3 parallel tracks:
    ├─ Pharmacy: Start med prep
    ├─ Insurance: Start verification
    └─ Transport: Start ride coordination
    ↓
System shows patient/family real-time status
    ↓
When all 3 are done, notify nurse
    ↓
Nurse does final check
    ↓
Patient walks out (goal: < 1 hour total)
```

### Key Entities

- **Discharge Order** – status: new, in_progress, completed, cancelled
- **Medication List** – status: queued, prepared, labeled
- **Insurance Verification** – status: pending, approved, denied, manual_review
- **Transport Booking** – status: pending, confirmed, arrived, completed
- **Patient Discharge** – status: new, cleared, ready, completed

### State Machine

```
Discharge Order:
    new ──start─→ in_progress ──all_clear──→ completed ──patient_leaves──→ closed

Sub-tasks (parallel):
    Pharmacy: new → preparing → ready
    Insurance: new → verifying → approved (or manual_review)
    Transport: new → booking → confirmed

Patient can leave when: discharge_order.status = "ready" AND pharmacy.ready AND insurance.approved AND transport.confirmed
```

### Ranking / Logic

**Determine discharge readiness (when all done):**

```python
def can_discharge_patient(order):
    pharmacy_ready = order.pharmacy_status == "ready"
    insurance_cleared = order.insurance_status in ["approved", "manual_review"]
    transport_confirmed = order.transport_status == "confirmed"
    nurse_signoff = order.nurse_approved == True

    return pharmacy_ready and insurance_cleared and transport_confirmed and nurse_signoff
```

### Edge Cases

- Insurance denies coverage → escalate to human, log issue, maybe negotiate
- Pharmacy can't fill meds → notify nurse to find alternative
- Patient declines transportation → mark as patient-initiated delay
- Doctor changes discharge order → restart workflow or update tasks
- Patient has no address/insurance → halt, escalate to social worker

### MVP

**2-week scope:**

- Basic workflow (doctor → pharmacy/insurance/transport in parallel)
- Status dashboard for staff
- Notifications (email/SMS)
- Manual override (staff can force complete tasks)
- No patient portal (staff only initially)

**NOT in MVP:**

- Insurance API integration (start manual)
- Transportation integration (staff books manually)
- Advanced analytics
- Mobile app

### Metrics

| Metric                           | Baseline          | Target         |
| -------------------------------- | ----------------- | -------------- |
| Time from med clear to discharge | 5 hours           | < 1 hour       |
| Workflow parallelization         | 0% (sequential)   | 90% (parallel) |
| Insurance delays                 | 25% of discharges | < 5%           |
| Staff time per discharge         | 1.5 hours         | 0.5 hours      |

### V2

- Insurance API integration (auto-verify)
- Patient portal (check status, provide insurance info online)
- Transport integration with Uber/Lyft or hospital fleet
- Predictive alerts (flag patients who might delay)

---

## Rubric (Abbreviated)

Evaluate yourself on:

1. **Workflow parallelization** – Did you identify that tasks can run in parallel?
2. **State machine clarity** – Are transitions well-defined?
3. **Edge case coverage** – Insurance denial, patient decline, etc.?
4. **Practical timeline** – Is MVP launchable in 2 weeks?
5. **Stakeholder coordination** – Did you address all actors (doctor, nurse, insurance, transport)?

---

## Next Steps

1. Read full solution in `solutions/02_hospital_discharge_solution.md`
2. Implement a simple workflow state machine in `js/workflow_state_machine.js`
3. Test with edge cases (insurance denial, patient decline)
