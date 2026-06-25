# 🎯 Interactive Decomposition Template

Use this template for **every drill**. Write your answers in the blank sections. Do not peek at solutions until you've filled in each section.

---

## 1. Goal (5 minutes)

**Read the prompt. Now, answer these questions in your own words:**

### 1a. What problem are we solving?

(In 1–2 sentences, describe the core problem without jargon.)

**Your answer:**

```
_______________________________________
_______________________________________
```

### 1b. Who has this problem?

(Name the people/roles affected.)

**Your answer:**

```
_______________________________________
_______________________________________
```

### 1c. What is the **primary** success metric?

(What does success look like? How do we measure it?)

**Your answer:**

```
_______________________________________
```

### 1d. What is a realistic baseline and target?

(Example: "Current response time is 12 min. Target is 8 min.")

**Your answer:**

```
Baseline: _______________
Target: _______________
```

---

## 2. Clarifying Questions (5–10 minutes)

**Before you design anything, ask these questions:**

### 2a. What is the **current workflow**?

(How does this work today, without your system?)

**Your answer:**

```
_______________________________________
_______________________________________
```

### 2b. Where is the bottleneck?

(What is slow, broken, or manual?)

**Your answer:**

```
_______________________________________
```

### 2c. How much **scale** are we talking about?

(Incidents/day? Users? Data size?)

**Your answer:**

```
_______________________________________
```

### 2d. What are the key **constraints**?

(Latency SLA? Budget? Compliance?)

**Your answer:**

```
_______________________________________
```

### 2e. What **data sources** exist?

(Where does data come from? How fresh?)

**Your answer:**

```
_______________________________________
_______________________________________
```

---

## 3. Users / Personas (5 minutes)

**Identify all the people who interact with your system.**

### 3a. Primary user #1: ******\_\_\_\_******

- **Role:** (What do they do?)
  ```
  _______________________________________
  ```
- **Pain point:** (What frustrates them?)
  ```
  _______________________________________
  ```
- **Key actions:** (What do they do with your system?)
  ```
  _______________________________________
  ```

### 3b. Primary user #2: ******\_\_\_\_******

- **Role:**
  ```
  _______________________________________
  ```
- **Pain point:**
  ```
  _______________________________________
  ```
- **Key actions:**
  ```
  _______________________________________
  ```

### 3c. Secondary user / Admin: ******\_\_\_\_******

- **Role:**
  ```
  _______________________________________
  ```
- **Why they use your system:**
  ```
  _______________________________________
  ```

---

## 3. Current Workflow

**Today, how does this work?** (or how should it work?)

```
[Draw or describe the flow]
User A → System → User B → Outcome
```

**Key bottleneck:**

- ***

## 4. Data Sources

**Where does data come from?**

- Source 1: **\_\_\_** (SLA: **\_**, Freshness: **\_**)
- Source 2: **\_\_\_** (SLA: **\_**, Freshness: **\_**)

**What data is missing or stale?**

- ***

## 5. Core Entities

**What are the main objects?**

| Entity   | Attributes                   | Relationships | Notes            |
| -------- | ---------------------------- | ------------- | ---------------- |
| Entity A | id, name, status, created_at | has many B    | Primary entity   |
| Entity B | id, ref_to_A, ...            | belongs to A  | Secondary entity |

---

## 6. State Transitions

**What states can each entity be in?**

```
Entity A:
  NEW → PROCESSING → COMPLETED → CLOSED

Transitions:
  NEW → PROCESSING: when triggered_by_user = true
  PROCESSING → COMPLETED: when condition_met = true
  COMPLETED → CLOSED: when confirmed_by_admin = true
```

**Who can trigger each transition?**

- Transition 1: User, System, Admin
- Transition 2: User, Admin

---

## 7. APIs / Actions

**What actions do users take?**

| Action   | User   | Input      | Output     | Side Effect  |
| -------- | ------ | ---------- | ---------- | ------------ |
| create_X | User A | name, ...  | id, status | Event logged |
| get_X    | User A | id         | X obj      | None         |
| list_X   | User A | filters    | [X]        | None         |
| update_X | Admin  | id, fields | updated X  | Event logged |

**API endpoints:**

```
POST /api/v1/x
  Input: { name, ... }
  Output: { id, status, created_at }
  Errors: 400 (invalid), 409 (conflict), 500 (server)

GET /api/v1/x/:id
  Input: { id }
  Output: { id, name, status, ... }
  Errors: 404 (not found)

GET /api/v1/x
  Input: { filter_by_status, filter_by_user, limit, offset }
  Output: { items: [X], total, next_offset }
  Errors: 400 (invalid filter)
```

---

## 8. Logic / Algorithm

**How do we rank, match, score, or recommend?**

```
def rank_candidates(user, context):
  candidates = filter_by_constraints(user, context)
  scores = [score(c, context) for c in candidates]
  return sorted(scores, key=lambda s: s.score, reverse=True)

def score(candidate, context):
  score = 0
  score += 10 if candidate.availability == "available" else 0
  score += 5 if candidate.distance < 5km else 2 if candidate.distance < 10km else 0
  return score
```

**Heuristics & trade-offs:**

- Distance vs availability vs skill level → weighted score
- Real-time accuracy vs stale data → use cache with TTL
- Fairness vs optimality → randomize among top-3

**How do you handle ties?**

- If scores are equal, prefer the one with lower workload
- If still tied, prefer the one with most recent success

---

## 9. Edge Cases

| Edge Case               | Scenario                       | Mitigation                                       |
| ----------------------- | ------------------------------ | ------------------------------------------------ |
| No candidates available | All options exhausted          | Escalate to human, queue the request             |
| Stale data              | Location data is 1 hour old    | Use cache TTL + fallback to approximate position |
| Missing data            | User has no location           | Use default location or ask user                 |
| Conflicting signals     | Two data sources disagree      | Log discrepancy, use more recent source          |
| Bad data                | Negative score, invalid status | Validate input, log anomaly, alert operator      |

---

## 10. Security / Permissions

**Who can see what?**

- User A can see their own data and data they created
- Admin can see all data
- System can see everything for logging

**Who can take what actions?**

- User A: create, read own
- Admin: create, read all, update, delete
- System: audit all actions

**How do we prevent abuse?**

- Rate limit API calls (100 req/min per user)
- Validate all input (length, format, range)
- Log all actions for audit trail
- Encrypt sensitive data at rest

**Audit trail:**

```
{
  action: "create_X",
  actor: "user_123",
  resource: "X_456",
  timestamp: "2024-01-15T10:30:00Z",
  changes: { before: {}, after: { name: "foo" } }
}
```

---

## 11. MVP (Minimum Viable Product)

**What's the smallest viable system?**

- **Scope:** Support 100 users, 1000 requests/day
- **Features:**
  - Create X
  - View X
  - List X with basic filters
  - Simple ranking algorithm (distance + availability)
- **No:** Advanced analytics, historical reports, integrations
- **Timeline:** 2 weeks

**Why these cuts?**

- Authentication/RBAC can be added later (start with single role)
- Advanced scoring requires more data (start with simple heuristics)
- Analytics requires instrumentation (add after MVP proves value)

---

## 12. Metrics

**How do you measure success?**

| Metric        | Baseline | Target          | How to track       |
| ------------- | -------- | --------------- | ------------------ |
| Latency (p95) | 500ms    | <200ms          | APM tool           |
| Accuracy      | 60%      | >85%            | Manual spot checks |
| Adoption      | 0%       | >50% users/week | Event tracking     |
| Error rate    | 5%       | <1%             | Error logs         |

**How do you iterate?**

- Weekly dashboard review
- Monthly analysis of failure cases
- Quarterly roadmap update based on metrics

---

## 13. V2 / V3

**Iteration 2 (Month 2):**

- Add advanced scoring (ML model)
- Add historical performance tracking
- Add user feedback loop

**Iteration 3 (Month 3):**

- Add real-time dashboard for admins
- Add batch optimization for multi-request workloads
- Add integration with external systems

---

## Interview Notes

**Interviewer's curveballs:**

- Curveball 1: "What if data is 80% accurate?"
  - Response: We'd add a confidence score to each signal, lower weight for low-confidence, escalate to human for review
- Curveball 2: "Your solution failed. Users aren't adopting it."
  - Response: We'd investigate through surveys and logs. Check if UX is confusing, if the recommendations are poor, or if there's organizational resistance. Iterate based on feedback.

- Curveball 3: "We now have 100x more data. What breaks?"
  - Response: Latency would break if we're doing real-time aggregation. We'd add caching, async processing, and sampling for analytics.

**Communication notes:**

- [Practice narrating this design out loud]
- [Draw the workflow 3x until it feels natural]
- [Prepare 2–3 analogies to explain the logic]
