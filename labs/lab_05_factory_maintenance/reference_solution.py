def detect_anomalies(sensor_logs, thresholds, maintenance_history):
    # Group by machine and metric, sort by timestamp
    from collections import defaultdict
    
    grouped = defaultdict(list)
    for log in sensor_logs:
        grouped[(log["machine_id"], log["metric"])].append(log)
        
    alerts = []
    
    for (m_id, metric), logs in grouped.items():
        # Check maintenance history (skip if serviced recently)
        if m_id in maintenance_history:
            last_maint = maintenance_history[m_id]
            # assume current time is max timestamp in logs
            current_time = max(l["timestamp"] for l in sensor_logs)
            if current_time - last_maint < 24: # e.g. 24 hours
                continue
                
        logs.sort(key=lambda x: x["timestamp"])
        
        thresh = thresholds.get(metric, float('inf'))
        
        # Check for 3 consecutive above threshold
        consecutive = 0
        max_val = 0
        for log in logs:
            if log["value"] > thresh:
                consecutive += 1
                max_val = max(max_val, log["value"])
            else:
                consecutive = 0
                
            if consecutive >= 3:
                # Determine severity
                percent_over = (max_val - thresh) / thresh
                severity = "High" if percent_over > 0.5 else "Medium"
                
                alerts.append({
                    "machine_id": m_id,
                    "metric": metric,
                    "severity": severity,
                    "suggested_action": f"Inspect {metric}. Sustained value at {max_val}."
                })
                break # Only one alert per machine/metric
                
    return alerts
