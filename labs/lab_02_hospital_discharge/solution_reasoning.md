# Solution Reasoning

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
