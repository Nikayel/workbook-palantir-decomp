"""
Event Ledger — starter.

Before coding, answer (Part 4 of the workbook):
1. What is the minimal data model for an event?            Your answer: ________
2. Why store events append-only instead of a running total? Your answer: ________
3. What makes an event "malformed" and what do you return?  Your answer: ________
4. How will idempotency avoid double-applying an event?      Your answer: ________

Implement the four LEVELS in order. Each level extends the previous one and must
not break earlier tests. Run:  python3 -m unittest tests.py

Expected event schema:
    event = {"account_id": "acct_1", "type": "credit", "amount": 100}
    # type is "credit" or "debit"; amount is a non-negative number.
"""


class Ledger:
    def __init__(self):
        # TODO (L1): choose your storage. Append-only list of events is recommended.
        # TODO (L4): you will also need to remember applied idempotency keys.
        pass

    # ---- Level 1 ----
    def record_event(self, event, idempotency_key=None):
        # TODO (L1): validate + store the event; return True/False.
        # TODO (L2): reject malformed events (bad type, missing/negative amount, empty id).
        # TODO (L4): if idempotency_key was already applied, ignore and return False.
        pass

    def get_events(self, account_id):
        # TODO (L1): return this account's events in insertion order.
        pass

    # ---- Level 2 ----
    def get_balance(self, account_id):
        # TODO (L2): credits - debits; unknown account -> 0.
        pass

    # ---- Level 4 ----
    def reverse_event(self, account_id, index):
        # TODO (L4): append a compensating entry for the event at `index`.
        # Do NOT mutate or delete prior events (keep L1/L2 behaviour intact).
        pass
