# Drill 1: 911 Emergency Dispatch System

**Interview difficulty:** ⭐⭐⭐ (Medium-Hard)  
**Estimated time:** 45 minutes  
**Topics:** Ranking, real-time systems, geo-spatial queries, state machines, edge cases

---

## The Prompt

> A major city wants to reduce 911 emergency response times from an average of 12 minutes to under 8 minutes. Currently, dispatchers manually assign responders by calling them over radio and tracking them on a wall map. You've been asked to design a software system that helps dispatchers quickly find and assign the best responders to incidents. The system should recommend the top 3 most suitable units for each incident type.
>
> Design this system from first principles. Be specific about data, APIs, ranking logic, edge cases, and trade-offs.

---

## Clarifying Questions

**Ask these questions during the interview. Answers help scope the solution.**

### Goal & Success Metrics

1. **What's the current response time, and what's the target?**  
   _Current: 12 min average. Target: 8 min. This tells us latency SLA._

2. **How much should response time improve vs. cost/complexity trade-off?**  
   _Even 10% improvement might be worth it. What's the metric?_

3. **Are we optimizing for speed, fairness, cost, or safety?**  
   _Speed alone might burn out responders. Safety alone might not save lives._

### Users & Workflow

4. **Who are the users?**  
   _Dispatchers, responders (fire/ambulance/police), incident reporters, supervisors._

5. **How do dispatchers currently work?**  
   _Radio calls, wall map, memory. Do they always accept the system's recommendation?_

6. **Can responders override or decline assignments?**  
   _If yes, what happens? Do we re-rank?_

### Data & Scale

7. **How many incidents per day?**  
   _City-wide: maybe 1000–5000 per day. This affects query latency._

8. **How many responders are available?**  
   _Maybe 500–1000 total units. But only 50–100 at any time in a given district._

9. **How fresh is responder location data?**  
   _GPS updates every 10–30 seconds? Or real-time via radio check-in?_

### Constraints & Tradeoffs

10. **What if all available responders are busy?**  
    _Do we queue the incident? Call in off-duty staff? Escalate?_

11. **What if location data is stale or inaccurate?**  
    _Do we use last known location? Escalate to dispatcher to verify?_

12. **Can the system decline to make a recommendation?**  
    _Yes, sometimes dispatcher override is safer. When should we abstain?_

---

## Expected Decomposition

### Users & Personas

| Persona               | Goal                           | Pain Point                            | Key Action                             |
| --------------------- | ------------------------------ | ------------------------------------- | -------------------------------------- |
| **Dispatcher**        | Quickly find best responders   | Manually searching, radio congestion  | View recommendations, assign units     |
| **Responder**         | Know where to go, help people  | Unclear assignments, wrong units sent | Receive assignment, confirm, navigate  |
| **Incident Reporter** | Get help fast                  | Long wait times                       | Report incident (phone/app)            |
| **Supervisor**        | Manage team, optimize coverage | No visibility into dispatch quality   | Review assignments, override if needed |

### Current Workflow

```
1. Citizen calls 911
2. Operator records incident (type, location, severity)
3. Dispatcher looks at map, remembers unit locations (often stale!)
4. Dispatcher calls units over radio: "Unit 5, respond to fire at 123 Main St"
5. Unit responds: "Unit 5 responding" → en route → on scene
6. Dispatcher tracks on map, might redirect units
7. Unit resolves incident, returns to station
8. Dispatcher updates records
```

**Bottleneck:** Steps 3–4 are slow. Dispatcher must search, remember, radio. Information is stale.

### Core Entities & Relationships

```
┌──────────────┐
│  Incident    │ (fire, medical, accident, ...)
│              │ status: new → triaged → assigned → en_route → resolved → closed
└──────┬───────┘
       │ has many
       └─────────────────────┐
                             │
                        ┌────▼────────┐
                        │ Assignment   │ (dispatcher → responder link)
                        │              │ status: assigned → acknowledged → en_route → completed
                        └────┬─────────┘
                             │ links to
                             └──────────────┬────────────┐
                                            │            │
                                       ┌────▼────────┐  etc.
                                       │ Responder   │
                                       │  (fire_truck,
                                       │   ambulance)
                                       │  status: available, en_route, on_scene, off_duty
                                       └─────────────┘
```

**Key attributes:**

- Incident: { id, type, severity, location (lat/lon), time, status }
- Responder: { id, unit_type, station, current_location, status, capabilities, workload, last_location_update }
- Assignment: { incident_id, responder_id, assigned_at, status, eta, assigned_by_dispatcher }

### State Transitions

**Incident state machine:**

```
new ──triaged──→ assigned ──→ en_route ──→ resolved ──→ closed
```

**Responder state machine:**

```
available ──assignment──→ en_route ──arrived──→ on_scene ──complete──→ returning ──arrive_station──→ available
```

### APIs / Actions

**Core endpoints:**

```
1. POST /api/incidents
   Input: { type, severity, location, description }
   Output: { incident_id, status: "new", recommended_responders: [3 top units with ETA] }

2. GET /api/incidents/{incident_id}
   Output: { incident, assigned_responders, current_status }

3. POST /api/incidents/{incident_id}/assign
   Input: { responder_id }
   Output: { assignment_id, status: "assigned" }
   Triggers: notification to responder

4. PUT /api/responders/{responder_id}/status
   Input: { status: "en_route" | "on_scene" | "returning" }
   Output: { responder, updated_status, updated_at }

5. GET /api/responders/available
   Input: { location, unit_types: ["fire_truck"], limit: 5 }
   Output: [ { responder_id, unit_type, eta_seconds, distance_km, workload }, ... ]
```

### Ranking / Matching Logic

**Algorithm: Score and rank responders**

```python
def rank_responders(incident, available_responders):
    """
    Score responders by:
    1. Capability match (must have required skills)
    2. Distance/ETA (closer is better, but balanced with other factors)
    3. Workload (less busy is better)
    4. Reliability (prefer responders with good history)
    """
    candidates = []
    for responder in available_responders:
        # Filter by capability
        if not has_required_capabilities(responder, incident.type):
            continue

        # Calculate ETA
        eta = calculate_eta(responder.location, incident.location)

        # Score factors
        distance_score = 10 - (eta / 60)  # 0–10, lower ETA = higher score
        workload_score = 10 - responder.workload  # 0–10, fewer jobs = higher score
        capability_score = 10 if perfect_match else 8  # specialty bonus

        # Weighted sum
        total_score = (
            0.5 * distance_score +
            0.3 * workload_score +
            0.2 * capability_score
        )

        candidates.append({
            'responder_id': responder.id,
            'score': total_score,
            'eta': eta,
            'workload': responder.workload,
            'reason': f"ETA {eta}s, workload {responder.workload}, capability match"
        })

    # Sort by score descending, return top 3
    return sorted(candidates, key=lambda x: x['score'], reverse=True)[:3]
```

**Heuristics:**

- ETA: use straight-line distance + traffic model (could be simple formula)
- Capability match: fire_truck for fires, ambulance for medical, etc.
- Workload fairness: prefer units with fewer active assignments (prevents burnout)
- Ties: random or by responder ID (to distribute load)

**Trade-offs:**

- Accuracy vs latency: Use cached location (30s old) vs real-time GPS query
- Fairness vs speed: Perfect load balancing adds complexity; simple heuristic might miss better choices
- Optimality vs interpretability: ML model would rank better but hard to explain to dispatcher

### Edge Cases

| Edge Case                           | Scenario                                              | Mitigation                                                                  |
| ----------------------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------- |
| **No available responders**         | All units busy                                        | Queue incident, notify supervisor, escalate                                 |
| **Stale location data**             | Responder location >1 min old                         | Mark location as "stale", ask dispatcher to verify, use last known position |
| **Conflicting locations**           | GPS says unit is at HQ, but radio says en route       | Use most recent timestamp, log discrepancy                                  |
| **Responder declines assignment**   | Unit says "unable to respond"                         | Re-rank and suggest next-best unit                                          |
| **Missing data**                    | No location for responder                             | Exclude from ranking, alert ops team                                        |
| **Incident location is inaccurate** | Caller says "near Main St" but wrong part of city     | Prompt dispatcher to confirm; offer map search                              |
| **Incident escalates**              | Fire becomes structure collapse, need different units | Automatically suggest additional unit types, notify units already en route  |

### Security & Permissions

**Who can see what?**

- Dispatcher: all incidents, all responders, all locations
- Responder: their own assignment, nearby incidents (optional), their own workload
- Citizen: only their reported incident status (not responder locations)
- Supervisor: all incidents + performance metrics (not PII)

**Who can take what actions?**

- Dispatcher: create incident, assign responders, update incident status
- Responder: acknowledge assignment, update their status
- Supervisor: override assignment, mark incident closed

**Prevent abuse:**

- Rate limit incident creation (1000 per minute city-wide is reasonable)
- Validate location coordinates (within city bounds)
- Audit all assignments: log who assigned, when, reason

### MVP (2-week scope)

**Launch with:**

- Single city, one dispatch center
- 100 responders (or fewer for test)
- Basic ranking: distance + availability (no workload balancing yet)
- Manual assignment by dispatcher (system suggests, human approves)
- Text-based API (no UI)

**What we cut:**

- Workload balancing (too complex for MVP)
- Traffic model (use straight-line distance)
- Responder performance history (too much data)
- Mobile app for responders (phone calls initially)
- Multi-language support

**Why:** Simpler logic means faster deployment, easier debugging, easier for dispatcher to understand recommendations.

### Metrics

| Metric                  | Baseline | Target                                    | How to measure                                                 |
| ----------------------- | -------- | ----------------------------------------- | -------------------------------------------------------------- |
| Avg response time       | 12 min   | < 8 min                                   | Timestamp incident created vs responder arrives on scene       |
| Time-to-assignment      | 2 min    | < 30 sec                                  | Timestamp incident created vs assignment made                  |
| Recommendation accuracy | N/A      | > 85% (dispatcher accepts recommendation) | # times dispatcher accepted recommendation / total assignments |
| Responder utilization   | Variable | 40–60% (healthy)                          | avg workload / max workload                                    |
| False assignments       | Unknown  | < 5% (wrong unit type sent)               | Auditor reviews assignments, counts wrong type                 |

### V2 / V3 (Future)

**V2 (Month 2):**

- Add traffic model (Google Maps API for real ETA)
- Add responder performance tracking (success rate, average resolution time)
- Add workload balancing (prefer less-busy units, but not always)
- Add mobile app for responders (push notifications)

**V3 (Month 3):**

- Add predictive routing (suggest where responders should station for quick response)
- Add demand forecasting (predict incident hotspots by time of day)
- Add multi-incident optimization (assign multiple responders to one big incident)
- Add integration with external systems (hospitals, other agencies)

---

## Interview Simulation: Follow-Up Questions

**As you present your solution, interviewer might ask:**

1. **"What if all responders are busy? Walk me through that scenario."**
   - _You:_ "We'd check if any responders are about to become available in the next 2 minutes. If yes, we queue. If no, we notify the supervisor to call in off-duty staff or redirect to a nearby city. We'd also log this as a system overload alert."

2. **"How do you prevent a responder from being sent to the wrong type of incident?"**
   - _You:_ "Capability filtering is the first gate. A fire truck can't be assigned to a medical emergency. Second, we log all assignments with reason codes so supervisor can spot mistakes. Third, responders can decline if truly unable."

3. **"Your location data is only accurate 80% of the time. How does this change your design?"**
   - _You:_ "We'd add a confidence score to each location update. If confidence < 60%, we'd mark it stale and either ask dispatcher to verify or use the last known location with explicit disclaimer. We'd also add a feedback loop: after responder arrives, we compare actual location to predicted location to improve our model."

4. **"Users are complaining that the same responder always gets assigned. Why?"**
   - _You:_ "Good catch. Our scoring is greedy: we always pick the closest available responder. Over time, they become less available, but their load is already high. We need workload balancing. Solution: in V2, we introduce a 'fairness factor' that slightly penalizes high-workload responders, even if they're closest."

5. **"What if a responder's GPS location is wrong (e.g., drifting in a tunnel)?"**
   - _You:_ "We'd add geospatial validation: check if reported location is reachable from their last known position given elapsed time and known speeds. If the jump is impossible, flag as suspicious and use previous location. We'd also have responders do periodic radio check-ins."

6. **"How do you roll this out without breaking the current system?"**
   - _You:_ "Phase 1: system runs in parallel, provides recommendations but dispatcher manually assigns (no automation). Dispatcher can compare system recommendation vs their own choice. Phase 2: after 2 weeks, enable automated assignment but with supervisor override always available. Phase 3: full automation after 4 weeks if adoption is high."

### Curveball Questions (Hard Mode)

7. **"We just learned responders are gaming the system: they're going off-duty when they get high-workload assignments to avoid them."**
   - _You:_ "This is a perverse incentive. We need to redesign: (1) change scoring to not always pick the closest (add randomness), (2) track 'acceptance rate' per responder and penalize low acceptance, (3) add incentives (bonus pay for high-utilization responders), (4) cap max workload so no one is ever overwhelmed."

8. **"Dispatchers are ignoring the system and doing it their way. Adoption is 5%."**
   - _You:_ "Lack of trust in the system. We'd investigate: Is the recommendation wrong? Is the UI confusing? Are dispatchers overloaded? Solution: (1) A/B test recommendations vs dispatcher choices to show if system is actually better, (2) make recommendations more explainable ('ETA 240s, 2 active incidents'), (3) add direct feedback: let dispatcher rate recommendations ('good' / 'poor'), (4) iterate on the algorithm based on dispatcher feedback."

9. **"We now support police, fire, and ambulance. They can't be cross-assigned. How does ranking change?"**
   - _You:_ "Capability filtering becomes the dominant factor. We'd separate responders by unit_type in the data model and filter first before scoring distance/workload. This is actually simpler, not harder."

---

## Rubric: Score Your Answer

### 1. Ambiguity Handling (1–5)

- **1:** Doesn't ask clarifying questions; assumes details
- **2:** Asks a few vague questions, misses key scope items
- **3:** Asks 5–7 targeted questions covering goal, users, scale, constraints
- **4:** Asks 8–10 excellent questions in a logical sequence
- **5:** Asks 12+ probing questions that lock down scope; anticipates follow-ups; adjusts design based on answers

### 2. Workflow Understanding (1–5)

- **1:** Misses the main flow; focuses on wrong part of system
- **2:** Describes flow but misses the bottleneck
- **3:** Describes current flow + identifies bottleneck (manual search = slow)
- **4:** Describes current flow, bottleneck, and how new system fits
- **5:** Describes current flow, bottleneck, alternative approaches to fix it, and why ranking is the right lever

### 3. Data Modeling (1–5)

- **1:** Entities not well-defined; relationships missing
- **2:** Entities rough, some relationships missing (e.g., Assignment entity unclear)
- **3:** Incident, Responder, Assignment entities clear; state transitions sketched
- **4:** All entities defined with attributes; relationships clear; state transitions detailed
- **5:** Entities + relationships + state transitions crystal clear; considers partitioning / indexing; validates edge cases

### 4. API Design (1–5)

- **1:** No API proposed or very vague
- **2:** Basic CRUD endpoints, missing validation / error cases
- **3:** Core endpoints (create incident, list responders, assign) defined with request/response shapes
- **4:** Endpoints + validation + error cases + role-based access control
- **5:** Endpoints + validation + errors + RBAC + audit logging + rate limiting + versioning

### 5. Practical MVP (1–5)

- **1:** No MVP defined; proposes too much (6+ months)
- **2:** MVP too large (4+ weeks); too many features
- **3:** MVP reasonable (2–3 weeks); cuts some features but not justified
- **4:** MVP crisp (< 2 weeks); clear trade-offs (manual assignment vs automatic, simple ranking vs ML)
- **5:** MVP + phased roadmap (V2, V3) with clear rationale; MVP is launchable in 2 weeks

### 6. Edge Cases (1–5)

- **1:** No edge cases mentioned
- **2:** Mentions 1–2 edge cases (e.g., "all busy")
- **3:** Identifies 3–4 edge cases with mitigation (no available responders, stale location, responder declines)
- **4:** Identifies 5–7 edge cases with clear mitigations; considers failure modes
- **5:** Comprehensive edge case analysis; proposes fallback flows; tests edge cases in mock code

### 7. Communication (1–5)

- **1:** Hard to follow; rambling; unclear reasoning
- **2:** Some structure but gaps; makes unsupported claims
- **3:** Clear structure; explains reasoning; minor gaps (e.g., skips security)
- **4:** Well-structured; clear examples; anticipates questions
- **5:** Crystal-clear; concise; uses analogies; handles follow-ups gracefully; adjusts explanation for audience

---

## Next Steps

1. **Time yourself:** Can you go through all 7 phases (clarify → model → design → edge cases → MVP → metrics → V2) in 45 min?
2. **Run the code:** Go to `python/911_dispatch_sim.py` and complete the TODO sections.
3. **Compare:** Read `solutions/01_911_dispatch_solution.md` for a full reference answer.
4. **Mock interview:** Record yourself presenting this solution, then watch it back and improve your pace and clarity.

---

_Good luck! 🚓🚒🚑_
