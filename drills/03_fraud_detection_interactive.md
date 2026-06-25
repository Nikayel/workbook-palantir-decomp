# 🚨 Drill 3: Fraud Detection & Risk Scoring

**Interview difficulty:** ⭐⭐⭐⭐⭐ (Very Hard)  
**Estimated time:** 50 minutes  
**Topics:** Risk scoring, real-time processing, false positives, data freshness, user friction

---

## The Prompt

> A large fintech company processes $10B in transactions/day. They're seeing increasing fraud losses (~$5M/day). Currently, they block suspicious transactions, but their false positive rate is 5%—meaning 50,000 legitimate customers per day are blocked. This causes support costs and customer churn.
>
> You've been asked to design a real-time fraud detection system that:
>
> - Detects fraud with <1% false positive rate
> - Processes transactions in <100ms
> - Learns from customer feedback
> - Handles novel fraud patterns
> - Balances security vs. customer experience
>
> The goal is to reduce fraud losses from $5M/day to <$1M/day while keeping false positives under 1%.

---

## Phase 1: Stop and Think (5 minutes)

### 1. What data signals fraud?

```
Signal 1: _______________________________
Signal 2: _______________________________
Signal 3: _______________________________
Signal 4: _______________________________
Signal 5: _______________________________
```

### 2. What's the trade-off you're making?

```
_______________________________________
_______________________________________
```

### 3. How do you balance false positives vs false negatives?

```
_______________________________________
_______________________________________
```

---

## Phase 2: Clarifying Questions

**Question 1: What's the cost of false positives vs false negatives?**

_Expected answer:_

```
False positive: Block legitimate transaction
  Cost: Customer friction, support call, possible churn
  Estimate: $5–50 per false positive (opportunity + support)

False negative: Miss fraud
  Cost: Fraud loss + chargeback + investigation
  Estimate: $500–5000 per false negative

This asymmetry matters: FN is ~100x more expensive.
So: Optimize for false negatives first, then reduce false positives.
```

**Your answer:**

```
_______________________________________
```

---

**Question 2: What types of fraud are we fighting?**

_Expected answer:_

```
1. Card theft (stolen card, unknown location)
2. Account takeover (hacked password, attacker uses account)
3. Money laundering (layering transactions to hide origin)
4. Merchant fraud (fake merchant, collusion with customer)
5. Friendly fraud (customer claims transaction didn't happen; chargeback)

Different frauds need different signals.
```

**Did you think of all five?**

```
_______________________________________
```

---

**Question 3: What's the latency requirement?**

_Expected answer:_

```
<100ms to decide: approve, decline, or challenge.
This is tight for real-time ML.
```

**Your thoughts:**

```
_______________________________________
```

---

**Question 4: How do customers react to friction?**

_Expected answer:_

```
If we challenge 1% of transactions (2FA, security questions):
- 80% pass 2FA easily
- 20% abandon / churn
- Support cost: 100,000 challenges/day × $5 = $500K/day

We must minimize challenges.
Alternative: silent risk scoring (no friction to customer, internal decision).
```

**Your approach:**

```
_______________________________________
```

---

## Phase 3: Expected Decomposition

### Core Entities

| Entity           | Attributes                                                         |
| ---------------- | ------------------------------------------------------------------ |
| **User/Account** | id, email, phone, created_date, location, avg_transaction_amount   |
| **Transaction**  | id, amount, merchant, location, timestamp, payment_method, user_id |
| **Device**       | id, user_id, device_fingerprint, os, browser                       |
| **Fraud Flag**   | id, transaction_id, is_fraud, reason, manual_review, feedback      |

---

### Fraud Scoring Signals

```python
def score_transaction(transaction, user_history, device):
  score = 0

  # Signal 1: Amount deviation (unusual amount = higher risk)
  avg_amount = user_history.avg_transaction_amount
  amount_deviation = (transaction.amount - avg_amount) / avg_amount
  if amount_deviation > 2:  # >2x average
    score += 20
  elif amount_deviation > 1:  # >1x average
    score += 10

  # Signal 2: Location deviation (new location = higher risk)
  last_location = user_history.last_transaction_location
  distance_km = haversine(last_location, transaction.location)
  time_since_last = now - user_history.last_transaction_time

  if distance_km > 500:  # Very far from last transaction
    # Check if physically possible (aviation speed ~900km/hr)
    time_hours = time_since_last / 3600
    travel_speed = distance_km / time_hours if time_hours > 0 else 0
    if travel_speed > 1000:  # Impossible travel
      score += 50
    else:
      score += 15

  # Signal 3: Device anomaly (new device = higher risk)
  if device.device_fingerprint not in user_history.known_devices:
    score += 15
  elif device.first_seen < 7 days ago:
    score += 8

  # Signal 4: Velocity (many transactions in short time = higher risk)
  txns_last_hour = count_transactions_last_hour(user_id)
  if txns_last_hour > 10:
    score += 25
  elif txns_last_hour > 5:
    score += 10

  # Signal 5: Merchant risk (high-risk merchant = higher risk)
  if is_high_risk_merchant(transaction.merchant):  # e.g., casinos, wire transfer
    score += 10

  # Signal 6: Amount round number (fraud often uses round numbers)
  if transaction.amount % 100 == 0 and transaction.amount > 1000:
    score += 5

  # Signal 7: Time of day (unusual times = higher risk)
  hour = transaction.timestamp.hour
  if hour < 6 or hour > 2:  # 2am–6am
    if user_history.avg_transaction_hour is between 9–17:
      score += 8

  # Signal 8: Account age (very new account = higher risk)
  if user.account_age < 7 days:
    score += 15
  elif user.account_age < 30 days:
    score += 5

  return min(score, 100)

def classify(score):
  if score < 20: return "LOW"
  elif score < 50: return "MEDIUM"
  else: return "HIGH"
```

**Did you think of these signals?**

```
_______________________________________
```

---

### Risk Thresholds & Actions

**LOW (<20):** Approve silently, no friction

**MEDIUM (20–50):**

```
Option 1: Approve quietly (monitor in background)
Option 2: Gentle challenge (email receipt, ask to confirm)
Depends on confidence level.
```

**HIGH (>50):**

```
Options:
1. Decline and investigate
2. Request 2FA
3. Contact customer (call/SMS)

Trade-off: Security vs. customer experience.
We use ML to rank which option is best.
```

**Did you stratify?**

```
_______________________________________
```

---

### Handling False Positives

**Problem:** 5% false positive rate = 500,000 customers blocked/day.

**Solution:**

```
1. Improve scoring (add more features, better weighting)
2. Use contextual risk (is customer on known wifi? logged in?)
3. Graduated responses (don't always decline; try challenge first)
4. Feedback loop (user says "that was me" → lower risk score next time)
5. Whitelist trusted patterns (recurring merchants, known amounts)
```

**Example:**

```
Scenario: User tries to buy $5K laptop from new seller in evening.
Score: 35 (MEDIUM)
Action: Don't decline. Instead: "Please confirm this unusual purchase (2FA)"
User: Confirms
Outcome: Approve. Add seller to whitelist. No friction.
```

**Did you think about false positive handling?**

```
_______________________________________
```

---

### Real-Time Requirements

**Latency budget: <100ms**

```
- Feature engineering: 10ms (cache features)
- Model inference: 5ms (pre-compute scores)
- Decision logic: 5ms (thresholds)
- Logging: 80ms (async)

Total: ~100ms
```

**How to achieve this:**

```
1. Pre-compute features (user history, device, merchant risk)
2. Use fast ML models (not deep neural nets; use XGBoost, LightGBM)
3. Cache frequently accessed data (Redis)
4. Async logging (don't block transaction)
5. Batch updates (compute new features every 1 hour, not per-transaction)
```

**Did you think about latency?**

```
_______________________________________
```

---

### Data Quality & Feedback

**Data quality problems:**

```
- Location data is sometimes wrong (GPS error, VPN, proxy)
- Device fingerprinting is imperfect (same device can have diff fingerprints)
- Transaction metadata is sometimes missing or incorrect
- User feedback is delayed (fraud reported days later)
```

**How to handle:**

```
1. Confidence scores (don't trust GPS 100%; use multiple signals)
2. Deduplication (same fraud pattern reported by many users)
3. Feedback loop (update model when user says "fraudulent" or "legitimate")
4. Backtesting (test model on past transactions to measure AUC, false positive rate)
```

**Did you think about data quality?**

```
_______________________________________
```

---

### APIs & Actions

**Action 1: Score Transaction**

```
POST /api/v1/transactions/score
Input: {
  user_id,
  amount,
  merchant,
  location: { lat, lng },
  device_fingerprint,
  timestamp
}
Output: {
  risk_score: 0-100,
  risk_level: "LOW" | "MEDIUM" | "HIGH",
  top_signals: ["impossible_travel", "new_device"],
  recommendation: "APPROVE" | "CHALLENGE" | "DECLINE",
  confidence: 0.89,
  reason: "Impossible travel detected"
}
Side effects: Event logged, features updated
```

**Action 2: Record Feedback**

```
POST /api/v1/transactions/:id/feedback
Input: {
  transaction_id,
  user_feedback: "LEGITIMATE" | "FRAUD",
  user_id,
  timestamp
}
Output: {
  feedback_id,
  model_update_scheduled: true,
  new_score: 15 (re-scored with feedback)
}
Side effects: Model retrained daily using feedback
```

**Action 3: Get User Risk Profile**

```
GET /api/v1/users/:id/risk-profile
Input: { user_id }
Output: {
  account_age,
  avg_transaction_amount,
  known_devices: [...],
  trusted_merchants: [...],
  fraud_history: { count, dates },
  risk_level: "LOW" | "MEDIUM" | "HIGH"
}
Side effects: None (read-only)
```

**Did you design these?**

```
_______________________________________
```

---

### Edge Cases

**Edge case 1: New user (no history)**

```
Handling:
- No baseline to compare against
- Use cohort defaults (what do similar users typically spend?)
- Increase tolerance for unusual transactions
- Lower thresholds for high-confidence fraud signals
```

**Edge case 2: Compromised account (many frauds)**

```
Handling:
- Detect cluster (10+ declines in 1 hour from new locations)
- Immediately block account
- Notify user (email/SMS)
- Flag for investigation
```

**Edge case 3: False positive feedback (user says "legitimate" but it's fraud)**

```
Handling:
- Don't blindly trust user feedback
- Cross-check with other signals
- If 100 users say "legitimate" for same merchant, but it's actually fraud:
  - Don't lower score
  - Instead: investigate merchant
  - Could be collusion (merchant + users)
```

**Edge case 4: Adversarial attacks (fraudsters adapt to our model)**

```
Handling:
- Monitor fraud patterns (are fraudsters avoiding our signals?)
- Iterate model regularly (monthly, not yearly)
- Use ensemble models (don't rely on one signal)
- Add adversarial constraints (e.g., penalize "too perfect" patterns)
```

**Did you think about adversarial attacks?**

```
_______________________________________
```

---

### Security & Privacy

**Who can see what?**

```
User: Their risk score, transactions, feedback history
Analyst: Aggregate fraud statistics (no individual PII)
Investigator: High-risk transactions (with PII, for investigation)
Admin: All data (with audit logging)
```

**Privacy concerns:**

```
1. Don't expose score to competitors (they shouldn't know our model)
2. Don't expose customer data to third parties
3. Encrypt location data (PII)
4. GDPR: User can request data, deletion
```

**Did you think about privacy?**

```
_______________________________________
```

---

### MVP (1 week, not 2)

```
✓ Rule-based scoring (amount deviation + velocity)
✓ Simple decision tree (LOW/MEDIUM/HIGH)
✓ Approve LOW transactions
✓ Decline HIGH transactions
✓ Logging for feedback
```

**NOT in MVP:**

```
✗ ML model (XGBoost, neural net)
✗ Device fingerprinting
✗ Impossible travel detection
✗ Merchant risk modeling
✗ User feedback loop
```

**Why fast MVP?** Fraud is costing $5M/day. Even rough scoring helps.

**Did you scope MVP?**

```
_______________________________________
```

---

### Success Metrics

| Metric              | Baseline | Target   | How to measure              |
| ------------------- | -------- | -------- | --------------------------- |
| Fraud rate          | $5M/day  | <$1M/day | $ lost / $ processed        |
| False positive rate | 5%       | <1%      | Declined legitimate txns    |
| False negative rate | 2%       | <0.5%    | Missed fraud                |
| Latency (p95)       | N/A      | <100ms   | APM tool                    |
| Detection AUC       | N/A      | >0.95    | Backtest on historical data |

**Did you define metrics?**

```
_______________________________________
```

---

## Interviewer Curveballs

### Curveball 1: "Fraudsters are gaming your model. They're now doing transactions just under your threshold."

_Response:_

```
Adversarial adaptation. Fraudsters learned our thresholds.

Fix:
1. Don't rely on single signal (amount)
2. Add other signals (velocity, device, location)
3. Use ensemble (multiple models disagree on small amounts → escalate)
4. Randomize thresholds (don't always block at $1K; sometimes $800, sometimes $1.2K)
5. Monitor fraud patterns (if fraud rate spikes for amounts $900–1100, investigate)

Longer term:
- Retrain model monthly with latest fraud patterns
- Use adversarial ML techniques (train model to be robust to gaming)
```

**Your response:**

```
_______________________________________
```

---

### Curveball 2: "You're blocking too many legitimate customers. Executive says 'reduce false positives by 50% by Friday'."

_Response:_

```
Tension between security and customer experience.

Quick fix (Friday):
1. Raise thresholds (more permissive)
2. Escalate to 2FA instead of declining (gentler)
3. Whitelist trusted patterns (known merchants, regular amounts)

But this increases fraud losses short-term.

Long-term:
- Improve model (better features, not just thresholds)
- Use challenge/friction instead of decline (2FA, email confirm)
- Learn from feedback (model improves over time)

Metric to discuss: It's not just false positives; it's false positives per dollar of fraud prevented. Maybe 1% false positives is fine if we're catching $4M/day fraud.
```

**Your response:**

```
_______________________________________
```

---

### Curveball 3: "Your model has demographic bias. It's declining more minority customers."

_Response:_

```
This is a serious ethical issue.

Investigation:
1. Audit model by demographic
2. Check features: do any corr with demographics? (location, merchant type, device)
3. Check data: is past fraud data biased? (were minorities overpoliced?)
4. Check outcomes: are minority customers actually more likely to commit fraud?

Fix:
- If bias is in features (e.g., "zip code" as proxy for race), remove it
- If bias is in training data, rebalance it
- Add fairness constraint: equal false positive rate across groups
- Monitor post-deployment for continued bias
```

**Your response:**

```
_______________________________________
```

---

## Scoring Yourself

| Dimension                     | You    |
| ----------------------------- | ------ |
| **Ambiguity handling**        | \_\_/5 |
| **Data signals**              | \_\_/5 |
| **Real-time constraints**     | \_\_/5 |
| **False positive trade-offs** | \_\_/5 |
| **Feedback loop**             | \_\_/5 |
| **Ethics & fairness**         | \_\_/5 |
| **Communication**             | \_\_/5 |

**Total: \_\_/35**
