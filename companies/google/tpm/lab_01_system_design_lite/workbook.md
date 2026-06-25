Status: Ready — work through all parts in order

# Google TPM Lab 01 — System Design Lite
## Design a URL Shortener at Scale (Tier 2)

**Tier:** 2 | **Role:** TPM | **Est. time:** 45 min | **Difficulty:** Medium

**Before you start:** Set a timer for 45 minutes. This lab simulates the Google Technical PM screen. You will NOT write code, but you must reason about architecture, scale, and tradeoffs. The artifact is a brief design document and a V1 scope list — the kind of thing a TPM produces before handing off to an engineering lead.

---

## Milestones

- [ ] M1 · Scoped — named functional requirements (shorten, redirect, analytics?) and non-functional (latency, availability, consistency)
- [ ] M2 · Designed — high-level architecture: API layer → shortening service → datastore → redirect
- [ ] M3 · Scaled — named the bottleneck at 1B URLs + 100K redirects/sec
- [ ] M4 · Tradeoffs — named 2 explicit build-vs-buy and cache-vs-no-cache decisions
- [ ] M5 · V1 scoped — defined MVP that ships in 6 weeks
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Part 0 — Forethought

**Scenario:** Your Google Technical PM screen interviewer says:

> "Design a URL shortener like bit.ly. You don't need to code it, but walk me through: the system design, how you'd handle 1B shortened URLs, what breaks at scale, and how you'd prioritize a V1. You have 45 minutes."

**What this question is really evaluating:**
- Can you scope a system before designing it (requirements → design, not design → requirements)?
- Do you know what breaks at scale, and can you reason about WHY (not just name buzzwords)?
- Can you make explicit build-vs-buy and tradeoff decisions, not just list options?
- Can you scope an MVP with discipline — knowing what NOT to build in V1 is as important as knowing what to build?

**Target time:** 45 minutes. Suggested breakdown:
- 5 min — clarifying questions and requirements
- 10 min — high-level architecture
- 10 min — scale reasoning (bottlenecks)
- 10 min — tradeoffs and V1 scoping
- 10 min — reasoning write-up and curveballs

**Google TPM rubric note:** "A TPM doesn't code, but they must be the person in the room who can explain WHY the architecture is the way it is to both engineers and stakeholders. If the TPM can't reason about the bottleneck, they can't unblock the team."

**Confidence rating before starting (circle one):** 1 — 2 — 3 — 4 — 5

**What I want to get right this session:** [blank]

---

## Part 1 — Clarifying Questions

*Scope the system before designing it. A TPM who starts designing without requirements has made a career-limiting move.*

**Q1 (Goal): "What's the primary use case — public URL shortening (anyone can use it) or internal use only (our own teams)?"**

Rationale: Public use means you need rate limiting, abuse prevention, and unknown traffic patterns. Internal use means you can trust callers and skip some infrastructure.

*Your assumption:* [blank]

**Q2 (Features): "Do we need analytics — click tracking, geographic distribution, referrer data — or just shorten and redirect?"**

Rationale: Analytics changes the write path dramatically. Every redirect becomes a write event (log this click) in addition to a read event (return the destination URL). At 100K redirects/sec, analytics = 100K additional writes/sec.

*Your assumption:* [blank]

**Q3 (Scale): "1B total shortened URLs over the system lifetime, or 1B new URLs per day? And what's the expected redirect volume — 100K redirects/sec peak, or sustained?"**

Rationale: 1B total URLs ≈ 1B rows in a database — a storage problem. 1B per day ≈ 11,600 new URLs per second — a write throughput problem. These are orders of magnitude apart.

*Your assumption:* [blank]

**Q4 (SLA): "What's the latency target for redirect, and what's the availability requirement?"**

Rationale: Redirect latency budget defines your caching strategy. < 50ms end-to-end means you must serve from cache for almost every request. 99.99% availability = 52 minutes of downtime per year — this changes your replication and failover architecture.

*Your assumption:* [blank]

**Q5 (Constraints): "Are there any custom short code requirements, URL expiry, or content policy requirements (block malicious URLs)?"**

Rationale: Custom short codes = collision management. URL expiry = TTL management. Content policy = pre-shortening URL scanning (Safe Browsing API call on every shorten request).

*Your assumption:* [blank]

**Checkpoint M1:** Check the box above once you've written your own assumptions for all 5 questions.

---

## Part 2 — System Decomposition

**Functional requirements (fill in):**
- Core: [blank — what the system MUST do]
- Extended: [blank — what it SHOULD do if scope allows]

**Non-functional requirements (fill in):**
- Latency: [blank]
- Availability: [blank]
- Consistency: [blank — strong consistency needed, or eventual? For redirects specifically]
- Scale: 1B total URLs, 100K redirects/sec peak

**Data model:**
```
URL record:
  short_code: string (6 chars, base62)    ← the key
  long_url:   string (max 2048 chars)     ← the value
  created_at: timestamp
  created_by: user_id (optional)
  expires_at: timestamp (optional)
  click_count: integer (if analytics)
```

**State machine for a short URL:**
[blank — name the states a URL can be in and the transitions]

*Model:* Active → Expired (by TTL) → Deleted (by user or policy). Also: Flagged (content policy scan in progress) → Active (clean) or Deleted (malicious).

---

## Part 3 — Architecture Design

*Write a design brief, not code. This is your TPM artifact.*

**FUNCTIONAL:**
- `POST /shorten` → accepts long URL, returns short URL
- `GET /{short_code}` → HTTP 301/302 redirect to long URL
- `GET /analytics/{short_code}` → click stats (if extended scope)

**NON-FUNCTIONAL (your assumptions from Part 1):**
- Redirect latency: [blank]
- Availability: [blank]
- Consistency model: [blank — and why eventual is acceptable here for redirects]

**HIGH-LEVEL ARCHITECTURE:**

```
Client
  ↓
CDN (cache redirects at edge — cache hit rate ~90% for popular URLs)
  ↓ (cache miss only)
API Layer (stateless, horizontally scalable)
  ↓
[blank — what service sits here?]
  ↓
Datastore ([blank] — what type? Why?)
  +
Cache Layer ([blank] — what technology? What TTL?)
```

*Fill in the blanks and explain each choice.*

**SHORTCODE GENERATION — pick one and defend it:**

| Option | Description | Pros | Cons |
|---|---|---|---|
| A | Random 6-char base62 (62^6 = 56B possible) | No coordination needed between nodes | Collision check required on every generate |
| B | Hash of long URL + truncate to 6 chars | Same URL always → same short code | Collision risk: two URLs → same hash prefix |
| C | Auto-increment integer → base62 encode | Guaranteed no collision | Sequential (predictable); requires central counter |

**Your choice:** [blank] **Why:** [blank]

**COLLISION PROBABILITY:**
Base62 with 6 characters = 62^6 = 56,800,235,584 possible codes (~56B).
At 1B URLs, the probability of at least one collision (birthday paradox): [blank]

*Model:* P(at least one collision) ≈ 1 - e^(-n²/2N) where n = stored URLs, N = code space.
At n = 1B, N = 56B: P ≈ 1 - e^(-(10^9)²/(2×56×10^9)) = 1 - e^(-8.9) ≈ 99.9%. The base62 space is NOT sufficient for 1B URLs without collision handling. You need either: 7-char codes (62^7 = 3.5T, much safer), or an explicit collision check-and-retry on generation.

**CACHING:**
- Observation: URL access follows a power law. Top 1% of URLs (most popular) receive ~[blank]% of redirect traffic.
- Cache strategy: Cache the top URLs in Redis. On a redirect request: check cache first, if miss → DB read → cache for TTL.
- What TTL? [blank — and the tradeoff]

**Checkpoint M2 + M3:** Check both boxes once the architecture block is filled in with your own reasoning for each choice.

---

## Part 4 — Scale Reasoning

*Name the bottleneck at 1B URLs + 100K redirects/sec. Don't just name the component — explain WHY it's the bottleneck and what specifically breaks.*

**Redirect path at scale (100K redirects/sec):**

The bottleneck is [blank].

*Break it down:*
- Without cache: 100K DB reads/sec. A single PostgreSQL instance handles ~5K-10K reads/sec. You'd need [blank] shards, each with a replica for high availability.
- With Redis cache (hot URL cache): ~95% of redirects served from Redis without hitting the DB. Redis handles ~100K+ ops/sec on a single node. The bottleneck shifts to [blank].
- At the CDN layer: redirect responses are cacheable at the CDN edge (301 permanent, or 302 temporary). If you cache at CDN, ~90% of requests never reach your servers. The bottleneck shifts to [blank].

**Shorten path at scale:**
- At peak: [blank] new URLs per second (derive this from your stated assumption in Part 1).
- Bottleneck for write path: [blank — hint: the counter if you chose Option C, or the collision check DB if you chose Option A]

**What breaks at 1B total URLs:**
- Storage: 1B records × avg row size ([blank] bytes including indexes) = [blank] GB. Is this a single-instance problem or a sharding problem?
- Index size: The short_code column must be indexed for redirect lookup. Index size for 1B rows × 6-char string key ≈ [blank] GB in memory for a B-tree index. Does it fit in RAM on a single DB host?

**Checkpoint M3 (already checked above):** This section completes the scale reasoning milestone.

---

## Part 5 — Tradeoffs and V1 Scoping

**TPM Tradeoff 1 — Build vs. Buy: Shortcode Generation Service**

Option A (build): Write your own distributed ID generator (Snowflake-style, or UUIDs hashed to base62). Full control, no external dependency.

Option B (buy): Use an existing distributed ID service (Twitter Snowflake, Sonyflake, ULIDs). Battle-tested, faster to ship.

**Your recommendation:** [blank] **Rationale:** [blank]

**TPM Tradeoff 2 — Cache vs. No Cache**

Without cache: Every redirect hits the DB. Simpler architecture. Lower operational complexity.
With cache: Dramatically lower latency (< 5ms from Redis vs 20-50ms from DB). Adds Redis dependency and cache invalidation complexity.

**Your recommendation:** [blank] **Rationale:** [blank]

*Key insight:* The URL redirect use case is ideal for caching because: (a) reads massively outnumber writes (read-heavy), (b) data is immutable for most URLs (once shortened, the destination doesn't change), (c) a small subset of URLs (popular links in viral content) receives a disproportionate share of traffic — exactly the power-law pattern that caching is designed for.

**V1 Scope (what ships in 6 weeks):**

**V1 includes:**
- [blank — list 3-5 things that are core to V1]

**V1 explicitly defers:**
- Analytics / click tracking: [blank — why defer?]
- Custom short codes: [blank — why defer?]
- URL expiry: [blank — why defer?]
- Content policy scanning: [blank — why defer?]
- Geographic redirect (serve different destination by region): [blank — why defer?]

*Model V1 defers rationale:* Analytics requires a separate write path and storage system (ClickHouse or BigQuery) — adding it to V1 more than doubles the engineering scope. Custom short codes require collision management and a separate namespace — defer to V2 once the base system is stable. URL expiry requires a background job to clean up expired records — important but not blocking the core shorten/redirect use case.

**Checkpoint M4 + M5:** Check both boxes once tradeoffs are filled in with your reasoning and V1 scope is explicitly stated.

---

## Part 6 — Interview Simulation (Curveballs)

### Curveball 1

**Interviewer:** "A politician's campaign uses your service. They complain that someone shortened a malicious URL to the same 6 characters as their campaign URL (collision). How do you prevent this?"

**Your answer:** [blank]

*Things to address:*
- This is a collision scenario (two different long URLs mapping to the same short code) combined with a reputational harm scenario.
- Prevention: On every shorten request, check whether the generated short code already exists. If it does, generate a new one (retry). The probability of a collision at 1B URLs in 56B code space is ~10% per attempt — you'd need to retry on average 1.1× per request. Acceptable.
- But the politician's scenario isn't a random collision — it's a targeted attack where someone deliberately chose the same 6 characters. Your system should prevent this by: (a) not allowing users to choose their own short codes in V1 (all codes are system-generated), OR (b) if custom codes are allowed, requiring a unique check before reservation.
- Additional safeguard: once a short code is claimed, it can never be reused even after deletion — use a "soft delete" that retains the code in a blocklist.

---

### Curveball 2

**Interviewer:** "Your CDN is caching stale redirects — a URL's destination changed but the CDN still returns the old target. How do you handle cache invalidation?"

**Your answer:** [blank]

*Things to address:*
- This is the classic CDN cache invalidation problem. There are 3 strategies:
  1. **Short TTL**: Cache redirects for only 60 seconds. Simple, but degrades cache hit rate for popular URLs that never change.
  2. **Cache purge on update**: When a URL's destination changes, call the CDN purge API to invalidate the cached redirect. Requires CDN purge API support (Cloudflare, Fastly both support this). Latency to propagation: usually 1-30 seconds.
  3. **302 vs 301 redirect**: Use 302 (temporary) instead of 301 (permanent). Browsers cache 301 redirects indefinitely; they don't cache 302. For a URL shortener where destinations might change, 302 is the safer default — it trades cache efficiency for correctness.
- TPM recommendation: Use 302 for user-created URLs (which might change) and 301 only for system-owned URLs (which are immutable). Combine with a 5-minute CDN TTL for 302 responses.

---

### Curveball 3

**Interviewer:** "At 1B URLs, your base62 shortcode space has a 10% collision probability. What do you do?"

**Your answer:** [blank]

*Things to address:*
- The 10% per-generation collision probability means you need to retry ~1.1× on average. This is acceptable operationally but increases with more URLs.
- Options:
  1. **Increase code length**: 7 characters = 62^7 = 3.5T. At 1B stored URLs, collision probability drops to < 0.01%. Tradeoff: URLs get longer (hard to memorize, but URL shorteners are rarely memorized anyway).
  2. **Partition the namespace**: Assign different prefixes per data center or per generator node. Eliminates inter-node collisions entirely (each node's prefix is unique). Reduces per-node code space but also reduces coordination cost.
  3. **Pre-generate code pool**: Generate 100M unique codes in a batch job (guaranteed no collision within the batch), store them in a fast queue (Redis LPOP). Each shorten request pops one code. Eliminates per-request collision risk. Tradeoff: pool maintenance and the "last code in the pool" edge case.
- As a TPM, you'd frame this as: "The 7-char upgrade is a data migration — we need to move all existing 6-char codes and update our API contract. That's a 2-week engineering effort. The pre-generated pool is a smaller operational change we can ship in 3 days. I'd recommend the pool approach first, then plan the 7-char migration for V2."

---

## Part 7 — TPM Rubric

*Self-grade after completing the lab. Score as a Google Technical PM interviewer would.*

| Dimension | 5 — Strong | 3 — Adequate | 1 — Weak | Your Score |
|---|---|---|---|---|
| Technical fluency | Correctly explained base62 encoding, collision probability, cache hit rate, and redirect latency budget without prompting | Explained most concepts accurately but needed hints on one or two | Couldn't explain why base62 is used or what the collision probability math means | __ /5 |
| Architecture tradeoffs | Named and defended 2 explicit tradeoffs (build vs. buy, cache vs. no cache); articulated the mechanism of each tradeoff | Named tradeoffs but didn't defend them; or defended without naming the mechanism | Listed options without making a recommendation | __ /5 |
| Build-vs-buy | Made a recommendation on shortcode generation service with engineering time as the decision criterion | Mentioned build-vs-buy but didn't apply it to a specific decision | Didn't mention build-vs-buy | __ /5 |
| Scale / reliability | Named the specific bottleneck at 100K redirects/sec (DB reads without cache), explained why (reads/sec limit of a single DB), and how caching resolves it | Named the bottleneck but couldn't explain the mechanism | Said "we'd need to scale horizontally" without identifying what the bottleneck actually is | __ /5 |
| Communicates with engineers | Used accurate technical vocabulary (base62, collision, TTL, CDN, sharding, read replica); could hand off the design brief to a senior engineer who could build from it | Mostly accurate; one or two imprecise terms | Non-engineers might follow; engineers would have too many open questions to build | __ /5 |
| Translates to non-technical | Explained the cache decision in terms of "90% of requests served before they hit our servers" (business benefit) not just "Redis reduces DB load" (technical fact) | Gave mostly technical explanations; could adapt when asked | Explained everything in engineering terms; could not reframe for a business stakeholder | __ /5 |
| Handling ambiguity | Scoped the system with clarifying questions before designing; made explicit assumptions; updated the design when the interviewer introduced the 10% collision scenario | Scoped before designing but some requirements were assumed, not asked | Started designing without scoping; or couldn't update the design when requirements changed | __ /5 |

**Total: __ / 35**

---

## Reflection

**Which architectural decision did you find hardest to reason about?** [blank]

**Did you scope V1 before the interviewer asked, or only after?** [blank]

**Could you explain the 302 vs 301 decision to a business stakeholder in one sentence?** [blank]

---

## You're Ready When...

- You complete the full design (Parts 0–6) in under 40 minutes without model answers
- You can articulate the collision probability at 1B URLs and why 6-char base62 is insufficient without prompting
- You answer Curveball 2 (CDN cache invalidation) with the 302 vs 301 insight
- You scope a V1 with explicit deferrals and reasons before being asked to
- You self-grade ≥ 28/35 on two separate attempts

**Next labs:** Meta PM or Meta SWE tracks for continued prep.

---

*Google TPM Lab 01 · Tier 2 · v1.0*
