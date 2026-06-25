# Drill 3: Fraud Detection System

**Interview difficulty:** ⭐⭐⭐⭐ (Hard)  
**Estimated time:** 45 minutes  
**Topics:** Risk scoring, multi-signal anomaly detection, false positives, real-time decisions

---

## The Prompt

> A fintech company is losing $2M annually to fraud. You're asked to design a system that identifies suspicious transactions in real-time (< 100ms decision) and decides whether to block, challenge (ask for 2FA), or allow each transaction. The system should reduce fraud by 50% while keeping false positives under 2% (to avoid customer frustration).

---

## Clarifying Questions

1. **What types of fraud are we catching?** (Card not present, account takeover, money laundering, refund fraud, etc.)
2. **What's the transaction volume?** (Maybe 10M transactions/day; need sub-100ms latency)
3. **Can we block transactions?** (Yes, but high false positive rate loses customers)
4. **What data do we have?** (Transaction amount, user history, device, merchant, location, time, IP)
5. **How do we measure success?** (Fraud $$ prevented vs customer complaints)
6. **Do we learn from feedback?** (If customer disputes, we update model)
7. **What's the cost of a false positive?** (Customer calls support, might churn)
8. **What's the cost of a false negative?** (Chargebacks, fraud $$$, regulatory fines)

---

## Expected Decomposition (Abbreviated)

### Scoring Signals

Each transaction scored on:

1. **Amount anomaly** – Is this amount unusual for this user?
2. **Device anomaly** – Is this a new device or stolen device?
3. **Location anomaly** – Did user travel impossibly fast?
4. **Merchant risk** – Is this a high-risk merchant category?
5. **Velocity** – Too many transactions in short time?
6. **Time anomaly** – Is this outside user's normal activity hours?

### Risk Score Formula

```
risk_score = 0
risk_score += 3 * amount_anomaly_score  # Amount is high signal
risk_score += 2 * device_risk_score
risk_score += 2 * location_risk_score
risk_score += 1 * merchant_risk_score
risk_score += 1 * velocity_score
risk_score += 1 * time_anomaly_score

# Weighted from 0–10
risk_score = min(10, risk_score / normalization_factor)

if risk_score >= 8:
    action = "BLOCK"
elif risk_score >= 5:
    action = "CHALLENGE" (ask for 2FA)
else:
    action = "ALLOW"
```

### State Machine

```
Transaction:
    received → scored → action_taken (BLOCK/CHALLENGE/ALLOW) → resolved (success/dispute)
```

### Edge Cases

- **False positive** – User blocked, complains, we apologize
- **User in new country** – Location anomaly high, but legitimate travel
- **Retry attack** – Many rapid declined transactions
- **Account takeover** – Sudden change in user behavior
- **Data stale** – User history unavailable, must gracefully degrade

### Metrics

| Metric              | Baseline | Target     |
| ------------------- | -------- | ---------- |
| Fraud detected      | 40%      | 70%+       |
| False positive rate | 5%       | < 2%       |
| Latency (p99)       | N/A      | < 100ms    |
| User satisfaction   | N/A      | > 4.5/5    |
| Chargebacks         | $2M/year | < $1M/year |

### MVP

- Basic scoring (5 signals)
- Simple thresholds (BLOCK > 8, CHALLENGE 5–8, ALLOW < 5)
- Real-time transaction stream processing
- No ML (rule-based only)
- Manual review queue for CHALLENGE actions

### V2

- ML model instead of rules
- Feedback loop: learn from disputes
- Device fingerprinting
- Merchant reputation system
- Geographic velocity checks

---

## Key Takeaways

This is a **trade-off problem**. High fraud detection requires high false positives. Good system designers balance:

- Precision (few false alarms) vs Recall (catch all fraud)
- Simplicity (easy to explain to users) vs Accuracy (complex model)
- Latency (must be < 100ms) vs Accuracy (more data = slower)

---

## Rubric Focus

1. **Signal identification** – Did you identify the 5–6 key risk signals?
2. **Scoring design** – How do you combine signals into one score?
3. **Trade-off discussion** – Did you acknowledge false positive / false negative trade-off?
4. **Real-time feasibility** – Can your system decide in < 100ms?
5. **Feedback loop** – How do you improve over time (learn from disputes)?

---

## Next Steps

1. Complete `python/fraud_scoring.py`
2. Implement scoring function with all signals
3. Test with edge cases (new card, travel, retry attack)
4. Read solution in `solutions/03_fraud_detection_solution.md`
