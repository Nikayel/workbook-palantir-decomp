# Artifact — Metric tree + product brief (fill this in)

## 1. Metric tree
Connect the North Star down to the levers your feature moves. (Worked top; fill the rest.)

```
North Star: meaningful notification-driven sessions / weekly active user
        │
        ├── value per notification ──┬── relevance (predicted) ......... [blank lever]
        │                            └── bundling ratio ................ [blank lever]
        ├── volume control ──────────┬── low-value sends / user / day .. [blank lever]
        │                            └── frequency cap hit-rate ........ [blank lever]
        └── trust / opt-in ──────────┬── opt-out rate (GUARDRAIL ↓) .... [blank]
                                     └── re-enable rate ................ [blank]
```

## 2. Product brief (≤200 words)
**Problem.** [blank — heavy users drown in low-value notifications and opt out; opt-out is near-irreversible]
**Who / job.** [blank]
**What we'll build (MVP).** [blank — relevance ranking + bundling of low-value types; safety notifications bypass]
**What we won't build yet.** [blank — granular per-type UI; heavy ML]
**Why now.** [blank — opt-outs are a long-term retention leak]
**Success.** North Star = [blank]; Guardrail = opt-out rate must not rise; Counter-metric = [blank].
**Top risk.** [blank — relevance model is wrong → hides important items; mitigate with the bypass list + guardrail]

## 3. Experiment one-liner
[blank — "Ship if North Star ↑ with opt-out rate flat-or-down over a 2-week run."]
