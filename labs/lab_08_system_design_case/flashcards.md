# Flashcards — System Design Case: Case Management Platform

> Review **day 1 → 3 → 7 → 14**. Reset to day 1 on a miss.
> Cover each answer before reading. Free-recall — no peeking.

---

**Q:** Two analysts open the same annotation record simultaneously. Analyst A submits a change at T=100ms; Analyst B submits a conflicting change at T=150ms. How does "last write wins" resolve this, and what is its key weakness?
**A:** Last write wins (LWW) picks the change with the later timestamp — Analyst B's change survives and Analyst A's is silently discarded. Key weakness: in distributed systems, clocks are not perfectly synchronized, so T=100ms on one node may be genuinely later in wall-clock time than T=150ms on another. LWW also silently loses data — Analyst A sees their change disappear with no notification, which is unacceptable in an annotation workflow.

---

**Q:** What is optimistic locking, and how does it differ from pessimistic locking in a collaborative annotation system?
**A:** Optimistic locking: let multiple users read and edit freely; at write time, check if the version the client started with still matches the server version. If not, reject the write and return a conflict error for the client to resolve. Pessimistic locking: acquire an exclusive lock before any edit, blocking all other users until released. Optimistic is better for collaborative systems with low conflict rates — it avoids blocking and scales well. Pessimistic is safer when conflicts are frequent or transactions are long.

---

**Q:** What is a state machine in the context of case management, and what must you specify beyond just the list of states?
**A:** A state machine defines: (1) all valid states (e.g. OPEN, IN_REVIEW, CLOSED), (2) all valid transitions between states (e.g. OPEN → IN_REVIEW is valid; CLOSED → IN_REVIEW is not), (3) guards on each transition (e.g. OPEN → CLOSED requires supervisor approval), (4) actions triggered by transitions (e.g. "on CLOSED: write audit log entry"). Without guards and actions, you have a list of states, not a state machine.

---

**Q:** Design a REST API endpoint to transition a case from OPEN to CLOSED. What are the method, path, request body, success response, and at least two error responses?
**A:** `POST /cases/{case_id}/transitions` with body `{"to_state": "CLOSED", "approver_id": "u_456", "reason": "resolved"}`. Success: `200 {"case_id": "c_123", "state": "CLOSED", "transitioned_at": "2026-06-24T10:00:00Z"}`. Errors: `409 {"error": "INVALID_TRANSITION", "from": "OPEN", "to": "CLOSED", "reason": "supervisor approval required"}` if guard fails; `404 {"error": "CASE_NOT_FOUND"}` if case_id unknown; `409 {"error": "VERSION_CONFLICT"}` if optimistic lock check fails.

---

**Q:** What is event sourcing, and why is it a natural fit for a case management audit trail?
**A:** Event sourcing stores state as an append-only log of events (e.g. `CaseOpened`, `EvidenceAttached`, `StateMachineTransitioned`, `CaseClosed`) rather than as a mutable current-state record. The current state is derived by replaying events. It is a natural fit for audit trails because: every change is permanently recorded with who did what and when; you can reconstruct the full history of any case; no data is ever deleted or overwritten.

---

**Q:** When should you use WebSockets instead of polling for real-time collaboration, and what is the key operational cost of WebSockets?
**A:** Use WebSockets when you need sub-second latency for many users simultaneously (e.g. live annotation presence indicators, immediate conflict notifications). Polling works when updates are infrequent or slight delay is acceptable. Key operational cost of WebSockets: persistent connections consume server resources proportional to concurrent users — you need a connection broker (e.g. Redis Pub/Sub) to fan out messages across multiple server instances, adding infrastructure complexity.

---

**Q:** What does idempotency mean, and how do you make a "close case" API endpoint idempotent?
**A:** An idempotent operation produces the same result whether called once or N times. To make "close case" idempotent: (1) if the case is already CLOSED, return `200` with the existing closed state rather than an error; (2) use an idempotency key (client-generated UUID in the request header) — if the server has already processed a request with that key, return the cached response without re-executing the operation. This handles retries after network failures safely.

---

**Q:** What is a version vector, and how does it detect conflicts more reliably than a single timestamp?
**A:** A version vector is a map of `{node_id → counter}` that tracks how many updates each node has contributed. When two clients each independently edit from the same base version, their version vectors diverge (each increments only its own counter). On merge, if neither vector dominates the other (neither has all counts ≥ the other), it is a true conflict requiring resolution. A single timestamp fails because two nodes may produce the same timestamp or clocks may be skewed.

---

**Q:** What is a CRDT and in what scenario would you choose it over "last write wins" for a collaborative annotation system?
**A:** A CRDT (Conflict-free Replicated Data Type) is a data structure designed so that concurrent edits always merge deterministically without conflicts — no coordination required. Choose CRDTs when: (1) offline editing is required (annotations made with no connectivity must merge cleanly when synced), (2) you cannot afford merge conflicts surfaced to users, (3) the data type is amenable (text with Logoot/YATA, counters, sets). LWW is simpler but silently loses data; CRDTs are complex to implement but guarantee convergence.

---

**Q:** What is the correct structure for a system design interview answer, and what are the four phases in order?
**A:** (1) Scope: clarify requirements, name constraints, identify the one bottleneck and primary user. Do not skip this — 5 minutes here saves 20 minutes of redesign. (2) Model: define the data model and state machine before any API or code. (3) API: specify endpoints with concrete request/response schemas and error cases. (4) Tradeoffs: name 2–3 explicit design decisions, state what you chose and why, name what you explicitly did NOT build and why. End with the riskiest assumption and how you would validate it.
