# Solution Reasoning

## 1. State Machine
- `OPEN` -> `IN_PROGRESS` (Analyst)
- `IN_PROGRESS` -> `PENDING_APPROVAL` (Analyst)
- `PENDING_APPROVAL` -> `CLOSED` (Supervisor)
- `PENDING_APPROVAL` -> `IN_PROGRESS` (Supervisor rejects)

## 2. Idempotency & Transactions
Transitioning a state and writing an audit log must happen in a database transaction. If the audit write fails, the state change must roll back.

## 3. Data Model
`Case`, `Evidence`, `AuditLogEvent`, `User`.
