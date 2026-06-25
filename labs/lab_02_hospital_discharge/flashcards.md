# Flashcards — Hospital Discharge Optimization

> Review **day 1 → 3 → 7 → 14**. Reset to day 1 on a miss.
> Cover each answer before reading. These are free-recall — no peeking.

---

**Q:** What is a multi-stakeholder workflow and why is it harder to decompose than a single-user system?
**A:** A multi-stakeholder workflow involves multiple independent actors (doctor, pharmacist, transport coordinator) who each own a step and can independently block progress. It is harder to decompose because the bottleneck is rarely in any one step — it is at the handoff between steps, and different actors have different incentives, data systems, and availability.

---

**Q:** How do you identify the administrative bottleneck in a discharge workflow in code?
**A:** Compute the elapsed time at each step transition (e.g., discharge_ordered_at to pharmacy_signed_at). The step with the highest median elapsed time is the bottleneck. In Python: `max(steps, key=lambda s: s.median_duration)`.

---

**Q:** What are the state transitions for a patient discharge task as a DB lifecycle (not UI flow)?
**A:** PENDING → IN_PROGRESS → BLOCKED → COMPLETED (or CANCELLED). BLOCKED is a key state — it records which department is holding the task and when the block started, enabling SLA violation detection.

---

**Q:** When should discharge subtasks run in parallel vs sequentially, and why does the distinction matter for system design?
**A:** Independent subtasks (pharmacy sign-off and transport booking) can run in parallel — starting them concurrently reduces total wall-clock time. Dependent subtasks (doctor must sign before pharmacy can dispense) must run sequentially. Modeling this incorrectly either wastes time (forcing sequential when parallel is safe) or creates errors (starting pharmacy before doctor approval).

---

**Q:** How does a notification system in a discharge workflow differ from a simple alert, and what three fields must a notification carry?
**A:** A simple alert just fires once. A discharge notification must carry: (1) which task is blocked, (2) which actor is responsible, and (3) how long the SLA has been violated. Without the responsible actor, no one knows who to page. Without the SLA duration, no one knows how urgent it is.

---

**Q:** What is an SLA and how would you implement SLA tracking for discharge tasks in Python?
**A:** SLA (Service Level Agreement) is the maximum allowed time for a step to complete. Track it by storing `deadline_at = started_at + sla_hours` on the task record. A background job (or query) finds all tasks where `now() > deadline_at AND status != COMPLETED` and surfaces them as violations.

---

**Q:** What must an audit trail record in a healthcare system that is different from other domains?
**A:** Healthcare audit trails must record: (1) who accessed the record (not just who changed it — HIPAA read access), (2) the clinical reason or authorization for the action, and (3) every status change with a timestamp. The log must be tamper-proof and retained for the legally mandated period (often 6–10 years). This differs from most domains where read access is not audited.

---

**Q:** Why is real-time processing preferable to batch for discharge coordination, and when would batch be acceptable?
**A:** Real-time is preferable because a patient held an extra hour due to a delayed batch update directly costs a bed and patient wellbeing. Batch is acceptable for reporting and analytics (e.g., daily bottleneck summary for hospital leadership) where a few hours of lag has no operational impact.

---

**Q:** What is the "missing timestamp" problem and how do you handle it defensively in a discharge pipeline?
**A:** The missing timestamp problem occurs when an upstream system fails to write a key event (e.g., discharge_ordered_at is null). Handle it by: (1) treating null timestamps as "unknown start" and not computing duration for that step, (2) flagging the record for manual review rather than silently skipping it, and (3) never inferring a missing timestamp from adjacent events.

---

**Q:** What is the riskiest assumption in a hospital discharge system and how do you validate it early?
**A:** The riskiest assumption is that the EHR (Electronic Health Record) system reliably emits events in real time. In reality, many hospitals use overnight batch exports or have integration gaps. Validate it early by asking: "Does the EHR have a real-time event stream or a database we can poll?" before designing any alerting logic.
