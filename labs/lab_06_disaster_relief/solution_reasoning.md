# Solution Reasoning

## 1. Why these users?
Logistics Coordinator (HQ) and Truck Drivers. The Coordinator decides, the driver executes.

## 2. Why this workflow?
Replaces chaotic radio broadcasts with a centralized, priority-based ledger.

## 3. Why this data model?
`Shelter` (needs, priority), `Depot` (inventory), `Route` (status: open/closed), `DeliveryTask`.

## 4. Why these APIs/actions?
- `POST /report-need`: Async, built for offline-first since cell service is spotty.
- `GET /manifest`: Fetches the plan for a truck.

## 5. Failure modes
- **Offline environments**: Cell networks are often down in disasters. Mitigation: The app needs offline caching and SMS fallbacks.
- **Fairness vs Priority**: Do you give all water to the most critical shelter, or spread it out? MVP: Strict priority. V2: Fair distribution.

## 6. Strong vs weak answer
**Weak**: "I'll build a live real-time websocket map." (Ignores the reality of disaster zones lacking internet).
**Strong**: "I'll build a greedy allocation algorithm prioritizing critical medical needs, and ensure the mobile app can sync via SMS or work offline when drivers leave the depot."
