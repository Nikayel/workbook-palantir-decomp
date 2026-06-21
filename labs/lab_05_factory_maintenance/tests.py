import unittest
from starter import detect_anomalies

class TestAnomalyDetector(unittest.TestCase):
    def test_sustained_anomaly(self):
        # Machine 1 has a spike but then recovers
        # Machine 2 has sustained high temp
        logs = [
            {"machine_id": "m1", "metric": "temp", "value": 110, "timestamp": 1},
            {"machine_id": "m1", "metric": "temp", "value": 90,  "timestamp": 2},
            {"machine_id": "m1", "metric": "temp", "value": 95,  "timestamp": 3},
            
            {"machine_id": "m2", "metric": "temp", "value": 120, "timestamp": 1},
            {"machine_id": "m2", "metric": "temp", "value": 125, "timestamp": 2},
            {"machine_id": "m2", "metric": "temp", "value": 130, "timestamp": 3},
        ]
        
        thresholds = {"temp": 100}
        history = {}
        
        alerts = detect_anomalies(logs, thresholds, history)
        
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["machine_id"], "m2")
        self.assertEqual(alerts[0]["severity"], "High")

if __name__ == '__main__':
    unittest.main()
