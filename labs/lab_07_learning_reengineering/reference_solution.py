def assign_tickets(tickets, agents):
    # Do not mutate input
    sorted_tickets = sorted(tickets, key=lambda x: x["priority"], reverse=True)
    
    # Copy agent state locally to avoid mutating inputs
    agent_state = {a["name"]: a["current_workload"] for a in agents}
    
    assignments = {}
    
    for t in sorted_tickets:
        best_agent = None
        min_workload = float('inf')
        
        req_lang = t.get("language", "en")
        
        for a in agents:
            if a["status"] == "vacation":
                continue
                
            if req_lang not in a.get("languages", ["en"]):
                continue
                
            curr_wl = agent_state[a["name"]]
            if curr_wl < min_workload:
                best_agent = a
                min_workload = curr_wl
                
        if best_agent is not None:
            assignments[t["id"]] = best_agent["name"]
            agent_state[best_agent["name"]] += 1
        else:
            assignments[t["id"]] = "UNASSIGNED"
            
    return assignments
