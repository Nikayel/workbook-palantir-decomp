"""
Lab 7: Flawed Ticket Assigner

Read this code. Do NOT run it yet.
Find the bugs.
"""

def assign_tickets(tickets, agents):
    """

    Expected Input Schema:
    tickets = [
        {
            "id": 1, 
            "priority": 1, 
            "status": "open", 
            "language": "es"
        }, ...
    ]

    Assigns tickets to agents.
    """
    # Bug 1?
    tickets.sort(key=lambda x: x["priority"])
    
    assignments = {}
    
    for t in tickets:
        best_agent = None
        
        for a in agents:
            # Bug 2?
            if a["status"] == "vacation":
                pass
                
            # Bug 3?
            if best_agent == None:
                best_agent = a
            elif a["current_workload"] < best_agent["current_workload"]:
                best_agent = a
                
        # Bug 4?
        assignments[t["id"]] = best_agent["name"]
        
        # Bug 5?
        best_agent["current_workload"] += 1
        
    return assignments
