"""
Lab 3: Fraud Investigation Scorer

Before coding, answer:

1. What factors make a transaction risky?
   Your answer: ________________________________

2. How do you handle a new device vs a known device?
   Your answer: ________________________________
"""

def score_transaction(transaction, account_history, device_history):
    """

    Expected Input Schema:
    tx = {
        "amount": 50, 
        "location": "London", 
        "timestamp": 5600, 
        "device_id": "device_1"
    }
    
    history = [
        {"amount": 100, "location": "NYC", "timestamp": 1000}, ...
    ]
    
    known_devices = ["device_1", "device_2"]

    TODO:
    1. Check for unusual amounts (e.g., > 3x average).
    2. Check if the device is new.
    3. Check for impossible travel (e.g., US to UK in 1 hour).
    4. Check for high transaction velocity.
    5. Return an overall risk score (0 to 100) and a list of reasons.
    """
    pass
