# Solution Reasoning

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
