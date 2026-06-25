Status: Ready — work through all parts in order

# Lab 01 · Two-Sided Marketplace Metrics — Uber Eats Diagnosis
**Uber PM · Tier 1 · ~75 minutes**

---

## 🪜 Milestones

- [ ] M1 · Framed — identified the 3 hypothesis buckets (supply, demand, platform) before looking at any data
- [ ] M2 · Metrics mapped — named 3+ specific metrics per bucket with clear definitions
- [ ] M3 · Root-caused — narrowed to the most likely cause using structured reasoning
- [ ] M4 · Proposed — suggested 2 interventions with expected impact, both sides of marketplace considered
- [ ] M5 · Defended — curveballs handled with data-driven responses
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Scenario

You're in an **Uber PM interview**. The interviewer says:

> "Uber Eats is seeing declining order volume in the SF Bay Area over the past 3 months. The head of Ops wants to know: is this a supply problem (not enough restaurants or drivers), a demand problem (fewer customers ordering), or a platform problem (bugs, UX, or technical issues)?
>
> Walk me through how you'd diagnose this."

There's a data scientist in the room. They can pull any data you name — but they'll evaluate whether you're asking for the RIGHT data.

This is a marketplace metrics lab. **Every decision must be evaluated through three lenses: supply, demand, and Uber's bottom line.**

---

## Part 0: Forethought

Before clarifying — 3 minutes:

1. What's the difference between "order volume is down" and "the app is broken"? Why is that distinction important for diagnosis?
   [blank]

2. Who are the "supply side" in Uber Eats? Who is the "demand side"?
   [blank]

3. What's your prior on what USUALLY causes a regional metric decline? (Geography? Seasonality? Competitive entry? Platform bug?)
   [blank — this is about structured intuition before data]

---

**--- CHECKPOINT: Forethought complete. Move to Part 1. ---**

---

## Part 1: Clarifying Questions

Ask these before framing any hypothesis. The data scientist in the room is watching to see if you ask smart questions.

**Time:**
- Is the decline across all 3 months, or sudden (suggests bug) vs gradual (suggests structural)?
  [blank — your interpretation of each]

**Geography:**
- Is SF Bay Area a proxy for something? Is this decline Bay Area-only or also in NYC, Chicago?
  [blank — if Bay Area only: local competitive or regulatory cause likely; if everywhere: platform cause likely]

**Segment:**
- Is the decline across all restaurant categories, or specific to a type (pizza, sushi, fast food)?
  [blank — if specific category: supply issue in that category; if broad: demand or platform]

**Cohort:**
- Is the decline in new users, existing users, or both?
  [blank — new user decline = acquisition/awareness issue; existing user decline = retention/experience issue]

**Business context:**
- Did DoorDash or Grubhub launch a promotion in the Bay Area in this period?
  [blank — competitive entry is a demand-side cause that looks like a platform problem]

- Did Uber change the delivery fee or restaurant commission rate recently?
  [blank — fee changes affect both sides of the marketplace]

---

**--- CHECKPOINT: Clarifying questions written. Move to Part 2. ---**

---

## Part 2: The Diagnostic Framework

**The Three Buckets — always start here before touching any data.**

Write 3+ specific metrics for each bucket. Be precise: not "look at demand" but "measure session count for users who opened the app in the last 30 days in the Bay Area."

**SUPPLY METRICS**

| Metric | Definition | What a decline signals |
|---|---|---|
| Restaurant availability rate | % of partner restaurants that are "open" in the app during peak hours | If low: restaurants are closing/pausing |
| Driver acceptance rate | % of delivery requests accepted by couriers | If low: courier supply shortage or earnings are unattractive |
| Restaurant menu completeness | % of menu items that are in-stock (not marked unavailable) | If low: restaurant ops issue |
| [blank — add a 4th supply metric] | [blank] | [blank] |

**DEMAND METRICS**

| Metric | Definition | What a decline signals |
|---|---|---|
| App sessions per day | Unique users opening the Eats app | If down: awareness, habit, or churn issue |
| Order conversion rate | Orders placed / app sessions (or menu views) | If down: UX issue, price sensitivity, or cart abandonment |
| Cart abandonment rate | % of users who add items but don't complete checkout | If up: pricing, delivery fee, or UX issue |
| [blank — add a 4th demand metric] | [blank] | [blank] |

**PLATFORM METRICS**

| Metric | Definition | What a decline signals |
|---|---|---|
| App error rate | % of sessions with a crash or critical error | If high: technical regression |
| Payment failure rate | % of checkout attempts that fail at payment step | If high: payment integration bug |
| Menu load time (p99) | 99th percentile load time for restaurant menu page | If high: performance regression causing abandonment |
| [blank — add a 4th platform metric] | [blank] | [blank] |

**UBER'S BOTTOM LINE (Cross-bucket)**

| Metric | Definition |
|---|---|
| Gross Bookings | Total dollar value of all orders |
| Take rate | Uber's revenue as a % of Gross Bookings |
| Contribution margin | Revenue minus variable costs per order (delivery pay, etc.) |
| [blank] | [blank] |

---

**Which metric would you look at FIRST? Why?**
[blank — there's no single right answer, but your reasoning must be explicit. Consider: which bucket do you have the strongest prior on? Which metric, if it's bad, immediately narrows you to one bucket?]

**What's the first data SPLIT you'd do?**
[blank — time (gradual vs sudden), geography (Bay Area vs national), user cohort (new vs existing), device (iOS vs Android), order type (pickup vs delivery)?]

---

**--- CHECKPOINT: Framework complete. Move to Part 3. ---**

---

## Part 3: Root Cause Tree

Structure your diagnostic as a decision tree. You're narrowing from "order volume is down" to one specific root cause.

```
Order volume ↓ in SF Bay Area (3 months)
│
├── Is it supply, demand, or platform?
│    │
│    ├── Check: Restaurant availability rate
│    │     │
│    │     ├── Normal (> 85%) → Supply side is healthy → move to demand
│    │     └── Low (< 75%) → [blank — what do you investigate next?]
│    │
│    ├── Check: App error rate
│    │     │
│    │     ├── Normal (< 1%) → Platform is healthy → move to demand
│    │     └── High (> 5%) → [blank — what do you do next?]
│    │
│    └── Check: Session count trend
│          │
│          ├── Sessions stable, conversion down → [blank — what hypothesis?]
│          └── Sessions down AND conversion down → [blank — what hypothesis?]
│
└── After narrowing to one bucket:
     What's your top-3 ranked hypotheses within that bucket?
     1. [blank]
     2. [blank]
     3. [blank]
```

---

**--- CHECKPOINT: Root cause tree complete. Move to Part 4. ---**

---

## Part 4: Diagnosis Artifact (PM Deliverable)

Write this as a crisp Uber-style brief. Pretend it's going to the head of Ops.

```
UBER EATS — BAY AREA ORDER VOLUME INVESTIGATION
Date: [blank]
Author: [blank]

─────────────────────────────────────────

HYPOTHESIS
The decline is primarily driven by: [blank — pick one: supply / demand / platform]

Because: [blank — the specific data signal that pointed you here]

─────────────────────────────────────────

EVIDENCE SUPPORTING THIS HYPOTHESIS
1. [blank — specific metric + value + what it means]
2. [blank]
3. [blank]

─────────────────────────────────────────

EVIDENCE THAT CONTRADICTS OR IS AMBIGUOUS
1. [blank — what data would have ruled this hypothesis out if it were different?]
2. [blank]

─────────────────────────────────────────

PROPOSED INTERVENTION
1. [blank — specific action: who does what, in what time frame]
   Expected impact: [blank — be quantitative if possible]
   How to measure: [blank — A/B test? holdout? before/after?]

2. [blank — second intervention]
   Expected impact: [blank]
   How to measure: [blank]

─────────────────────────────────────────

RISKS
[blank — what could go wrong with the interventions?]

─────────────────────────────────────────

OPEN QUESTIONS
[blank — what data would you want before acting?]
```

---

**--- CHECKPOINT: Diagnosis artifact written. Move to Part 5. ---**

---

## Part 5: Marketplace Reasoning

Answer these before curveballs. These are the "think in supply/demand/Uber bottom line" questions.

**If sessions are down 10% but conversion rate is also down 10%, what's the total order volume change?**
[blank — it's multiplicative: 0.9 × 0.9 = 0.81 = 19% decline in order volume even though each individual metric dropped by "only" 10%]

**Who is impacted by a driver acceptance rate drop?**
[blank — demand side: longer wait times for eaters; Uber bottom line: lower throughput and take; supply side: driver earnings drop if they're declining because trips are less attractive]

**How do you distinguish "fewer customers wanting to order" from "customers who want to order but aren't converting"?**
[blank — look at session count (intent to use the app) vs conversion rate separately. If sessions are stable but conversion dropped, demand intent is fine but something is blocking the order.]

---

**--- CHECKPOINT: Marketplace reasoning complete. Move to Part 6. ---**

---

## Part 6: Curveballs

**Curveball 1:**
"Order volume is down but gross bookings (total dollar value) are up. What does that tell you?"
[blank — hint: average order value went up. This could mean: customers are ordering more expensive items (fewer but bigger orders), or cheaper restaurants left the platform and only premium ones remain, or a high-fee promotion drove up basket size. Is this good or bad? Consider take rate and margin impact.]

**Curveball 2:**
"The data scientist says: driver acceptance rate dropped from 85% to 72% over the same 3-month period. Is that a supply problem or a demand problem?"
[blank — it's primarily a SUPPLY signal (couriers are declining orders), but the cause could be demand-driven (orders became less profitable per trip because customers are ordering less, so surge doesn't kick in). Ask: what happened to earnings per hour for couriers in this period? Did Uber cut delivery pay? Did gas prices rise? Did DoorDash offer a driver bonus?]

**Curveball 3:**
"You recommend a 20% driver incentive campaign to boost acceptance rates. The VP of Finance says it's too expensive. What's your alternative?"
[blank — consider: (1) route optimization to reduce driver empty miles (supply-side efficiency, no cost), (2) demand stimulation (promotions to increase order density, making each driver trip more efficient), (3) restaurant clustering incentives (nudge restaurants to cluster orders from the same neighborhood to reduce courier travel time), (4) dynamic pricing that increases delivery fee at low-supply times (passes cost to customer). Connect to Uber's bottom line: a 20% incentive that generates 15% more orders is a net loss. A 10% incentive that generates 25% more orders (via density) is a win.]

---

**--- CHECKPOINT: Curveballs answered. Move to Part 7. ---**

---

## Part 7: Self-Assessment Rubric

Score yourself honestly. Total = 35 points. Target: ≥ 28 to be ready.

| Dimension | 5 | 3 | 1 | Your Score |
|---|---|---|---|---|
| Structure | Three-bucket hypothesis framework applied immediately before any data; buckets clearly separated | Got to the framework but not immediately; some bucket bleed | No framework; jumped directly to one hypothesis | /5 |
| User Empathy | Named specific impacts on drivers, restaurants, AND eaters; considered the experience of each stakeholder | Considered 2 of 3 stakeholders | Only thought about one side of the marketplace | /5 |
| Prioritization | Identified which metric to look at FIRST with clear reasoning; ranked hypotheses after narrowing | Identified multiple metrics but didn't prioritize clearly | Listed metrics without prioritization | /5 |
| Metrics Literacy | All metric definitions are precise; articulated the multiplicative effect of simultaneous metric drops; knows gross bookings vs take rate vs contribution margin | Metrics mostly correct; some imprecision in definitions | Vague metrics ("look at engagement") or confused gross bookings with profit | /5 |
| Communication | Diagnosis brief is crisp, complete, and actionable; a non-technical VP could act on it | Diagnosis brief is adequate but missing 1-2 elements | Diagnosis is too vague or too technical | /5 |
| Creativity | Proposed at least one non-obvious intervention (e.g., restaurant clustering, density-based dispatch) | Proposed standard interventions (incentives, promotions) with some nuance | Proposed a single generic intervention | /5 |
| Handling Ambiguity | When sessions + conversion both dropped, immediately quantified the compounding effect; when driver acceptance dropped, asked about earnings per hour before labeling it "supply problem" | Handled 1-2 ambiguities cleanly | Got stuck when data was ambiguous or contradictory | /5 |

**Total: /35**

---

### Reflection

What's the most important lesson about marketplace thinking you're taking from this lab?
[blank]

---

### Ready-When Checklist

- [ ] I can name 3+ supply metrics, 3+ demand metrics, and 3+ platform metrics for Uber Eats from memory
- [ ] I understand the difference between gross bookings, take rate, and contribution margin
- [ ] I can explain why a 10% session drop + 10% conversion drop = 19% order volume drop
- [ ] I can distinguish "supply problem" from "demand problem" even when the data is ambiguous
- [ ] I can propose an intervention that considers all three sides (supply, demand, Uber's bottom line)
- [ ] I have a crisp answer to "why is order volume down?" that I could deliver in 2 minutes
- [ ] Self-score ≥ 28/35
