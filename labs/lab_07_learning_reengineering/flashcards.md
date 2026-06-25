# Flashcards — Learning Reengineering: Code Review and Bug Fix

> Review **day 1 → 3 → 7 → 14**. Reset to day 1 on a miss.
> Cover each answer before reading. Free-recall — no peeking.

---

**Q:** What is the recommended first step when you inherit unfamiliar code, and why should you NOT run it immediately?
**A:** Read the code and write down in plain English what it is *trying* to do — before running it. Running it first biases you toward "it works" or "it errors" rather than understanding intent. You may miss logic bugs that don't throw exceptions. Reading first trains the skill of code comprehension under interview conditions where you often cannot run code at all.

---

**Q:** What is a mutation bug in Python, and give a concrete example involving a list parameter?
**A:** A mutation bug occurs when a function modifies a mutable argument (list, dict) that was passed in, changing the caller's data as a side effect. Example: `def assign(tickets, agents): tickets.sort(...)` — the caller's `tickets` list is now sorted in place, which the caller did not expect. Fix: work on a copy (`sorted_tickets = sorted(tickets, ...)`) so the original is untouched.

---

**Q:** What is the correct order of operations when fixing bugs in unfamiliar code, and why?
**A:** (1) Read and understand intent. (2) Write tests that FAIL because of each bug. (3) Fix the bugs. (4) Confirm tests now pass. Never fix first and test after — if you fix without a failing test first, you don't know if your test actually exercises the bug or if your fix addresses the real cause.

---

**Q:** What is defensive programming, and name three techniques for it in Python?
**A:** Defensive programming means writing code that handles unexpected inputs gracefully rather than assuming happy-path inputs. Techniques: (1) validate inputs at function entry (`if not tickets: return []`), (2) use `.get()` with a default on dict access instead of `dict[key]` which raises KeyError, (3) guard against None explicitly (`if agent is None: raise ValueError("agent cannot be None")`).

---

**Q:** What does "extend without breaking" mean in practice, and what is the key technique for achieving it?
**A:** It means adding new behavior (a new feature, parameter, or code path) without causing previously passing tests to fail. Key technique: make the new behavior opt-in or additive — e.g. add an optional `language` parameter that defaults to `None`, and only apply the new routing logic when it is provided. Existing callers that don't pass `language` continue to work unchanged.

---

**Q:** Name five common code smells and describe what each signals.
**A:** (1) Long function — does too many things; should be split. (2) Magic number — `if priority > 3` with no explanation; should be a named constant. (3) Mutable default argument — `def f(lst=[])` is a Python trap; the default is shared across calls. (4) Deep nesting — more than 3 levels of if/for; extract inner logic into a function. (5) Commented-out code — indicates uncertainty; delete it or document why it was kept.

---

**Q:** What is a side effect in a function, and why do side effects make code harder to test?
**A:** A side effect is any change a function makes outside its return value — writing to a file, modifying a global variable, mutating a passed-in list, making a network call. Side effects make testing hard because: (1) you must set up and tear down external state, (2) tests can interfere with each other if they share mutable state, (3) you cannot test the function in isolation without mocking the external dependency.

---

**Q:** What is a pure function, and why are pure functions easier to test?
**A:** A pure function always returns the same output for the same input and has no side effects. It is easier to test because: (1) no setup or teardown needed, (2) tests are independent of each other, (3) you can test by simply asserting `f(input) == expected_output` with no mocking. Aim to push side effects to the edges of your system and keep core logic pure.

---

**Q:** What does "self-documenting code" mean, and what are two techniques for achieving it?
**A:** Self-documenting code communicates its intent through naming and structure, reducing the need for comments to explain "what." Techniques: (1) use descriptive names — `available_agents` instead of `lst2`, `assign_by_priority` instead of `process`; (2) extract complex conditions into named booleans — `agent_is_available = not agent.on_vacation and agent.capacity > 0` — so the `if` statement reads like English.

---

**Q:** What does "make it work, make it right, make it fast" mean, and in what order should you apply these phases?
**A:** (1) Make it work: get the correct output for the happy path — don't optimize prematurely. (2) Make it right: handle edge cases, remove side effects, make it readable and testable, eliminate duplication. (3) Make it fast: only after correctness is established, profile and optimize the specific bottleneck — do not guess at performance. Skipping phase 2 before phase 3 leads to fast, wrong, unmaintainable code.
