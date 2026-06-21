def recommend_responders(incident, responders, top_k=3):
    if not incident or "location" not in incident:
        return []
        
    req_cap = incident.get("type")
    valid = []
    
    for r in responders:
        # Check status
        if r.get("status") != "available":
            continue
            
        # Check capabilities
        if req_cap not in r.get("capabilities", []):
            continue
            
        # Check stale data (assume timestamp > 300 is stale for this simple example)
        if r.get("last_update", 0) > 300:
            continue
            
        # Compute distance (simple euclidean for proxy)
        lat1, lon1 = incident["location"]
        lat2, lon2 = r["location"]
        dist = ((lat1 - lat2)**2 + (lon1 - lon2)**2)**0.5
        
        valid.append({
            "id": r["id"],
            "distance": dist,
            "explanation": f"Available {req_cap} unit, {dist:.2f} units away."
        })
        
    # Sort by distance
    valid.sort(key=lambda x: x["distance"])
    
    return valid[:top_k]
