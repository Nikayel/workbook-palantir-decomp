# Solution Reasoning

## 0. Clarifying Questions Answer Key
- **Goal**: 
  - *Question*: Is the goal to discharge patients faster, or just map the bottlenecks?
  - *Assumption*: I'll assume the goal is to pinpoint the exact department causing the bottleneck so administrators can intervene.
- **Users**: 
  - *Question*: Who will read these reports?
  - *Assumption*: I'll assume hospital administrators are the end users viewing these metrics.
- **Data**: 
  - *Question*: Do all departments use the same timestamp format, and is it complete?
  - *Assumption*: I'll assume the legacy data is messy and might be missing timestamps for certain steps.
- **Constraints**: 
  - *Question*: Does this need to run in real-time or as a nightly batch job?
  - *Assumption*: I'll assume a nightly batch job is sufficient for historical bottleneck analysis.
- **Scale**: 
  - *Question*: How many patients are discharged per day?
  - *Assumption*: I'll assume ~500 patients a day, meaning the data volume is very low and easily fits in memory.


## 1. Why these users?
Charge nurses and department heads (Pharmacy, Transport) are the main users. They need visibility to unblock the flow.

## 2. Why this workflow?
By surfacing incomplete tasks tied to "medically ready" patients, we shift from a reactive pull model to a proactive push model.

## 3. Why this data model?
A Patient has many Tasks. Each Task has an Owner and a Status.

## 4. Why these APIs/actions?
- `GET /blockers`: Powers the dashboard.
- `POST /tasks/{id}/complete`: Allows manual unblocking if the upstream EMR is delayed.

## 5. Failure modes
- **Stale data**: If EMR batch sync is delayed, the dashboard shows false blockers, causing alert fatigue. Mitigation: allow manual override.

## 6. Strong vs weak answer
**Weak**: Build an ML model to predict when someone will be discharged. (Doesn't solve the operational communication issue).
**Strong**: Build a state machine for tasks, map them to owners, and aggregate a real-time queue of blockers for the charge nurse.
