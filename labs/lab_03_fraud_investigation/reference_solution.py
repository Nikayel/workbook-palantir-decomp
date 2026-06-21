def score_transaction(transaction, account_history, device_history):
    score = 0
    reasons = []
    
    # 1. Device check
    if transaction["device_id"] not in device_history:
        score += 30
        reasons.append("New device detected")
        
    # 2. Amount check
    if account_history:
        avg_amount = sum(x["amount"] for x in account_history) / len(account_history)
        if transaction["amount"] > avg_amount * 3:
            score += 20
            reasons.append("Unusual amount")
            
    # 3. Impossible travel
    if account_history:
        last_tx = max(account_history, key=lambda x: x["timestamp"])
        time_diff = transaction["timestamp"] - last_tx["timestamp"]
        # Very simplified check: if diff < 3600s (1hr) and location is different
        if time_diff < 3600 and transaction["location"] != last_tx["location"]:
            score += 40
            reasons.append("Impossible travel detected")
            
    # Cap score
    score = min(100, score)
    return score, reasons
