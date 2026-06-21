# Solution Reasoning

## 0. Clarifying Questions Answer Key
- **Goal**: 
  - *Question*: Do we just fix the bugs, or rewrite the whole system?
  - *Assumption*: I'll assume we should safely patch the critical bugs without rewriting everything, to minimize regression risk.
- **Users**: 
  - *Question*: Who relies on the output of this script?
  - *Assumption*: I'll assume downstream reporting pipelines rely on the exact current output format.
- **Data**: 
  - *Question*: Is the historical data format changing?
  - *Assumption*: I'll assume no, we must maintain backwards compatibility.
- **Constraints**: 
  - *Question*: Are there testing constraints?
  - *Assumption*: I'll assume I must write unit tests that prove the fix works on old buggy inputs.
- **Scale**: 
  - *Question*: Does this script process massive data?
  - *Assumption*: I'll assume scale isn't the issue here; correctness and edge-case handling are.


## The 5 Bugs
1. `tickets.sort(key=lambda x: x["priority"])` sorts ascending. If 1 is high priority, this is fine. But usually, higher numbers mean higher priority, or it mutates the input array which is a side-effect.
2. `if a["status"] == "vacation": pass` does nothing. It should be `continue`. The vacationing agent still gets evaluated!
3. `best_agent == None` should be `best_agent is None`. More importantly, if *all* agents are on vacation, `best_agent` remains None, causing a crash on line `best_agent["name"]`.
4. The system assigns tickets even if no agent is eligible.
5. Mutating `best_agent["current_workload"]` mutates the input dictionary.

## The Fix
- Do not mutate inputs. Return a new structure.
- Add robust filtering.
- Handle the `None` case gracefully.
- Implement the `language` requirement by adding a filter condition.
