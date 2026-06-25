Status: Spec incomplete — fill in all blank fields before implementing

# Scenario
You've been dropped into a small service that tracks money movement for a marketplace. Every payout, charge, and refund is an **event** (`credit` or `debit`) against an account. The current code is a stub. Your job is to grow it into a working **event ledger** in four increments — exactly how a feature evolves in a real codebase. Upstream is messy: some events arrive **malformed**, and the network sometimes **delivers the same event twice**, so the same payout must not be applied twice.

## 🪜 Milestones — check them off as you go
You'll watch this build from nothing to a working, tested system. Each code milestone is gated by a **test group going green**.
- [ ] M1 · Scoped — clarifying questions + assumptions written
- [ ] M2 · Decomposed — entities + bottleneck identified
- [ ] M3 · Designed — the IO contract is filled in
- [ ] M4 · Built — Level 1 → 2 → 3 → 4, tests green after each:
  - [ ] L1 record + query (`TestLevel1` green)
  - [ ] L2 balance + edge cases (`TestLevel2` green)
  - [ ] L3 refactor into the `Ledger` class (L1+L2 still green)
  - [ ] L4 idempotency + reversal (`TestLevel4*` green, **nothing earlier broke**)
- [ ] M5 · Defended — survived all 3 curveballs out loud
- [ ] M6 · Ready — self-graded ≥ 36/45

# Part 0: Forethought
Goal (one sentence): Build an append-only ledger that survives malformed and duplicate events.
Target time: 70 minutes
Confidence before starting (1–5): [blank]

# Part 1: Clarifying questions
> Codebase rounds reward asking before coding just as much as algorithmic ones. Pair each question with an assumption so you keep moving.

Goal:
> Are we optimizing for correctness of balances, or throughput?
Question: [blank]
Assumption: I'll assume **correctness of balances** is paramount — this is money.

Data:
> Are amounts always non-negative, with direction encoded by `type`?
Question: [blank]
Assumption: I'll assume `amount >= 0` and direction is `type` ∈ {credit, debit}.

Constraints:
> Can an event be deleted, or only compensated?
Question: [blank]
Assumption: I'll assume the ledger is **append-only** — reversals are compensating entries, never deletions.

Scale:
> Does the active state fit in memory for this exercise?
Question: [blank]
Assumption: I'll assume in-memory is fine for the interview.

<details><summary>Small hint</summary>
Append-only + a <code>seen_keys</code> set gives you idempotency for free in Level 4. Don't store malformed events at all — then balances can't be corrupted.
</details>

# Part 2: Decomposition
Current workflow (worked example — this is what a Tier-1 model looks like):
1. Upstream emits credit/debit events (some malformed, some duplicated).
2. Today: a stub that stores nothing.
3. Consumers want per-account event history and a net balance.

Bottleneck:
1. There is no storage or validation layer — every downstream number is wrong.

Core entities:
*(Tutorial: nouns/tables, not properties.)*
1. Event
2. Account (implicit — identified by `account_id` on events)

State transitions (for an Event):
*(Tutorial: DB lifecycle, not UI.)*
1. RECEIVED → (valid?) → STORED → (later) → COMPENSATED-BY a reversal entry
2. RECEIVED → (malformed or duplicate key) → IGNORED

> 🚩 Checkpoint M2 · Decomposed — you should now have **Event** (plus an implicit Account) as your entities and **reverse-chronological order with no ranking** as the bottleneck. Stuck? The bottleneck is the step that buries the signal under noise.

# Part 3: System / contract design
## Input / Output contract
**Input:**
| Parameter | Type | Description |
|---|---|---|
| event | dict | `{"account_id": str, "type": "credit"\|"debit", "amount": number>=0}` |
| idempotency_key | str \| None | optional; if seen before, the event is ignored |

**Output:**
| Method | Returns | Description |
|---|---|---|
| record_event | bool | True if stored, False if ignored (malformed/duplicate) |
| get_events | list[dict] | the account's events in insertion order |
| get_balance | number | credits − debits; unknown account → 0 |
| reverse_event | bool | appends a compensating entry; False if index out of range |

## Named design decisions
### Append-only storage
[blank — why append-only beats a mutable running total for an auditable ledger]

### Idempotency boundary
[blank — where do you check the key, before or after validation, and why?]

### Malformed-input policy
[blank — fail closed: never store a malformed event so balances can't be corrupted]

## Tradeoff table
| Decision | Option A | Option B | Choice | Why |
|---|---|---|---|---|
| Reversal | delete the original | append a compensating entry | [blank] | [blank] |

> 🚩 Checkpoint M3 · Designed — your contract names `record_event`, `get_events`, `get_balance`, `reverse_event` with types. Stuck? Re-read the method table above before you touch code.

# Part 4: Build — the 4 levels (the build-up)
Implement **in order** in `starter.py`. After each level run `python3 -m unittest tests.py` and watch the next group go green — **that green is your checkpoint**. You're going from an empty stub to a working, tested system.

- **L1 — record + query.** `record_event` (store) + `get_events`.
  > 🚩 M4·L1 — `TestLevel1RecordAndQuery` passes.
- **L2 — balance + edge cases.** `get_balance` + reject malformed events (bad type, missing/negative amount, empty id, `bool` amount).
  > 🚩 M4·L2 — `TestLevel2Balance` passes (unknown account → 0, malformed ignored).
- **L3 — refactor & encapsulate.** Keep all state inside the `Ledger` class; tidy **without changing behaviour**.
  > 🚩 M4·L3 — L1 **and** L2 still pass. (If they don't, your refactor broke something — that's the lesson the codebase round teaches.)
- **L4 — extend.** Idempotency (`idempotency_key` dedupe) + `reverse_event`, **without breaking L1–L3**.
  > 🚩 M4·L4 — `TestLevel4Idempotency` + `TestLevel4Reversal` pass **and every earlier group is still green**. M4 done — nothing → a working ledger.

Edge cases to handle:
1. [blank — duplicate idempotency key]
2. [blank — `amount` is a bool / negative / missing]
3. [blank — `get_balance` on an unknown account]
4. [blank — `reverse_event` index out of range]

# Part 5: Reasoning write-up
Why an append-only event model instead of a stored balance? [blank]
Why validate-then-store (fail closed)? [blank]
Why is L1–L2 the right MVP? [blank]
What would you intentionally NOT build first? [blank]
What breaks if events arrive out of order? [blank]
What needs to be audited? [blank]
What needs permissions? [blank]
What should be real-time vs batch? [blank]
Simplest version that still helps? [blank]
Riskiest assumption? [blank]

# Part 6: Interview simulation
## 90-second talk track
"I built an append-only ledger so every balance is a pure function of stored events, which makes it auditable and idempotent-friendly… [blank]"

## Curveballs (answer out loud)
Curveball 1: The same payout event is delivered three times in 50ms. What happens?
Your response: [blank]

Curveball 2: A reversal itself was sent twice. How do you keep the books correct?
Your response: [blank]

Curveball 3: Product asks to "just delete the bad event." Why might you push back?
Your response: [blank]

# Part 7: Self-grade + reflection
Score 1–5 against the descriptors (SWE rubric + codebase add-ons; see `rubric_bank.md`).

Communication / think-aloud: __/5
Problem solving: __/5
Correctness: __/5
Code quality / readability: __/5
Testing & edge cases: __/5
Debugging: __/5
Time management: __/5
Works against the provided tests: __/5
Diagnosis quality (if you debugged): __/5

Total: __ / 45

One thing I did well: [blank]
One thing I missed: [blank]
Confidence now (1–5): [blank]   ← compare to your Part 0 prediction; the delta is the point.
Lowest rubric row → my next action: [blank]

## ✅ You're ready when…
- [ ] You go scenario → **all 4 levels green in < 45 min** without the hints.
- [ ] You can explain idempotency and "extend, don't mutate" out loud without notes.
- [ ] You answer all 3 curveballs without freezing.
- [ ] You self-grade ≥ 36/45 on **two** attempts running.
> Any unchecked box is your next rep. Re-run cold and timed until all four are checked — that's interview-ready.
