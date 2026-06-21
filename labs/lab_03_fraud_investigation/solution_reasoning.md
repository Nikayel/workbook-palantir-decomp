# Solution Reasoning

## 0. Clarifying Questions Answer Key
- **Goal**: 
  - *Question*: Are we trying to block transactions automatically, or alert analysts?
  - *Assumption*: I'll assume we are alerting analysts, so minimizing false positives to reduce alert fatigue is the primary goal.
- **Users**: 
  - *Question*: Who is reviewing these alerts?
  - *Assumption*: I'll assume a small team of fraud analysts, meaning we must rank the alerts by severity.
- **Data**: 
  - *Question*: Do we have a complete graph of all linked accounts?
  - *Assumption*: I'll assume we have transaction edges and shared-IP edges between accounts.
- **Constraints**: 
  - *Question*: Is there a strict latency requirement for this graph traversal?
  - *Assumption*: I'll assume this runs asynchronously (within seconds/minutes), not synchronously blocking the actual swipe.
- **Scale**: 
  - *Question*: How many transactions per second?
  - *Assumption*: I'll assume thousands per second, requiring efficient graph structures or bounded depth limits on traversal.


## 1. Why these users?
The primary user is the Fraud Analyst. The goal is to speed up their investigation.

## 2. Why this workflow?
By pre-computing risk scores and surfacing reasons, the analyst doesn't have to jump between tools. The workflow becomes: Review Alert -> Accept/Reject -> Feedback Loop.

## 3. Why this data model?
We need `Transaction`, `AccountProfile` (averages, typical locations), `DeviceProfile` (known devices), and `Alert`.

## 4. Why these APIs/actions?
- `POST /score`: Synchronous or async depending on the payment gateway requirement.
- `POST /alerts/{id}/resolve`: Closes the alert and writes to the audit log.

## 5. Why this algorithm?
We use a heuristic-based approach (rules) rather than ML for the MVP because rules are easily explainable to the analyst. The output provides explicit *reasons*, not just a black-box score.

## 6. Failure modes
- **False positives**: Analyst fatigue. Mitigation: Implement a feedback loop to tune the thresholds.
- **Data lag**: If history is delayed, velocity rules fail.

## 7. Strong vs weak answer
**Weak**: "I'll train a neural net on the transactions." (Analysts won't trust it if it can't explain *why*).
**Strong**: "I'll build a transparent rules engine that flags anomalies (velocity, location, amount, device) and presents a prioritized queue to the analyst with clear evidence tags."
