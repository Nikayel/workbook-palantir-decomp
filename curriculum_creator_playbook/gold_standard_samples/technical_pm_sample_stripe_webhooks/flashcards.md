# Flashcards — Idempotent Events + Webhooks API

> Review day 1 → 3 → 7 → 14. Reset on a miss. Free recall only.

**Q:** Webhooks vs polling — why push, and what do you add for resilience?
**A:** Push = lower latency, less load, fewer missed events. Add a **replayable events list endpoint** so partners can catch up after downtime.

**Q:** Why at-least-once delivery instead of exactly-once?
**A:** Exactly-once across an unreliable network is impractical; at-least-once + **consumer dedupe on a stable `event.id`** is simpler and robust.

**Q:** Two different idempotency tools — producer vs consumer side?
**A:** Producer: an **`Idempotency-Key`** header makes a write safe to retry (server returns the original result). Consumer: dedupe on the **stable `event.id`** for duplicate deliveries.

**Q:** Why cursor pagination, not offset, for an events list?
**A:** On an append-only log, offset drifts and double-counts when new events arrive mid-page; a cursor (`starting_after=evt_id`) is stable.

**Q:** How does a partner verify a webhook is genuine, and avoid replay?
**A:** Recompute an **HMAC** of the body with the endpoint's signing secret and compare; include a **timestamp** and reject stale signatures.

**Q:** Ship a payload change without breaking 10,000 integrations — how?
**A:** **Additive-only** changes, **pin `api_version`** per account/endpoint, deprecate with a window, never repurpose a field.

**Q:** What is the Technical-PM deliverable here, and what is it NOT?
**A:** A **spec + written memo** with tradeoffs — **not** production code. (That's the PM/SWE line.)

**Q:** Stripe-style memo — what makes it score well?
**A:** Short declarative sentences, descriptive headings, surfaced tradeoffs, and decisions tied to **second-order developer impact** (trust, fewer tickets), not topline revenue.

**Q:** Idempotency in one sentence for a non-engineer?
**A:** Doing the same operation twice has the same effect as doing it once (so a retried charge bills the customer only once).
