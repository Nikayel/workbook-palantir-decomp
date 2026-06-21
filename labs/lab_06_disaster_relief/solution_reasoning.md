# Solution Reasoning

## 0. Clarifying Questions Answer Key
- **Goal**: 
  - *Question*: Is the goal equitable distribution or fulfilling the most critical needs first?
  - *Assumption*: I'll assume we strictly prioritize critical needs (medical, water) over general needs.
- **Users**: 
  - *Question*: Are field workers using this on mobile devices?
  - *Assumption*: I'll assume they use tablets in the field that frequently lose cellular connection.
- **Data**: 
  - *Question*: How do we know what inventory a truck has?
  - *Assumption*: I'll assume the truck's manifest is updated when it leaves the depot and synced when offline.
- **Constraints**: 
  - *Question*: What is the offline requirement?
  - *Assumption*: I'll assume the app must function fully offline and resolve conflicts (like double-claimed water) when reconnecting.
- **Scale**: 
  - *Question*: How many trucks and shelters are there?
  - *Assumption*: I'll assume < 100 trucks and shelters, so conflict resolution payloads are very small.


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
