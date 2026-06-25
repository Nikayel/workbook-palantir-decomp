# Data Model Template

Use this template to define entities, relationships, and state transitions for your solution.

---

## Core Principle

A good data model answers:

1. **What are the nouns?** (entities)
2. **What do they have?** (attributes)
3. **How do they relate?** (relationships)
4. **What states can they be in?** (state machines)
5. **When do states change?** (transitions)

---

## Example: Incident Dispatch System

---

## Entity 1: Incident

**Purpose:** Represents a single emergency event

**Attributes:**

| Name                     | Type        | Required | Constraints                                        | Meaning                    |
| ------------------------ | ----------- | -------- | -------------------------------------------------- | -------------------------- |
| `incident_id`            | UUID        | Yes      | Primary key                                        | Unique identifier          |
| `type`                   | enum        | Yes      | fire, medical, accident, utility, other            | Category of incident       |
| `severity`               | int         | Yes      | 1-10                                               | Urgency scale              |
| `latitude`               | float       | Yes      | -90 to 90                                          | Location North/South       |
| `longitude`              | float       | Yes      | -180 to 180                                        | Location East/West         |
| `address`                | string      | No       | max 200 chars                                      | Human-readable location    |
| `description`            | string      | No       | max 500 chars                                      | Incident details           |
| `status`                 | enum        | Yes      | new, triaged, assigned, en_route, resolved, closed | Current state              |
| `created_at`             | timestamp   | Yes      | UTC                                                | When incident was reported |
| `updated_at`             | timestamp   | Yes      | UTC                                                | Last time modified         |
| `created_by_user_id`     | UUID        | Yes      | Foreign key to User                                | Who reported               |
| `assigned_responder_ids` | array<UUID> | No       | Foreign keys to Responder                          | Current responders         |

**Indexes:**

- Primary: `incident_id`
- Secondary: `status`, `created_at`, `(latitude, longitude)` for geospatial queries

**Partitioning (if needed):**

- Partition by `created_at` (month) for time-series queries

---

## Entity 2: Responder

**Purpose:** Represents a person/unit that can respond to incidents

**Attributes:**

| Name                  | Type          | Required | Constraints                                        | Meaning                        |
| --------------------- | ------------- | -------- | -------------------------------------------------- | ------------------------------ |
| `responder_id`        | UUID          | Yes      | Primary key                                        | Unique identifier              |
| `unit_type`           | enum          | Yes      | fire_truck, ambulance, police, utility             | Type of unit                   |
| `station_id`          | UUID          | Yes      | Foreign key to Station                             | Home base                      |
| `current_latitude`    | float         | Yes      | -90 to 90                                          | Current location (real-time)   |
| `current_longitude`   | float         | Yes      | -180 to 180                                        | Current location (real-time)   |
| `status`              | enum          | Yes      | available, en_route, on_scene, returning, off_duty | Availability status            |
| `capabilities`        | array<string> | Yes      | e.g., ["rescue", "medical", "hazmat"]              | Skills/equipment               |
| `workload`            | int           | Yes      | >= 0                                               | Number of active incidents     |
| `location_updated_at` | timestamp     | Yes      | UTC                                                | When location was last updated |
| `last_incident_id`    | UUID          | No       | Foreign key to Incident                            | Most recent assignment         |
| `created_at`          | timestamp     | Yes      | UTC                                                | When responder joined system   |

**Indexes:**

- Primary: `responder_id`
- Secondary: `status`, `station_id`, `(current_latitude, current_longitude)` for geospatial queries

---

## Entity 3: Assignment

**Purpose:** Represents the relationship between an Incident and Responders

**Attributes:**

| Name                  | Type      | Required | Constraints                                           | Meaning                   |
| --------------------- | --------- | -------- | ----------------------------------------------------- | ------------------------- |
| `assignment_id`       | UUID      | Yes      | Primary key                                           | Unique identifier         |
| `incident_id`         | UUID      | Yes      | Foreign key to Incident                               | Which incident            |
| `responder_id`        | UUID      | Yes      | Foreign key to Responder                              | Which responder           |
| `assigned_at`         | timestamp | Yes      | UTC                                                   | When assigned             |
| `assigned_by_user_id` | UUID      | Yes      | Foreign key to User                                   | Who made the assignment   |
| `status`              | enum      | Yes      | assigned, acknowledged, en_route, on_scene, completed | Assignment status         |
| `eta_seconds`         | int       | No       | >= 0                                                  | Estimated time to arrival |
| `notes`               | string    | No       | max 500 chars                                         | Dispatch instructions     |
| `completed_at`        | timestamp | No       | UTC                                                   | When responder finished   |

**Indexes:**

- Primary: `assignment_id`
- Secondary: `incident_id`, `responder_id`, `status`
- Composite: `(incident_id, status)` for "get all active assignments for incident"

---

## Entity 4: Station

**Purpose:** Represents a dispatch station or depot

**Attributes:**

| Name                 | Type   | Required | Constraints   | Meaning                   |
| -------------------- | ------ | -------- | ------------- | ------------------------- |
| `station_id`         | UUID   | Yes      | Primary key   | Unique identifier         |
| `name`               | string | Yes      | max 100 chars | Station name              |
| `latitude`           | float  | Yes      | -90 to 90     | Station location          |
| `longitude`          | float  | Yes      | -180 to 180   | Station location          |
| `district`           | string | No       | max 50 chars  | Geographic district       |
| `capacity`           | int    | Yes      | > 0           | Max responders at station |
| `current_responders` | int    | Yes      | >= 0          | Currently stationed here  |

**Indexes:**

- Primary: `station_id`
- Secondary: `district`

---

## Relationships

**Entity Relationship Diagram (text format):**

```
Incident (1) ──────────────────── (M) Assignment
            ├─> created_by ────> User
            ├─> assigned_responders ─> [Responder via Assignment]
            └─> location ────> (latitude, longitude)

Responder (1) ────────────────── (M) Assignment
           ├─> works_at ──────> Station
           └─> assigned_incidents ─> [Incident via Assignment]

Station (1) ──────────────────── (M) Responder

User (1) ──────────────────── (M) Incident [created_by]
     └──────────────────── (M) Assignment [assigned_by]
```

**Relationship Details:**

| Relationship           | Type | Meaning                                                             | Cardinality               |
| ---------------------- | ---- | ------------------------------------------------------------------- | ------------------------- |
| Incident → Responder   | M:N  | An incident has many responders; a responder handles many incidents | Via Assignment            |
| Responder → Station    | M:1  | Many responders work at one station                                 | Foreign key in Responder  |
| Incident → User        | M:1  | Many incidents reported by one user                                 | Foreign key in Incident   |
| Assignment → Incident  | M:1  | Many assignments for one incident                                   | Foreign key in Assignment |
| Assignment → Responder | M:1  | Many assignments for one responder                                  | Foreign key in Assignment |

---

## State Machines

### Incident State Machine

```
                    ┌─ new ──┐
                    │        │ (triage complete)
                    │        ▼
                    │      triaged
                    │        │ (dispatcher assigns responders)
                    │        ▼
                    │     assigned
                    │        │ (responder en route)
                    │        ▼
                    │     en_route
                    │        │ (responder on scene)
                    │        ▼
                    │     resolved (or escalated)
                    │        │ (cleanup)
                    │        ▼
                    └─────► closed
```

**Valid Transitions:**

| From       | To          | Condition                                | Actor                        |
| ---------- | ----------- | ---------------------------------------- | ---------------------------- |
| `new`      | `triaged`   | Triage assessment complete               | Dispatcher or System         |
| `triaged`  | `assigned`  | Responders assigned                      | Dispatcher                   |
| `assigned` | `en_route`  | Responders acknowledge and leave station | Responder                    |
| `en_route` | `resolved`  | Incident handled                         | Responder                    |
| `resolved` | `closed`    | Final report and cleanup                 | Dispatcher or Admin          |
| `assigned` | `closed`    | Incident cancelled                       | Dispatcher (manual override) |
| Any        | `escalated` | Supervisor override                      | Admin (curveball state)      |

**Invalid Transitions (prevent in code):**

- ❌ `new` → `resolved` (must go through triage and assignment)
- ❌ `en_route` → `new` (no rewinding)
- ❌ `closed` → anything (terminal state)

---

### Responder State Machine

```
           ┌─ available ──┐
           │               │ (assigned to incident)
           │               ▼
           │            en_route
           │               │ (arrived at scene)
           │               ▼
           │            on_scene
           │               │ (incident resolved, returning to station)
           │               ▼
           │            returning
           │               │ (back at station)
           │               ▼
           └──────────────► available

           Available ──────────┐
                               │ (off duty)
                               ▼
                           off_duty
```

**Valid Transitions:**

| From        | To          | Condition            | Trigger                 |
| ----------- | ----------- | -------------------- | ----------------------- |
| `available` | `en_route`  | Assigned to incident | Dispatcher assignment   |
| `en_route`  | `on_scene`  | Responder checks in  | Responder action        |
| `on_scene`  | `returning` | Incident resolved    | Responder action        |
| `returning` | `available` | Back at station      | Responder action or GPS |
| `available` | `off_duty`  | End of shift         | Admin or responder      |
| `off_duty`  | `available` | Start of shift       | Admin                   |
| `*`         | `off_duty`  | Emergency shutdown   | Admin only              |

---

## Data Freshness & Consistency

**Real-time Data:**

- Responder location: updated every 10 seconds via GPS
- Incident status: updated on action (seconds-level latency acceptable)
- Assignment status: updated on responder action

**Trade-offs:**

- If responder location is stale (>30 sec), mark as "stale location" in assignments
- If incident has conflicting status updates, use last-write-wins (prefer most recent timestamp)
- If assignment and incident status diverge, use incident as source of truth (responder may be offline)

**Eventual Consistency:**

- Assignment status eventually syncs with responder status within 5 minutes
- If sync fails after 10 min, alert dispatcher to manual intervention

---

## Data Access Patterns

**Common queries:**

```sql
-- Pattern 1: Get available responders near an incident
SELECT responder_id, unit_type, workload, distance_km
FROM responder
WHERE status = 'available'
  AND distance_from_incident < 5km
  AND unit_type IN ('fire_truck', 'ambulance')
ORDER BY distance_km, workload ASC
LIMIT 5;

-- Pattern 2: Get all assignments for an incident
SELECT assignment_id, responder_id, status, eta_seconds, assigned_at
FROM assignment
WHERE incident_id = ?
ORDER BY assigned_at DESC;

-- Pattern 3: Get responder's active incidents
SELECT incident_id, incident_type, severity, status
FROM incident
WHERE responder_id = ? AND status NOT IN ('resolved', 'closed');

-- Pattern 4: Get incidents by time range (analytics)
SELECT incident_id, type, severity, created_at, response_time
FROM incident
WHERE created_at BETWEEN ? AND ?
ORDER BY created_at DESC;
```

**Optimization strategies:**

- Geospatial index on (latitude, longitude) for nearby queries
- Time-series partitioning for historical analytics
- Cache responder availability status (TTL 30 sec)
- Cache incident → responder mappings (TTL 5 sec)

---

## Schema Definition (SQL example)

```sql
CREATE TABLE incident (
  incident_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  type VARCHAR(20) NOT NULL,
  severity INT NOT NULL CHECK (severity BETWEEN 1 AND 10),
  latitude FLOAT NOT NULL CHECK (latitude BETWEEN -90 AND 90),
  longitude FLOAT NOT NULL CHECK (longitude BETWEEN -180 AND 180),
  address VARCHAR(200),
  description VARCHAR(500),
  status VARCHAR(20) NOT NULL DEFAULT 'new',
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  created_by_user_id UUID NOT NULL,
  FOREIGN KEY (created_by_user_id) REFERENCES "user"(user_id),
  INDEX idx_status (status),
  INDEX idx_created_at (created_at),
  SPATIAL INDEX idx_location (latitude, longitude)
);

CREATE TABLE responder (
  responder_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  unit_type VARCHAR(20) NOT NULL,
  station_id UUID NOT NULL,
  current_latitude FLOAT NOT NULL,
  current_longitude FLOAT NOT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'available',
  capabilities JSON NOT NULL,
  workload INT DEFAULT 0,
  location_updated_at TIMESTAMP DEFAULT NOW(),
  last_incident_id UUID,
  created_at TIMESTAMP DEFAULT NOW(),
  FOREIGN KEY (station_id) REFERENCES station(station_id),
  FOREIGN KEY (last_incident_id) REFERENCES incident(incident_id),
  INDEX idx_status (status),
  INDEX idx_station (station_id),
  SPATIAL INDEX idx_location (current_latitude, current_longitude)
);

CREATE TABLE assignment (
  assignment_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  incident_id UUID NOT NULL,
  responder_id UUID NOT NULL,
  assigned_at TIMESTAMP DEFAULT NOW(),
  assigned_by_user_id UUID NOT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'assigned',
  eta_seconds INT,
  notes VARCHAR(500),
  completed_at TIMESTAMP,
  FOREIGN KEY (incident_id) REFERENCES incident(incident_id),
  FOREIGN KEY (responder_id) REFERENCES responder(responder_id),
  FOREIGN KEY (assigned_by_user_id) REFERENCES "user"(user_id),
  UNIQUE KEY (incident_id, responder_id),
  INDEX idx_incident (incident_id),
  INDEX idx_responder (responder_id),
  INDEX idx_status (status)
);

CREATE TABLE station (
  station_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(100) NOT NULL,
  latitude FLOAT NOT NULL,
  longitude FLOAT NOT NULL,
  district VARCHAR(50),
  capacity INT NOT NULL,
  current_responders INT DEFAULT 0,
  INDEX idx_district (district)
);
```

---

## Validation Rules (implement in code)

```python
# Example: Incident validation
def validate_incident(data):
    assert -90 <= data['latitude'] <= 90, "Invalid latitude"
    assert -180 <= data['longitude'] <= 180, "Invalid longitude"
    assert 1 <= data['severity'] <= 10, "Severity must be 1-10"
    assert data['type'] in ['fire', 'medical', 'accident', 'utility', 'other'], "Invalid type"
    assert len(data['description']) <= 500, "Description too long"
    return True

# Example: State transition validation
def can_transition(current_status, new_status):
    valid_transitions = {
        'new': ['triaged'],
        'triaged': ['assigned'],
        'assigned': ['en_route', 'closed'],
        'en_route': ['resolved'],
        'resolved': ['closed'],
        'closed': []  # terminal
    }
    return new_status in valid_transitions.get(current_status, [])
```

---

## Data Retention & Privacy

**Retention policies:**

- Incident records: keep for 7 years (regulatory)
- Responder location history: keep for 90 days
- User audit logs: keep for 1 year

**Privacy rules:**

- Never expose individual responder locations to citizens
- Mask precise addresses in public reports (show district only)
- Responder personal data only visible to authorized dispatchers
- Anonymize historical data after 2 years for analytics
