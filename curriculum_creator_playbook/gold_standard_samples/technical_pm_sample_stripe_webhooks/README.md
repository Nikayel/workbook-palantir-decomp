# Design an Idempotent Events + Webhooks API for Partners

**Company / role / track:** Stripe · Technical PM
**Simulates:** Stripe's technical-PM bar — an **API-design discussion** plus the **written-memo take-home** Stripe is famous for.
**Tier:** 1 (worked) · **Difficulty:** medium

Target time: 75 minutes · Minimum: 45 · Deep version: 110

> **Why this is the Technical-PM gold-standard sample.** Stripe has the **highest developer/API bar** of the ten companies, and **writing is its #1 hiring signal**. This lab makes the learner design a real developer-facing API — webhooks, **idempotency keys**, cursor pagination, **signature verification**, and **backward-compatible versioning** — and then **write it up as a Stripe-style memo** connecting each decision to second-order developer impact (trust, integration effort), not topline revenue. Crucially, the deliverable is a **spec + memo, never production code** — that's the line between Technical PM and SWE.

## What you'll practice
API resource modeling, push-vs-poll (webhooks), idempotency for safe retries, at-least-once delivery + retries/backoff + dead-letter, cursor pagination, versioning that won't break integrations "for the next 10 years," and **crisp technical writing**.

## Time plan
Part 0–1 forethought + clarifying (10) · Part 2 decomposition (10) · **Part 3 API contract design (25)** · **Part 4 produce the spec + memo (20)** · Part 5 reasoning (10) · Part 6 simulation (10) · Part 7 self-grade (5).

## How to use
1. Open `workbook.md`; fill every `[blank]`. Don't open the solution.
2. Produce the two artifacts in `artifacts/api_design_scaffold.md` (the spec) and the in-workbook memo.
3. Practice the Part 6 curveballs out loud (as if explaining to a partner engineer).
4. Only then read `solution_reasoning.md`.
5. Self-grade on the **Technical-PM rubric** (note: a "Writing clarity & rigor" row is added — Stripe weights it). Review `flashcards.md` today, then day 3/7/14.

> **Authoring note for the curriculum creator:** to re-skin this for **Microsoft** (API for 3rd-party payments), **Uber** (events for a marketplace), or **Amazon PMT** (an architecture explainer), keep Part 3 and swap the product surface + the "what's scored" emphasis from the company pack. Drop the memo for Amazon (use an LP-framed explainer instead).
