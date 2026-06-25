# Flashcards — Stripe SWE Lab 01: Integration Lab

---

**Card 01 — Integration Round Mindset (Read Before Write)**

Q: What is the most important habit for Stripe's integration round?

A: Read ALL the existing code before writing a single line. Stripe interviewers are specifically watching for this signal. Writing before reading suggests recklessness. Reading first shows:
1. You understand the existing patterns (authentication, error handling, logging)
2. You'll match those patterns in your new code
3. You won't introduce inconsistencies (e.g., different error type, different log format)

The integration round is a test of professional engineering behavior, not just algorithmic skill.

---

**Card 02 — HTTP Status Codes (400 vs 402 vs 500)**

Q: What do 400, 402, and 500 mean in a payment API context?

A:
- **400 Bad Request**: Client error — invalid parameters, malformed request, no such resource. Example: charge_id doesn't exist. Fix: don't retry, fix the request.
- **402 Payment Required**: Domain-specific error — payment action failed. Example: refund exceeds original charge. Fix: don't retry, surface error to merchant.
- **500 Internal Server Error**: Server error — transient problem. Example: database outage. Fix: retry with backoff (but careful in payment context — may have partially processed).
- **429 Too Many Requests**: Rate limit hit. Fix: exponential backoff.

---

**Card 03 — Partial vs Full Refund API Pattern**

Q: How does the Stripe refund API distinguish partial from full refunds?

A: Full refund: omit the `amount` field from the request body entirely.
Partial refund: include `amount` in cents (e.g., `{"charge": "ch_xxx", "amount": 500}`).

In Python implementation:
```python
body = {"charge": charge_id}
if amount_cents is not None:
    body["amount"] = amount_cents
```
This pattern — "include field only if provided" — is common in REST APIs where omitting a field means "use the default."

---

**Card 04 — Idempotency in Payment APIs**

Q: What is idempotency and why does it matter for payment APIs?

A: An operation is **idempotent** if calling it multiple times produces the same result as calling it once. For payment APIs, idempotency prevents double-charges or double-refunds on network retries.

Stripe's mechanism: the `Idempotency-Key` request header. If the same idempotency key is sent twice, Stripe returns the cached response from the first request — it does NOT process a second refund.

```python
headers = {
    "Authorization": f"Bearer {api_key}",
    "Idempotency-Key": f"refund-{charge_id}-{amount_cents}"  # unique per intent
}
```

Without idempotency keys, a network timeout on a refund could cause you to refund twice.

---

**Card 05 — Error Handling Hierarchy**

Q: What's the error handling hierarchy for a payment integration?

A: Layer from innermost to outermost:
1. **Input validation** (before any API call): check amount > 0, charge_id not empty
2. **API error response** (400, 402): extract error message, raise domain exception
3. **Network error** (timeout, connection refused): catch `requests.exceptions.RequestException`, decide: retry or raise?
4. **Unexpected error** (500): log, raise; DO NOT silently swallow

Payment systems should be loud about failures, not quiet. Silent failures in financial systems cause ledger discrepancies.

---

**Card 06 — Why Validate Before Calling API**

Q: Why validate `amount_cents > 0` before calling the Stripe API, when the API would reject it anyway?

A: Three reasons:
1. **Speed**: fail fast locally instead of paying API round-trip latency
2. **Clarity**: your error message can be more specific than the API's ("`amount_cents` must be positive" vs Stripe's generic "invalid_request_error")
3. **Auditability**: local validation can be logged and monitored separately from API failures
4. **Cost**: some APIs charge per request; avoiding invalid calls saves money at scale

Stripe's philosophy: be explicit about preconditions. Don't rely on the API to catch what you could have caught locally.

---

**Card 07 — Logging in Payment Systems (Audit Trail)**

Q: Why is the transaction log important in a payment system? What should it contain?

A: The transaction log is an **audit trail** — the source of truth for what happened when disputes arise. In a real system, it feeds:
- Customer support ("did the refund go through?")
- Finance reconciliation (debits match credits?)
- Fraud detection (unusual refund patterns?)

Minimum log entry for a refund:
```json
{"type": "refund", "id": "re_xxx", "amount_cents": 500, "charge_id": "ch_xxx", "timestamp": 1234567890}
```

Log ONLY on success (like the existing `process_charge` does). Logging failed transactions is a separate concern, usually to an error monitoring system, not the financial ledger.

---

**Card 08 — Stripe Writing Culture**

Q: What does Stripe mean by "writing-first" in an engineering context?

A: At Stripe:
- Design decisions are written in **RFCs** (Request for Comments) before coding begins
- Code reviews include **written explanations** of design trade-offs
- Features are described in **internal memos** before launch
- API designs go through **written versioning proposals**

In interviews, this manifests as: your code should read like clear prose. Variable names are complete words. Function docs match behavior. Your verbal explanation of your design is as important as the design itself.

The interviewer is evaluating: "Would I want to read this person's code in 2 years?"

---

**Card 09 — Refund Idempotency Key Concept**

Q: Design an idempotency key for `process_refund(charge_id, amount_cents)`. What makes a good key?

A: A good idempotency key is:
- **Unique per intent**: represents exactly one logical operation
- **Deterministic**: the same intent always generates the same key
- **Human-readable**: helps debugging

For refunds: `f"refund-{charge_id}-{amount_cents}"` works if you intend exactly one refund of that amount per charge. But what if you want to allow multiple partial refunds of the same amount? Then include a nonce or timestamp.

Trade-off: too broad a key (just `charge_id`) prevents any second refund. Too narrow (include timestamp) defeats idempotency on retries.

---

**Card 10 — Production Code Signals (No Hacks)**

Q: What distinguishes "production-quality" integration code from "just working" code in Stripe's evaluation?

A: Stripe's checklist (inferred from culture and interview feedback):
1. **Error handling is complete**: all non-200 responses handled, not just 400
2. **Input validation is explicit**: preconditions stated and checked before API call
3. **No magic strings or numbers**: `"charge"` in body, not `"chg"` or wrong field name
4. **Follows existing conventions**: same error type (`PaymentError`), same log format, same auth header
5. **Code reads like documentation**: function docstring matches actual behavior
6. **No resource leaks**: file handles closed, connections returned to pool
7. **No silent failures**: every exception either handled meaningfully or re-raised
