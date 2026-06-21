import unittest
from starter import recommend_responders

class TestDispatch(unittest.TestCase):
    def setUp(self):
        self.incident = {
            "id": "inc_1",
            "type": "medical",
            "location": (40.7128, -74.0060),
            "severity": "high"
        }
        self.responders = [
            {"id": "r_1", "capabilities": ["medical"], "status": "available", "location": (40.7130, -74.0060), "last_update": 0},
            {"id": "r_2", "capabilities": ["fire"], "status": "available", "location": (40.7128, -74.0060), "last_update": 0},
            {"id": "r_3", "capabilities": ["medical"], "status": "busy", "location": (40.7128, -74.0060), "last_update": 0},
        ]

    def test_basic_filtering(self):
        results = recommend_responders(self.incident, self.responders)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "r_1")

if __name__ == '__main__':
    unittest.main()
