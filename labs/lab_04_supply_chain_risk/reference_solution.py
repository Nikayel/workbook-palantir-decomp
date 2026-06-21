from collections import deque

def propagate_risk(disrupted_suppliers, supplier_graph, product_mapping):
    impacted_products = set()
    visited_suppliers = set()
    
    queue = deque(disrupted_suppliers)
    
    while queue:
        current = queue.popleft()
        
        if current in visited_suppliers:
            continue
            
        visited_suppliers.add(current)
        
        # Add products directly affected by this supplier
        if current in product_mapping:
            for prod in product_mapping[current]:
                impacted_products.add(prod)
                
        # Traverse to downstream suppliers
        if current in supplier_graph:
            for downstream in supplier_graph[current]:
                if downstream not in visited_suppliers:
                    queue.append(downstream)
                    
    return list(impacted_products)
