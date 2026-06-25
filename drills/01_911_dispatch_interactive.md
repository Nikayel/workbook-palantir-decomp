# 🚨 Drill 1: 911 Emergency Dispatch System

**Interview difficulty:** ⭐⭐⭐ (Medium-Hard)  
**Estimated time:** 45 minutes  
**Topics:** Ranking, real-time systems, geo-spatial queries, state machines, edge cases

---

## The Prompt

> A major city wants to reduce 911 emergency response times from an average of 12 minutes to under 8 minutes. Currently, dispatchers manually assign responders by calling them over radio and tracking them on a wall map. You've been asked to design a software system that helps dispatchers quickly find and assign the best responders to incidents. The system should recommend the top 3 most suitable units for each incident type.
>
> Design this system from first principles. Be specific about data, APIs, ranking logic, edge cases, and trade-offs.

---

## Phase 1: Stop and Think (5 minutes)

**Before reading anything else, write down:**

### 1. What questions would you ask?

```
Question 1: _______________________________
Question 2: _______________________________
Question 3: _______________________________
Question 4: _______________________________
Question 5: _______________________________
```

### 2. What are the core entities?

```
Entity 1: _______________________________
Entity 2: _______________________________
Entity 3: _______________________________
Entity 4: _______________________________
```

### 3. How would you rank responders?

```
Signal 1: _______________________________
Signal 2: _______________________________
Signal 3: _______________________________
```

---

## Phase 2: Clarifying Questions

**Now read the questions the interviewer wants you to ask:**

### Goal & Success Metrics

**Question 1: What's the current response time, and what's the target?**

_Sample answer:_

```
Current: 12 min average.
Target: 8 min (33% improvement)
This tells us our latency SLA.
```

**What did you ask instead?**

```
_______________________________________
```

---

**Question 2: Are we optimizing for speed, fairness, cost, or safety?**

_Sample answer:_

```
Speed alone might burn out responders.
Safety alone might not save lives.
Likely: Speed + fairness (rotate among available).
This affects the ranking heuristic.
```

**Your thoughts:**

```
_______________________________________
```

---

### Users & Workflow

**Question 3: Who are the users?**

_Sample answer:_

```
Dispatchers (primary): assign responders
Responders (fire/ambulance/police): execute assignments
Incident reporters: call 911
Supervisors: monitor performance
```

**Did you think of all four? Who did you miss?**

```
_______________________________________
```

---

**Question 4: How do dispatchers currently work?**

_Sample answer:_

```
Radio calls, wall map, memory.
Dispatcher hears incident → looks at map → calls available units.
Responders answer over radio.
No digital assignment.
```

**Your understanding:**

```
_______________________________________
```

---

**Question 5: Can responders override or decline assignments?**

_Sample answer:_

```
Yes, they can say "I'm unavailable" or "Too far".
If yes, we need a fallback: re-rank and offer #2, #3.
If no, we might get poor compliance.
This is critical for the API design.
```

**Your thoughts:**

```
_______________________________________
```

---

### Data & Scale

**Question 6: How many incidents per day?**

_Sample answer:_

```
City-wide: 1000–5000 per day.
That's maybe 50–200 per hour.
Affects: cache size, query latency, alert design.
```

**Your estimate:**

```
_______________________________________
```

---

**Question 7: How many responders are available?**

_Sample answer:_

```
City-wide: 500–1000 total units.
At any time: maybe 50–100 active units per district.
Each unit can handle ~1 incident at a time (serial or parallel?).
```

**Your estimate:**

```
_______________________________________
```

---

**Question 8: How fresh is responder location data?**

_Sample answer:_

```
GPS updates every 10–30 seconds → call it "real-time".
Radio check-in every 5 minutes → slower.
Our system should use GPS data.
```

**Your thoughts:**

```
_______________________________________
```

---

### Constraints & Tradeoffs

**Question 9: What if all available responders are busy?**

_Sample answer:_

```
Option 1: Queue the incident
Option 2: Call in off-duty staff
Option 3: Escalate to supervisor
Option 4: Recommend farther unit anyway
We'd likely do #3 or #4.
```

**Your approach:**

```
_______________________________________
```

---

**Question 10: What if location data is stale or inaccurate?**

_Sample answer:_

```
Stale (1 hour old): Use last known location + confidence score
Inaccurate (GPS error): Use approximate location
Very wrong: Escalate to dispatcher for verification
```

**Your approach:**

```
_______________________________________
```

---

## Phase 3: Expected Decomposition

**Now fill in the decomposition template as you read the answers below.**

### Users / Personas

**Persona 1: Dispatcher**

- Role: Reviews incident, selects responders, monitors progress
- Pain point: Manual lookup is slow; they memorize maps
- Actions: calls 911-center, sees recommended units, sends assignment, monitors

**Persona 2: Responder (Fire/Ambulance/Police officer)**

- Role: Receives dispatch, drives to incident, handles emergency
- Pain point: Radio communication is hard; long response times
- Actions: accepts/declines assignment, updates status, reports arrival

**Persona 3: Supervisor/Manager**

- Role: Monitors system performance, handles escalations
- Pain point: No visibility into response times; can't predict staffing needs
- Actions: reviews metrics, re-assigns tasks manually if needed

**What did you think of?**

```
_______________________________________
```

---

### Current Workflow

```
Incident reported
     ↓
911 dispatcher answers call
     ↓
Dispatcher looks at wall map + radio
     ↓
Dispatcher calls available units (radio)
     ↓
Unit accepts/declines (radio)
     ↓
Unit drives to scene
     ↓
Responder handles emergency
     ↓
Responder reports completion
```

**Bottleneck:** Dispatcher must manually search available units. With 500–1000 units, they can't optimize. They use heuristics (memory, nearest, recently used). This adds 2–3 minutes per assignment.

**Solution fits:** Between "dispatcher answers call" and "dispatcher calls unit". Our system suggests top 3 units. Dispatcher confirms and sends.

**Did you identify this bottleneck?**

```
_______________________________________
```

---

### Core Entities

| Entity         | Attributes                                              | Relationships                                 |
| -------------- | ------------------------------------------------------- | --------------------------------------------- |
| **Incident**   | id, type, severity, location, status, created_at        | reported_by User; assigned_to many Responders |
| **Responder**  | id, unit_type, status, location, capabilities, workload | assigned_to many Incidents                    |
| **Assignment** | id, incident_id, responder_id, status, created_at       | belongs_to Incident & Responder               |
| **Location**   | lat, lng, address                                       | used_by Incident & Responder                  |

**Did you think of all four?**

```
_______________________________________
```

---

### State Transitions

**Incident states:**

```
NEW (just reported)
  ↓ (dispatcher assigns)
TRIAGED (dispatcher has seen it, decided on responders)
  ↓ (responder accepts)
ASSIGNED (responder committed)
  ↓ (responder starts driving)
EN_ROUTE (en route to scene)
  ↓ (responder arrives)
ON_SCENE (responder at incident location)
  ↓ (responder finishes)
RESOLVED (medical/fire treatment done)
  ↓ (supervisor marks closed)
CLOSED (filed away)
```

**Responder states:**

```
AVAILABLE (on shift, not assigned)
RESPONDING (assigned, driving or on scene)
UNAVAILABLE (off duty or temporarily unavailable)
```

**Assignment states:**

```
PENDING (recommended, awaiting responder acceptance)
ACCEPTED (responder confirmed)
DECLINED (responder refused)
COMPLETED (incident resolved)
```

**Did you model state like this?**

```
_______________________________________
```

---

### APIs / Actions

**Action 1: Report Incident**

```
POST /api/v1/incidents
Input: {
  type: "fire" | "medical" | "police",
  severity: 1-5,
  location: { lat, lng, address },
  description: string
}
Output: {
  id: string,
  status: "NEW",
  created_at: timestamp,
  recommendations: [
    { responder_id, unit_type, eta, reason }
  ]
}
Side effects:
- Incident created
- Ranking algorithm runs
- Top 3 recommendations computed
- Dispatcher notified
```

**Action 2: Get Recommendations**

```
GET /api/v1/incidents/:id/recommendations
Input: { incident_id, count: 3 }
Output: [
  {
    responder_id,
    unit_type,
    location,
    eta_minutes,
    workload,
    score,
    why: "nearest available"
  }
]
Side effects: None (read-only)
```

**Action 3: Assign Responder**

```
POST /api/v1/incidents/:id/assign
Input: {
  incident_id,
  responder_id,
  assigned_by: "dispatcher_user_id"
}
Output: {
  status: "ASSIGNED",
  assignment_id,
  notification_sent_to_responder: true
}
Side effects:
- Assignment created
- Responder status → RESPONDING
- Notification sent to responder
- Event logged
```

**Action 4: Responder Updates Status**

```
PUT /api/v1/responders/:id/status
Input: {
  responder_id,
  status: "EN_ROUTE" | "ON_SCENE" | "RESOLVED",
  location: { lat, lng }
}
Output: {
  responder_id,
  status,
  incidents_active: count
}
Side effects:
- Responder location updated
- Incident status updated
- Alert triggered if ETA exceeded
```

**Did you think of these actions?**

```
_______________________________________
```

---

### Ranking Logic

**The algorithm to find top 3 responders:**

```python
def rank_responders(incident):
  candidates = get_available_responders(incident.location)
  candidates = filter_by_capability(candidates, incident.type)

  scored = []
  for responder in candidates:
    score = compute_score(responder, incident)
    scored.append((responder, score))

  scored = sorted(scored, key=lambda x: x[1], reverse=True)
  return scored[:3]  # Top 3

def compute_score(responder, incident):
  score = 0

  # Signal 1: Distance (nearest is best)
  distance_km = haversine(incident.location, responder.location)
  distance_score = 100 - (distance_km * 2)  # 100 at 0km, 0 at 50km
  score += distance_score * 0.5

  # Signal 2: Availability (available is best)
  if responder.status == "AVAILABLE":
    score += 50
  elif responder.status == "EN_ROUTE" but responder.workload < 3:
    score += 25
  else:
    score += 0  # Skip unavailable

  # Signal 3: Capability match (perfect match is best)
  if has_matching_capability(responder, incident.type):
    score += 30

  # Signal 4: Workload (less busy is better)
  if responder.active_incidents <= 1:
    score += 20
  elif responder.active_incidents <= 2:
    score += 10

  # Signal 5: Recent success (boost if successful)
  if responder.recent_success_rate > 0.9:
    score += 10

  return score
```

**Scoring summary:**

- Distance: 0–50 points (nearest is best)
- Availability: 0–50 points (free responders preferred)
- Capability: 0–30 points (skill match)
- Workload: 0–20 points (less busy is better)
- Recent performance: 0–10 points (bonus for reliable units)

**Total: 0–160 points**

**How did your logic differ?**

```
_______________________________________
```

---

### Edge Cases

**Edge case 1: No available responders**

```
Scenario: All units in city are busy or off-duty
Handling:
  - Check 50km radius
  - Offer farther responders anyway
  - If still nothing: escalate to supervisor
  - Queue incident for next available responder
  - Log alert for commander
```

**Edge case 2: Stale location data**

```
Scenario: GPS data is 30 min old; responder moved
Handling:
  - Mark location as "stale" (confidence: low)
  - Use last known location + ask responder for update
  - Radio check-in to verify availability
  - If conflict: use more recent signal
```

**Edge case 3: Responder declines assignment**

```
Scenario: Recommended responder says "no"
Handling:
  - Immediately offer #2
  - Log decline reason (if given)
  - Don't re-recommend same responder for 5 min
  - Track high-decline responders (possible burnout)
```

**Edge case 4: Bad data (impossible location)**

```
Scenario: Responder location is [-180, 0] or invalid
Handling:
  - Validate lat/lng bounds on input
  - Log anomaly
  - Flag for manual verification
  - Don't recommend that responder
```

**Edge case 5: Dispatcher doesn't accept recommendation**

```
Scenario: Dispatcher ignores top 3 and picks different responder
Handling:
  - Log this choice (for ML improvement)
  - Ask dispatcher why (future feedback)
  - Track if this was a better choice
  - Use this signal to improve ranking
```

**Did you think of these?**

```
_______________________________________
```

---

### Security & Permissions

**Who can see what?**

```
Dispatcher: Can see all responders in district, all incidents in district
Responder: Can see their own assignment, active incident location
Supervisor: Can see all responders, all incidents, aggregate metrics
Admin: Can see everything + audit logs
```

**Who can take what actions?**

```
Dispatcher: Create incident, request recommendations, assign responder, escalate
Responder: Accept/decline/update status, send location
Supervisor: Reassign, override, monitor, generate reports
Admin: Configure system, reset data, audit log access
```

**How to prevent abuse?**

```
- Rate limit API (100 req/min per user)
- Validate all input (lat/lng range, incident type enum)
- Require authentication
- Log all assignments (who assigned to whom, when)
- Audit trail for every state change
- PII protection: don't expose responder home addresses
```

**Did you think of these?**

```
_______________________________________
```

---

### MVP (Minimum Viable Product)

**What ships in 2 weeks?**

**MVP Feature List:**

```
✓ Report incident (lat/lng, type, severity)
✓ Compute top 3 recommendations
✓ Dispatcher assigns responder
✓ Responder receives notification
✓ Status updates (EN_ROUTE, ON_SCENE, RESOLVED)
✓ Metrics: avg response time, adoption rate
```

**NOT in MVP:**

```
✗ ML-based ranking
✗ Predictive dispatch (forecast incidents)
✗ Multi-responder coordination
✗ Historical analytics / dashboards
✗ Advanced RBAC
```

**Rationale:**

- Authentication/RBAC can be added later (start with simple role)
- Advanced scoring requires more data (start with heuristics)
- Analytics requires instrumentation (add after MVP proves value)
- Multi-responder (fire + ambulance) is complex; handle in V2

**Did you scope an MVP?**

```
_______________________________________
```

---

### Success Metrics

| Metric                  | Baseline | Target                            | How to track                                     |
| ----------------------- | -------- | --------------------------------- | ------------------------------------------------ |
| Avg response time       | 12 min   | 8 min                             | Timestamp: incident_created → responder_on_scene |
| Adoption rate           | 0%       | 50% dispatchers                   | Event tracking: is_recommendation_used           |
| System latency (p95)    | N/A      | <200ms                            | APM tool (New Relic)                             |
| Recommendation accuracy | N/A      | >75% (was top-3 good?)            | Manual spot checks + feedback                    |
| Responder compliance    | N/A      | >90% (accept ratio)               | Decline events                                   |
| False negatives         | N/A      | <5% (could dispatcher do better?) | Log dispatcher overrides                         |

**Did you define metrics?**

```
_______________________________________
```

---

### V2 / V3 Roadmap

**V2 (Month 2–3):**

```
- Multi-responder coordination (fire + ambulance + police)
- Predictive dispatch (forecast high-incident zones)
- Advanced ML ranking (learn from dispatcher feedback)
- Historical dashboards for supervisors
```

**V3 (Month 4–6):**

```
- Real-time incident clustering (handle surge)
- Fatigue-aware scheduling (prevent burnout)
- Integration with external systems (hospitals, police HQ)
- Mobile app for responders
```

**When do we expand?**

```
Expand when:
- Adoption reaches 80%
- Response time consistently <8 min
- New incident types added (animal control, wellness checks)
- Scale increases 10x
```

**Did you plan iterations?**

```
_______________________________________
```

---

## Interviewer Curveballs

**Now the interviewer throws curveballs. How do you respond?**

### Curveball 1: "What if GPS data is 80% accurate?"

_Expected response:_

```
We'd add a confidence score to each location signal.
- High confidence (recent, validated): weight 100%
- Medium confidence (old, unvalidated): weight 50%
- Low confidence (very old, flagged): weight 10%

Then we'd lower the distance score for low-confidence data.
If confidence is <10%, escalate to dispatcher: "Please verify location".

We could also correlate multiple data sources:
- GPS + cellular triangulation + last radio check-in
- If all three agree → high confidence
- If they conflict → escalate
```

**Your response:**

```
_______________________________________
_______________________________________
```

---

### Curveball 2: "Our system failed. Dispatchers aren't using it."

_Expected response:_

```
This is a classic adoption problem. Root causes:
1. UX is confusing (they don't trust the UI)
2. Recommendations are bad (they pick manually anyway)
3. Organizational resistance (they like radio)
4. Not faster than radio (latency was too high)

What I'd do:
- Survey 10 dispatchers: "Why don't you use it?"
- Check logs: Do they ignore recommendations? If yes: improve ranking.
- Check latency: Is it >1s? If yes: optimize queries.
- Check UX: Is the interface confusing? Simplify.
- Check change management: Did we train them? Do management support it?

I'd iterate weekly based on feedback.
First metric: adoption rate (50% of dispatchers using it daily).
```

**Your response:**

```
_______________________________________
_______________________________________
```

---

### Curveball 3: "We now have 100x more data. What breaks?"

_Expected response:_

```
With 100x scale:
- Query latency would increase (10 responders → 1000 responders)
- Geo-spatial queries would be slow (naive distance calc)
- Cache hit rate would drop (more unique locations)
- Database index strategy matters (need geo-index)

How I'd fix it:
1. Add geo-spatial indexing (PostGIS or similar)
2. Pre-compute district boundaries (run ranking per-district, not city-wide)
3. Add caching layer (Redis) for recent assignments
4. Async ranking (start ranking before dispatcher asks)
5. Sample data if needed (rank top-100 first, then top-3)

I'd load test at 100x scale to identify exact bottleneck.
```

**Your response:**

```
_______________________________________
_______________________________________
```

---

### Curveball 4: "A responder was fired for misconduct, but they're still in the system."

_Expected response:_

```
Data quality issue. We need:
1. Soft delete (mark responder as INACTIVE, don't delete)
2. Audit trail (log who changed their status and when)
3. Access control (only HR + Admin can deactivate)
4. Notification (alert supervisor when responder deactivated)
5. Cleanup (don't re-assign INACTIVE responders)

In code:
- Query: "WHERE status != 'INACTIVE'"
- Log all deactivations with reason
- Alert on deactivation

For MVP: Just add an INACTIVE status.
For V2: Add full audit trail.
```

**Your response:**

```
_______________________________________
_______________________________________
```

---

## Scoring Yourself

**Score yourself on each dimension (1–5):**

| Dimension                  | You    | Notes                                 |
| -------------------------- | ------ | ------------------------------------- |
| **Ambiguity handling**     | \_\_/5 | Did you ask clarifying questions?     |
| **Workflow understanding** | \_\_/5 | Did you identify the bottleneck?      |
| **Data modeling**          | \_\_/5 | Are entities and relationships clear? |
| **API design**             | \_\_/5 | Do your APIs handle all actions?      |
| **Practical MVP**          | \_\_/5 | Is your MVP 2 weeks, not 6 months?    |
| **Edge cases**             | \_\_/5 | Did you handle 5+ edge cases?         |
| **Communication**          | \_\_/5 | Can you explain this clearly?         |

**Total: \_\_/35**

---

## Next Steps

1. **Compare your answers to the solution** – Where did you diverge?
2. **Run the Python exercise** – `python/911_dispatch_sim.py`
3. **Implement the ranking algorithm** – Code it up
4. **Discuss trade-offs** – Why distance vs availability?
5. **Prepare for curveballs** – Rehearse your responses
