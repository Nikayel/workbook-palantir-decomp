# Solution Reasoning

## 0. Clarifying Questions Answer Key
- **Goal**: 
  - *Question*: Are we trying to optimize for cost, or time-to-dispatch?
  - *Assumption*: I'll assume minimizing time-to-dispatch is the primary metric to save lives.
- **Users**: 
  - *Question*: Will responders use this on their phones, or just dispatchers?
  - *Assumption*: I'll assume dispatchers are the primary user bottleneck, so we'll build for their desktop workflow.
- **Data**: 
  - *Question*: Is the GPS data reliable and real-time?
  - *Assumption*: I'll assume GPS drops out or is noisy, so we must handle stale timestamps in our ranking logic.
- **Constraints**: 
  - *Question*: Can the system automatically dispatch a responder without human review?
  - *Assumption*: I'll assume a human-in-the-loop is legally/safety required.
- **Scale**: 
  - *Question*: How many concurrent incidents and responders are we tracking?
  - *Assumption*: I'll assume ~1000 responders per city, easily fitting in memory for fast ranking.


## 1. Why these users?
The primary user is the dispatcher. The secondary user is the responder. We focus on the dispatcher because they are the operational bottleneck.

## 2. Why this workflow?
We intercept the manual search step. The workflow remains: Call -> Dispatcher -> **System Recommends** -> Dispatcher Confirms -> Responder Assigned.

## 3. Why this data model?
We need `Incident` (where, what, severity) and `Responder` (where, capabilities, status, last_update). We also need an `AssignmentEvent` for the audit log.

## 4. Why these APIs/actions?
- `POST /recommend`: Stateless, pure function to rank.
- `POST /assign`: State transition (Available -> Busy) and writes to audit log.

## 5. Why this algorithm?
Simple filtering first (status, capabilities). Then ranking by distance (ETA proxy). We don't need ML yet; deterministic rules are easier to debug and explain.

## 6. Why this MVP?
MVP excludes automatic dispatch. Human-in-the-loop is safer for V1, allowing dispatchers to build trust and catch edge cases.

## 7. Tradeoffs
| Decision | Option A | Option B | Choice | Why |
|---|---|---|---|---|
| Assignment | Auto-dispatch | Human-in-the-loop | Human-in-the-loop | Safety and trust. |

## 8. Failure modes
- **Stale data**: If a responder's GPS died 10 mins ago, we might send them to the wrong place. *Mitigation: Filter out stale updates.*
- **System goes down**: Dispatchers revert to manual map.

## 9. How to explain this in an interview
"I built a recommendation engine that acts as a copilot for the dispatcher. It filters out ineligible responders and ranks by distance, but leaves the final decision to the human to ensure safety."

## 10. Strong vs weak answer
**Weak**: "I will build an AI model to predict where crimes happen." (Solves wrong problem, too complex).
**Strong**: "I will build a deterministic filter-and-rank function, ensuring we drop stale GPS data, and present the top 3 options with clear reasons to the dispatcher."
