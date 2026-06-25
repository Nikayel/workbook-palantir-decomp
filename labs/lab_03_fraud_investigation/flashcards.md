# Flashcards — Fraud Investigation

> Review **day 1 → 3 → 7 → 14**. Reset to day 1 on a miss.
> Cover each answer before reading. These are free-recall — no peeking.

---

**Q:** What is graph-based fraud detection and what two entities are the nodes?
**A:** Graph-based fraud detection models relationships between entities as a graph and traverses it to find connected suspicious accounts. In credit card fraud, the two primary node types are Accounts (or customers) and Transactions. Edges connect accounts that share an IP, device, phone number, or address — shared attributes that humans wouldn't normally share unless one actor controls many accounts.

---

**Q:** What is entity linking in a fraud context and why is it harder than a simple JOIN?
**A:** Entity linking is the process of determining that two records refer to the same real-world entity even when identifiers differ (e.g., "Jon Smith" and "Jonathan Smith" at the same address). It is harder than a JOIN because the match is probabilistic, not exact. You need fuzzy matching, a scoring threshold, and human review for borderline cases.

---

**Q:** What are the four DB lifecycle states of a fraud alert, in order?
**A:** GENERATED → QUEUED → UNDER_REVIEW → RESOLVED (with sub-states CONFIRMED_FRAUD or FALSE_POSITIVE). QUEUED is important — it distinguishes alerts that exist in the system from alerts that an analyst has actively started working. Without it, you cannot measure queue depth or analyst throughput.

---

**Q:** How would you prioritize an analyst's fraud review queue to maximize dollars recovered per hour?
**A:** Sort descending by (risk_score × transaction_amount). This ensures analysts see the highest-impact cases first. Optionally cap the queue size (e.g., top 200 per day) to prevent alert fatigue — showing 10,000 alerts is the same as showing none.

---

**Q:** What is a confidence score vs a hard rule, and when should you use each in a fraud system?
**A:** A hard rule fires a definitive action when a condition is met (e.g., "block any transaction over $10,000 in a country the customer has never visited"). A confidence score (0.0–1.0) represents the model's probability that a transaction is fraudulent and routes it to a queue for human review. Use hard rules for clear-cut, high-stakes cases. Use confidence scores where the signal is ambiguous and you want a human to make the final call.

---

**Q:** What is alert fatigue and what are two concrete mitigations?
**A:** Alert fatigue occurs when analysts receive so many alerts that they start ignoring or auto-approving them without reviewing. Two mitigations: (1) Raise the threshold — only surface alerts with risk_score > 0.85 instead of > 0.5, accepting that some fraud slips through in exchange for higher analyst engagement. (2) Deduplicate — if an account triggers 15 alerts in 10 minutes, surface one consolidated alert for the account, not 15 individual ones.

---

**Q:** What explainability requirement applies to fraud decisions, and what does "explainable" mean technically?
**A:** Regulators (e.g., FCRA in the US) require that if a financial institution takes an adverse action (declines a transaction, closes an account), they must be able to explain the specific factors that led to that decision. Technically, "explainable" means storing the top-N features and their weights at decision time (not just the score), so a human can reconstruct the reasoning — even if the underlying model changes later.

---

**Q:** What must every fraud audit log entry contain for regulatory compliance?
**A:** (1) analyst_id — who reviewed it, (2) decision — CONFIRMED_FRAUD or FALSE_POSITIVE, (3) decision_at — timestamp, (4) risk_score_at_review — the score that was shown, (5) evidence_snapshot — the features used to generate the score. The evidence snapshot is critical: if the model is retrained, you need to know what the model saw when the original decision was made.

---

**Q:** How do you prevent a graph traversal from running forever when looking for linked fraud accounts?
**A:** Track a `visited` set. Before processing any node, check if it is already in `visited`. If it is, skip it. This breaks cycles and bounds the traversal. Also set a maximum depth (e.g., 3 hops) — fraud rings rarely require traversal deeper than 3 degrees, and deeper traversal produces noisy, low-confidence links.

---

**Q:** When should fraud transaction scoring be real-time vs batch, and what is the decision criterion?
**A:** Real-time (< 200ms) for transaction decisions where you can still block the charge before it clears — this requires a lightweight scoring function (rule engine or a pre-trained model, not a full graph traversal). Batch (nightly) for deep graph analysis, pattern mining, and model retraining — these are too slow for inline scoring but surface patterns that improve real-time rules over time.
