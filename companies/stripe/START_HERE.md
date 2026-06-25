# Stripe — Interview Prep START HERE

---

## Snapshot

| Program | Who | Notes |
|---|---|---|
| SWE Intern | Juniors + seniors | ~1-2% acceptance rate. Described internally as a "hiring audition" — interns ship real features to production. No toy projects. |
| PM Intern | Juniors + seniors | Writing-first product sense. Memo format, not slide decks. |
| TPM Intern | Juniors + seniors | Highest API design bar of any company in this curriculum. |

Stripe hires fewer people than any other company in this workbook. The bar is exceptionally high and the signal is precision: can you build something that actually works, with professional craft, quickly?

---

## Culture

Stripe's culture operates on five principles. Know these — they surface in every interview signal:

**Writing-first.**
Stripe runs on written memos and RFCs, not slides. Code reviews are thorough prose documents. Design docs are expected before any significant system. In interviews, this means: your explanation of your thinking matters as much as your answer. Sloppy communication = weak signal.

**Move with urgency.**
Stripe values speed of execution. Not recklessness — urgency. In a 45-minute integration round, you're expected to ship a working feature, not just describe it. Interviewers notice if you spend 20 minutes planning and 5 minutes coding.

**Think rigorously.**
Financial infrastructure demands correctness. Stripe's systems handle billions of dollars. Every assumption must be stated. Every edge case must be named. "It should probably work" is not a Stripe-level answer.

**Users first.**
In PM interviews: the "user" is a developer building on Stripe's API. Developer experience is a product decision, not an afterthought.

**Create with craft.**
Code quality is a signal. Clear naming, clean error handling, no hacks. The integration round rewards production-quality code explicitly.

---

## What's Distinctive About Stripe Interviews

**WRITING is the #1 signal.**
More than any other company in this curriculum, Stripe evaluates written communication. Your code will be read like a document. Your explanations will be judged on clarity and rigor. Practice writing before the interview — not just coding.

**Practical engineering, not algorithm trivia.**
Stripe's SWE interview is not LeetCode. You're not asked to invert a binary tree. You're asked to integrate against an API, fix a bug in an unfamiliar codebase, or implement a feature end-to-end. The skills being tested are: reading code fast, understanding contracts, writing clean integration code.

**Full internet access in the integration round — but NO AI assistants.**
You can use Stripe's actual API docs, Stack Overflow, MDN, etc. You cannot use ChatGPT, Claude, Copilot, or any AI assistant. This is explicitly stated and enforced. The round tests YOUR ability to read documentation and integrate quickly — not your ability to prompt an AI.

**Bug-squash rewards clear diagnosis even without a complete fix.**
In the bug-squash round, you're given a failing test in an open-source library. A clear explanation of why the bug exists and what the fix approach is scores nearly as high as a complete fix. Stripe values rigorous thinking about root cause.

---

## Assessment Format

**SWE:**
1. Integration round (45-60 min): Drop into an unfamiliar codebase, integrate against a provided API/SDK, ship a feature that makes tests pass. Internet OK. AI: NO.
2. Bug-squash round (45 min): Given a failing test in a library. Find the bug. Fix it. Explain root cause clearly.
3. 3-part progressive OA: Three increasingly complex implementation problems. Each builds on the previous.

**PM:**
1. Written product memo (design a Stripe product improvement in memo format, not slides)
2. Developer product sense case (evaluate API design decisions from a developer's perspective)

**TPM:**
1. API design screen (design an API end-to-end: resource model, endpoints, idempotency, versioning)
2. System design (webhook delivery, pagination, financial invariants)

---

## Lab Menu

### SWE Track

| Lab | Tier | Focus |
|---|---|---|
| Lab 01: Integration Lab | Tier 1→2 | Read unfamiliar codebase, integrate against mock API, ship `process_refund` |
| Lab 02: Bug-Squash | Tier 2 | Find and fix a bug in provided code, explain root cause clearly |
| Lab 03: 3-Part Progressive OA | Tier 2 | Three-part implementation problem with escalating complexity |

### PM Track

| Lab | Tier | Focus |
|---|---|---|
| Lab 01: Written Product Memo | Tier 1 | Design a Stripe product improvement in memo format |
| Lab 02: Developer Product Sense | Tier 2 | Evaluate API design choices from a developer's perspective |

### TPM Track

| Lab | Tier | Focus |
|---|---|---|
| Lab 01: Idempotent Payments API + Versioning (FLAGSHIP) | Tier 1→2 | Full API design: Payment Links, idempotency, webhooks, 10-year versioning |
| Lab 02: Webhook + Pagination Design | Tier 2 | Webhook delivery guarantees, cursor pagination, retry logic |

---

## Before You Start

**The one habit to build before any Stripe lab:**

Read Stripe's actual API documentation at stripe.com/docs. Spend 30 minutes clicking through:
- How a charge is created
- How a refund is created
- What an idempotency key looks like in the real API
- What a webhook event looks like
- How Stripe versions its API (the `Stripe-Version` header, date-based versioning)

You cannot pass the Stripe integration round without understanding what "production-quality API integration" looks like. The docs are the single best preparation resource.

**Practice writing before you start the labs:**
After each lab section, before checking the answer, write a 2-3 sentence explanation of your reasoning. Stripe evaluates communication throughout — not just at the end.

**No AI in the integration round — but learn WITH AI now:**
During practice, use Claude or ChatGPT freely to understand concepts. When you do a timed integration simulation (Lab 01 Part 4), close all AI tabs and simulate the actual constraint. The integration round tests you, not your tools.
