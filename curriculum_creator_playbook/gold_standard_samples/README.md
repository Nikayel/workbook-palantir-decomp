# Gold-Standard Samples

Three **fully-worked example labs** — one per role — built to the `03` authoring standard. These are your **clone-me references**: copy the closest one into a new `labs/<NN>_<company>_<slug>/`, then re-skin to another company using its pack. "Show, don't just tell."

| Sample | Role | Demonstrates | Runnable? |
|---|---|---|---|
| [`pm_sample_meta_notifications/`](./pm_sample_meta_notifications/) | **PM** | product sense + **data-driven execution**; North Star **+ guardrail**; explicit RICE cut; A/B design; artifact = brief + metric tree (no code) | n/a (artifact-based) |
| [`technical_pm_sample_stripe_webhooks/`](./technical_pm_sample_stripe_webhooks/) | **Technical PM** | the highest API bar — **idempotency, webhooks vs polling, cursor pagination, signatures, additive versioning** — written up as a **Stripe-style memo + spec** (no code) | n/a (spec + memo) |
| [`swe_sample_codebase_event_ledger/`](./swe_sample_codebase_event_ledger/) | **SWE** | the **codebase / practical style** (CodeSignal Industry-Coding-Framework): build & **evolve** a system across 4 levels without breaking earlier ones | ✅ `python3 -m unittest tests.py` (8 tests green) |

## What each sample proves
- **The 8-part spine** (forethought → clarifying → decomposition → contract → build → reasoning → simulation → self-grade) flexes across all three roles.
- **The fade works:** each is Tier 1 (a worked example shown, learner finishes the rest).
- **The feedback engine is real:** every `solution_reasoning.md` has the model answers, the **strong-vs-weak with the weak annotated**, curveball responses, and rubric exemplars.
- **Role adaptation (`03` §9):** PM/TPM produce **artifacts (brief/memo/spec)**; SWE produces **runnable code**.
- **Authenticity:** Meta's "build for billions" + guardrails; Stripe's API rigor + writing culture; the codebase refactor-without-breaking skill.

## Using a sample to author a new lab
1. Pick the sample matching your **role**.
2. Open the target **company pack** for the new realism (product surface, values, OA format).
3. Copy the folder, swap the scenario + Part-3 specifics + rubric emphasis, keep the spine.
4. Run the `08` checklists. For SWE, keep the tests green against your reference.
