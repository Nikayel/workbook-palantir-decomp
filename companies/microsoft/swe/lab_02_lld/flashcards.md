# Flashcards — Microsoft SWE Lab 02: LLD / OOD A/B Test

---

**Card 01 — OOD Pillars**

Q: Name the four pillars of OOP and give a one-sentence example of each in the A/B test context.

A:
- **Encapsulation**: `ABTest` hides its hashing logic; callers only call `assign_variant()` and never touch the hash directly.
- **Inheritance**: `ABTest` and `MultiVariantTest` both extend `Experiment`, sharing the `name` attribute and the contract.
- **Polymorphism**: `ExperimentManager.get_variant()` calls `experiment.assign_variant(user_id)` without knowing whether the experiment is AB or MultiVariant.
- **Abstraction**: `Experiment` defines the interface (`assign_variant`) without specifying the implementation.

---

**Card 02 — Deterministic Hashing for A/B**

Q: Why do you hash `user_id + experiment_name` instead of just `user_id`?

A: If you only hash `user_id`, two experiments with the same 50% split would assign the SAME set of users to variant A. User 1234 would always be in the "A bucket" for every experiment. By appending the experiment name to the key before hashing, you break this correlation — different experiments get different (but still deterministic) assignments for the same user.

---

**Card 03 — Hash-to-Integer Pattern**

Q: How do you deterministically map a user_id (string) to an integer in [0, 100)?

A:
```python
import hashlib

def _user_bucket(user_id: str, experiment_name: str) -> int:
    key = (user_id + experiment_name).encode('utf-8')
    digest = hashlib.md5(key).hexdigest()   # 32-char hex string
    return int(digest, 16) % 100            # integer in [0, 100)
```
MD5 is fast and not needed for security here. SHA-256 is also fine. The `% 100` maps to a bucket that maps to a percentage threshold.

---

**Card 04 — Abstract Base Class vs Interface (Python)**

Q: In Python, what is the difference between an ABC with `@abstractmethod` and just raising `NotImplementedError`?

A:
- **`@abstractmethod` (ABC)**: Python enforces the contract at class instantiation time. You CANNOT instantiate a subclass that doesn't implement all abstract methods — you get a `TypeError` immediately, not at call time.
- **`raise NotImplementedError`**: No enforcement at instantiation. The bug surfaces only when the method is called at runtime, which might be deep in a production flow.

Use ABC when you want the contract enforced early. Use `raise NotImplementedError` when you want a soft "please override this" reminder.

---

**Card 05 — Extensibility via Inheritance**

Q: What design property lets `ExperimentManager` stay unchanged when you add `MultiVariantTest`?

A: `ExperimentManager` is coded against the `Experiment` base class interface, not against `ABTest` directly. Since `MultiVariantTest` extends `Experiment` and implements `assign_variant()`, `ExperimentManager.get_variant()` calls it polymorphically with zero changes. This is the **Open/Closed Principle**: open for extension, closed for modification.

---

**Card 06 — Thread Safety in Python**

Q: Does Python's GIL protect a dict from concurrent writes? When do you need explicit locking?

A: The GIL ensures that only one thread runs Python bytecode at a time, but a single dict operation can still be interrupted between bytecodes. Simple reads are generally safe, but a `register()` call that checks "does this key exist" + "add the key" is a two-step operation that can have a race condition. For true thread safety (e.g., in a multithreaded Flask server), use `threading.Lock()`:

```python
import threading

class ExperimentManager:
    def __init__(self):
        self.experiments = {}
        self._lock = threading.Lock()
    
    def register(self, experiment):
        with self._lock:
            if experiment.name in self.experiments:
                raise ValueError(f"Experiment {experiment.name} already registered")
            self.experiments[experiment.name] = experiment
```

---

**Card 07 — Microsoft LLD Interview Style**

Q: What does the Microsoft LLD interviewer care about most?

A: Three things, in order:
1. **Extensibility rationale**: "Why did you choose inheritance here? What would break if you added a new type without it?"
2. **OOP vocabulary**: Can you say "polymorphism," "abstract base class," "Open/Closed Principle" naturally?
3. **C#/.NET mental model**: Microsoft engineers think in C# interfaces and virtual methods. Knowing Python's ABC is sufficient, but demonstrating you understand the C# `interface` concept earns extra credit.

---

**Card 08 — When to Use Composition vs Inheritance**

Q: In this A/B test problem, why did we use inheritance (not composition) for `ABTest` and `MultiVariantTest`?

A: **Use inheritance when** the subclass IS-A version of the base class and shares the same interface. `ABTest` IS-A `Experiment`. `MultiVariantTest` IS-A `Experiment`. They both answer the same question: "what variant does this user get?"

**Use composition when** the relationship is HAS-A. For example, `ExperimentManager` HAS-A collection of `Experiment` objects. It doesn't extend `Experiment` — it owns and delegates to them.

Rule of thumb: if the "is-a" relationship holds and the interface is stable → inheritance. If you'd need to subclass just to change one behavior → prefer composition.

---

**Card 09 — C#/.NET vs Python OOD Idioms**

Q: If a Microsoft interviewer asks you to implement this in C#, what changes?

A:
- Python `ABC` + `@abstractmethod` → C# `interface` or `abstract class`
- Python `dict[str, Experiment]` → C# `Dictionary<string, IExperiment>`
- Python `@property` → C# `{ get; private set; }`
- C# enforces types at compile time; Python enforces ABC at instantiation

The OOD structure is the same. Microsoft interviewers who work in C#/.NET may use C# vocabulary ("interface," "sealed class," "virtual method") even if you code in Python. Know the mapping.

---

**Card 10 — "Make It Extensible" Signal in OOD Problems**

Q: When an OOD interviewer says "make it extensible," what is the design signal?

A: They want to see you reach for the **Open/Closed Principle** (OCP). This means:
1. Define an abstraction (abstract class or interface)
2. Write the orchestrator (ExperimentManager) against the abstraction, not the concrete class
3. Add new types by subclassing, not by modifying the orchestrator

A common failure mode: hardcoding `if type == "AB": ... elif type == "multivariant": ...` inside ExperimentManager. That violates OCP and breaks on every new experiment type.

Second signal: ask about "what new types might we add?" before designing. It shapes your abstraction.
