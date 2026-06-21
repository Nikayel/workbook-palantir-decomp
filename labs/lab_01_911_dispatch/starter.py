"""
Lab 1: 911 Dispatch Recommender

Before coding, answer:

1. What makes a responder eligible?
   Your answer: ________________________________

2. What factors should ranking use?
   Your answer: ________________________________

3. What explanation should the dispatcher see?
   Your answer: ________________________________

4. What edge cases can make the recommendation unsafe?
   Your answer: ________________________________
"""

def recommend_responders(incident, responders, top_k=3):
    """
    Recommends the top available responders for a given incident.

    Expected Input Schema:
    incident = {
        "id": "inc_1",
        "type": "medical",          # What kind of response is needed?
        "location": (40.71, -74.0), # Tuple of (lat, lon)
        "severity": "high"          # String enum
    }

    responders = [
        {
            "id": "r_1",
            "capabilities": ["medical", "fire"], 
            "status": "available",        # "available" or "busy"
            "location": (40.72, -74.0),   # Tuple of (lat, lon)
            "last_update": 1670000000     # Unix timestamp of last GPS ping
        }, ...
    ]
    TODO:
    1. Validate the incident.
    2. Filter unavailable responders.
    3. Filter responders missing required capability.
    4. Handle stale location/status.
    5. Compute ranking score.
    6. Return top_k recommendations.
    7. Include explanation strings.
    """
    pass
