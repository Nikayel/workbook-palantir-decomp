# Artifact — Events + Webhooks API spec (fill this in)

> Produce a concrete, partner-facing spec. Concrete fields and status codes, not prose. This is the "code" of a Technical-PM lab.

## 1. The Event object (schema)
```json
{
  "id": "evt_...",            // stable, used for consumer-side dedupe
  "type": "[blank: e.g. payment.succeeded]",
  "created": 0,               // unix ts, for ordering
  "api_version": "YYYY-MM-DD",// pins payload shape
  "data": { "object": { /* the affected resource */ } }
}
```

## 2. List / replay endpoint
```
GET /v1/events?limit=20&starting_after=evt_abc&type=payment.succeeded
-> 200 { "data": [ ...events... ], "has_more": true }
```
- Pagination: **cursor** (`starting_after` = last event id). Why not offset? [blank]
- Filtering: by `type`, time range. [blank]

## 3. Register a webhook endpoint
```
POST /v1/webhook_endpoints  { "url": "https://partner/...", "enabled_events": ["payment.succeeded"] }
-> 201 { "id": "we_...", "secret": "whsec_...", "status": "enabled" }
```
- The `secret` is returned **once** and used to sign deliveries. [blank: why only once?]

## 4. Delivery (server → partner)
```
POST {partner_url}
Headers: Stripe-Signature: t=<ts>,v1=<hmac_sha256(ts + "." + body, secret)>
Body: <the Event object>
Partner returns 2xx to acknowledge.
```
- Verification steps the partner performs: [blank — recompute HMAC, compare, check timestamp freshness]
- Retry policy on non-2xx: [blank — exponential backoff, N attempts, then dead-letter + alert]

## 5. Idempotency on writes (for endpoints partners call)
```
POST /v1/refunds
Headers: Idempotency-Key: <client-generated-uuid>
```
- Server behavior on a repeated key: [blank — return the original result, do not re-execute]
- TTL for keys: [blank]

## 6. Versioning policy
- [blank — additive-only changes; `api_version` pinned per account/endpoint; deprecation window; never repurpose a field]

## 7. Error model
| Status | Meaning | Partner action |
|---|---|---|
| 400 | malformed | fix request |
| 401 | bad/missing signature or key | check secret |
| 409 | idempotency conflict (same key, different body) | [blank] |
| 429 | rate limited | back off (Retry-After) |
| 5xx | transient | retry with backoff |
