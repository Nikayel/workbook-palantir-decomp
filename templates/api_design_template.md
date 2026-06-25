# API Design Template

Use this template to design REST-like APIs for your decomposition solution.

---

## Principles

1. **Resources, not verbs** – Use nouns (incidents, responders, tasks)
2. **Standard HTTP methods** – GET (retrieve), POST (create), PUT (update), DELETE (remove)
3. **Consistent response format** – Always { data, error, metadata }
4. **Validation first** – Check inputs before processing
5. **Access control** – Every endpoint enforces role-based permissions
6. **Error handling** – Use standard HTTP codes, provide error details

---

## API Design Checklist

- [ ] Resource identified (e.g., `/api/v1/incidents`)
- [ ] Four CRUD operations defined (C, R, U, D)
- [ ] Request shape with validation rules
- [ ] Response shape with example
- [ ] Error cases (4xx, 5xx) with messages
- [ ] Role-based access control (who can call this?)
- [ ] Rate limiting (if needed)
- [ ] Audit logging (if sensitive)

---

## Template: One Resource

### Resource: Incidents

**Purpose:** Create, retrieve, and manage emergency incidents

---

### 1. Create Incident

**Endpoint:** `POST /api/v1/incidents`

**Description:** Create a new incident and request responders

**Permissions:** Requires role: `dispatcher`, `citizen`, `admin`

**Request:**

```json
{
  "type": "string (enum: fire, medical, accident, etc.)",
  "severity": "integer (1-10)",
  "location": {
    "latitude": "number",
    "longitude": "number",
    "address": "string (optional)"
  },
  "description": "string (optional)"
}
```

**Validation:**

- `type` is one of: fire, medical, accident, utility, other
- `severity` is between 1 and 10
- `location` latitude is between -90 and 90
- `location` longitude is between -180 and 180
- `description` is <= 500 characters

**Response (201 Created):**

```json
{
  "data": {
    "incident_id": "uuid",
    "status": "new",
    "type": "fire",
    "severity": 8,
    "location": { "latitude": 40.7128, "longitude": -74.006 },
    "created_at": "2024-01-15T10:30:00Z",
    "created_by": "user_123"
  },
  "metadata": {
    "responders_assigned": 0
  }
}
```

**Error Responses:**

- `400 Bad Request` – Invalid input (e.g., severity > 10)
  ```json
  { "error": "Validation failed", "details": { "severity": "must be <= 10" } }
  ```
- `403 Forbidden` – User lacks permission to create incidents
  ```json
  { "error": "Insufficient permissions", "required_role": "dispatcher" }
  ```
- `409 Conflict` – Incident already exists at location
  ```json
  { "error": "Incident already exists", "existing_id": "uuid" }
  ```
- `500 Internal Server Error` – System failure
  ```json
  { "error": "Internal server error", "request_id": "req_xxx" }
  ```

**Rate Limit:** 1000 requests per minute

**Audit Log:** Log user, timestamp, location, severity

---

### 2. Get Incident

**Endpoint:** `GET /api/v1/incidents/{incident_id}`

**Description:** Retrieve details of a specific incident

**Permissions:** Requires role: `dispatcher`, `responder`, `admin`

**Request Parameters:** None

**Response (200 OK):**

```json
{
  "data": {
    "incident_id": "uuid",
    "status": "assigned",
    "type": "fire",
    "severity": 8,
    "location": {
      "latitude": 40.7128,
      "longitude": -74.006,
      "address": "123 Main St"
    },
    "description": "Structure fire in warehouse",
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:31:00Z",
    "responders_assigned": [
      {
        "responder_id": "resp_1",
        "unit_type": "fire_truck",
        "eta_seconds": 240
      },
      { "responder_id": "resp_2", "unit_type": "ambulance", "eta_seconds": 180 }
    ]
  }
}
```

**Error Responses:**

- `404 Not Found` – Incident does not exist
- `403 Forbidden` – User lacks permission to view this incident

---

### 3. List Incidents

**Endpoint:** `GET /api/v1/incidents`

**Description:** List all incidents with filters

**Permissions:** Requires role: `dispatcher`, `admin`

**Query Parameters:**

```
?status=new,assigned,resolved
&severity_min=5
&severity_max=10
&created_after=2024-01-15T00:00:00Z
&limit=50
&offset=0
```

**Response (200 OK):**

```json
{
  "data": [
    {
      "incident_id": "uuid",
      "status": "assigned",
      "type": "fire",
      "severity": 8,
      "location": { "latitude": 40.7128, "longitude": -74.006 },
      "created_at": "2024-01-15T10:30:00Z",
      "responders_count": 2
    }
  ],
  "metadata": {
    "total": 1250,
    "limit": 50,
    "offset": 0,
    "next_offset": 50
  }
}
```

**Validation:**

- `limit` is 1–100 (default 50)
- `offset` is >= 0
- `severity_min`, `severity_max` are 1–10
- `status` is one of: new, assigned, en_route, resolved, closed

**Error Responses:**

- `400 Bad Request` – Invalid filter (e.g., limit > 100)
- `403 Forbidden` – User lacks permission to list all incidents

---

### 4. Update Incident

**Endpoint:** `PUT /api/v1/incidents/{incident_id}`

**Description:** Update incident status or details

**Permissions:** Requires role: `dispatcher`, `admin`

**Request:**

```json
{
  "status": "string (enum: assigned, en_route, resolved, closed)",
  "severity": "integer (optional, 1-10)",
  "notes": "string (optional)"
}
```

**Validation:**

- `status` is one of: assigned, en_route, resolved, closed
- `severity` is between 1 and 10
- Only `dispatcher` or `admin` can update status
- Can only transition from one valid state to another (e.g., new → assigned, not new → resolved)

**Response (200 OK):**

```json
{
  "data": {
    "incident_id": "uuid",
    "status": "en_route",
    "severity": 8,
    "notes": "Responders en route, ETA 2 min"
  }
}
```

**Error Responses:**

- `404 Not Found` – Incident does not exist
- `400 Bad Request` – Invalid status transition (e.g., resolved → new)
- `403 Forbidden` – User lacks permission to update

**Audit Log:** Log who changed status, when, and reason (if provided)

---

### 5. Delete Incident

**Endpoint:** `DELETE /api/v1/incidents/{incident_id}`

**Description:** Delete an incident (typically only for test/admin)

**Permissions:** Requires role: `admin` only

**Response (204 No Content):** Empty response, status 204

**Error Responses:**

- `404 Not Found` – Incident does not exist
- `403 Forbidden` – User lacks permission to delete
- `400 Bad Request` – Cannot delete incident in resolved/closed status

**Audit Log:** Log admin who deleted, timestamp, incident details

---

## Request / Response Format Standards

### All Requests

**Headers:**

```
Authorization: Bearer {jwt_token}
Content-Type: application/json
X-Request-ID: uuid (generated by client for tracing)
```

### All Responses

**Success (2xx):**

```json
{
  "data": { ... },
  "metadata": { ... } // optional
}
```

**Error (4xx, 5xx):**

```json
{
  "error": "string (human-readable message)",
  "error_code": "string (machine-readable code, e.g., VALIDATION_ERROR)",
  "details": { ... }, // optional, field-level errors
  "request_id": "uuid" // for debugging
}
```

---

## Role-Based Access Control (RBAC)

**Roles:**

- `citizen` – Can create incidents, view their own incidents
- `dispatcher` – Can create/view/update/delete incidents, assign responders
- `responder` – Can view assigned incidents, update status
- `admin` – Can do anything

**Rule Matrix:**

| Endpoint               | Citizen | Dispatcher | Responder       | Admin |
| ---------------------- | ------- | ---------- | --------------- | ----- |
| POST /incidents        | ✓       | ✓          | ✗               | ✓     |
| GET /incidents/{id}    | ✓ (own) | ✓          | ✓ (assigned)    | ✓     |
| GET /incidents         | ✗       | ✓          | ✗               | ✓     |
| PUT /incidents/{id}    | ✗       | ✓          | ✓ (status only) | ✓     |
| DELETE /incidents/{id} | ✗       | ✗          | ✗               | ✓     |

---

## Error Codes

**Standard error codes to use consistently:**

| Code               | HTTP Status | Meaning                                    |
| ------------------ | ----------- | ------------------------------------------ |
| `VALIDATION_ERROR` | 400         | Input validation failed                    |
| `UNAUTHORIZED`     | 401         | Missing/invalid authentication             |
| `FORBIDDEN`        | 403         | Authenticated but insufficient permissions |
| `NOT_FOUND`        | 404         | Resource does not exist                    |
| `CONFLICT`         | 409         | Request conflicts with current state       |
| `RATE_LIMITED`     | 429         | Too many requests                          |
| `INTERNAL_ERROR`   | 500         | Server error                               |

---

## Rate Limiting

**Per-user rate limits:**

- Authenticated: 1000 requests / minute
- Unauthenticated: 100 requests / minute

**Response headers:**

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1705316460
```

**When limit exceeded:**

```
HTTP 429 Too Many Requests

{
  "error": "Rate limit exceeded",
  "error_code": "RATE_LIMITED",
  "retry_after_seconds": 60
}
```

---

## Versioning

**API Version in URL:**

```
/api/v1/incidents
/api/v2/incidents  (future)
```

**Backward compatibility:**

- Minor changes (new optional fields): no version bump
- Major changes (removed fields, breaking format): version bump
- Deprecation window: 6 months before v1 shutdown

---

## Implementation Checklist

- [ ] All endpoints defined with method, path, description
- [ ] All request/response shapes defined with examples
- [ ] Validation rules explicit for each input
- [ ] Error cases and HTTP codes listed
- [ ] Role-based access control matrix complete
- [ ] Rate limiting strategy defined
- [ ] Audit logging points identified
- [ ] Versioning strategy clear
