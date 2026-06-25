# Flashcards — Uber PM Lab 01: Two-Sided Marketplace Metrics

---

**Card 01 — Supply vs Demand vs Platform Diagnostic Framework**

Q: Name the three diagnostic buckets for a marketplace metric drop and give 2 example metrics for each.

A:
**Supply side** (providers):
- Restaurant availability rate (% of partner restaurants currently open in app)
- Driver/courier acceptance rate (% of delivery requests accepted)

**Demand side** (customers):
- App sessions per day (unique users opening the app)
- Order conversion rate (orders placed / app sessions)

**Platform side** (the tech):
- App error rate (% of sessions with a crash or error)
- Payment failure rate (% of checkout attempts that fail)

Start with the bucket you have the strongest prior on, then check the other two if the first doesn't explain the drop.

---

**Card 02 — Uber Eats Key Metrics (Definitions)**

Q: Define these Uber Eats metrics precisely: order volume, acceptance rate, conversion rate, take rate.

A:
- **Order volume**: total number of orders placed in a given time period and geography
- **Driver/courier acceptance rate**: (delivery requests accepted by courier) / (total delivery requests dispatched). If a courier declines a job, that's a miss.
- **Order conversion rate**: (orders placed) / (unique app sessions) — measures how well the app converts intent into action
- **Take rate**: Uber's revenue / Gross Bookings. If a $40 order generates $8 for Uber, take rate = 20%.
- **Gross Bookings**: total dollar value of all orders (before Uber's cut — the total the merchant + Uber receives)
- **Contribution margin**: Gross Bookings × take rate minus variable costs (courier pay, payment processing, support)

---

**Card 03 — Root-Cause Tree Structure**

Q: How do you structure a marketplace metric drop diagnostic as a tree?

A: Start at the top (the symptom), then branch by the three buckets, then branch within each bucket:

```
Order volume ↓
├── Supply: restaurant availability? acceptance rate? menu completeness?
│    └── If all normal → eliminate supply
├── Platform: error rate? load time? payment failures?
│    └── If all normal → eliminate platform
└── Demand: sessions? conversion? cohort (new vs existing)?
     ├── Sessions stable, conversion down → UX/price issue
     └── Sessions down, conversion down → awareness/churn issue
```

Always state which bucket you're eliminating and why before moving to the next.

---

**Card 04 — Data Scientist Collaboration Signals**

Q: What signals does the Uber PM data scientist co-interviewer look for?

A: The data scientist evaluates:
1. **Metric precision**: "look at engagement" = weak. "Look at 7-day active users in the Bay Area segment, split by new vs existing" = strong.
2. **Correct data splits**: do you ask for the right breakdowns before interpreting raw numbers?
3. **Statistical thinking**: do you ask about sample size, seasonality, or statistical significance before declaring a root cause?
4. **Causal reasoning**: do you distinguish correlation from causation? ("Acceptance rate dropped AND order volume dropped" ≠ "acceptance rate CAUSED order volume to drop")
5. **Quantitative proposals**: "run a promotion" is weak. "Run a 2-week A/B test with 50% of SF Bay Area drivers receiving $2/delivery incentive, measuring acceptance rate lift and contribution margin impact" is strong.

---

**Card 05 — Cohort Analysis for Marketplace Drops**

Q: When diagnosing a metric drop, what cohort splits should you always check?

A: The four standard cohort splits for a marketplace metric investigation:
1. **New vs existing users**: new user drop = acquisition/awareness; existing user drop = retention/experience
2. **Geography**: is this Bay Area only, or also in other cities? Bay Area = local cause; everywhere = platform/product cause
3. **Time of day**: is the drop concentrated in lunch, dinner, or late night? Points to supply (couriers offline) or restaurant-specific issues
4. **Device**: iOS vs Android. If one platform dropped, likely a tech regression on that platform.

Also: user tier (high-frequency vs occasional orderers), restaurant category (fast food vs sushi), and order type (delivery vs pickup).

---

**Card 06 — Driver Incentive Economics**

Q: How do you evaluate whether a driver incentive program is worth its cost?

A: Build a unit economics model:

```
Current state:
  Driver acceptance rate: 72%
  Orders per hour (per driver): 3.2
  Take rate: 20%
  Avg order value: $35
  Uber revenue per driver-hour: 3.2 × $35 × 20% = $22.40

After $2/delivery incentive:
  Expected acceptance rate: 82% (assumption — needs validation)
  Orders per hour: 3.7 (higher acceptance → more efficient routing)
  Uber revenue per driver-hour: 3.7 × $35 × 20% = $25.90
  Incremental cost per driver-hour: 3.7 × $2 = $7.40
  Net change: $25.90 - $22.40 - $7.40 = -$3.90 per driver-hour

Verdict: this incentive LOSES money at these assumptions. Try a smaller incentive or different mechanism.
```

Always quantify before recommending an incentive.

---

**Card 07 — A/B Testing in a Marketplace (Interference Effects)**

Q: Why is A/B testing hard in a two-sided marketplace and how do you handle interference?

A: Standard A/B testing assumes the treatment group doesn't affect the control group (SUTVA — Stable Unit Treatment Value Assumption). In a marketplace, this fails:

**Problem**: If you give courier incentives to 50% of drivers (treatment), those drivers will take more orders, leaving fewer orders for the control-group drivers. Control group is contaminated.

**Solutions**:
1. **Geographic holdout**: put entire cities in treatment vs control (Bay Area = treatment; LA = control). Cities don't share supply.
2. **Time-based holdout**: alternate treatment periods (week 1 = treatment, week 2 = control). Assumes no carryover effects.
3. **Switchback design**: randomize treatment at the time-of-day level across multiple weeks.

Always ask: "Will this experiment contaminate the control group?" before designing the test.

---

**Card 08 — "Do the Right Thing" in PM Context**

Q: What does Uber's "do the right thing" norm mean when evaluating a driver incentive program?

A: "Do the right thing" in this context means:
1. **Don't recommend an expensive incentive before diagnosing the root cause** — if the drop is actually a platform bug, incentivizing drivers won't fix it and wastes money.
2. **Consider driver welfare, not just Uber's margin** — if couriers are declining orders because the pay is genuinely unfair, the "right thing" may be raising the base rate, not a short-term promotion.
3. **Be honest about uncertainty** — don't claim a 15% acceptance rate lift if you don't have data supporting it. Say "I'd run a pilot to validate this assumption."
4. **Consider externalities** — a surge in courier activity might conflict with local traffic ordinances in some cities.

---

**Card 09 — Gross Bookings vs Revenue vs Contribution Margin**

Q: Explain the difference between gross bookings, Uber Eats revenue, and contribution margin. Give a numerical example.

A:
**Example**: a $40 Uber Eats order

| Metric | Definition | Value |
|---|---|---|
| Gross Bookings | Total order value | $40.00 |
| Uber Revenue | Gross Bookings × take rate (20%) | $8.00 |
| Variable costs | Courier pay + payment processing + support | $5.50 |
| Contribution Margin | Revenue − Variable costs | $2.50 |

A metric drop might mean different things:
- If order volume ↓ but avg order value ↑: Gross Bookings might be stable
- If couriers are paid more per delivery: Contribution Margin drops even if Gross Bookings are flat
- "The business is healthy" requires checking Contribution Margin, not just Gross Bookings

---

**Card 10 — When Order Volume Drops but Revenue Rises**

Q: If Uber Eats order volume is down 10% but gross bookings are up 5%, what does that mean and is it good or bad?

A: This means **average order value (AOV) increased** significantly.

Math: if order volume is 0.9x and Gross Bookings is 1.05x, then AOV = 1.05 / 0.9 = 1.167x, a ~17% increase in average order size.

Possible explanations:
- Cheaper restaurants left the platform (selection effect — only expensive ones remain)
- Customers are ordering for groups rather than individuals
- Fewer but higher-quality customers ordering (low-frequency casual users churned; high-frequency power users remain)
- A promotion targeted at high-AOV orders drove up basket size

Is it good? **It depends on contribution margin.** Higher AOV is good if fixed costs dominate (delivery is fixed per trip). It's bad if it means fewer couriers are making fewer trips (less density = less efficiency).

Always follow gross bookings with: "but what happened to take rate and contribution margin?"
