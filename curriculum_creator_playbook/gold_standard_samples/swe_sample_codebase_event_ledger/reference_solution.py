"""
Event Ledger — reference solution (final, Levels 1-4).

GOLD-STANDARD SAMPLE: a "codebase / practical" SWE lab in the CodeSignal
Industry-Coding-Framework style (the template for Stripe integration, Atlassian
craft, and Palantir practical rounds). The whole point is that each level
*extends the same code* and must not break the earlier levels.

Level 1 — design the data model + record/query events.
Level 2 — derive balances, handling edge cases (unknown account, malformed input).
Level 3 — refactor the loose functions into an encapsulated Ledger class.
Level 4 — extend with idempotency keys and reversals WITHOUT breaking L1-L3.
"""


class Ledger:
    """An append-only ledger of credit/debit events per account."""

    def __init__(self):
        self._events = []        # list[dict], preserved in insertion order
        self._seen_keys = set()  # idempotency keys already applied (Level 4)

    # ---- Level 1: record + query -------------------------------------
    def record_event(self, event, idempotency_key=None):
        """
        Record an event of the shape:
            {"account_id": str, "type": "credit"|"debit", "amount": number >= 0}

        Returns True if stored, False if ignored.
        Ignored when: the idempotency_key was already applied (Level 4),
        or the event is malformed (Level 2).
        """
        if idempotency_key is not None and idempotency_key in self._seen_keys:
            return False
        if not self._is_valid(event):
            return False
        self._events.append({
            "account_id": event["account_id"],
            "type": event["type"],
            "amount": event["amount"],
        })
        if idempotency_key is not None:
            self._seen_keys.add(idempotency_key)
        return True

    def get_events(self, account_id):
        """Return this account's events, in insertion order."""
        return [e for e in self._events if e["account_id"] == account_id]

    # ---- Level 2: balance with edge cases ----------------------------
    def get_balance(self, account_id):
        """
        Net balance = sum(credits) - sum(debits). Unknown account -> 0.
        Malformed events were never stored, so they cannot corrupt the balance.
        """
        balance = 0
        for e in self.get_events(account_id):
            balance += e["amount"] if e["type"] == "credit" else -e["amount"]
        return balance

    # ---- Level 4: reversal (compensating entry) ----------------------
    def reverse_event(self, account_id, index):
        """
        Reverse the event at `index` within the account's events by APPENDING a
        compensating entry (credit<->debit, same amount). Returns True if reversed,
        False if the index is out of range.

        Backward-compatible by construction: it never mutates or deletes prior
        events, so Level 1/2 behaviour is preserved.
        """
        events = self.get_events(account_id)
        if not (0 <= index < len(events)):
            return False
        original = events[index]
        opposite = "debit" if original["type"] == "credit" else "credit"
        self._events.append({
            "account_id": account_id,
            "type": opposite,
            "amount": original["amount"],
        })
        return True

    # ---- helpers -----------------------------------------------------
    @staticmethod
    def _is_valid(event):
        if not isinstance(event, dict):
            return False
        if event.get("type") not in ("credit", "debit"):
            return False
        amount = event.get("amount")
        # NB: bool is a subclass of int in Python; exclude it explicitly.
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            return False
        if amount < 0:
            return False
        account_id = event.get("account_id")
        if not isinstance(account_id, str) or not account_id:
            return False
        return True
