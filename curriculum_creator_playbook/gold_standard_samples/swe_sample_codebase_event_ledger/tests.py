"""
Tests for the Event Ledger lab, grouped by level (mirrors the ICF progression).

This SAMPLE imports from `reference_solution` so it ships GREEN and proves the
target behaviour. In a real lab, change the import to `from starter import Ledger`
and implement the TODOs until each level passes.
"""
import unittest
from reference_solution import Ledger   # learners: change to `from starter import Ledger`


class TestLevel1RecordAndQuery(unittest.TestCase):
    def test_record_and_get_in_order(self):
        l = Ledger()
        self.assertTrue(l.record_event({"account_id": "a", "type": "credit", "amount": 100}))
        self.assertTrue(l.record_event({"account_id": "a", "type": "debit", "amount": 30}))
        self.assertTrue(l.record_event({"account_id": "b", "type": "credit", "amount": 5}))
        self.assertEqual([e["amount"] for e in l.get_events("a")], [100, 30])
        self.assertEqual(len(l.get_events("b")), 1)
        self.assertEqual(l.get_events("missing"), [])


class TestLevel2Balance(unittest.TestCase):
    def test_balance(self):
        l = Ledger()
        l.record_event({"account_id": "a", "type": "credit", "amount": 100})
        l.record_event({"account_id": "a", "type": "debit", "amount": 30})
        self.assertEqual(l.get_balance("a"), 70)

    def test_unknown_account_is_zero(self):
        self.assertEqual(Ledger().get_balance("nope"), 0)

    def test_malformed_events_are_ignored(self):
        l = Ledger()
        self.assertFalse(l.record_event({"account_id": "a", "type": "credit"}))         # no amount
        self.assertFalse(l.record_event({"account_id": "a", "type": "xfer", "amount": 5}))  # bad type
        self.assertFalse(l.record_event({"account_id": "a", "type": "credit", "amount": -5}))  # negative
        self.assertFalse(l.record_event({"account_id": "a", "type": "credit", "amount": True}))  # bool
        self.assertFalse(l.record_event({"account_id": "", "type": "credit", "amount": 5}))     # empty id
        self.assertEqual(l.get_balance("a"), 0)


class TestLevel4Idempotency(unittest.TestCase):
    def test_duplicate_key_applied_once(self):
        l = Ledger()
        self.assertTrue(l.record_event({"account_id": "a", "type": "credit", "amount": 100}, idempotency_key="k1"))
        self.assertFalse(l.record_event({"account_id": "a", "type": "credit", "amount": 100}, idempotency_key="k1"))
        self.assertEqual(l.get_balance("a"), 100)

    def test_distinct_keys_both_applied(self):
        l = Ledger()
        l.record_event({"account_id": "a", "type": "credit", "amount": 10}, idempotency_key="k1")
        l.record_event({"account_id": "a", "type": "credit", "amount": 10}, idempotency_key="k2")
        self.assertEqual(l.get_balance("a"), 20)


class TestLevel4Reversal(unittest.TestCase):
    def test_reverse_restores_balance(self):
        l = Ledger()
        l.record_event({"account_id": "a", "type": "credit", "amount": 100})  # index 0
        l.record_event({"account_id": "a", "type": "debit", "amount": 40})    # index 1
        self.assertEqual(l.get_balance("a"), 60)
        self.assertTrue(l.reverse_event("a", 1))   # compensate the debit -> +40
        self.assertEqual(l.get_balance("a"), 100)

    def test_reverse_out_of_range(self):
        self.assertFalse(Ledger().reverse_event("a", 0))


if __name__ == "__main__":
    unittest.main()
