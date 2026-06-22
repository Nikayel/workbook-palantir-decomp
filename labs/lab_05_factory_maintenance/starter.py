"""
Lab 5: Factory Anomaly Detector

Before coding, answer:

1. How do you avoid false positives if a sensor spikes for just 1 second?
   Your answer: ________________________________

2. What action should be suggested if temperature is high vs vibration is high?
   Your answer: ________________________________
"""

def detect_anomalies(sensor_logs, thresholds, maintenance_history):
    """

    Expected Input Schema:
    stream = [
        {"machine_id": "m1", "temp": 110, "timestamp": 1000}, ...
    ]

    TODO:
    1. Filter out machines that just had maintenance (e.g. in the last 24h).
    2. Check for sustained anomalies (e.g., 3 consecutive readings above threshold).
    3. Determine the severity (e.g. >10% over threshold is Medium, >50% is High).
    4. Return a list of alerts with suggested actions.
    """
    pass
