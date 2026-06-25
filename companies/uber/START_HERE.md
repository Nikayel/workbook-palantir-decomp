# Uber — Interview Prep START HERE

---

## Snapshot

| Program | Who | Notes |
|---|---|---|
| SWE Intern | Juniors + seniors | CodeSignal GCA or HackerRank OA, then 2 technical + 1 behavioral interview |
| UberSTAR | 1st & 2nd year students | Uber's freshmen/sophomore program — resume + 1 interview, lower bar than SWE Intern |
| PM Intern | Juniors + seniors | Resume + PM phone screen + "JAM session" (ideation) + final round with data scientist |
| APM | New grads | 18-month rotational program. Cross-functional exposure. High bar. |
| Data Science Intern | Juniors + grad students | Coding + stats + case; assessed alongside PM in joint sessions |

---

## Culture: The 8 Norms

Uber explicitly codified 8 cultural norms. Know these verbatim — they come up in behavioral questions explicitly:

1. **Build globally, live locally** — think about global scale, but understand local nuance (drivers in Lagos ≠ drivers in London)
2. **Customer obsessed** — the experience of riders, drivers, eaters, and couriers comes first
3. **Celebrate differences** — diverse teams, inclusive culture
4. **Do the right thing** — ethics first, even when it's costly
5. **Act like owners** — care about the business, make decisions as if it's your company
6. **Persevere** — Uber's product is hard (regulation, drivers, two-sided market); keep going when it's hard
7. **Value ideas over hierarchy** — the best idea wins, regardless of seniority
8. **Make big bold bets** — take calculated risks; incrementalism is not Uber's default mode

In behavioral interviews: connect EVERY story to at least one of these 8 norms by name.

---

## What's Distinctive About Uber Interviews

**Multi-sided marketplace thinking is mandatory.**
For every PM and DS question, Uber evaluates whether you think in three buckets simultaneously:
- **Supply**: drivers, restaurants, couriers — the people/businesses providing the service
- **Demand**: riders, eaters, shippers — the customers
- **Uber's bottom line**: take rate, contribution margin, profitability

If you optimize for demand without considering supply, or vice versa, you're thinking in one dimension. Uber's entire business is about balancing all three.

**PM bar is notably quantitative — you may be assessed with a data scientist.**
Uber PM interviews often include a data scientist in the room or as a co-interviewer. This means:
- Metric definitions must be precise (not "we'll look at engagement")
- A/B testing knowledge is expected (experiment design, guardrail metrics, novelty effects)
- Root-cause analysis must be data-driven (not just "maybe it's supply")

**SWE coding leans toward routing/geospatial/pricing problems.**
Uber's actual tech stack involves:
- Graph algorithms (Dijkstra, matching algorithms)
- Geospatial indexing (H3, S2, quadtrees)
- Distributed systems at scale (1M+ requests/minute)
- Real-time pricing (surge algorithms)
- Driver-rider matching (assignment algorithms)

You're more likely to see a Dijkstra question at Uber than a string manipulation question.

---

## Assessment Format

**SWE:**
1. CodeSignal GCA (or HackerRank): 70-minute general coding assessment, 4 problems, standardized score
2. Technical interviews (2 rounds): algorithm + data structures, often Uber-flavored (routing, matching, geospatial)
3. Behavioral interview (1 round): 8 norms, ownership, ownership, ownership

**PM:**
1. PM phone screen: product sense + behavioral (30-45 min)
2. JAM session: ideation sprint — "you have 20 minutes, generate 10 ideas for X problem"
3. Final round: marketplace metrics case + data scientist co-interview

**TPgM (Technical Program Manager):**
1. Technical screen: system design-lite (1-2 components of Uber's architecture)
2. Take-home case: design a program/initiative, not just a system
3. Behavioral: ownership, cross-functional collaboration, big bold bets

---

## Lab Menu

### SWE Track

| Lab | Tier | Focus |
|---|---|---|
| Lab 01: Graph / Shortest-Path Routing | Tier 1 | Dijkstra with path reconstruction, Uber ETA framing |
| Lab 02: Rate Limiter / Hit Counter | Tier 2 | Sliding window, design + implementation |
| Lab 03: Sliding-Window Moving Average | Tier 2 | Streaming data, window algorithms |
| Lab 04: Ownership Behavioral | Tier 2 | STAR stories using "act like owners" norm |

### PM Track

| Lab | Tier | Focus |
|---|---|---|
| Lab 01: Two-Sided Marketplace Metrics | Tier 1 | Supply vs demand vs Uber bottom line diagnostic |
| Lab 02: JAM Session Ideation | Tier 2 | 10 ideas in 20 minutes, Uber product flavor |
| Lab 03: Metric Drop Root-Cause | Tier 2 | Data-driven diagnosis of a metric decline |

### TPM Track

| Lab | Tier | Focus |
|---|---|---|
| Lab 01: Distributed System Design Lite | Tier 2 | Design 1-2 components of Uber's dispatch or pricing system |
| Lab 02: Take-Home Case | Tier 3 | Program design case, cross-functional stakeholder framing |

---

## Before You Start

**The one mental model to install before any Uber lab:**

Every decision at Uber has three dimensions. Before answering ANY question, ask yourself:
- How does this affect **supply** (drivers/restaurants/couriers)?
- How does this affect **demand** (riders/eaters/shippers)?
- How does this affect **Uber's bottom line** (take rate, margin, profitability)?

A PM who recommends a driver incentive program without modeling the demand impact and the margin impact will not pass the Uber PM bar.

**Know the 8 norms verbatim.** Print them. Carry them. Connect your answers explicitly.
