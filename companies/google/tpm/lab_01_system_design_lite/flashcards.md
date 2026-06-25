# Flashcards — Google TPM Lab 01: System Design Lite

*10 cards for spaced repetition. Study 24–48 hours after completing the workbook.*

---

## Card 1 — Base62 Encoding

**Q:** What is base62 encoding and why is it used for URL shorteners? What is 62^6?

**A:** Base62 uses 62 characters: digits 0-9 (10), lowercase a-z (26), uppercase A-Z (26). It's used for short codes because: (a) it produces human-readable, URL-safe strings without special characters like `+`, `/`, or `=` that appear in base64; (b) it is more compact than base10 (more codes per character); (c) a 6-character code in base62 gives 62^6 = **56,800,235,584 ≈ 56 billion** unique codes.

62^6 math shortcut: 62^2 = 3,844. 62^3 ≈ 238,000. 62^6 ≈ 56.8 billion. Memorize: **62^6 ≈ 56B**.

For URL shorteners, 6 characters strikes the balance between code space (56B >> practical URL count) and URL length (short.ly/aB3xZq is 6 chars). However, at 1B stored URLs, collision probability is non-trivial (see Card 2).

---

## Card 2 — Collision Probability Math

**Q:** A URL shortener has stored 1 billion URLs in a base62 6-character code space (56B possible codes). What is the approximate probability that the NEXT generated code collides with an existing one?

**A:** The probability that a randomly generated code collides with an existing code in a space of N codes when n codes are already used:

P(collision on next generate) ≈ n / N

At n = 1B used, N = 56B possible:
P ≈ 1,000,000,000 / 56,800,235,584 ≈ **1.76% per generation attempt**

This means roughly 1 in 57 generated codes will collide when the database has 1B entries. Operationally: every shorten request needs a collision check and retry loop. Expected retries before success: ~1.02 (low — still manageable).

At n = 5B used (about 9% of code space filled), P ≈ 8.8% per attempt. At n = 10B: P ≈ 17.6%. The system degrades gracefully until code space is substantially exhausted.

Mitigation if this becomes a problem: Move to 7 characters (62^7 ≈ 3.5 trillion — virtually no collision at 1B entries).

---

## Card 3 — CDN Cache Invalidation Strategies

**Q:** A URL shortener's CDN is caching a redirect. The user changes the destination URL. The CDN still returns the old destination. Name 3 strategies to handle this, with their tradeoffs.

**A:**
1. **Short TTL (e.g., 5 minutes):** Cache the redirect response for only 5 minutes. After expiry, CDN re-fetches the latest destination. Simple. Tradeoff: high CDN miss rate for popular URLs — much of the caching benefit is lost. Best for URLs that may change frequently.

2. **CDN purge on update:** When the user updates a short URL's destination, call the CDN's purge API (Cloudflare, Fastly, Akamai all support this). The CDN evicts the cached entry immediately. The next request hits the origin and gets the new destination. Tradeoff: requires CDN API integration and purge latency (1-30 seconds). Best for URLs that rarely change but MUST be current when they do.

3. **302 vs. 301 redirects:** Use HTTP 302 (Found / temporary) instead of 301 (Moved Permanently). Browsers cache 301 redirects indefinitely by default; they check 302 on every request. For a URL shortener where destinations might change, 302 is semantically correct and avoids browser-side staleness. Tradeoff: 302 is slightly slower (requires origin check) and doesn't benefit from browser-side caching. Best default for user-created short URLs; use 301 only for immutable system-owned URLs.

---

## Card 4 — SQL vs. NoSQL for URL Shortener

**Q:** Should you use SQL (e.g., PostgreSQL) or NoSQL (e.g., DynamoDB, Cassandra) for a URL shortener datastore? What are the deciding factors?

**A:** **SQL is appropriate for most URL shorteners**, including at scale with proper sharding. Here's the decision:

**Use SQL when:**
- You need ACID transactions (e.g., atomic "generate code + store record" to prevent duplicate codes)
- Your query pattern is simple (lookup by short_code — a single-column primary key lookup)
- You need joins (e.g., analytics queries joining URLs to click events)
- Your scale is < 100M rows and you can afford a single primary with read replicas

**Use NoSQL when:**
- Your write volume is extremely high (> 50K new URLs/sec) and you need horizontal write sharding without coordination
- Your read pattern is pure key-value (short_code → long_url) with no joins ever needed
- You're willing to sacrifice transaction guarantees for throughput

**For this system (1B total URLs, 100K redirects/sec):** Use PostgreSQL with a single primary and 2+ read replicas. The redirect path is read-only (lookup by short_code) — reads scale with replicas. Sharding to NoSQL adds operational complexity that isn't justified until you're at 10B+ URLs or 1M+ writes/sec.

---

## Card 5 — Read-Heavy vs Write-Heavy Design Implications

**Q:** A URL shortener has a 99:1 read-to-write ratio (99 redirects for every 1 new URL created). How does this ratio change the architecture decisions?

**A:** A 99:1 read-to-write ratio is a strongly read-heavy system. Design implications:

**Caching is high-value:** Every cache hit eliminates a database read. At 99% reads, even a 70% cache hit rate eliminates 70% of all DB operations. At 100K redirects/sec with 70% cache hit rate, DB handles only 30K reads/sec — manageable on a single replica.

**Read replicas before sharding:** Scale reads with read replicas (copies of the primary). Add sharding only if reads overwhelm even the replica fleet. For most URL shorteners, 3-5 read replicas is sufficient for 100K redirects/sec.

**Write path optimization is secondary:** The shorten operation (the write) is infrequent. Optimize the redirect path first. The shorten path gets less engineering attention than in a write-heavy system.

**CDN is high-value:** Read-heavy workloads benefit enormously from CDN caching — the most popular URLs (which get the most reads) are exactly the ones CDNs are designed to cache.

---

## Card 6 — Consistent Hashing for Sharding

**Q:** If you do need to shard a URL shortener's database, how does consistent hashing work and why use it instead of simple modular sharding?

**A:** **Simple modular sharding:** Assign each short_code to a shard based on hash(short_code) % N_shards. Problem: when you add a shard (N changes), nearly every record remaps to a different shard — requiring a massive data migration.

**Consistent hashing:** Arrange shards on a virtual ring. Each shard owns a range of the ring. When you add a shard, only the records in its ring range move — typically 1/N of all records. Adding a shard causes only ~1/N records to migrate.

**For URL shorteners specifically:** The short_code is already a good shard key — it's randomly distributed (for random-generation or base62-encoded ID approaches). Hash the short_code, place it on the consistent hash ring, route to the correct shard.

**When sharding becomes necessary:** At >500M rows and >100K reads/sec that exceed read replica capacity. Most URL shorteners at bit.ly scale (a few billion URLs) shard the DB horizontally using consistent hashing with 8-16 shards.

---

## Card 7 — V1 Scoping Discipline

**Q:** A URL shortener has 10 possible features. How do you decide what goes in V1? Name 3 questions that determine if a feature belongs in V1 or V2.

**A:**
1. **Is it on the critical path of the core use case?** The core use case is: shorten a URL, redirect to it. If the feature doesn't enable that loop, it's V2. Analytics is NOT on the critical path (users can shorten and redirect without knowing the click count). Analytics goes to V2.

2. **Would its absence make the product unusable to the target user?** URL expiry is not required for the product to work. A URL shortener without expiry is still functional. An analytics dashboard without expiry is still functional. Expiry goes to V2. But: content safety scanning might be V1 if the product is public-facing and enabling spam/phishing via the shortener is a launch blocker.

3. **Does it create engineering debt that's expensive to fix later if we defer it?** Shortcode generation strategy (random vs. sequential) is a V1 architecture decision — it's expensive to change later. Custom short codes create namespace collisions that are hard to unwind if you launch without the reservation mechanism. These are V1. The dashboard UI for analytics is easy to add later.

Rule of thumb: V1 = core loop + what makes the core loop safe to ship. Everything else is V2.

---

## Card 8 — Redirect Latency Budget Breakdown

**Q:** A user clicks a short URL and their browser must display the destination page. If the redirect latency target is < 100ms end-to-end, break down where that time goes.

**A:** End-to-end breakdown for a short URL redirect (browser clicks → destination page loads):

1. **DNS resolution of short URL domain:** 0-20ms (cached in browser/OS) to 50-100ms (cold lookup). For URL shorteners: use a short TTL on DNS but rely on OS DNS cache for active sessions. Budget: 5ms (cached).

2. **TCP + TLS handshake to CDN edge:** 10-30ms (CDN edge is geographically close). Budget: 15ms.

3. **CDN → origin request (on cache miss):** 20-100ms (depends on CDN-to-origin RTT). Budget: 30ms (if cache hit, this step = 0ms).

4. **Origin lookup (DB or cache):** < 5ms (Redis cache hit) to 10-20ms (DB read). Budget: 5ms.

5. **HTTP redirect response transmitted:** 1-2ms. Budget: 2ms.

**Total on cache hit (CDN):** 5 + 15 + 0 + 0 + 2 = 22ms. Well within 100ms.
**Total on cache miss (origin):** 5 + 15 + 30 + 5 + 2 = 57ms. Still within 100ms.

**The 302 vs. 301 implication:** 301 responses are cached by the browser indefinitely. Subsequent clicks skip all server interaction — effectively 0ms redirect latency. But if the destination changes, the browser serves the stale redirect until cache is cleared. For immutable system URLs: use 301. For user-modifiable URLs: use 302.

---

## Card 9 — 99.99% Uptime = 52 Minutes Downtime Per Year

**Q:** A URL shortener commits to 99.99% availability. What does this mean in practice? How many minutes of downtime are allowed per year, and what architectural decisions does this drive?

**A:** 99.99% availability = 52.6 minutes of allowed downtime per year (unplanned).

Architecture decisions required to hit 99.99%:
1. **No single point of failure:** Every component must have a redundant replica. Database: primary + warm standby with automatic failover. API layer: ≥ 3 stateless nodes behind a load balancer. Cache: Redis Cluster (multiple shards, each with replica).

2. **Deployment strategy:** Blue-green deployments (route 100% traffic to new version only after health checks pass on the new instances). Zero-downtime deploys. Any deploy that requires the DB to be offline cannot happen on a 99.99% SLA.

3. **Failover time:** Automatic failover (no human in the loop) must complete in < 30 seconds. If the primary DB fails at 2am, a human can't respond in time. Automatic failover via orchestration (AWS RDS Multi-AZ, Patroni) is required.

4. **CDN as buffer:** If the origin is temporarily down but the CDN has cached redirects, users don't experience downtime — they hit the CDN cache. This extends the effective availability beyond 99.99% for cached URLs. CDN is the highest-leverage uptime investment for a URL shortener.

Comparison: 99.9% = 8.7 hours/year downtime (acceptable for internal tools). 99.99% = 52 minutes (requires automated failover + CDN). 99.999% = 5.2 minutes (requires active-active multi-region replication — very expensive).

---

## Card 10 — Google TPM = Scope + Scale + Tradeoffs (No Code)

**Q:** What is the Google TPM interview rubric for a system design question? What specifically distinguishes a TPM design interview from a SWE design interview?

**A:** Google TPM system design is evaluated on 5 dimensions (not code):

1. **Scoping before designing:** Did you establish functional + non-functional requirements before drawing the architecture? SWEs sometimes jump to designing; TPMs must NOT.

2. **Scale reasoning:** Can you name the bottleneck at stated scale AND explain the mechanism (not just "we'd add more servers")? A TPM must say: "At 100K redirects/sec without caching, a single PostgreSQL instance fails because it handles only 5-10K reads/sec. We need a Redis cache to absorb 95% of reads."

3. **Explicit tradeoffs:** Did you name the decision (302 vs 301, SQL vs NoSQL, random vs sequential code generation) AND defend your choice with a reason? Listing options without choosing is not adequate for a TPM.

4. **V1 scoping:** Did you define an MVP with explicit deferrals AND reasons for deferring? "We defer analytics to V2 because it adds a second write path that more than doubles the engineering scope" is the expected answer pattern.

5. **Translating for stakeholders:** Can you explain the cache decision to a business stakeholder in business terms? "Caching means 90% of redirects are served before they reach our servers — this is what allows us to offer < 100ms redirect latency globally while keeping the infrastructure cost manageable."

**Key difference from SWE:** A SWE interview asks you to code the shortcode generator. A TPM interview asks you to explain WHY you chose one generation strategy over another, what breaks if you're wrong, and how you'd scope the V1 to ship in 6 weeks.

---

*10 cards · Google TPM Lab 01 · Review 24–48 hrs after completing workbook*
