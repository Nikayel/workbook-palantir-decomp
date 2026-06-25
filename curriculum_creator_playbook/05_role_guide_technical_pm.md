# 05 · Role Guide — Technical PM Intern

> **Audience:** the curriculum creator.
> **Purpose:** how to author the Technical-PM track. This role sits between PM and SWE: a PM who owns technical/platform/API/infra/ML products and is expected to "get in the weeds with engineers" — but **does not write production code** in interviews. Pair with the company pack and `03`.

---

## 0. Disambiguate three roles before you author (this matters)

Interns constantly conflate three roles that share the "TPM" letters. Put this table in the README of every Technical-PM lab so learners prep the right thing:

| Role | Core question | Measured on | Titles |
|---|---|---|---|
| **(a) Classic PM** | *What* to build & why | product/business impact | PM, APM (Google), RPM (Meta) |
| **(b) Technical PM / PMT** ← *our focus* | *What technical product* to build & why, with deep technical fluency | product impact for technical/developer users | "PM, Technical"; Amazon **PMT** |
| **(c) Technical *Program* Manager (TPgM)** | *How / who / when* to deliver across teams | execution / delivery | TPM, TPgM; Apple **EPM** |

Industry mental model: **PM-T builds the *right* product; TPgM builds the product *right*.** Our Technical-PM track targets **(b)**, but interns meet **(c)** constantly (Amazon TPM, Apple EPM, Nvidia/Uber TPgM), so include one TPgM-flavored execution lab (dependencies, risk, RACI) per relevant company.

**Term-to-company map:** Amazon explicitly splits **PMT** (product) from **TPM** (program). Google screens technical aptitude inside the APM/PM loop — **no separate Technical-PM intern title** (route through APM/SWE). Microsoft "Program Manager"→"Product Manager," informally "Technical PM" on Azure/platform teams. Apple uses **EPM** for the program flavor. Stripe/Nvidia just say "PM" but with a very high technical bar.

---

## 1. How the Technical-PM loop differs from PM

It keeps the PM rounds (`04`) and **adds/deepens technical rounds**:

1. **System design (lite)** — *why & what* to build + tradeoffs (cost/latency/reliability), scoping, estimation. Not "build it" like an engineer.
2. **API design** — the interface (resources, endpoints, request/response, errors, versioning) — **not** backend internals. Heaviest at Stripe.
3. **Data modeling / SQL** — schemas/entities/relationships; reason with metrics.
4. **Technical tradeoffs / explainer** — build-vs-buy, batch-vs-streaming, SQL-vs-NoSQL, sync-vs-async; "explain <concept> to a non-engineer."
5. **Working-with-engineering scenarios** — scoping, architecture disagreement, prioritizing tech debt, managing a launch.
6. **Light coding / pseudocode (rare).** Mostly **not** programming. Amazon is explicit: a PMT technical question "is likely not a programming question… a technical explainer or architecture question."

---

## 2. Technical topics to drill — in priority order

Author labs roughly in this order; the first three are the backbone.

1. **API design** — REST verbs/status codes, resource modeling, **idempotency** (idempotency keys + TTL for safe retries), **pagination** (offset vs cursor), **auth** (API keys/OAuth/tokens), **rate limiting** (token bucket, 429s), **webhooks** (push vs poll, signature verification), versioning/backward-compatibility.
2. **System-design-lite** — latency vs throughput, **caching** (+ invalidation), **queues** (async decoupling), **consistency** (strong vs eventual), load balancing, horizontal vs vertical **scaling**, the canonical "what happens when a user clicks…" flow (client → DNS → LB → service → DB/cache → response).
3. **SQL + metrics selection** — joins/aggregation/GROUP BY; pick the right metric; p50/p95/p99, error rate, uptime, SLA vs SLO, QPS.
4. **Data modeling + batch-vs-streaming** — schemas/entities, normalization, pipelines/ETL, OLTP vs OLAP.
5. **Technical explainer** — "explain idempotency / the cloud / recursion-vs-iteration to a non-engineer."
6. **ML/AI product literacy** — precision/recall, offline eval vs online metrics, data labeling, model lifecycle (data→train→eval→deploy→monitor→retrain), drift, human-in-the-loop. (Rising fast in 2024–2026.)
7. **Build-vs-buy / architecture tradeoffs.**
8. **Working-with-engineering scenarios.**

---

## 3. Question archetypes (lab seeds) by technical area

- **API design:** "Design the API for a URL shortener / payments integration / file-upload." "Make a payment-creation endpoint safe to retry." "Paginate an endpoint returning millions of orders." "Version this API without breaking integrations." "Design a webhook system so partners avoid polling." "Rate-limit a public API and communicate the limits."
- **System-design-lite:** "Walk me through what happens when a user clicks Buy Now." "Design a notification service for 10M daily events." "Where would you add caching, and what breaks when it's stale?" "Diagnose a p99 latency regression (200ms→2s) after a launch." "Strong vs eventual consistency for a likes-counter vs a bank balance?"
- **Data / SQL:** "Design the data model for ride-sharing (riders/drivers/trips/payments)." "Batch vs streaming for fraud detection — which and why?" "Compute weekly active drivers from a trips table." "What tables/metrics measure marketplace supply vs demand?"
- **Explainer / tradeoffs:** "Explain idempotency to a non-engineer." "Build vs buy: third-party payments or in-house?" "SQL vs NoSQL for this product?"
- **ML/AI product:** "Measure the quality of an ML feature (search ranking / autocomplete)." "Offline metrics improved but engagement dropped — what happened?" "Design a data-labeling pipeline for a new classifier." "Eval + rollout plan for a new LLM feature."
- **Eng / estimation:** "An engineer says 3 months, you think 3 weeks — what do you do?" "Prioritize tech debt vs features." "Estimate AWS's annual revenue."

---

## 4. How Technical-PM rounds are scored (rubric rows)

Score **technical fluency, not production engineering**:

| Dimension | Strong | Weak |
|---|---|---|
| **Technical fluency** | speaks the concepts correctly, right altitude | hand-waves, fakes depth |
| **Architecture tradeoffs** | reasons about cost/latency/reliability | one option, no tradeoffs |
| **Build-vs-buy** | defensible recommendation | no decision |
| **Scale/reliability** | knows what breaks at 10×, finds bottlenecks | ignores scale |
| **Communicates with engineers** | credible peer | vague, can't engage |
| **Translates to non-technical** | clean analogy, right audience | jargon dump |
| **Handling ambiguity** | scopes + states assumptions | freezes |

Red flags to dramatize in the "weak" answer key: hand-waving; no tradeoffs; faking depth; or going so deep they lose the product/user. **No production code is required.**

---

## 5. The lab-build format for Technical PM

Use the `03` Technical-PM adaptation: **Part 4 produces a technical artifact, not an algorithm** — an `openapi.yaml`, a data model, a SQL file, or a written technical-tradeoff memo. The CodeSignal Industry-Coding-Framework's "design → core logic → refactor → extend" progression (see `06`) is a great spine for an **API-design lab** even though the learner writes a spec, not production code.

**What to build per company (counts in `07`):** typically 1 API-design lab, 1 system-design-lite lab, 1 data/SQL lab, 1 technical-explainer lab, plus the **company-signature** technical lab:
- **Stripe** → API design with **idempotency keys + double-entry ledger invariants (debits = credits) + 10-year backward-compatible versioning**, written up as a Stripe-style memo. (Highest technical bar of the ten — make this the flagship Technical-PM lab.)
- **Nvidia** → a **hardware-software constraint** tradeoff (GPU memory bandwidth, training-vs-inference economics) + "explain deep learning to a non-technical audience."
- **Amazon** → a **technical explainer + architecture** lab framed as a PMT phone screen (½ LPs, ½ "how does the internet/API work"), no coding.
- **Google** → system-design-lite weighted on **estimation/scoping**.
- **Uber / Atlassian** → SQL + marketplace/experimentation metrics; Uber adds a ~60-min distributed system-design + take-home case.
- **Meta** → data-driven execution; metric trees; light API.
- **Microsoft** → API design + concept explainer (Azure skin).
- **Apple** → EPM-flavored: scope/dependency/risk + a technical presentation; probe system architecture on the learner's own project.
- **Palantir** → there's no classic Technical PM; the **decomposition round** *is* the technical-product test (ontology/data-pipeline). Route to the Palantir pack + SWE guide.
