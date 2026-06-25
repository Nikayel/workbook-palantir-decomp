Status: Ready — work through all parts in order

# Lab 02 · LLD / OOD — A/B Test Class Design
**Microsoft SWE · Tier 2 · ~90 minutes**

---

## 🪜 Milestones

- [ ] M1 · Clarified — asked about: determinism (same user always gets same variant?), multiple experiments per user, concurrent users
- [ ] M2 · Designed — class diagram sketched on paper, interfaces named before coding
- [ ] M3 · Coded — working implementation with at least 2 classes
- [ ] M4 · Tested — wrote test cases including edge cases (0% split, 100% split, missing experiment)
- [ ] M5 · Extended — added a MultiVariant experiment type without breaking ABTest
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Scenario

You're at a **Microsoft onsite** (Superday). The interviewer says:

> "Design an A/B test class in Python. The class should support:
> - Registering experiments by name, with a percentage traffic split
> - Assigning users to experiment variants (A or B) deterministically
> - Reporting which variant a given user is assigned to
>
> Make it extensible — we'll want to add new experiment types in the future."

The interviewer then leans back and waits. There's no template. You have a blank editor.

---

## Part 0: Forethought

Before reading anything else — 3 minutes:

1. What does "deterministic" mean in this context? Why does it matter for A/B tests?
   [blank]

2. What OOP principle comes to mind when the interviewer says "extensible"?
   [blank]

3. What's one thing you'd do differently in this problem based on a past mistake?
   [blank — growth mindset priming]

---

**--- CHECKPOINT: Forethought complete. Move to Part 1. ---**

---

## Part 1: Clarifying Questions

Write the questions you'd ask before designing anything:

**Determinism:**
- Should the same user always get the same variant (even across sessions)?
  [blank — your answer and why it matters]
- If I restart the ExperimentManager, should assignments persist?
  [blank]

**Scope:**
- Can a user be enrolled in multiple experiments simultaneously?
  [blank]
- Should variants be limited to A/B, or will we eventually support A/B/C/D?
  [blank — note: the interviewer told you it should be extensible]

**Concurrency:**
- Will this class be used in a multithreaded web server?
  [blank — if yes, what does that imply?]

**Error handling:**
- What should happen if someone calls `get_variant` for an experiment that doesn't exist?
  [blank]

---

**--- CHECKPOINT: Clarifying questions complete. Move to Part 2. ---**

---

## Part 2: Design Before Coding

Sketch a class diagram. Write it here as text (or describe it):

```
[Your class diagram here]

Classes I'll need:
1. [blank — name and responsibility]
2. [blank — name and responsibility]
3. [blank — name and responsibility]

Relationships:
- [blank — which class depends on which?]
- [blank — inheritance or composition?]
```

**Design decisions you must make before coding:**

Decision 1 — How to achieve deterministic assignment:
"I'll assign users by [blank]. This achieves determinism because [blank]."

Decision 2 — How to achieve extensibility:
"I'll use [blank — abstract base class? interface? duck typing?] so future experiment types can [blank] without changing ExperimentManager."

Decision 3 — Thread safety:
"For thread safety, I'll [blank]. The reason is [blank — consider Python's GIL]."

---

**--- CHECKPOINT: Design documented. Move to Part 3. ---**

---

## Part 3: Design Decisions (Fill in the Blanks)

These are the canonical answers — fill them in before seeing Part 4's starter code.

**Determinism strategy:**
Use `hash(user_id + experiment_name) % 100 < threshold` to assign variant A.

Why does appending the experiment name matter?
[blank — hint: what happens if you just hash the user_id and have two experiments both with a 50% split?]

**Extensibility:**
Use [blank — abstract base class `Experiment` with `assign_variant()` as abstract method] so future `MultiVariantTest` can subclass without changing `ExperimentManager`.

Python's ABC module: `from abc import ABC, abstractmethod`. Why use `@abstractmethod` instead of just `raise NotImplementedError`?
[blank]

**Thread safety:**
[blank — does Python's GIL protect the `experiments` dict from concurrent writes? What would you add if you needed true safety?]

---

**--- CHECKPOINT: Design decisions filled in. Move to Part 4. ---**

---

## Part 4: Starter Code (Complete the Implementation)

The structure is given. Fill in all `[blank]` sections and `pass` statements.

```python
import hashlib
from abc import ABC, abstractmethod
from typing import Optional

class Experiment(ABC):
    """Base class for all experiments. Subclasses must implement assign_variant()."""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def assign_variant(self, user_id: str) -> str:
        """Return the variant label for this user (e.g., 'A', 'B', 'control')."""
        pass


class ABTest(Experiment):
    """Binary A/B experiment with a configurable percentage in variant A."""
    
    def __init__(self, name: str, percentage_in_a: float):
        """
        Args:
            name: Unique experiment name (used in hashing for determinism)
            percentage_in_a: Percentage of users assigned to A (0.0 to 100.0)
        """
        super().__init__(name)
        # TODO: validate percentage_in_a is between 0 and 100
        # [blank]
        
        # TODO: store the threshold
        # [blank]
    
    def assign_variant(self, user_id: str) -> str:
        """
        Deterministically assign a user to 'A' or 'B'.
        
        Strategy: hash(user_id + experiment_name) mod 100,
        then compare to threshold.
        """
        # TODO: compute a deterministic integer in [0, 100) from user_id + self.name
        # Hint: use hashlib.md5 or hashlib.sha256, take hexdigest, convert to int, mod 100
        # [blank]
        
        # TODO: compare to threshold and return 'A' or 'B'
        # [blank]
        pass


class MultiVariantTest(Experiment):
    """
    Extension: supports A/B/C/... with configurable weights.
    (Complete this after finishing ABTest — see Part 5)
    """
    pass


class ExperimentManager:
    """
    Central registry for all experiments.
    Provides registration and variant lookup.
    """
    
    def __init__(self):
        self.experiments: dict[str, Experiment] = {}
    
    def register(self, experiment: Experiment) -> None:
        """
        Register an experiment. Raises ValueError if name already registered.
        """
        # TODO: check for duplicate registration
        # [blank]
        
        # TODO: store in experiments dict
        # [blank]
        pass
    
    def get_variant(self, experiment_name: str, user_id: str) -> str:
        """
        Return the variant for this user in the named experiment.
        
        Raises:
            KeyError: if experiment_name is not registered
        """
        # TODO: look up experiment by name
        # [blank]
        
        # TODO: delegate to experiment's assign_variant
        # [blank]
        pass
    
    def list_experiments(self) -> list[str]:
        """Return names of all registered experiments."""
        # TODO
        # [blank]
        pass
```

---

**--- CHECKPOINT: ABTest and ExperimentManager implemented. Move to Part 5. ---**

---

## Part 5: Extension — MultiVariant Without Breaking ABTest

The interviewer says: "Now add `MultiVariantTest` that supports A/B/C/D with custom weights. For example, `MultiVariantTest('checkout_flow', weights={'A': 50, 'B': 30, 'C': 20})` means 50% get A, 30% get B, 20% get C."

Before coding, answer:

How does your `assign_variant` logic change for multiple variants?
[blank — hint: cumulative thresholds]

Does `ExperimentManager` need to change at all?
[blank — this is the test of your extensibility design]

Now implement `MultiVariantTest`:

```python
class MultiVariantTest(Experiment):
    def __init__(self, name: str, weights: dict[str, float]):
        """
        Args:
            weights: dict of variant_label -> percentage (must sum to 100)
        """
        super().__init__(name)
        # TODO: validate weights sum to 100
        # [blank]
        
        # TODO: store as cumulative thresholds for efficient lookup
        # e.g., {'A': 50, 'B': 80, 'C': 100} for weights A=50, B=30, C=20
        # [blank]
    
    def assign_variant(self, user_id: str) -> str:
        # TODO: same hash trick, then find which bucket the user falls into
        # [blank]
        pass
```

---

**--- CHECKPOINT: MultiVariantTest implemented. Move to Part 6. ---**

---

## Part 6: Curveballs

**Curveball 1:**
"What if the tree has 10 million users and you're calling `get_variant` 10,000 times per second? Is your current implementation fast enough?"
[blank — hint: hashing is O(1), dict lookup is O(1), so what's the actual bottleneck? Is there one?]

**Curveball 2:**
"A product manager says: 'I want to be able to pause an experiment and put everyone in the control group.' How do you add this without changing how ExperimentManager or the base Experiment class work?"
[blank — hint: can you add a `paused` flag or a `PausedExperiment` wrapper?]

**Curveball 3:**
"The interviewer says: 'Tell me about a time you had to refactor a class hierarchy that wasn't extensible. What did you learn?' How does today's A/B test design reflect that lesson?"
[blank — growth mindset connection to OOD]

---

**--- CHECKPOINT: Curveballs answered. Move to Part 7. ---**

---

## Part 7: Self-Assessment Rubric

Score yourself honestly. Total = 35 points. Target: ≥ 28 to be ready.

| Dimension | 5 | 3 | 1 | Your Score |
|---|---|---|---|---|
| Communication / Think-Aloud | Narrated design decisions, trade-offs, and class relationships throughout | Narrated most of the design, with some silent coding | Coded silently, revealed decisions only when asked | /5 |
| Problem Solving | Identified abstract base class + hashing strategy immediately; explained "why" behind each choice | Got to the right design after some prompting | Needed the starter code structure to make progress | /5 |
| Correctness | ABTest + ExperimentManager correct; MultiVariant handles cumulative thresholds correctly | ABTest correct but MultiVariant had a logic error | ABTest implementation incorrect or non-deterministic | /5 |
| Code Quality | Clean class hierarchy, clear method names, no code smell, docstrings or comments where needed | Mostly clean with one or two issues (e.g., magic numbers, inconsistent naming) | Messy, tightly coupled, or hard to extend | /5 |
| Testing & Edge Cases | Proactively tested: 0% split, 100% split, duplicate registration, missing experiment, same user across 2 experiments | Tested happy path + one edge case | Only tested happy path | /5 |
| Debugging | Caught and explained at least one design error during implementation | Got confused but resolved it | Could not debug without assistance | /5 |
| Growth Mindset | Authentically reflected on what was hard (OOP design, hashing, thread safety) and what you'd do differently | Some reflection but minimal depth | Claimed the design came naturally, no reflection | /5 |

**Total: /35**

---

### Reflection

What's the most important OOD lesson you're taking from this lab?
[blank]

---

### Ready-When Checklist

- [ ] I can explain what `@abstractmethod` does and why it's better than `raise NotImplementedError`
- [ ] I can explain the `hash(user_id + experiment_name) % 100` trick and why the experiment name is included
- [ ] I can extend this design to support MultiVariant without touching `ExperimentManager`
- [ ] I can explain Python's GIL and when it's not sufficient for thread safety
- [ ] I have a genuine story about a class design that wasn't extensible and what I learned
- [ ] Self-score ≥ 28/35
