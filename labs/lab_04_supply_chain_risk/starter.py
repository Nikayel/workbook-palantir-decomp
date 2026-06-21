"""
Lab 4: Supply Chain Risk Propagator

Before coding, answer:

1. What algorithm is best for traversing dependencies?
   Your answer: ________________________________

2. How do you prevent infinite loops if the data has a cycle?
   Your answer: ________________________________
"""

def propagate_risk(disrupted_suppliers, supplier_graph, product_mapping):
    """
    TODO:
    1. disrupted_suppliers: list of supplier IDs
    2. supplier_graph: dict of {supplier_id: [dependent_supplier_ids]}
    3. product_mapping: dict of {supplier_id: [product_ids]}
    4. Traverse the graph to find all downstream impacted suppliers.
    5. Map the impacted suppliers to final products.
    6. Return a list of impacted product IDs.
    """
    pass
