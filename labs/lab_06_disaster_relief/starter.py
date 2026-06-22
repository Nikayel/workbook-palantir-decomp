"""
Lab 6: Relief Supply Allocator

Before coding, answer:

1. If two shelters need water, but we only have enough for one, how do you prioritize?
   Your answer: ________________________________

2. How do you handle road closures in your logic?
   Your answer: ________________________________
"""

def allocate_supplies(shelters, depots, road_closures, trucks):
    """

    Expected Input Schema:
    inventory = {
        "water": 100,
        "medical": 50
    }
    
    shelters = [
        {
            "id": "s1", 
            "needs": {"water": 100, "medical": 20}, 
            "priority": "high"
        }, ...
    ]

    TODO:
    1. Filter out depots that are cut off by road closures.
    2. Sort shelters by priority (e.g., medical needs > water > food).
    3. Allocate inventory from the closest depot.
    4. Respect truck capacities.
    5. Return an allocation plan and a list of unmet needs.
    """
    pass
