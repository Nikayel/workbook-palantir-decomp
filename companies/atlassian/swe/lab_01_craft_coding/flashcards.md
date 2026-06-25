# Flashcards — Lab 01 Craft Coding

**Company:** Atlassian | **Lab:** 01 | **Style:** Craft coding + test-first debugging

---

## Card 1: Test-First vs Test-After — Why Does It Matter?

**Q:** Why write tests before fixing a bug instead of after?

**A:** A test written after the fix only proves "the fix didn't break the test" — it doesn't prove the test actually catches the original bug. Writing a failing test first proves you have a reproducible definition of the bug. If your test doesn't fail on the buggy code, you don't understand the bug yet. This is the test-first discipline Atlassian specifically rewards: it shows methodical craft over rushing to ship.

---

## Card 2: What "Craft" Means at Atlassian

**Q:** What does Atlassian mean by "craft" in engineering? Name 3 concrete behaviors.

**A:**
1. **Voluntarily testing** — adding tests that weren't asked for because you saw they were needed
2. **Reading before writing** — spending 5+ minutes understanding code intent before touching anything
3. **Raising out-of-scope issues** — noticing a data integrity bug you weren't asked to fix, and surfacing it instead of ignoring it

Craft is not about flawless syntax. It's about judgment, care, and professional discipline.

---

## Card 3: The 5 Atlassian Values (Verbatim)

**Q:** Recite all 5 Atlassian values exactly as written.

**A:**
1. "Open company, no bullshit"
2. "Build with heart and balance"
3. "Don't #@!% the customer"
4. "Play, as a team"
5. "Be the change you seek."

Note: The Values interview is a standalone scored gate. A "No" here cannot be overridden by technical performance.

---

## Card 4: "No Brilliant Jerks" Policy

**Q:** What is Atlassian's "no brilliant jerks" stance, and how does it show up in hiring?

**A:** Atlassian explicitly rejects candidates who are technically exceptional but who undermine team trust, hoard credit, dismiss colleagues, or behave with arrogance. The Values interview is a named checkpoint in the hiring loop designed to catch this. Stories that reveal passive-aggressive behavior, credit-stealing, or contempt for teammates will fail the gate even if the code was excellent. The 5 values are operationalized into rubrics that trained interviewers score against.

---

## Card 5: Karat Screening Format

**Q:** What is the Karat screen at Atlassian and what format does it take?

**A:** Karat is a third-party interview panel (real human interviewers, not automated). The Atlassian Karat screen typically runs 45–60 minutes and covers:
- Live coding in a shared editor
- Reading and debugging an existing codebase (not greenfield)
- Voluntarily writing tests
- Explaining your reasoning aloud

It is NOT a LeetCode grind — you will rarely see a classic algorithm problem. Expect to read messy code, identify issues, and communicate your thinking.

---

## Card 6: Integer Division Pitfall in Python 3

**Q:** What does `1 / 16 * 100` return in Python 3? What should it be for a percentage?

**A:** In Python 3, `/` is always true division (returns float). So `1 / 16 * 100` returns `6.25` — which is correct. BUT: `1 / 16 * 100` evaluated left-to-right computes `0.0625 * 100 = 6.25`.

The bug in this lab is **operator order with integer counts**: if you did `count / total * 100` and `count` is `int` and `total` is `int`, Python 3 gives the right answer. The real danger is in C/C++/Java where `1 / 16 = 0` (integer truncation). The fix there: `(count * 100) / total` — multiply first to preserve precision.

**Interview version:** `"In C: count / total * 100 truncates to 0 when count < total. Always multiply before dividing when computing percentages in integer arithmetic."`

---

## Card 7: task_id Collision Danger — Use UUID Instead

**Q:** What is wrong with `task_id = len(self.tasks) + 1` and what's the correct approach?

**A:** If task with id=3 is deleted and a new task is created, `len(tasks) + 1` gives id=3 again — a collision. The new task will silently overwrite or confuse references to the old deleted one. The correct approach: use `uuid.uuid4()` (universally unique identifier) or a monotonically incrementing counter that is NEVER decremented, even on deletion. In production systems: auto-increment primary keys in a database handle this. Never derive IDs from mutable collection sizes.

---

## Card 8: "Open Company, No Bullshit" in Code Review Context

**Q:** How does "Open company, no bullshit" apply during a code review?

**A:** It means: say what you actually think. If you see a data integrity bug, name it clearly — don't soften it so much that the reviewer misses the severity. If your own code has a flaw, disclose it before being asked. Don't let social friction stop you from flagging a real problem. In an interview: proactively naming bugs you found, including ones out of scope, is a direct demonstration of this value. "I noticed bug 6 is out of scope, but I wanted to flag it because it could cause data loss" is the right behavior.

---

## Card 9: When to Raise Issues Out of Scope — "Be the Change You Seek"

**Q:** During an interview, you find a bug that's out of scope for the task you were given. What do you do?

**A:** Mention it explicitly, but don't derail the session. The correct pattern:
1. Finish the in-scope work first
2. Then say: "I also noticed [bug X] on line Y — it's outside what you asked for, but I wanted to flag it because [reason]. Would you like me to fix it or should I leave it?"

This demonstrates "Be the change you seek" (notice problems, act on them) and "Open company, no bullshit" (say what you see). Staying silent about a data integrity bug you noticed is the wrong choice — it signals low craft and low transparency.

---

## Card 10: "Don't #@!% the Customer" and Data Integrity

**Q:** What does "Don't #@!% the customer" mean in the context of a bug where done tasks still appear in active sprint views?

**A:** Jira is a tool that teams use to track real work. If done tasks appear as active, sprint managers make wrong decisions: they might think the sprint is behind schedule when it isn't, assign duplicate work, or ship incorrect completion-rate metrics to stakeholders. The customer (the team using Jira) is actively harmed by this data error. "Don't #@!% the customer" means: data correctness is non-negotiable. Shipping code that returns wrong query results — even partially — is a values violation, not just a quality issue.
