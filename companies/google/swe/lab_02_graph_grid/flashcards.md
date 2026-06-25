# Flashcards — Google SWE Lab 02: Rate Limiter Sliding Window Design

*10 cards for spaced repetition. Study these 24–48 hours after completing the workbook. Cover the answer and try to recall it before reading.*

---

## Card 1 — Fixed Window vs Sliding Window: The Core Tradeoff

**Q:** Explain the "2× burst problem" in a fixed-window rate limiter. Give a concrete numeric example and explain why a sliding window avoids it.

**A:** Fixed window divides time into discrete non-overlapping buckets (e.g., each minute). The counter resets at the start of each bucket.

Example: max_requests = 100/min. Fixed window resets at :00 each minute.
- User sends 100 requests at 12:00:59 (end of window 1). All 100 allowed.
- Window resets at 12:01:00.
- User sends 100 more requests at 12:01:01 (start of window 2). All 100 allowed.
- In the span of 3 seconds (12:00:59 to 12:01:01), the user made 200 requests — twice the limit.

Sliding window avoids this because the window always covers exactly the last W seconds relative to the current timestamp. At 12:01:01, the window covers 12:00:01 to 12:01:01, capturing the 100 requests at 12:00:59 — the user is blocked.

Fixed window is still commonly used in production when the 2× burst is acceptable or when simplicity is valued (Nginx rate limiting uses fixed window by default).

---

## Card 2 — Deque for Sliding Window Log

**Q:** Why is a deque (collections.deque) the right data structure for the sliding window log approach? What makes a regular list inadequate?

**A:** The sliding window log algorithm does two things with the timestamp collection:
1. Appends new timestamps to the back (append).
2. Removes expired timestamps from the front (popleft).

Deque is O(1) for both append and popleft. These are the two operations we need.

A regular list's `pop(0)` (remove from front) is O(n) because it shifts all remaining elements leftward. If a user has N timestamps in the window and they all expire at once, cleanup with a list is O(N²) over all the calls it takes to clear them. With a deque, the same cleanup is O(N) total — each timestamp is popped exactly once.

In CPython, `collections.deque` is implemented as a doubly-linked list of fixed-size blocks, giving true O(1) head and tail operations.

---

## Card 3 — Memory Cost of the Sliding Window Log

**Q:** What is the memory cost of the sliding window log approach per user, and under what conditions is it too expensive?

**A:** The sliding window log stores every timestamp for each user that falls within the current window. Memory per user = O(N) where N = max_requests.

This is bounded by the rate limit: once a user hits max_requests, no more timestamps are appended (blocked requests are not recorded). So the worst case is exactly max_requests timestamps per user.

When is it too expensive:
- High rate limits with many users. Example: 10,000 requests/minute, 1M active users. Each user's deque holds up to 10,000 8-byte timestamps = 80KB. Total: 80KB × 1M = 80GB of RAM for timestamps alone.
- Contrast: sliding window counter with 60 second-buckets = 60 × 8 bytes = 480 bytes per user. More tractable.
- Real systems: Redis LRU eviction and persistence handle the memory problem. In-memory Python dicts do not scale to millions of users without sharding.

---

## Card 4 — Token Bucket vs Leaky Bucket vs Sliding Window

**Q:** Name the three most common rate limiting algorithms and explain the core behavioral difference between token bucket and leaky bucket.

**A:**

**Sliding window log / counter:** Counts requests in the last W seconds. What we implemented. Accurate and flexible.

**Token bucket:** A bucket fills with tokens at a steady rate (e.g., 10 tokens/second, max 60 tokens). Each request consumes one token. If the bucket is empty, the request is blocked.
- Key behavior: allows bursts up to bucket capacity, then enforces average rate.
- A user who has been idle for a minute can immediately make 60 requests (if bucket_max = 60).
- Used by: AWS API Gateway, Stripe.

**Leaky bucket:** Requests enter a queue (the bucket) and are processed at a fixed output rate. If the queue is full, requests are dropped.
- Key behavior: smooths out bursts — no matter how many requests arrive simultaneously, they exit at a steady rate.
- Burst unfriendly: the output rate is constant regardless of arrival pattern.
- Used by: network traffic shaping at the router level.

Key difference: token bucket ALLOWS bursts (up to bucket capacity). Leaky bucket ABSORBS and SMOOTHS bursts — requests exit at a constant rate, not the arrival rate.

---

## Card 5 — Distributed Rate Limiting with Redis

**Q:** How would you implement a sliding window log rate limiter across multiple servers using Redis? Name the specific Redis commands.

**A:** Use a Redis sorted set per user. Key = user_id, score = timestamp, member = a unique request ID (or the timestamp itself if uniqueness within the same second is not critical).

Algorithm for `is_allowed(user_id, timestamp)`:
```
ZREMRANGEBYSCORE user_id -inf (timestamp - window_seconds)  # remove expired
ZADD user_id timestamp timestamp                             # record this request  
ZCARD user_id                                               # count in-window
EXPIRE user_id window_seconds                               # auto-cleanup after inactivity
```

For atomicity, wrap in a Lua script (EVAL) rather than MULTI/EXEC, which has limitations in clustered Redis.

If ZCARD > max_requests: remove the just-added entry (ZREM) and return False.

Trade-off added by Redis: ~1ms network round-trip per request vs ~1µs in-memory. At 1M req/sec, unsharded Redis becomes the bottleneck. Mitigation: shard Redis by consistent hash of user_id, or use a local sliding window cache with periodic Redis sync (accepting small over-limit windows during sync delay).

---

## Card 6 — Two-Limit Composition: Check-Then-Record Pattern

**Q:** You need to enforce BOTH a 10 req/sec limit AND a 100 req/min limit. Describe the race condition in naive composition and how to fix it.

**A:** Naive composition (sequential):
```python
if per_second.is_allowed(user_id, ts) and per_minute.is_allowed(user_id, ts):
    return True
```

Race condition: `per_second.is_allowed` returns True AND records the request before `per_minute.is_allowed` returns False. The request ends up recorded in the per-second limiter but not in the per-minute limiter — state is inconsistent.

Fix — separate check and record steps:
```python
def check_only(limiter, user_id, ts):
    window = limiter.user_windows[user_id]
    while window and window[0] <= ts - limiter.window_seconds:
        window.popleft()
    return len(window) < limiter.max_requests

def record(limiter, user_id, ts):
    limiter.user_windows[user_id].append(ts)

# Composite check:
if check_only(per_second, user_id, ts) and check_only(per_minute, user_id, ts):
    record(per_second, user_id, ts)
    record(per_minute, user_id, ts)
    return True
return False
```

In practice: the minor inconsistency of the naive approach (one limiter records a request the other blocked) results in a slightly conservative rate limiter (users blocked slightly earlier), which is usually acceptable.

---

## Card 7 — Monotonic Timestamp Assumption

**Q:** The sliding window log implementation assumes timestamps are monotonically non-decreasing per user. What breaks if this assumption is violated?

**A:** The cleanup loop `while window and window[0] <= timestamp - window_seconds` relies on the deque being sorted. The loop pops from the front until it finds an entry inside the window, then stops — assuming everything behind that entry is also inside the window.

What breaks with out-of-order timestamps:
1. An expired timestamp could be buried in the middle of the deque. The cleanup loop would stop at the front entry (which is inside the window) without removing the buried expired entry.
2. The window count would be inflated — old requests that should have expired remain in the deque, making users appear to have used more of their limit than they actually have.

Fix: if out-of-order timestamps are possible, use a sorted structure (bisect.insort into a list, or a sortedcontainers.SortedList) instead of a deque. This increases per-request time from O(1) amortized to O(log N) per insert.

In practice: within a single server, system time is monotonically non-decreasing (time.time() never goes backward on a normally-operating clock). Cross-server clock skew is the main risk for distributed systems.

---

## Card 8 — Memory-Constrained Approximate Counting

**Q:** When the sliding window log is too memory-intensive, what are two memory-efficient approximate alternatives?

**A:**

**Sliding window counter (second-granularity buckets):**
Store one count per second-bucket for the window duration. For a 60-second window: 60 integers × 8 bytes = 480 bytes per user. When a request arrives at second T, increment the bucket for T. Expire buckets older than T - W. To get the window count, sum all non-expired buckets.

Accuracy: exact within 1-second granularity (requests within the same second are undifferentiated). For most rate limiters, 1-second precision is sufficient.

**Count-Min Sketch:**
A probabilistic data structure using multiple hash functions and a 2D array of counters. Answers "how many times has this user_id appeared?" in O(1) time and O(width × depth) space, with a bounded probability of over-counting (never under-counting — false positives only, not false negatives).

Use case: DDoS protection across millions of IPs where even O(1) per user is too much total memory. Trade-off: occasional legitimate users are blocked (false positive rate depends on sketch parameters).

For most interview answers: sliding window counter with second-granularity is the correct constrained-memory choice.

---

## Card 9 — Rate Limiters in Real Systems

**Q:** Name three real systems that use rate limiting and describe what each protects and which algorithm they use.

**A:**

**Nginx (ngx_http_limit_req_module):**
Protects web servers from request floods and brute-force login attempts. Uses a leaky bucket variant: requests are admitted at a steady rate; excess requests return 503. Config: `limit_req_zone $binary_remote_addr zone=one:10m rate=10r/s` limits per IP to 10 requests/second with a 10MB shared memory zone.

**Stripe API:**
Protects the payment processing API from runaway clients (SDK bugs, loops). Uses a token bucket per API key: an initial burst allowance that refills at a steady rate. Clients exceeding the limit receive HTTP 429 with a `Retry-After` header indicating when to retry. Implemented in Redis with Lua scripts for atomicity.

**AWS API Gateway:**
Per-stage and per-route throttling. Token bucket: burst limit (e.g., 5,000 requests — the bucket size) and rate limit (e.g., 10,000 requests/second — the refill rate). Exceeding either returns HTTP 429. Configured in the AWS console or via CloudFormation.

Common thread: all three use rate limiting as a denial-of-service mitigation, not as a business logic constraint. The algorithm choice (leaky vs token bucket vs sliding window) reflects the specific burst tolerance of the service.

---

## Card 10 — GCA Narration: State Tradeoffs Before Choosing

**Q:** When an interviewer gives you a design-a-DS problem with multiple valid approaches, what is the GCA-optimal narration structure before you start coding?

**A:** Use a three-part structure: (1) Name the approaches. (2) Compare them on the dimensions that matter for this specific problem. (3) Commit with rationale.

Example for Rate Limiter:

"I can see three approaches. Fixed window is O(1) time and O(1) space per user, but it allows up to 2× the limit at window boundaries — not acceptable for strict enforcement. Sliding window log is exact but uses O(N) memory per user and O(N) cleanup time in the worst case. Sliding window counter is O(1) time, O(W) memory per user, and approximately accurate.

Given that the problem says 'millions of requests per second' and 'optimize for speed,' I'll start with the sliding window log because it is exact and easy to reason about — then note that for production I would switch to the sliding window counter for memory efficiency. Implementing the log approach now."

This narration earns GCA points because it demonstrates: awareness of the full problem space, ability to reason about tradeoffs across time and memory, and commitment with explicit rationale rather than defaulting to the first approach that came to mind.

---

*10 cards · Google SWE Lab 02 · Rate Limiter Sliding Window Design · Review 24–48 hrs after completing workbook*
