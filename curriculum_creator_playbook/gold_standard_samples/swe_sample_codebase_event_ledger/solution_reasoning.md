# Solution Reasoning — Event Ledger

> 🔒 Open only after you attempt the workbook.

## 0. Clarifying-questions answer key
- **Goal** — *Q:* Correctness of balances or throughput? *A:* Correctness — it's money.
- **Data** — *Q:* Amounts non-negative, direction via `type`? *A:* Yes; `amount >= 0`, `type ∈ {credit, debit}`.
- **Constraints** — *Q:* Delete or compensate? *A:* Append-only; reversals are compensating entries.
- **Scale** — *Q:* In-memory OK? *A:* Yes for the exercise.

## 1. Why this design
- **Entities:** `Event` (the atomic record) and an implicit `Account` keyed by `account_id`. One table, append-only.
- **Storage:** a single insertion-ordered list of events + a `set` of applied idempotency keys.
- **Algorithm:** balance is a *derived* fold over stored events (`credits − debits`), not a mutable counter — so it's always reproducible from the log.
- **MVP:** Levels 1–2 (record + query + balance with edge cases). Idempotency/reversal are L4 extensions.

## 2. Tradeoff table (filled)
| Decision | Option A | Option B | Choice | Why |
|---|---|---|---|---|
| Reversal | delete the original | append a compensating entry | **append** | append-only keeps the ledger auditable and reproducible; deletion destroys history and breaks idempotency reasoning |
| Idempotency check | after validation | **before** validation | **before** | a duplicate key should short-circuit regardless of payload; cheaper and avoids re-validating |
| Malformed events | store and flag | **never store (fail closed)** | **fail closed** | money: a malformed event must never be able to move a balance |

## 3. Failure modes
- **Duplicate delivery:** idempotency key dedupes (`record_event` returns False on a seen key).
- **Out-of-order events:** balance is order-independent for sums, **but** reversal-by-index is fragile if ordering changes — in production you'd reverse by a stable event id, not a positional index (call this out; it's the riskiest assumption).
- **Malformed input:** rejected at the boundary; never stored.

## 4. How to explain it in 90 seconds (model talk track)
"I modeled the ledger as an append-only event log, so a balance is a pure fold over stored events — auditable and reproducible. I validate at the boundary and fail closed, so malformed events can't corrupt a balance. Idempotency is a `seen_keys` set checked before anything else, which makes duplicate delivery a no-op. Reversals are compensating entries, never deletions, so history is preserved. The one thing I'd harden for production is reversing by a stable event id instead of a positional index."

## 5. Strong vs weak answer
- **Weak:** keeps a single mutable `balances[account] += amount` counter and deletes events to reverse. *Why it's weak:* no audit trail; double-delivery double-counts (no idempotency); deletion makes the books unreconcilable; a malformed event that slipped in permanently corrupts the balance. It also conflates "store" with "aggregate," so Level 3's refactor has nothing to encapsulate.
- **Strong:** append-only log + derived balance + `seen_keys` + compensating reversals + fail-closed validation (the reference). *Why it's strong:* every number is reproducible from the log, duplicates are no-ops, and L4 extends L1–L3 **without touching** their behaviour — which is exactly what the codebase round scores.

## 6. Curveball model responses
- **Triple delivery in 50ms →** if each carries the same idempotency key, only the first is applied; the other two return False. If they carry *no* key, that's the bug to flag — you'd require keys for at-least-once delivery.
- **Reversal sent twice →** give the reversal its own idempotency key too; otherwise you over-compensate. (Demonstrates that idempotency must cover *all* mutations, not just the happy path.)
- **"Just delete the bad event" →** push back: deletion breaks auditability and makes historical balances irreproducible; a compensating entry achieves the same net effect while preserving the trail (and is what real ledgers/double-entry systems do).

## 7. Rubric exemplars (calibration)
- **Weak (1–2):** L1 only; mutable counter; no malformed handling; can't explain idempotency.
- **Adequate (3):** L1–L2 pass; append-only; handles unknown account and malformed amount; idempotency partially working.
- **Strong (5):** all four levels green; reversals don't mutate prior events; articulates the index-vs-id production risk unprompted; clean `Ledger` encapsulation after L3.

## 8. Key takeaways / reusable primitives
- **Append-only + derived aggregate** beats a mutable counter for anything auditable (money, inventory, access logs).
- **Idempotency = check a `seen_keys` set before applying** any mutation; cover reversals too.
- **Fail closed** on malformed input at the boundary.
- **Backward compatibility = extend, don't mutate** earlier behaviour (the ICF L4 skill).

## 9. Sources
Codebase/practical-round realism per `company_packs/stripe.md`, `company_packs/atlassian.md`, `company_packs/palantir.md`, and the CodeSignal Industry-Coding-Framework (see `06_role_guide_swe.md` §3). Last verified: 2026 summer.
