# Event Ledger — Build & Evolve a Small System (codebase style)

**Company / role / track:** Generic (codebase-style template) · SWE
**Simulates:** the **practical / real-codebase** round used by Stripe (integration), Atlassian (craft), Palantir (practical), and the **CodeSignal Industry-Coding-Framework** OA.
**Tier:** 1 (worked) · **Difficulty:** medium

Target time: 70 minutes · Minimum: 45 · Deep version: 100

> **Why this lab is the SWE gold-standard sample.** It demonstrates the format the user specifically asked about — *codebase style*. Unlike a one-shot LeetCode puzzle, you build a small system in **4 progressive levels** where each level **extends the same code** and must **not break the earlier levels**. That "evolve existing code + preserve backward compatibility" skill is exactly what Stripe/Atlassian/CodeSignal test and what most interns never practice.

## What you'll practice
Designing a minimal data model, handling edge cases, **refactoring loose functions into an encapsulated class**, and **extending a working system (idempotency, reversals) without regressions**.

## The 4 levels (this is Part 4 of the workbook)
- **L1 — Initial design & basic functions** (~15 min): record events + query by account.
- **L2 — Core logic & edge cases** (~15 min): derive balances; handle unknown accounts + malformed input.
- **L3 — Refactor & encapsulate** (~15 min): move the loose state into a `Ledger` class with the same behaviour. *Separates engineers who can evolve code from those who only write fresh code.*
- **L4 — Extend** (~20 min): add idempotency keys and event reversal **without breaking L1–L3**.

## Time plan
Part 0–1 forethought + clarifying (8) · Part 2 decomposition (10) · Part 3 contract (10) · **Part 4 build the 4 levels (45)** · Part 5 reasoning (10) · Part 6 simulation (10) · Part 7 self-grade (7).

## How to use
1. Open `workbook.md`; fill every `[blank]`. Don't open the solution.
2. Implement the levels **in order** in `starter.py`. Run `python3 -m unittest tests.py` after each level. *(This sample ships green against `reference_solution.py`; in a real lab you'd point the import at `starter`.)*
3. Practice the Part 6 talk-track and curveballs out loud.
4. Only then read `solution_reasoning.md` and `reference_solution.py`.
5. Self-grade (Part 7), noting the codebase add-on rows (works-against-tests, diagnosis). Review `flashcards.md` today, then day 3/7/14.
