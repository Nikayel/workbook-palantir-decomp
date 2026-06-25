Status: Spec incomplete — fill in all blank fields before writing the memo

# Scenario
Partners building on your payments platform need to know when things happen — a payment succeeds, a dispute opens, a payout lands — **without polling your API every few seconds**. Today they poll, which is slow, wasteful, and misses events. You're the Technical PM. Design the **Events + Webhooks API** that lets partners reliably consume events. The network is unreliable: deliveries can be **duplicated or dropped**, and partners will **retry**. Your design must make retries safe and keep integrations working as the product evolves.

> Deliverable is a **design + written memo**, not code. You are scored on technical fluency, tradeoffs, and clarity — not implementation.

## 🪜 Milestones — check them off as you go
This track ships a **spec + memo, not code** — so M4 is "artifact complete & self-checked against the model answer."
- [ ] M1 · Scoped — clarifying questions + assumptions written
- [ ] M2 · Decomposed — entities + the polling bottleneck identified
- [ ] M3 · Designed — endpoints, idempotency, signatures, versioning decided
- [ ] M4 · Built — `artifacts/api_design_scaffold.md` filled **and** the ≤250-word memo written
- [ ] M5 · Defended — survived all 3 curveballs out loud
- [ ] M6 · Ready — self-graded ≥ 32/40 (incl. the writing row)

# Part 0: Forethought
Goal (one sentence): Design an events/webhooks API that is reliable, safe to retry, and stable for years.
Target time: 75 minutes
Confidence before starting (1–5): [blank]

# Part 1: Clarifying questions
Goal:
> Are we optimizing for delivery reliability or lowest latency?
Question: [blank]
Assumption: I'll assume **reliability first** (at-least-once delivery) — a missed dispute event is worse than a slightly late one.

Users:
> Who integrates — partner engineers? How sophisticated?
Question: [blank]
Assumption: I'll assume partner **developers** with varying skill; the API must be hard to misuse.

Data:
> What's an "event"? Is it immutable once emitted?
Question: [blank]
Assumption: I'll assume events are **immutable, append-only**, each with a stable id and type.

Constraints:
> Must we never break existing integrations?
Question: [blank]
Assumption: I'll assume **backward compatibility is sacred** — versioning must be additive.

Scale:
> Volume of events/sec; fan-out per partner?
Question: [blank]
Assumption: I'll assume high volume; an events **list endpoint** must paginate by cursor, not offset.

# Part 2: Decomposition
Current workflow:
1. Partner polls `GET /charges` on a timer.
2. They diff against last-seen state to infer what changed.
3. They miss events between polls and hammer the API.

Bottleneck:
1. Polling — high latency, wasted load, missed/duplicated state.

Core entities:
*(Tutorial: nouns, not properties.)*
1. Event
2. WebhookEndpoint (a partner's registered URL)
3. DeliveryAttempt

State transitions (for a DeliveryAttempt):
1. PENDING → DELIVERED (2xx from partner)
2. PENDING → FAILED → RETRYING → (max retries) → DEAD_LETTER

> 🚩 Checkpoint M2 · Decomposed — you should now have **Event, WebhookEndpoint, DeliveryAttempt** as entities and **polling** as the bottleneck. Stuck? The bottleneck is the thing that makes partners hammer your API and still miss events.

# Part 3: API contract design  ← the core of a Technical-PM lab
Fill the worked example, then complete the blanks. The full spec goes in `artifacts/api_design_scaffold.md`.

## The Event object (worked example — a Tier-1 model)
```json
{
  "id": "evt_1a2b3c",
  "type": "payment.succeeded",
  "created": 1730000000,
  "api_version": "2026-06-01",
  "data": { "object": { "id": "pay_99", "amount": 1200, "currency": "usd" } }
}
```
Why these fields: a **stable `id`** (idempotency on the consumer side), a **`type`** for routing, **`created`** for ordering, **`api_version`** so the payload shape is pinned, and a nested **`data.object`** so new object fields are additive.

## Endpoints (complete the blanks)
| Method + path | Purpose | Key design choice |
|---|---|---|
| `GET /v1/events?limit=&starting_after=` | list/replay events | **cursor** pagination (`starting_after=evt_id`), not offset — [blank: why?] |
| `POST /v1/webhook_endpoints` | register a partner URL | returns a **signing secret** — [blank] |
| (delivery, server→partner) `POST {partner_url}` | push an event | signed with `Stripe-Signature` header — [blank: what does the partner verify?] |

## Named design decisions
### Idempotency (safe retries)
> Partners (and you) will retry. How do you make a `POST` safe to repeat?
[blank — idempotency key on writes; the consumer dedupes on `event.id`; explain both sides]

### Delivery semantics + retries
> At-least-once or exactly-once? What's the retry policy?
[blank — at-least-once + exponential backoff + max attempts → dead-letter; consumer must be idempotent]

### Signature verification (auth)
> How does a partner know the webhook really came from you?
[blank — HMAC the payload with the endpoint's signing secret; include a timestamp to prevent replay]

### Versioning (don't break integrations "for 10 years")
> A field must change shape. How do you ship it without breaking anyone?
[blank — pin `api_version` per account/endpoint; additive-only changes; never repurpose a field]

## Tradeoff table
| Decision | Option A | Option B | Choice | Why |
|---|---|---|---|---|
| Notify partners | polling | webhooks (push) | [blank] | [blank] |
| Pagination | offset/page | cursor | [blank] | [blank] |
| Delivery | exactly-once | at-least-once + idempotency | [blank] | [blank] |

> 🚩 Checkpoint M3 · Designed — you've decided push-vs-poll, the idempotency mechanism, signature verification, and the versioning policy. Stuck? Each "Named design decision" above must have a one-line answer before you write the spec.

# Part 4: Produce the artifacts
1. Complete `artifacts/api_design_scaffold.md` (the spec).
2. Write a **≤250-word Stripe-style memo** here connecting each major decision to **second-order developer impact** (trust, integration effort, fewer support tickets) — short declarative sentences, descriptive headings, surfaced tradeoffs, zero fluff:

> **Memo:** [blank]

# Part 5: Reasoning write-up
Why webhooks over polling? [blank]
Why at-least-once + consumer idempotency instead of exactly-once? [blank]
Why is the events-list (replay) endpoint the right MVP companion to webhooks? [blank]
What would you NOT build first? [blank]
What breaks if a partner's endpoint is down for an hour? [blank]
What needs to be audited? [blank]
What needs permissions/secrets? [blank]
Real-time vs batch? [blank]
Riskiest assumption? [blank]

# Part 6: Interview simulation
## 90-second talk track
"I'd replace polling with signed webhooks plus a replayable events endpoint, and make delivery at-least-once so reliability doesn't depend on the partner being up… [blank]"

## Curveballs (answer out loud)
Curveball 1: A partner complains they processed the same payout twice. Whose bug is it, and how does your design help?
Your response: [blank]

Curveball 2: You must add a field to the event payload next quarter. How do you ship it without breaking 10,000 integrations?
Your response: [blank]

Curveball 3: Explain idempotency to a non-engineer partner-success teammate in two sentences.
Your response: [blank]

# Part 7: Self-grade + reflection
Score 1–5 (Technical-PM rubric from `rubric_bank.md` + a Stripe writing row).

Technical fluency: __/5
Architecture tradeoffs: __/5
Build-vs-buy / API choices: __/5
Scale / reliability: __/5
Communicates with engineers: __/5
Translates to non-technical: __/5
Handling ambiguity: __/5
**Writing clarity & rigor (memo): __/5**

Total: __ / 40

One thing I did well: [blank]
One thing I missed: [blank]
Confidence now (1–5): [blank]   ← compare to your Part 0 prediction.
Lowest rubric row → my next action: [blank]

## ✅ You're ready when…
- [ ] You go scenario → a complete spec + memo in **< 60 min** without the hints.
- [ ] You can explain idempotency, at-least-once delivery, and additive versioning **out loud** without notes.
- [ ] Your memo ties each decision to **second-order developer impact** (trust, fewer tickets), not revenue.
- [ ] You self-grade ≥ 32/40 (incl. the writing row) on **two** attempts running.
> Any unchecked box is your next rep. Re-run cold and timed until all four are checked.
