# Flashcards — Stripe TPM Lab 01: Payments API Design

---

**Card 01 — Idempotency Key: Definition and Implementation**

Q: What is an idempotency key? How does Stripe implement it?

A: An **idempotency key** is a unique string supplied by the client in a request header. If the same key is sent in a subsequent request, the server returns the cached response from the first request without re-processing.

Stripe's implementation:
1. Client generates a UUID and sends: `Idempotency-Key: my-uuid-here`
2. Stripe stores: `(api_key, idempotency_key) → response body`
3. On retry with same key: return cached response, no re-execution
4. Keys expire after 24 hours
5. Same key with different parameters → `400 invalid_request_error`

Why it matters: prevents double-charges and double-resource-creation on network timeouts.

---

**Card 02 — Webhook Signing with HMAC**

Q: How does Stripe sign webhooks, and how does the merchant verify them?

A:
Stripe signs every webhook payload using HMAC-SHA256:

1. Stripe concatenates: `{timestamp}.{raw_payload_body}`
2. Computes: `HMAC-SHA256(signing_secret, concatenated_string)`
3. Sends header: `Stripe-Signature: t={timestamp},v1={signature}`

Merchant verification:
```python
import hmac, hashlib, time

def verify_webhook(payload_body, sig_header, signing_secret):
    elements = dict(item.split("=") for item in sig_header.split(","))
    timestamp = elements["t"]
    signature = elements["v1"]
    
    signed_payload = f"{timestamp}.{payload_body}"
    expected = hmac.new(
        signing_secret.encode(), signed_payload.encode(), hashlib.sha256
    ).hexdigest()
    
    if not hmac.compare_digest(expected, signature):
        raise ValueError("Invalid signature")
    
    if abs(time.time() - int(timestamp)) > 300:  # 5-minute tolerance
        raise ValueError("Timestamp too old — replay attack?")
```

---

**Card 03 — Exponential Backoff Retry Logic**

Q: How should a webhook system retry failed deliveries?

A: Use **exponential backoff with jitter**:

| Attempt | Delay |
|---|---|
| 1 | 5 seconds |
| 2 | 30 seconds |
| 3 | 5 minutes |
| 4 | 30 minutes |
| 5 | 2 hours |
| 6 | 5 hours |
| 7 | 10 hours |
| 8+ | Up to 72 hours |

After max retries: mark event as `failed`. Allow merchant to query missed events via `GET /v1/events`. The merchant must make their webhook handler **idempotent** (because at-least-once delivery means they may receive the same event twice).

---

**Card 04 — Additive-Only Versioning Principle**

Q: What is the additive-only versioning rule and why is it the only safe approach for a 10-year API?

A: **You may ONLY add to an API. You may never remove or rename.**

Safe changes (additive):
- Add a new optional field to a response
- Add a new optional field to a request body
- Add a new endpoint
- Add a new event type
- Add a new enum value (with care)

Unsafe changes (breaking):
- Remove a field
- Rename a field
- Change a field's type (int → string)
- Change the meaning of an existing enum value
- Change a required field to optional (can break validation logic)

Why: clients parse responses and may hardcode field names, types, and enum values. Any breaking change silently corrupts client data.

Stripe's versioning: `Stripe-Version: 2024-01-01` header. New versions released annually. Old versions maintained for years. Breaking changes require advance deprecation notice.

---

**Card 05 — Cursor vs Offset Pagination**

Q: Why does Stripe use cursor pagination instead of offset/page-number pagination?

A: **Offset pagination failure mode**: if new records are inserted between fetching page 1 and page 2, the offset shifts and you either skip records or see duplicates.

Example: offset=10, limit=10. If 2 new records are inserted after you fetch page 1, page 2 starts at the wrong position.

**Cursor pagination solution**: each response includes a cursor (typically the `id` of the last item). The next request uses `starting_after={cursor_id}`. The server returns records AFTER that id, regardless of insertions.

Stripe's convention:
```json
{
  "data": [...],
  "has_more": true,
  "url": "/v1/payment_links"
}
```
Next page: `GET /v1/payment_links?starting_after=pl_last_id`

---

**Card 06 — PaymentLink Resource Model**

Q: What are the essential fields in a PaymentLink resource?

A:
```
PaymentLink:
  id:            "pl_xxx"           — Stripe-style prefixed ID
  url:           "buy.stripe.com/x" — generated shareable URL
  amount:        5000               — cents
  currency:      "usd"              — ISO 4217
  status:        "active"           — enum: active | expired | archived
  merchant_id:   "acct_xxx"         — Stripe account ID
  description:   "Conf ticket"      — optional label
  payment_count: 0                  — times paid (for analytics)
  created_at:    1700000000         — Unix timestamp
  metadata:      {}                 — freeform key-value for merchant use
```

Note: `expires_at` is NOT in v1 — it's planned for a future additive version.

---

**Card 07 — Double-Entry Ledger Invariant**

Q: What is the double-entry ledger invariant and why does it matter for Stripe?

A: Every financial transaction must have matching debit and credit entries. The sum of all debits must equal the sum of all credits. This prevents money from being created or destroyed.

In a payment API context:
- When a charge succeeds: debit the customer's payment method, credit the merchant's Stripe balance
- When a refund succeeds: debit the merchant's Stripe balance, credit the customer's payment method

If a bug causes a charge to be recorded without its corresponding ledger entries, Stripe's books don't balance. This is caught by reconciliation jobs that run continuously. API idempotency protects this invariant by preventing duplicate charge records.

---

**Card 08 — Stripe API Date Versioning (YYYY-MM-DD)**

Q: How does Stripe's date-based API versioning work?

A:
1. Every API request includes a version: `Stripe-Version: 2024-01-01`
2. The version pins the request to the behavior of that date's API spec
3. New accounts default to the latest version
4. Existing accounts stay on their pinned version until manually upgraded
5. Stripe maintains backwards compatibility for old versions indefinitely (with sunset notices for very old ones)
6. In the Stripe Dashboard: each API key can be pinned to a version

For this lab: version the Payment Links API as `2024-01-01`. When you add `expires_at` next year, release it as `2025-01-01`. Clients on `2024-01-01` see null for that field; clients on `2025-01-01` can set/read it.

---

**Card 09 — Event Delivery Guarantees (At-Least-Once)**

Q: What is "at-least-once" delivery and what does it require from webhook consumers?

A: **At-least-once delivery**: the system guarantees every event is delivered at least once. It does NOT guarantee exactly-once delivery. Network issues, retries, and infrastructure failures mean the same event may be delivered multiple times.

What this requires from webhook consumers:
1. Make your handler **idempotent**: processing the same event twice produces the same result
2. Track event IDs you've processed (in your own database) and skip duplicates
3. Never assume "I only get this once"

Alternative: **at-most-once** (no retries) — you might miss events. Not acceptable for payment notifications.

Ideal: **exactly-once** — technically impossible in distributed systems without a distributed transaction. Approximated by at-least-once + idempotent consumers.

---

**Card 10 — What Makes an API Last 10 Years**

Q: Name the five properties that allow a payment API to survive 10 years without breaking clients.

A:
1. **Additive-only changes**: never remove or rename fields; only add new optional ones
2. **Stable resource names**: `payment_links` today = `payment_links` in 10 years; no renames
3. **Explicit versioning**: clients pin to a version; new versions don't affect old ones
4. **No semantic changes**: the meaning of `status: "succeeded"` cannot change
5. **Forward-compatible parsers**: clients should ignore unknown fields gracefully (most JSON parsers do this by default)

Bonus: **Deprecation ceremony** — when you must eventually break something, announce it 12-18 months in advance, provide a migration guide, and give clients a sunset date.

Stripe's track record: some versions from 2014 are still supported in 2024. The cost is engineering maintenance; the payoff is merchant trust.
