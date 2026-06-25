# Rubric Bank — ready-to-paste countable rubric rows

> Paste the role's block into Part 7. Each row scores 1–5; descriptors must be **behavioral and countable** (03 §6). Ship one exemplar per level in `solution_reasoning.md` §7.

---

## PM rubric rows
```
Structure ( /5)
  5 — visible roadmap, MECE buckets, signposted
  3 — some structure, occasional rambling
  1 — rambling list, no signposting
User empathy ( /5)
  5 — names a segment + ≥2 real pains before solutioning
  3 — vague user, 1 pain
  1 — designs from personal preference
Prioritization ( /5)
  5 — explicit cut with rationale (e.g. RICE/CIRCLES); sacrifices ≥1 feature
  3 — implies priorities, no rationale
  1 — treats all ideas as equal
Metrics literacy ( /5)
  5 — NSM + ≥1 guardrail, defines success, discusses tradeoffs
  3 — names a metric, can't fully define success
  1 — vanity metrics / none
Communication ( /5)
  5 — concise, adapts to interviewer, structure invisible
  3 — understandable but verbose
  1 — jargon / framework-name-dropping
Creativity ( /5)
  5 — ≥1 non-obvious, differentiated idea
  3 — mostly conventional
  1 — generic me-too features
Handling ambiguity ( /5)
  5 — clarifies, states assumptions, moves
  1 — freezes or over-asks before starting
```

## Technical PM rubric rows
```
Technical fluency ( /5)
  5 — correct concepts at the right altitude, no faking
  1 — hand-waves / fakes depth
Architecture tradeoffs ( /5)
  5 — reasons about cost/latency/reliability with a clear choice
  1 — one option, no tradeoffs
Build-vs-buy ( /5)
  5 — defensible recommendation with rationale
  1 — no decision
Scale / reliability ( /5)
  5 — names what breaks at 10×, finds the bottleneck
  1 — ignores scale
Communicates with engineers ( /5)
  5 — credible peer; precise vocabulary
  1 — vague, can't engage
Translates to non-technical ( /5)
  5 — clean analogy at the right audience level
  1 — jargon dump
Handling ambiguity ( /5)
  5 — scopes + states assumptions
  1 — freezes
```

## SWE rubric rows
```
Communication / think-aloud ( /5)
  5 — clarifies, states assumptions, narrates tradeoffs
  1 — silent solving, unexplained jumps
Problem solving ( /5)
  5 — multiple approaches, states + optimizes Big-O
  1 — brute force, can't reason about complexity
Correctness ( /5)
  5 — clean, correct, idiomatic
  1 — buggy, fights the language
Code quality / readability ( /5)
  5 — good names, modular
  1 — messy, poor naming
Testing & edge cases ( /5)
  5 — tests normal + corner, self-corrects
  1 — declares "done" untested
Debugging ( /5)
  5 — finds & fixes own bugs calmly
  1 — needs interviewer to find bugs
Time management ( /5)
  5 — finishes the core in the window
  1 — over-invests in one part
```

### Codebase-style add-ons (Stripe/Palantir/Uber/Atlassian)
```
Works against provided tests/API ( /5)
  5 — feature ships / tests pass with clean integration
  1 — does not run
Diagnosis quality (bug-squash) ( /5)   ← can score 5 even without a complete fix
  5 — precise root-cause, well-reasoned, names the mechanism (e.g. race condition)
  1 — guesses, no diagnosis
```
