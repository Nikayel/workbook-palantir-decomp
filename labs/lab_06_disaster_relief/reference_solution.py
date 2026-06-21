def allocate_supplies(shelters, depots, road_closures, trucks):
    allocations = []
    unmet = {}
    
    # Sort shelters by priority (1 is highest)
    sorted_shelters = sorted(shelters, key=lambda x: x["priority"])
    
    # Simple global inventory tracker (ignoring distance and road closures for this simple MVP logic)
    global_inventory = {}
    for d in depots:
        for item, qty in d["inventory"].items():
            global_inventory[item] = global_inventory.get(item, 0) + qty
            
    # Simple global truck capacity
    total_capacity = sum(t["capacity"] for t in trucks)
    
    for shelter in sorted_shelters:
        s_id = shelter["id"]
        allocated_here = {}
        unmet_here = {}
        
        for item, needed_qty in shelter["needs"].items():
            available = global_inventory.get(item, 0)
            
            # How much can we actually give? (constrained by inventory and truck capacity)
            can_give = min(needed_qty, available, total_capacity)
            
            if can_give > 0:
                allocated_here[item] = can_give
                global_inventory[item] -= can_give
                total_capacity -= can_give
                
            if needed_qty > can_give:
                unmet_here[item] = needed_qty - can_give
                
        allocations.append({
            "shelter_id": s_id,
            "allocated": allocated_here
        })
        if unmet_here:
            unmet[s_id] = unmet_here
            
    return allocations, unmet
