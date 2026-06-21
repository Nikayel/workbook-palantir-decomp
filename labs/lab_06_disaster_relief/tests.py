import unittest
from starter import allocate_supplies

class TestReliefAllocation(unittest.TestCase):
    def test_basic_allocation(self):
        shelters = [
            {"id": "s1", "needs": {"water": 100}, "priority": 1, "location": "A"},
            {"id": "s2", "needs": {"water": 50},  "priority": 2, "location": "B"}
        ]
        depots = [
            {"id": "d1", "inventory": {"water": 120}, "location": "A"}
        ]
        road_closures = []
        trucks = [{"id": "t1", "capacity": 200, "depot_id": "d1"}]
        
        allocations, unmet = allocate_supplies(shelters, depots, road_closures, trucks)
        
        # S1 gets 100, S2 gets 20 (d1 only had 120 total)
        s1_alloc = next(x for x in allocations if x["shelter_id"] == "s1")
        s2_alloc = next(x for x in allocations if x["shelter_id"] == "s2")
        
        self.assertEqual(s1_alloc["allocated"]["water"], 100)
        self.assertEqual(s2_alloc["allocated"]["water"], 20)
        self.assertEqual(unmet["s2"]["water"], 30)

if __name__ == '__main__':
    unittest.main()
