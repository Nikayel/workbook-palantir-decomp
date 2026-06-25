# Lab 01 — Craft Coding + Write-Your-Own-Tests

**Company:** Atlassian
**Role:** SWE
**Style:** Codebase/craft — read unfamiliar code, test-first debugging, voluntary testing
**Tier:** 1
**Estimated time:** 45 minutes
**Status: Ready — work through all parts in order**

---

## Milestones

- [ ] M1 · Read — understood what the code does before writing any tests
- [ ] M2 · Audited — listed all 6 bugs with line numbers and severity
- [ ] M3 · Tests written — wrote failing tests for bugs 1 and 2 (the core ones) BEFORE fixing
- [ ] M4 · Fixed — bugs 1 and 2 fixed, tests now pass
- [ ] M5 · Voluntarily tested — added 3+ tests beyond what was asked (Atlassian rewards this)
- [ ] M6 · Ready — self-graded >= 28/35

---

## Scenario

"You're in the Atlassian Karat screen. The interviewer says:

'Here's a Jira-like task management module. It has a bug where tasks marked as done still show up in active sprint queries. Please: (1) read the code, (2) write a failing test that reproduces the bug, (3) fix the bug, (4) voluntarily add tests you think are missing.'

You have 45 minutes. You can write your own tests — that's encouraged."

**What this tests:** Reading code before writing, test-first discipline, bug identification, and — critically — whether you volunteer additional tests without being prompted. Atlassian specifically trains interviewers to reward this behavior.

---

## Part 0: Forethought (5 min before touching the code)

Before reading the code, write down:

What is a task management system responsible for?
```
[blank]
```

What are the most common bugs in sprint/task systems (from a user's perspective)?
```
[blank]
```

Which Atlassian value is most relevant to test-first development?
```
[blank — hint: think about what "Don't #@!% the customer" means for data integrity]
```

---

## The Buggy Module

```python
# task_manager.py — Jira-like task management (buggy)

from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class Task:
    def __init__(self, task_id, title, assignee=None):
        self.task_id = task_id
        self.title = title
        self.assignee = assignee
        self.status = TaskStatus.TODO
        self.created_at = datetime.now()
        self.completed_at = None
        self.sprint_id = None
    
    def complete(self):
        self.status = TaskStatus.DONE
        # BUG 1: completed_at never set

class Sprint:
    def __init__(self, sprint_id, name):
        self.sprint_id = sprint_id
        self.name = name
        self.tasks = []
        self.active = True
    
    def add_task(self, task):
        task.sprint_id = self.sprint_id
        self.tasks.append(task)
    
    def get_active_tasks(self):
        # BUG 2: returns all tasks, not filtering by status
        return self.tasks
    
    def close(self):
        self.active = False
        # BUG 3: doesn't handle incomplete tasks on sprint close
    
    def get_completion_rate(self):
        if not self.tasks:
            return 0
        # BUG 4: integer division in Python 3 loses precision
        return len([t for t in self.tasks if t.status == TaskStatus.DONE]) / len(self.tasks) * 100

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.sprints = {}
    
    def create_task(self, title, assignee=None):
        task_id = len(self.tasks) + 1
        # BUG 5: task_id collision if tasks are ever deleted
        task = Task(task_id, title, assignee)
        self.tasks[task_id] = task
        return task
    
    def assign_to_sprint(self, task_id, sprint_id):
        task = self.tasks[task_id]
        sprint = self.sprints[sprint_id]
        sprint.add_task(task)
        # BUG 6: no check that sprint is still active
    
    def get_active_sprint_tasks(self, sprint_id):
        sprint = self.sprints.get(sprint_id)
        if not sprint:
            return []
        return sprint.get_active_tasks()  # delegates to buggy method
```

---

## Part 1: Read Before Writing (Atlassian Craft Signal)

**Spend 5–8 minutes reading only. No tests yet. No fixes yet.**

Describe what this module is trying to do (without running it):

**TaskStatus enum:**
```
[blank — what are the three states and what do they represent?]
```

**Task class:**
```
[blank — what does a Task track? What is complete() supposed to do?]
```

**Sprint class:**
```
[blank — what is a sprint? What does get_active_tasks() represent in a real Jira sprint board?]
```

**TaskManager class:**
```
[blank — what is this the entry point for? What workflows does it coordinate?]
```

---

## Part 2: Bug Audit (find all 6)

Fill in the table BEFORE touching the code:

| # | Line(s) | Function | Bug description | Severity |
|---|---|---|---|---|
| 1 | [blank] | Task.complete() | [blank] | Medium — audit trail broken |
| 2 | [blank] | Sprint.get_active_tasks() | [blank] | Critical — wrong data returned |
| 3 | [blank] | Sprint.close() | [blank] | [blank] |
| 4 | [blank] | Sprint.get_completion_rate() | [blank] | [blank — hint: what is 1/16*100 in Python 3?] |
| 5 | [blank] | TaskManager.create_task() | [blank] | [blank] |
| 6 | [blank] | TaskManager.assign_to_sprint() | [blank] | Medium — data integrity |

**What would `1 / 16 * 100` return in Python 3?**
```
[blank — this is the heart of bug 4]
```

**What would `1 / 16 * 100` return if rewritten as `1 * 100 / 16`?**
```
[blank]
```

---

## Part 3: Write Failing Tests FIRST (Test-Driven — Atlassian Rewards This)

Write these tests **BEFORE fixing the code**. They should FAIL when you run them. That's the point — you're proving you understand the bug before you patch it.

```python
# tests.py — write these BEFORE fixing the code
import unittest
from task_manager import Task, Sprint, TaskManager, TaskStatus

class TestSprintActiveTasks(unittest.TestCase):
    
    def setUp(self):
        self.manager = TaskManager()
        self.sprint = Sprint(1, "Sprint 1")
        self.manager.sprints[1] = self.sprint
    
    def test_done_tasks_not_in_active_sprint(self):
        """
        BUG 2: get_active_tasks() returns ALL tasks including DONE ones.
        This test should FAIL before the fix — that's the point.
        """
        task = self.manager.create_task("Implement login")
        self.manager.assign_to_sprint(task.task_id, 1)
        task.complete()
        
        active = self.manager.get_active_sprint_tasks(1)
        
        # TODO: assert task is NOT in active tasks after completion
        # Write the assertion here:
        # [blank]
    
    def test_completed_at_set_on_completion(self):
        """
        BUG 1: completed_at is never set when task.complete() is called.
        This test should FAIL before the fix.
        """
        task = self.manager.create_task("Write unit tests")
        task.complete()
        
        # TODO: assert that task.completed_at is not None
        # Write the assertion here:
        # [blank]
        
        # TODO: also assert it's a datetime, not just truthy
        # [blank]


# ============================================================
# VOLUNTARY BONUS TESTS (Atlassian rewards adding these)
# Add at least 3 tests you think are important that weren't asked for.
# Think: what could go wrong in a real Jira that users would hate?
# ============================================================

class TestVoluntaryBonusTests(unittest.TestCase):
    
    def test_completion_rate_precision(self):
        """
        BUG 4: integer division order loses precision.
        Example: 1 task done out of 16 should be 6.25%, not 0%.
        """
        # TODO: write this test
        # [blank]
    
    def test_assign_to_closed_sprint_should_fail(self):
        """
        BUG 6: TaskManager.assign_to_sprint() doesn't check if sprint is active.
        """
        # TODO: write this test
        # [blank]
    
    def test_task_id_uniqueness_after_mixed_operations(self):
        """
        BUG 5: task_id based on len(tasks) — collides if a task is deleted.
        """
        # TODO: write this test — create tasks, then think about what happens
        # if one were deleted and a new one created
        # [blank]
    
    # Add more voluntary tests here:
    # What happens if get_active_tasks is called on a closed sprint?
    # What if a task is assigned to multiple sprints?
    # What if complete() is called twice?
    # [blank]


if __name__ == '__main__':
    unittest.main()
```

---

## Part 4: Fix the Bugs

Fix bugs 1 and 2 first (these are the core bugs named in the scenario). Then fix as many others as you can.

**Fixed task_manager.py:**

```python
# task_manager.py — FIXED VERSION
# Write your corrected implementation here:

# [blank — implement the full corrected module]
```

**Checkpoint:** After fixing, run your tests. They should now pass. If they don't, diagnose why before moving on.

---

## Part 5: Craft Reasoning

Answer these before moving to Part 6:

**Why write tests before fixing? What does the failing test prove that a passing test doesn't?**
```
[blank]
```

**What's the concrete danger of bug 5 (task_id collision)?**
```
[blank — hint: what happens to task_id = 3 if you create tasks 1, 2, 3, delete task 3, then create task 4?]
```

**If you were doing a code review of this module, beyond the 6 bugs, what would you flag?**
```
[blank — think about: error handling on None task/sprint lookups, missing type hints, no docstrings]
```

**Which Atlassian value does "voluntarily adding tests" most directly demonstrate?**
```
[blank — hint: you weren't asked to, but you did it anyway because you saw it was needed]
```

**Bug 4 is a Python 3 integer arithmetic issue. What's the general principle?**
```
[blank — think about: multiply before divide when you want floating-point precision]
```

---

## Part 6: Curveballs + Values Integration

These come up in the Karat screen and the Values interview. Answer each with both a **technical response** and a **values linkage**.

**Curveball 1:** "You notice bug 6 (assigning to a closed sprint) but it's not in scope for this task. Do you fix it silently, mention it, or ignore it?"
```
Technical decision: [blank]
Which value guides you: [blank]
Why: [blank]
```

**Curveball 2:** "You fixed bugs 1 and 2, but bug 3 (incomplete tasks on sprint close not being handled) is a data integrity issue — it could cause reporting dashboards to show incorrect completion rates for historical sprints. How do you raise this without derailing the interview?"
```
What you say: [blank]
Which value: [blank]
Why this matters to the customer: [blank]
```

**Curveball 3:** "A teammate says 'the tests are good enough, ship it.' You disagree — you think the task_id collision bug (bug 5) could cause silent data corruption in production. What do you do?"
```
Your response: [blank]
Tension between values: [blank — "Build with heart and balance" vs "Be the change you seek"]
How you resolve it: [blank]
```

**Curveball 4:** "If this module were used in production at Atlassian scale (millions of tasks, thousands of sprints), which bug is the most dangerous and why?"
```
Most dangerous: [blank]
Reasoning: [blank]
```

---

## Part 7: Self-Assessment Rubric

Score yourself honestly. Target >= 28/35 before considering this lab done.

| Dimension | 5 — Strong | 3 — Solid | 1 — Needs Work | Your Score |
|---|---|---|---|---|
| Code reading | Identified all 6 bugs; described intent of each class accurately | Found 3–5 bugs; intent mostly correct | Found 1–2 bugs or misread intent of key classes | __ /5 |
| Test-first discipline | Wrote failing tests BEFORE making any changes to the code | Fixed first, then wrote tests to verify | No tests written, or tests written after fix only | __ /5 |
| Voluntary testing | Added 3+ extra tests unprompted, covering realistic failure modes | Added 1–2 extra tests beyond requirements | Only wrote the two required tests | __ /5 |
| Bug fixing | All core bugs (1 and 2) fixed correctly; at least 2 of the remaining fixed cleanly | Core bugs fixed; some edge cases missed | Partial fix, or fixes introduced new bugs | __ /5 |
| Craft / code quality | Clean variable names, no hacks, idiomatic Python, consistent style | Functional but rough; some naming issues | Messy, over-engineered, or incorrect style | __ /5 |
| Values awareness | Linked specific decisions to named Atlassian values in Part 6 | Named values loosely; linkage was vague | No value awareness demonstrated | __ /5 |
| Time management | All parts complete in < 40 minutes with time to review | Complete in 40–50 minutes | Ran out of time before finishing Part 4 | __ /5 |

**Total: __ / 35**

---

## Reflection

**What was the hardest part?**
```
[blank]
```

**What would you do differently with 5 more minutes?**
```
[blank]
```

**Which Atlassian value felt most natural to demonstrate? Which felt hardest?**
```
[blank]
```

---

## Ready-When Checklist

- [ ] I can describe all 6 bugs from memory without looking at the code
- [ ] I can explain *why* test-first is better than fix-first in 30 seconds
- [ ] I have at least 5 voluntary test ideas ready (not just the 2 required)
- [ ] I can name the Atlassian value behind each decision in Part 6
- [ ] I completed the full workbook under 45 minutes
- [ ] I scored >= 28/35

---

*Next lab: `lab_02_lld_notification` — Code Design round, Observer pattern, Open/Closed Principle*
