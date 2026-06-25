# Solution Reasoning — Idempotent Events + Webhooks API

> 🔒 Open only after you attempt the workbook.

## 0. Clarifying-questions answer key
- **Goal** — reliability first (at-least-once); a missed dispute event is worse than a late one.
- **Users** — partner developers of varying skill → the API must be hard to misuse (safe defaults).
- **Data** — events are immutable, append-only, each with a stable id + type.
- **Constraints** — backward compatibility is sacred; versioning is additive.
- **Scale** — high volume → cursor pagination, not offset.

## 1. Why this design
- **Webhooks (push) + a replayable events endpoint (pull)** together: push for low latency, the list endpoint for catch-up after downtime. Belt and suspenders.
- **Stable `event.id`** lets the *consumer* dedupe; **`Idempotency-Key`** lets the *producer* make writes safe to retry. Idempotency on both sides.
- **At-least-once delivery + consumer idempotency** instead of exactly-once: true exactly-once across a network is impractical; at-least-once + dedupe is the industry-standard, simpler, and more robust.
- **Signature verification** (HMAC with a per-endpoint secret + timestamp) authenticates deliveries and prevents replay.
- **Additive, pinned versioning** (`api_version`) keeps 10,000 integrations working as payloads evolve.

## 2. Tradeoff table (filled)
| Decision | Option A | Option B | Choice | Why |
|---|---|---|---|---|
| Notify | polling | **webhooks (push)** | webhooks | lower latency, less load, fewer missed events; add a replay endpoint for catch-up |
| Pagination | offset/page | **cursor** | cursor | offset drifts and double-counts when new events arrive mid-page; cursor is stable on an append-only log |
| Delivery | exactly-once | **at-least-once + idempotency** | at-least-once | exactly-once across an unreliable network is impractical; dedupe on `event.id` is simpler and robust |
| Versioning | break + migrate | **additive + pinned** | additive | never break a live integration; pin `api_version`, deprecate with a window |

## 3. Failure modes
- **Partner endpoint down 1 hour:** deliveries retry with backoff, then dead-letter; the partner replays via `GET /v1/events` when back up. No data loss.
- **Duplicate delivery:** consumer dedupes on `event.id` → no double-processing.
- **Replay attack:** signature includes a timestamp; reject stale signatures.
- **Payload change:** additive field under `data.object`; old consumers ignore unknown fields.

## 4. Model 90-second talk track
"I'd pair signed webhooks with a replayable events endpoint, so partners get low-latency push but can always catch up after downtime. Delivery is at-least-once and every event carries a stable id, so duplicate deliveries are a no-op on the consumer side. Writes take an idempotency key so retries don't double-charge. Versioning is additive and pinned per account, so payloads can evolve for years without breaking a single integration. The thing I'd watch is signature/timestamp handling — that's where partners get replay bugs."

## 5. Strong vs weak answer
- **Weak:** "Add a webhook that POSTs the event; partners can retry if it fails." *Why it's weak:* no idempotency (retries double-process), no signature (anyone can forge events), no replay path (downtime = lost events), no versioning story (the first payload change breaks integrations). It also says nothing about *developer* impact — the thing Stripe actually scores.
- **Strong:** the reference — push + replay, at-least-once + consumer dedupe, HMAC+timestamp signatures, additive pinned versioning — **and** a memo that ties each choice to fewer support tickets and partner trust. *Why it's strong:* it's the real Stripe model, makes the API hard to misuse, and demonstrates the writing bar.

## 6. Curveball model responses
- **Processed a payout twice →** at-least-once delivery means duplicates are expected; the fix is consumer-side dedupe on `event.id`. Your design *enabled* that by guaranteeing a stable id; you'd point the partner at it (and confirm they're not ignoring the id).
- **Add a field next quarter →** additive change under `data.object`, ship behind a new `api_version`; existing accounts stay pinned to their version and ignore unknown fields; communicate a deprecation window. Zero breakage.
- **Explain idempotency to partner-success →** "It means doing the same thing twice has the same effect as doing it once — so if the network hiccups and we resend a payment instruction, the customer is only charged once."

## 7. Rubric exemplars
- **Weak (1–2):** webhook only; no idempotency/signature/versioning; memo restates the prompt.
- **Adequate (3):** webhooks + idempotency keys + signatures; versioning hand-waved; memo readable but generic.
- **Strong (5):** full design incl. replay + at-least-once + additive pinned versioning; memo connects each decision to second-order developer impact in crisp prose.

## 8. Key takeaways / reusable primitives
- **Push + replay** beats either alone for event delivery.
- **At-least-once + consumer idempotency** is the standard; exactly-once is a trap.
- **Idempotency keys** (producer) and **stable event ids** (consumer) are different tools for the same goal.
- **Sign with HMAC + timestamp**; **version additively and pin it.**
- **Technical PM deliverable = spec + memo, not code**; tie decisions to developer impact.

## 9. Sources
Stripe technical-PM bar, API/idempotency/ledger emphasis, and writing-first culture per `company_packs/stripe.md` and `05_role_guide_technical_pm.md`. Last verified: 2026 summer.
