# Solution Reasoning

## 0. Clarifying Questions Answer Key
- **Goal**: 
  - *Question*: What is the core lifecycle of a case?
  - *Assumption*: I'll assume cases move linearly from Open -> Investigating -> Resolved/Archived.
- **Users**: 
  - *Question*: Are there different roles for investigators vs managers?
  - *Assumption*: I'll assume basic RBAC where investigators can edit, but only managers can archive.
- **Data**: 
  - *Question*: Must every change be audited?
  - *Assumption*: I'll assume a strict append-only audit log is required for legal compliance.
- **Constraints**: 
  - *Question*: What happens on a network retry?
  - *Assumption*: I'll assume all state-changing endpoints must be idempotent.
- **Scale**: 
  - *Question*: How many cases are created per day?
  - *Assumption*: I'll assume < 10,000 per day, meaning a standard relational database is perfectly fine.


## 1. State Machine
- `OPEN` -> `IN_PROGRESS` (Analyst)
- `IN_PROGRESS` -> `PENDING_APPROVAL` (Analyst)
- `PENDING_APPROVAL` -> `CLOSED` (Supervisor)
- `PENDING_APPROVAL` -> `IN_PROGRESS` (Supervisor rejects)

## 2. Idempotency & Transactions
Transitioning a state and writing an audit log must happen in a database transaction. If the audit write fails, the state change must roll back.

## 3. Data Model
`Case`, `Evidence`, `AuditLogEvent`, `User`.
