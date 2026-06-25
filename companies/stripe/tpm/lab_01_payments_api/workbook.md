Status: Ready — work through all parts in order

# Lab 01 · Payments API Design — Payment Links (FLAGSHIP)
**Stripe TPM · Tier 1→2 · ~75 minutes**

---

## 🪜 Milestones

- [ ] M1 · Scoped — clarified: who creates Payment Links (merchants), who pays (customers), what events to send
- [ ] M2 · Resources modeled — PaymentLink, Payment, and Event entities defined with full attributes
- [ ] M3 · API designed — CREATE, GET, LIST endpoints + webhook event schema written out
- [ ] M4 · Idempotency handled — idempotency key design explained clearly in the memo
- [ ] M5 · Versioning addressed — explained how this API can be versioned for 10 years
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Scenario

You're in a **Stripe Technical PM screen**. The interviewer says:

> "You're designing the API for a new Stripe product: **Payment Links** — a no-code way for businesses to accept payments via a shareable URL. A merchant creates a link, shares it, and customers pay through it without writing any code.
>
> Design the API that powers this feature. It should handle idempotency, support webhooks for payment events, and be versioned to last at least 10 years. Deliver your design as a Stripe-style memo."

This is the most technically demanding lab in the curriculum. You're being evaluated on:
- API design rigor (resources, endpoints, contracts)
- Financial system thinking (idempotency, correctness guarantees)
- Communication (can you write a Stripe-quality memo?)
- Long-term thinking (how do you design an API that won't break in 10 years?)

---

## Part 0: Forethought

Before reading anything — 4 minutes:

1. Who are the two kinds of "users" in this product? What does each one need from the API?
   [blank — merchants vs customers; merchants need CRUD on Payment Links; customers need to see the link and pay]

2. What are the three most dangerous things that could go wrong with a payment API?
   [blank — double charges, missing payments, data inconsistency between what merchant sees and what actually happened]

3. What does "versioned to last 10 years" mean in concrete API terms?
   [blank — never remove fields, never rename resources, only add new optional fields, version with a date header]

---

**--- CHECKPOINT: Forethought complete. Move to Part 1. ---**

---

## Part 1: Clarifying Questions (Scope the Problem)

Ask these before designing anything. Write your answers as the interviewer would give them:

**Who creates Payment Links?**
Merchants, via the Stripe Dashboard or the API. [Your response about what this implies for auth and resource ownership: blank]

**Who pays?**
Customers — anyone with the URL. No Stripe account required. [What this implies for the Payment resource: blank]

**What payment methods?**
Cards only for now. [What this implies for the Payment resource: blank]

**What events should we support?**
At minimum: `payment_link.payment.succeeded` and `payment_link.payment.failed`. [What else might we need: blank]

**Can a Payment Link be paid multiple times?**
Yes (e.g., a link for selling a product can be used by multiple customers). [What this implies for the resource model: blank]

**Can a Payment Link expire?**
Yes, eventually. But `expires_at` is a future feature. [What this implies for versioning: blank]

**What currencies?**
USD for now. But design must support multi-currency in future. [What this implies for the amount field: blank]

---

**--- CHECKPOINT: Scope defined. Move to Part 2. ---**

---

## Part 2: Resource Modeling

Define all three resources completely. Fill in the `[blank]` fields — some are provided, some you must add.

**Resource 1: PaymentLink**

```
PaymentLink:
  id:            string    — "pl_xxx" (Stripe-style prefix)
  url:           string    — generated shareable URL (e.g., "buy.stripe.com/xxx")
  amount:        int       — price in cents (e.g., 5000 = $50.00)
  currency:      string    — ISO 4217 code (e.g., "usd")
  status:        enum      — [active, expired, archived]
  merchant_id:   string    — which merchant owns this link
  description:   string    — human-readable label (e.g., "Conference ticket")
  created_at:    timestamp — Unix timestamp
  
  [blank — what else does a Payment Link need?]
  [blank — what field would support a future "expires_at" feature?]
  [blank — what field would let a merchant see how many times it was used?]
```

**Resource 2: Payment**

```
Payment:
  id:               string    — "pay_xxx"
  payment_link_id:  string    — foreign key to PaymentLink
  amount:           int       — amount actually charged (may differ if currency conversion)
  currency:         string
  status:           enum      — [pending, succeeded, failed]
  customer_email:   string    — provided at checkout
  
  [blank — what payment method info should we store?]
                             — (card_last4, card_brand, card_exp_month, card_exp_year)
  [blank — what timestamp fields?]
                             — (created_at, succeeded_at, failed_at)
  [blank — what do we store if payment fails?]
                             — (failure_code, failure_message)
```

**Resource 3: Event**

```
Event:
  id:        string    — "evt_xxx"
  type:      string    — e.g., "payment_link.payment.succeeded"
  created:   timestamp — Unix timestamp
  livemode:  bool      — true = live keys, false = test keys
  data:      object    — { "object": { ... the Payment resource ... } }
```

---

**--- CHECKPOINT: Resources modeled. Move to Part 3. ---**

---

## Part 3: API Contract (The Core TPM Deliverable)

Define every endpoint. This is what you'd write in a Stripe RFC.

### Endpoint 1: Create Payment Link

```
POST /v1/payment_links

Request Headers:
  Authorization: Bearer {sk_live_xxx}
  Idempotency-Key: [blank — where does this go? Header or body? Why?]
                  — Answer: [blank]

Request Body:
  {
    "amount": 5000,          // required — amount in cents
    "currency": "usd",       // required
    "description": "...",    // optional — human-readable label
    [blank — what other optional fields might a merchant want to set at creation?]
  }

Response 200:
  {
    [blank — return the full PaymentLink resource]
  }

Response 400 — Invalid parameters:
  {
    "error": {
      "type": "invalid_request_error",
      "message": "[blank — example: 'amount must be at least 50 cents']"
    }
  }
```

### Endpoint 2: Retrieve Payment Link

```
GET /v1/payment_links/{id}

Path param: id — the PaymentLink id (e.g., "pl_xxx")

Response 200:
  {
    [blank — the PaymentLink resource]
  }

Response 404:
  {
    "error": {
      "type": "invalid_request_error",
      "message": "No such payment_link: 'pl_xxx'"
    }
  }
```

### Endpoint 3: List Payment Links

```
GET /v1/payment_links

Query params:
  limit:           int     — max results to return (default 10, max 100)
  starting_after:  string  — cursor for pagination (Payment Link id)
  status:          string  — filter by status (optional)
  [blank — what other filter might a merchant want?]

Response 200:
  {
    "object":      "list",
    "data":        [ ...array of PaymentLink objects... ],
    "has_more":    bool,
    "url":         "/v1/payment_links",
    [blank — what field enables the next page fetch?]
  }
```

Why cursor pagination instead of offset/page-number pagination?
[blank — hint: what happens with offset pagination if new records are inserted between page 1 and page 2 fetches?]

### Webhook Event Schema

```json
{
  "id": "evt_xxx",
  "object": "event",
  "type": "payment_link.payment.succeeded",
  "created": 1700000000,
  "livemode": true,
  "data": {
    "object": {
      [blank — paste the full Payment resource here]
    }
  },
  "request": {
    "id": null,
    "idempotency_key": null
  }
}
```

Webhook signature header (security):
```
Stripe-Signature: t=1700000000,v1=abc123...
```
How does the merchant verify the signature?
[blank — hint: HMAC-SHA256 of the raw payload + timestamp using the webhook signing secret]

---

**--- CHECKPOINT: API contract defined. Move to Part 4. ---**

---

## Part 4: Critical Concepts — Idempotency and Versioning

### Idempotency

**What is an idempotency key?**
[blank — write 3 sentences: definition, why it matters for payments, how Stripe implements it]

**How does Stripe's idempotency key work mechanically?**

```
Client sends:
  POST /v1/payment_links
  Idempotency-Key: my-merchant-client-generated-uuid-123

Stripe behavior:
  - First call: process the request, store result associated with the key
  - Second call with same key: return the cached response WITHOUT processing again
  - Key expires after: [blank — 24 hours? 7 days?]
  - What happens if the same key is used with DIFFERENT parameters? [blank]
```

**In your Payment Links API specifically:**
Where does the merchant supply the idempotency key for POST /v1/payment_links?
[blank — header: `Idempotency-Key: {uuid}`]

Why is idempotency especially important at creation (not just retrieval)?
[blank — network retries, double-creation of the same payment link]

### Versioning

Stripe uses **date-based API versioning** (e.g., `2024-01-01`). Fill in the answers:

**How does a client pin to a version?**
[blank — `Stripe-Version: 2024-01-01` header, or set at API key level in the dashboard]

**Additive-only rule:**
"You are allowed to: [blank]. You are never allowed to: [blank]."

**Scenario: Next year, you need to add `expires_at` to PaymentLink.**
How do you do this without breaking existing integrations?
[blank — add as an optional field with a default of null; existing clients ignore unknown fields; existing behavior unchanged]

**Scenario: You realize `merchant_id` should have been called `account_id` for consistency.**
Can you rename it?
[blank — NO. Never rename a field in a versioned API. You could ADD `account_id` alongside `merchant_id` (deprecated), then remove `merchant_id` in a major version (with advance notice and migration guide)]

---

**--- CHECKPOINT: Idempotency and versioning complete. Move to Part 5. ---**

---

## Part 5: Write the Stripe-Style Memo

This is the primary PM artifact. Write it in full — not bullet points.

```
TO:      Stripe Engineering
FROM:    [Your Name]
DATE:    [Today's Date]
RE:      Payment Links API Design

═══════════════════════════════════════════════════════

SUMMARY

[1-2 sentences: what problem does Payment Links solve, and what this memo proposes]

[blank]

═══════════════════════════════════════════════════════

PROPOSED API

[3-5 bullets summarizing the key API design decisions: resource structure, key endpoints,
auth model. No full JSON here — just the decisions and their rationale]

[blank]

═══════════════════════════════════════════════════════

IDEMPOTENCY

[2-3 sentences: how idempotency keys work in this API, where merchants supply them,
and what guarantee Stripe provides]

[blank]

═══════════════════════════════════════════════════════

WEBHOOKS

[2-3 sentences: what events exist, what's in the event payload, what delivery guarantees
we provide, how merchants verify authenticity]

[blank]

═══════════════════════════════════════════════════════

VERSIONING

[2-3 sentences: what versioning strategy we use, the additive-only constraint,
and how we'll handle the planned `expires_at` addition next year]

[blank]

═══════════════════════════════════════════════════════

OPEN QUESTIONS

[3-5 items you'd need to resolve before shipping: things like multi-currency support,
payment method expansion, fraud signals, dispute handling, etc.]

[blank]
```

---

**--- CHECKPOINT: Memo written. Move to Part 6. ---**

---

## Part 6: Curveballs

**Curveball 1:**
"A merchant calls `POST /v1/payment_links` with the same idempotency key twice (their server had a network timeout and retried). The first call succeeded. What does Stripe return on the second call? What does the merchant see?"
[blank — the cached response from the first call; the merchant sees a success with the same `pl_xxx` id; no second PaymentLink is created; this is the whole point of idempotency keys]

**Curveball 2:**
"A webhook delivery fails — the merchant's server returns 500. How many times do you retry? With what backoff? What happens if it keeps failing?"
[blank — exponential backoff: 5s, 30s, 5m, 30m, 2h, 5h, 10h, 18h, 24h (varies by provider). After some point: mark webhook as failed, allow merchant to query missed events via the Events API. At-least-once delivery guarantee means you retry until you get a 2xx. The merchant must handle duplicate deliveries idempotently.]

**Curveball 3:**
"A merchant wants to check if a specific payment succeeded without using webhooks. What do you tell them?"
[blank — poll: GET /v1/payments/{pay_xxx} and check status. Or use the Events API: GET /v1/events?type=payment_link.payment.succeeded. But polling is expensive at scale — encourage webhooks. Stripe calls this "pull vs push" — webhooks are push, polling is pull. Both are supported but push is preferred.]

---

**--- CHECKPOINT: Curveballs answered. Move to Part 7. ---**

---

## Part 7: Self-Assessment Rubric

Score yourself honestly. Total = 35 points. Target: ≥ 28 to be ready.

| Dimension | 5 | 3 | 1 | Your Score |
|---|---|---|---|---|
| Technical Fluency | API contract is precise: correct HTTP verbs, status codes, body shapes, header placement of idempotency key | Minor gaps (e.g., forgot the Stripe-Signature header or cursor field) | API contract is incomplete or has significant errors | /5 |
| Architecture Tradeoffs | Cursor vs offset pagination explained with a concrete failure scenario; webhook vs polling tradeoff addressed | One tradeoff explained, others skimmed | Tradeoffs not discussed or incorrect | /5 |
| Build-vs-Buy | Acknowledged Stripe's existing idempotency, webhook, and versioning infrastructure rather than reinventing | Partially leveraged existing patterns | Designed idempotency/webhooks from scratch without referencing Stripe's existing solutions | /5 |
| Scale / Reliability | Addressed: webhook retry logic, at-least-once delivery, idempotent payment processing, cursor pagination stability | Addressed one or two reliability concerns | No reliability discussion | /5 |
| Communicates with Engineers | Memo is precise enough for an engineer to implement from; resource model is unambiguous | Memo has gaps an engineer would need to ask about | Memo is too vague to implement from | /5 |
| Translates to Non-Technical | Could explain this API's value to a merchant (non-technical) in 2-3 sentences without jargon | Partial — some jargon leaked in | Could not explain without API-level detail | /5 |
| Handling Ambiguity | When multi-currency / multi-pay / expiry questions came up, made explicit assumptions and stated the impact | Made assumptions but didn't surface them | Got stuck when requirements were ambiguous | /5 |

**Total: /35**

---

### Reflection

What's the one API design principle you'll internalize from this lab?
[blank]

---

### Ready-When Checklist

- [ ] I can explain what an idempotency key is and why it prevents double-charges, in 3 sentences
- [ ] I can explain cursor pagination vs offset pagination and when each fails
- [ ] I can explain the additive-only versioning rule and give a concrete example
- [ ] I can describe Stripe's webhook signing (HMAC + timestamp) in 2 sentences
- [ ] I can write a clean Stripe-style memo under time pressure
- [ ] I can explain the difference between at-least-once and at-most-once delivery
- [ ] Self-score ≥ 28/35
