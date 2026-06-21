import unittest
from starter import detect_discharge_blockers

class TestDischarge(unittest.TestCase):
    def setUp(self):
        self.patients = [
            {"id": "p_1", "status": "medically_ready"},
            {"id": "p_2", "status": "in_treatment"}
        ]
        self.tasks = [
            {"patient_id": "p_1", "type": "pharmacy", "status": "pending", "owner": "pharmacist"},
            {"patient_id": "p_1", "type": "doctor_signoff", "status": "completed", "owner": "doctor"},
            {"patient_id": "p_2", "type": "pharmacy", "status": "pending", "owner": "pharmacist"}
        ]

    def test_blocker_detection(self):
        results = detect_discharge_blockers(self.patients, self.tasks)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["patient_id"], "p_1")
        self.assertEqual(results[0]["blocker"], "pharmacy")

if __name__ == '__main__':
    unittest.main()
