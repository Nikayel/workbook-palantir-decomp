# Flashcards — Event Ledger

> Review day 1 → 3 → 7 → 14. Reset a card to day 1 on a miss. Free recall only.

**Q:** In a CodeSignal Industry-Coding-Framework / Stripe-style round, what is Level 3 ("refactor & encapsulate") actually testing?
**A:** Whether you can *evolve* existing code — extract state into a class / modules and apply patterns — while preserving behaviour, not just write fresh code.

**Q:** Why model a ledger as an append-only event log instead of a mutable balance counter?
**A:** The balance becomes a reproducible fold over stored events (auditable), duplicates can be made no-ops, and reversals preserve history.

**Q:** How do you make `record_event` idempotent, and where do you check?
**A:** Keep a `seen_keys` set; check the idempotency key *before* validation/applying so a duplicate short-circuits to a no-op.

**Q:** A Python gotcha when validating an `amount` field — what is it?
**A:** `bool` is a subclass of `int`, so `isinstance(True, int)` is True; exclude `bool` explicitly before the numeric check.

**Q:** Why reverse an event with a compensating entry instead of deleting it?
**A:** Append-only preserves the audit trail and keeps balances reproducible; deletion makes the books unreconcilable. (This is double-entry thinking.)

**Q:** What's the production risk of reversing an event by its positional index?
**A:** Index is unstable if event order changes; reverse by a stable event id instead.

**Q:** What does "fail closed" mean for malformed financial events?
**A:** Never store them — so they can't move a balance — and return a clear False/error at the boundary.

**Q:** In a bug-squash / codebase round, what often scores higher than a completed fix?
**A:** A clear, well-reasoned diagnosis that names the mechanism (e.g., "lost update from an unguarded read-modify-write → race condition").

**Q:** Backward compatibility in a multi-level codebase task — the rule of thumb?
**A:** *Extend, don't mutate* earlier behaviour; new features must keep earlier tests green.
