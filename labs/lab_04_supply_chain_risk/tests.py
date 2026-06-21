import unittest
from starter import propagate_risk

class TestSupplyChain(unittest.TestCase):
    def test_risk_propagation(self):
        disrupted = ["sup_A"]
        # A -> B -> C
        graph = {
            "sup_A": ["sup_B"],
            "sup_B": ["sup_C"],
            "sup_C": []
        }
        products = {
            "sup_A": [],
            "sup_B": ["prod_1"],
            "sup_C": ["prod_2", "prod_3"]
        }
        
        impacted = propagate_risk(disrupted, graph, products)
        
        self.assertIn("prod_1", impacted)
        self.assertIn("prod_2", impacted)
        self.assertIn("prod_3", impacted)
        self.assertEqual(len(impacted), 3)

if __name__ == '__main__':
    unittest.main()
