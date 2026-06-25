# Flashcards — Factory Maintenance: Predictive Anomaly Detection

> Review **day 1 → 3 → 7 → 14**. Reset to day 1 on a miss.
> Cover each answer before reading. Free-recall — no peeking.

---

**Q:** What is the key difference between predictive maintenance and preventative maintenance?
**A:** Preventative maintenance runs on a fixed schedule regardless of machine state (wasteful if fine, too late if it breaks early). Predictive maintenance uses sensor signals to flag machines likely to fail *before* they do — triggering work orders only when risk exceeds a threshold.

---

**Q:** You have temperature and vibration readings arriving every 500ms from 500 machines. What are your two main choices for grouping them before analysis, and when would you pick each?
**A:** Tumbling windows (non-overlapping, fixed size e.g. 1-minute buckets) are simpler and cheaper — good for throughput metrics. Sliding windows (overlapping, e.g. last 5 minutes re-evaluated every 30s) catch faster-moving anomalies but cost more CPU. Pick sliding windows when a sudden spike must trigger an alert within seconds; tumbling windows when aggregate trends matter more than real-time spikes.

---

**Q:** A sensor sends a constant value of 9999. How do you distinguish a broken sensor from a genuinely dangerously hot machine, and what does your system do in each case?
**A:** Apply a physical-bounds filter: if a reading exceeds the mechanical maximum for that sensor type (e.g. >500°C for a CNC spindle), treat it as a sensor fault — raise a `SENSOR_FAULT` alert rather than a `MAINTENANCE_REQUIRED` alert, and suppress downstream anomaly scoring for that machine until the sensor is validated. A genuine high reading stays within physical bounds but triggers the anomaly model.

---

**Q:** What is the cost of a false positive in an industrial predictive maintenance system, and how does it affect your alert threshold design?
**A:** A false positive sends a technician to inspect a healthy machine — wasting 1–2 hours of skilled labor and potentially taking a functioning machine offline. If false positives are too frequent, technicians start ignoring alerts (alert fatigue). This pushes you toward a higher threshold (fewer alerts, higher precision), but at the cost of missing some real failures. The optimal tradeoff depends on the cost of a missed failure vs. the cost of a false inspection.

---

**Q:** What is threshold alerting, and why might you prefer it over an ML model for a V1 predictive maintenance system?
**A:** Threshold alerting fires an alert when a sensor reading crosses a fixed limit (e.g. temperature > 85°C for > 3 minutes). It is deterministic, explainable, easy to tune without training data, and has no model drift. An ML model can catch subtler patterns but requires labeled failure data, retraining pipelines, and explainability work. For V1, start with thresholds; layer ML on top once you have labeled incidents.

---

**Q:** Describe the work-order workflow from anomaly detection to ticket closure. What are the key state transitions?
**A:** DETECTED → TICKET_CREATED → ASSIGNED → IN_PROGRESS → RESOLVED → CLOSED. Key guards: a ticket cannot be ASSIGNED if no available technician exists (it stays TICKET_CREATED). RESOLVED requires the technician to log a repair action. CLOSED requires a supervisor sign-off or auto-close after N days with no recurrence.

---

**Q:** What are the key lifecycle states of a machine asset in a maintenance system?
**A:** OPERATIONAL → DEGRADED (anomaly detected, ticket open) → MAINTENANCE (taken offline for repair) → REPAIRED (work done, awaiting validation) → OPERATIONAL. Also: DECOMMISSIONED (end of life). The state machine prevents scheduling production on a machine in MAINTENANCE state.

---

**Q:** When should you process sensor data as a stream vs. as a batch, and what drives that decision?
**A:** Stream (e.g. Kafka + Flink) when you need sub-minute alert latency — a machine about to fail cannot wait for a nightly batch job. Batch (e.g. daily aggregation) for trend reports, model retraining, and SLA dashboards where latency of hours is acceptable. In practice: stream for anomaly detection triggers, batch for analytics and model updates.

---

**Q:** You need to schedule 50 technicians across 500 machines with varying urgency and skill requirements. What constraint makes this a hard optimization problem, and what is a pragmatic V1 shortcut?
**A:** It is a variant of the vehicle routing / assignment problem — NP-hard when you add travel time, skill matching, shift constraints, and machine interdependencies. V1 shortcut: sort tickets by severity score descending, assign greedily to the next available qualified technician. Accept suboptimality; measure SLA compliance and tighten the algorithm only if SLA is breached.

---

**Q:** How do you notify a technician of a new maintenance ticket without overwhelming them, and what information must the notification contain to be actionable?
**A:** Use push notification (mobile app) or SMS for high-severity tickets; email digest for low-severity. The notification must include: machine ID and location, anomaly type and current reading, severity score, estimated time to failure (if available), and a one-tap link to accept the ticket. Do NOT send raw sensor values — translate to human-readable status so the technician knows what tools to bring.
