# Solution Reasoning

## 1. Why these users?
Maintenance shift leads and technicians. They need prioritized work orders, not raw data.

## 2. Why this workflow?
We transform a scheduled 30-day loop into an event-driven queue, reducing downtime.

## 3. Why this data model?
We need `SensorReading`, `Machine`, `Threshold`, and `MaintenanceTicket`.

## 4. Why these APIs/actions?
- `POST /readings`: High throughput ingestion (e.g., Kafka).
- `GET /tickets`: Powers the technician's tablet app.

## 5. Failure modes
- **Alert Fatigue**: The biggest risk. If the threshold is too low, techs ignore the app. Mitigation: Require *sustained* anomalies over X minutes.
- **Sensor Failure**: A broken sensor sending nulls or max_int. Mitigation: Add a rule for "sensor out of bounds/offline" rather than "machine overheating."

## 6. Strong vs weak answer
**Weak**: "I'll train a deep learning model on the time-series data." (Too complex for MVP, hard to debug, what if there's no historical breakdown data?)
**Strong**: "For the MVP, I'll use a sliding window average against statistical thresholds to detect sustained anomalies and auto-generate tickets. I will ensure we don't alert if a machine was serviced yesterday."
