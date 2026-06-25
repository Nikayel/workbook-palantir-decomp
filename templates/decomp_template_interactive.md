# 🎯 Interactive Decomposition Template

**IMPORTANT:** Write your answers in the blank sections. Do not peek at solutions until you've filled in each section. This is hands-on practice, not a reading assignment.

---

## 1. Goal (5 minutes)

**Read the prompt. Now, answer these questions in your own words. No peeking!**

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

**Before you design anything, write your answer to each question.**

### 2a. What is the **current workflow**?

(How does this work today, without your system?)

**Your answer:**

```
Step 1: _______________________________
Step 2: _______________________________
Step 3: _______________________________
Step 4: _______________________________
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
Source 1: __________ (Freshness: _____)
Source 2: __________ (Freshness: _____)
```

---

## 3. Users / Personas (5 minutes)

**Identify all the people who interact with your system. Fill in the blanks.**

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

## 4. Current Workflow (5 minutes)

**Draw the current workflow. Describe it step-by-step.**

```
Actor 1: ________________________
Actor 2: ________________________
Actor 3: ________________________

Flow:
[Draw boxes and arrows]
```

**Write the steps:**

```
Step 1: ___________________________________
Step 2: ___________________________________
Step 3: ___________________________________
Step 4: ___________________________________
```

**Key bottleneck (what's slow/broken/manual)?**

```
_______________________________________
```

**Where does your solution fit?**

```
I would insert my system between Step ___ and Step ___,
because ___________________________________
```

---

## 5. Data Sources (3 minutes)

**Where does data come from? What's the freshness?**

| Source               | Type       | Freshness  | Problem?   |
| -------------------- | ---------- | ---------- | ---------- |
| ******\_\_\_\_****** | **\_\_\_** | **\_\_\_** | **\_\_\_** |
| ******\_\_\_\_****** | **\_\_\_** | **\_\_\_** | **\_\_\_** |
| ******\_\_\_\_****** | **\_\_\_** | **\_\_\_** | **\_\_\_** |

**What data are we missing?**

```
_______________________________________
_______________________________________
```

---

## 6. Core Entities (5 minutes)

**What are the main objects in this system?**

### Entity 1: ******\_\_\_\_******

**Attributes (what properties does it have?):**

```
- id: _______________________
- name: _____________________
- status: ____________________
- timestamp: __________________
- Other: ______________________
```

**Relationships (how does it connect to other objects?):**

```
This entity has_many/belongs_to _______________________
```

### Entity 2: ******\_\_\_\_******

**Attributes:**

```
- id: _______________________
- Other: ______________________
```

**Relationships:**

```
_______________________________________
```

### Entity 3 (if needed): ******\_\_\_\_******

**Attributes:**

```
_______________________________________
```

---

## 7. State Transitions (5 minutes)

**What states can each entity be in?**

### Entity 1: ******\_\_\_\_******

**Write the state names:**

```
State A: _______________
State B: _______________
State C: _______________
State D: _______________
```

**Draw the transitions:**

```
State A ---(trigger: _________)---> State B
State B ---(trigger: _________)---> State C
State B ---(trigger: _________)---> State D
State C ---(trigger: _________)---> State D
```

**Who can trigger each transition?**

```
Trigger 1 ("A → B"): Can be triggered by ________________
Trigger 2 ("B → C"): Can be triggered by ________________
Trigger 3 ("B → D"): Can be triggered by ________________
```

---

## 8. APIs / Actions (7 minutes)

**What are the main actions users take?**

### Action 1: ******\_\_\_\_******

- **Who does this?** ******\_\_\_\_******
- **Input data:**
  ```
  {
    _________________,
    _________________,
    _________________
  }
  ```
- **Output data:**
  ```
  {
    _________________,
    _________________,
    _________________
  }
  ```
- **What side effects?** (logs, events, state changes)
  ```
  _______________________________________
  ```

### Action 2: ******\_\_\_\_******

- **Who does this?** ******\_\_\_\_******
- **Input data:**
  ```
  _______________________________________
  ```
- **Output data:**
  ```
  _______________________________________
  ```
- **Side effects:**
  ```
  _______________________________________
  ```

### Action 3 (if needed): ******\_\_\_\_******

- **Who does this?** ******\_\_\_\_******
- **Input/Output/Side effects:**
  ```
  _______________________________________
  ```

---

## 9. Logic / Algorithm (7 minutes)

**How do we rank, match, score, or recommend?**

### Scoring formula (in plain English first):

**Explain your logic:**

```
We score each candidate by:
1. _____________________________ (weight: ____ )
2. _____________________________ (weight: ____ )
3. _____________________________ (weight: ____ )

Then we sort by total score and return top 3.
```

### Pseudo-code:

```python
def score(candidate):
  score = 0
  # Signal 1
  if ________________________:
    score += _______
  # Signal 2
  score += _______ * candidate.__________
  # Signal 3
  score += _______
  return score

def rank(candidates):
  scored = [(c, score(c)) for c in candidates]
  return sorted(scored, key=lambda x: x[1], reverse=True)[:3]
```

### Trade-offs:

**What are you optimizing for?**

```
_______________________________________
```

**What are you sacrificing?**

```
_______________________________________
```

**Why is this trade-off acceptable?**

```
_______________________________________
```

---

## 10. Edge Cases (7 minutes)

**For each scenario, describe what happens and how we handle it.**

### Edge case 1: No candidates available

**Scenario:** ************\_\_\_************

```
What do we do?
_______________________________________
_______________________________________
```

### Edge case 2: Data is missing or stale

**Scenario:** ************\_\_\_************

```
What do we do?
_______________________________________
_______________________________________
```

### Edge case 3: Conflicting signals

**Scenario:** ************\_\_\_************

```
What do we do?
_______________________________________
_______________________________________
```

### Edge case 4: All attempts fail

**Scenario:** ************\_\_\_************

```
Fallback: ___________________________
Who gets notified: ___________________
```

### Edge case 5: (Your choice) ******\_\_\_\_******

```
_______________________________________
```

---

## 11. Security / Permissions (5 minutes)

**Who can see what data?**

```
- User role A: Can see _________________________
- User role B: Can see _________________________
- Admin: Can see ________________________________
```

**Who can take what actions?**

```
- Action 1: Allowed for _____________________
- Action 2: Allowed for _____________________
- Action 3: Allowed for _____________________
```

**How do we prevent abuse?**

```
Protection 1: ____________________________
Protection 2: ____________________________
Protection 3: ____________________________
```

**What do we audit/log?**

```
- Log all: _________________________________
- Alert on: ________________________________
```

---

## 12. MVP: Minimum Viable Product (3 minutes)

**What's the smallest viable system?**

**In 2 weeks, we'd ship:**

```
✓ Feature 1: ____________________________
✓ Feature 2: ____________________________
✓ Feature 3: ____________________________
```

**What do we NOT ship in MVP?**

```
✗ Feature 4: ____________________________
✗ Feature 5: ____________________________
```

**Why these trade-offs?**

```
_______________________________________
```

---

## 13. Success Metrics (3 minutes)

**How do we measure success?**

### Metric 1: ******\_\_\_\_******

```
Definition: ______________________________
Baseline: __________________________________
Target: ____________________________________
How we measure: ____________________________
```

### Metric 2: ******\_\_\_\_******

```
Definition: ______________________________
Baseline: __________________________________
Target: ____________________________________
How we measure: ____________________________
```

### Metric 3: ******\_\_\_\_******

```
Definition: ______________________________
```

---

## 14. V2 / V3 Roadmap (3 minutes)

**What do we add after MVP?**

### V2 (Months 2–3):

```
- Feature: ____________________________
  Why: ______________________________
- Feature: ____________________________
  Why: ______________________________
```

### V3 (Months 4–6):

```
- Feature: ____________________________
- Feature: ____________________________
```

### When do we expand?

```
We expand when: ___________________________
New scale: ______________________________
```

---

## Scoring Checklist (Self-Review)

**Before comparing to the solution, score yourself:**

- [ ] I asked clarifying questions
- [ ] I identified the bottleneck
- [ ] I defined all users/personas
- [ ] I identified core entities and relationships
- [ ] I described state transitions
- [ ] I proposed APIs with inputs/outputs
- [ ] I explained my scoring/ranking logic
- [ ] I handled 5+ edge cases
- [ ] I discussed security/permissions
- [ ] I defined an MVP with clear trade-offs
- [ ] I defined success metrics
- [ ] I described V2/V3 plans
- [ ] I could explain this to an interviewer in 45 minutes

**Count your checkmarks: **\_** / 13**

---

## Now Compare to the Solution

**Once you've filled in all sections, read the expected decomposition.**

- Where did you miss something?
- Where did you go deeper than expected?
- Did you ask different questions?
- Did you think of edge cases they didn't?

**This is where you learn!**
