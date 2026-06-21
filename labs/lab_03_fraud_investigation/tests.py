import unittest
from starter import score_transaction

class TestFraudScorer(unittest.TestCase):
    def setUp(self):
        self.history = [
            {"amount": 100, "location": "NYC", "timestamp": 1000},
            {"amount": 50, "location": "NYC", "timestamp": 2000}
        ]
        self.devices = ["device_1"]

    def test_impossible_travel(self):
        # Transaction in London 1 hour after NYC
        tx = {"amount": 50, "location": "London", "timestamp": 5600, "device_id": "device_1"}
        score, reasons = score_transaction(tx, self.history, self.devices)
        self.assertTrue("impossible travel" in " ".join(reasons).lower())
        self.assertGreater(score, 50)

if __name__ == '__main__':
    unittest.main()
