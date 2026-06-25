# Google SWE Lab 02 — Design-a-Data-Structure
## Rate Limiter — Sliding Window Design (Tier 2 — Completion)

**Tier:** 2 (Completion) — The structure, comparison table, and model solution are provided. The key choices — which approach to use and why, what data structure tracks per-user requests, how to implement the sliding window logic — are left blank for you to fill in. You cannot pass this lab by copying; you have to supply the substance.

**Before you start:** Set a timer for 45 minutes. Write all code in a plain text area. No IDE. Narrate out loud.

**Prerequisite:** You should have completed Lab 01 (LRU Cache) before this lab. The modeling-before-coding habit from Lab 01 applies here too. This lab adds a new skill: comparing multiple approaches and choosing one with explicit reasoning.

---

## Milestones

- [ ] M1 · Clarified — asked about window type (fixed vs sliding), per-user vs global, thread safety, memory budget
- [ ] M2 · Compared — named at least 2 approaches (fixed window, sliding window log, sliding window counter) with tradeoffs
- [ ] M3 · Chosen — selected sliding window counter or log with rationale
- [ ] M4 · Coded — `is_allowed(user_id, timestamp)` working with all 5 edge cases
- [ ] M5 · Extended — described how to support two simultaneous rate limits (e.g., 10/sec AND 100/min)
- [ ] M6 · Ready — self-graded ≥ 28/35 on two separate attempts

---

## Part 0 — Forethought

**Goal:** Design a rate limiter that correctly enforces N requests per W seconds per user. Understand three distinct approaches, choose one explicitly, implement it, and reason about its limits. The interviewer is testing whether you can model a time-based system, not whether you know a formula.

**Target time:** 45 minutes total. Suggested breakdown:
- 5 min — clarifying questions (Part 1)
- 8 min — three-approach comparison (Part 2)
- 3 min — contract (Part 3)
- 15 min — implementation + tests (Part 4)
- 7 min — system reasoning (Part 5)
- 7 min — curveballs (Part 6)

**Your approach choice (fill in before Part 4):**

I will implement: [ ] Fixed window  [ ] Sliding window log  [ ] Sliding window counter

My reason (one sentence): [blank — commit before coding]

**Confidence rating before starting (circle one):** 1 — 2 — 3 — 4 — 5

**What I want to get right this session:** [blank]

---

## Part 1 — Clarifying Questions

*The scenario: You're in a Google phone screen, plain Google Doc. The interviewer says:*

> "Design a rate limiter that allows at most N requests per window of W seconds per user_id. If the limit is exceeded, return False. Otherwise record the request and return True. It will be called millions of times per second. Optimize for speed."

*Ask your questions before designing.*

**Q1: Is the window fixed (e.g., 12:00:00–12:00:59) or sliding (e.g., "the last 60 seconds from now")?**
Assumption: [blank — the answer changes your entire approach. Sliding window is more accurate but harder to implement.]

**Q2: Is rate limiting per user, per IP, or global?**
Assumption: [blank — per user_id, as stated. But confirm: is user_id a string or integer?]

**Q3: Is thread safety required?**
Assumption: [blank — in a multi-threaded server, concurrent requests for the same user_id could race on shared state.]

**Q4: What is the memory budget per user?**
Assumption: [blank — this determines whether you can store every timestamp (log approach) or must use approximate counting.]

**Q5: Are timestamps guaranteed to be monotonically increasing per user?**
Assumption: [blank — if yes, you can use deque and only pop from the front. If not, you need a sorted structure.]

**Q6: What happens to users who have no requests in the window — do they expire from memory?**
Assumption: [blank — relevant for memory management in long-running systems. For this lab, assume inactive users stay in the dict.]

**Checkpoint M1:** Check the box above if you asked at least 3 of these before proceeding to Part 2.

---

## Part 2 — Decomposition: Three Approaches

*This is Tier 2 — fill in the blank cells in the comparison table. Understanding all three approaches is the learning goal.*

### The Core Problem

A rate limiter answers the question: "How many of this user's requests have arrived in the last W seconds?" and blocks the request if the count exceeds N.

The challenge: you need this count in O(1) or O(log N) per request, across potentially millions of users.

### Approach Comparison Table

Fill in the cells marked [blank]:

| Approach | Memory per user | Accuracy | Time per request | When to use |
|---|---|---|---|---|
| **Fixed window** | O(1) — one counter + one window-start timestamp | Can allow up to 2× the limit at window boundaries (burst problem) | O(1) | [blank — when is 2× burst acceptable?] |
| **Sliding window log** | O(N) per user — stores every timestamp in the window | [blank — perfect or approximate?] | O(N) per request (cleanup pass) | [blank — when is exact correctness worth the memory cost?] |
| **Sliding window counter** | O(W) per user — stores one counter per second-bucket in the window | [blank — exact or approximate? Why?] | O(1) amortized | [blank — best general-purpose choice? Why?] |

*Model answers (read after filling in your own):*

- Fixed window / When to use: When requests are bursty in a pattern that aligns with your window boundaries — e.g., batch jobs that run at the top of the minute. Also acceptable when a 2× burst at the boundary is tolerable (many rate limiters in practice use this).
- Sliding window log / Accuracy: Perfect — stores every timestamp so the count is exact for any window position. No approximation error.
- Sliding window log / When to use: When exact accuracy is critical and N is small (e.g., N ≤ 1000 requests/min for a financial API where exact enforcement matters more than memory).
- Sliding window counter / Accuracy: Approximate — uses a weighted average of two fixed windows to estimate the count over the sliding window. Error is small in practice (< 1%) but technically not exact.
- Sliding window counter / When to use: Best default for most systems. O(1) time, O(W) memory per user (bounded by window size, not request count), and the approximation error is negligible for most rate-limiting use cases.

### The Sliding Window Log Approach (Used in Part 4)

**Data structure per user:** a deque of timestamps, in ascending order.

**Algorithm for `is_allowed(user_id, timestamp)`:**
1. Get or create the deque for this user.
2. Remove all timestamps from the front of the deque that are older than `timestamp - window_seconds` (they are outside the window).
3. If `len(deque) < max_requests`: append `timestamp` and return True.
4. Else: the window is full. Return False (do NOT append).

**Why deque and not a list?**
[blank — fill in your answer before reading below]

*Model answer:* Deque gives O(1) append to the back and O(1) pop from the front. A list's `pop(0)` is O(N) because it shifts all elements. The cleanup step in step 2 pops from the front, so a list would make cleanup O(N²) in the worst case.

**Why timestamps are stored (not just a counter)?**
[blank — fill in your answer]

*Model answer:* A counter alone cannot tell you which requests are still inside the window. When W seconds pass, you need to remove requests that are now outside the window. Without timestamps, you cannot identify which requests to remove.

**Checkpoint M2:** Check the box above if you filled in all table cells and answered the two sub-questions above.

---

## Part 3 — Contract

*The class interface you are implementing:*

```python
class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        # [blank — what data structure do you use to track per-user requests?]
        # Hint: you need one structure per user; you do not know users in advance.
        pass
    
    def is_allowed(self, user_id: str, timestamp: int) -> bool:
        # timestamp is an integer (seconds, monotonically increasing per user)
        # Returns True if the request is within the rate limit and records it.
        # Returns False if the limit is exceeded (request is NOT recorded).
        # [blank — implement sliding window logic here]
        pass
```

**Preconditions:**
- `max_requests` ≥ 1. `window_seconds` ≥ 1.
- `timestamp` values for a given `user_id` are monotonically non-decreasing.
- `user_id` is a string (or any hashable type).

**Postconditions:**
- If `is_allowed` returns True: the request at `timestamp` has been recorded and counts toward future rate limit checks.
- If `is_allowed` returns False: the request was NOT recorded. The state is unchanged.
- Calls across different `user_id` values are independent.

**Edge cases you must handle:**
- First request ever from a user → always True (window is empty).
- Two requests at exactly the same timestamp → both count separately.
- Exactly `max_requests` in the window → allow the next one (the window is not yet full).
- `max_requests + 1` in the window → block the next one.
- A burst of requests all at timestamp 0 followed by requests at timestamp W → requests at timestamp W are inside a fresh window (the old ones have expired).

---

## Part 4 — Code

*Fill in the blank implementation below. Write the complete class. Do not skip any edge case.*

### Your Implementation

```python
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        # [blank — initialize your per-user tracking structure]
        pass
    
    def is_allowed(self, user_id: str, timestamp: int) -> bool:
        # [blank — implement the sliding window log algorithm]
        # Step 1: Get the deque for this user
        # Step 2: Remove expired timestamps (older than timestamp - window_seconds)
        # Step 3: Check if under limit; if yes, record and return True; else return False
        pass
```

### Model Solution (Read AFTER your implementation)

```python
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.user_windows = defaultdict(deque)  # user_id -> deque of timestamps
    
    def is_allowed(self, user_id: str, timestamp: int) -> bool:
        window = self.user_windows[user_id]
        
        # Remove timestamps outside the sliding window
        # A timestamp t is outside the window if t <= timestamp - window_seconds
        # (i.e., it happened more than window_seconds seconds before now)
        while window and window[0] <= timestamp - self.window_seconds:
            window.popleft()
        
        if len(window) < self.max_requests:
            window.append(timestamp)
            return True
        return False
```

**Annotations:**

- `defaultdict(deque)` — creates a new empty deque automatically for any new user_id. Avoids an `if user_id not in self.user_windows` check.
- `window[0] <= timestamp - self.window_seconds` — this is the boundary condition. If the oldest timestamp is AT MOST `window_seconds` seconds before now, it is outside the window. If it is strictly LESS than `window_seconds` ago, it is also outside. The `<=` handles the boundary correctly: a request at `t - W` is exactly at the boundary and counts as expired.
- The while loop pops from the front until all expired entries are removed. Because timestamps are monotonically increasing, once `window[0]` is inside the window, all subsequent entries are too.
- We check `len(window) < self.max_requests` AFTER cleanup, so the count reflects only valid in-window requests.
- False case does NOT append — the blocked request is not recorded.

---

### Test Cases (Trace Through Manually)

**Test 1:** Basic allow/block
```
rl = RateLimiter(max_requests=2, window_seconds=10)
rl.is_allowed("user1", 1)   # True  — window: [1]
rl.is_allowed("user1", 2)   # True  — window: [1, 2]
rl.is_allowed("user1", 3)   # False — window: [1, 2], count=2, blocked
rl.is_allowed("user1", 11)  # True  — timestamp 1 expires (1 <= 11-10=1); window: [2, 11]
rl.is_allowed("user1", 12)  # False — window: [2, 11], count=2 (2 > 12-10=2 is False, so 2 stays); blocked
```

Wait — trace more carefully for Test 1 step 5:
- timestamp=12, window_seconds=10. Expiry threshold = 12 - 10 = 2. window[0]=2. Is 2 <= 2? Yes — pop. window: [11]. Is window empty? Yes, stop. len(window)=1 < 2. Append 12. Return True. window: [11, 12].

Corrected Test 1:
```
rl.is_allowed("user1", 12)  # True  — timestamp 2 expires; window: [11, 12]
rl.is_allowed("user1", 13)  # False — window: [11, 12], count=2, blocked
```

Trace: [blank — work through these step by step]

**Test 2:** Different users are independent
```
rl = RateLimiter(max_requests=1, window_seconds=5)
rl.is_allowed("alice", 1)   # True
rl.is_allowed("bob", 1)     # True  — bob's window is separate
rl.is_allowed("alice", 2)   # False — alice's window: [1], count=1
rl.is_allowed("bob", 2)     # False — bob's window: [1], count=1
```

Trace: [blank]

**Test 3:** Boundary — same timestamp
```
rl = RateLimiter(max_requests=3, window_seconds=10)
rl.is_allowed("user1", 5)   # True  — window: [5]
rl.is_allowed("user1", 5)   # True  — window: [5, 5]
rl.is_allowed("user1", 5)   # True  — window: [5, 5, 5]
rl.is_allowed("user1", 5)   # False — count=3, blocked
```

Trace: [blank]

**Test 4:** Window expiry — full fresh window
```
rl = RateLimiter(max_requests=2, window_seconds=60)
rl.is_allowed("user1", 0)   # True  — window: [0]
rl.is_allowed("user1", 30)  # True  — window: [0, 30]
rl.is_allowed("user1", 59)  # False — both 0 and 30 are still inside (0 > 59-60=-1)
rl.is_allowed("user1", 60)  # True  — 0 expires (0 <= 60-60=0); window: [30, 60]
```

Trace: [blank]

**Test 5:** First request from a new user
```
rl = RateLimiter(max_requests=5, window_seconds=60)
rl.is_allowed("newuser", 100)   # True — empty deque created automatically
rl.is_allowed("newuser", 200)   # True
```

Trace: [blank]

**Checkpoint M4:** Check the box at the top when you have traced all 5 tests and understand each step.

---

## Part 5 — System Reasoning

*Answer these in writing before looking at the model answers.*

**Q1: What is the time complexity of `is_allowed` and why is it O(1) amortized?**
[blank]

*Model answer:* In the worst case, a single call to `is_allowed` pops O(N) entries from the deque (if N entries just expired). But each timestamp is appended once and removed at most once. Across all calls for a user, total pops ≤ total appends. Amortized over all calls: O(1) per call. In the common case (few expirations per call), it is O(1) in the actual sense too.

**Q2: What is the space complexity per user?**
[blank]

*Model answer:* O(N) per user, where N = max_requests. The deque holds at most `max_requests` timestamps (once the limit is reached, new blocked requests are not appended). Total space across all users: O(users × max_requests).

**Q3: Why does the fixed window approach allow up to 2× the rate limit at a boundary?**
[blank]

*Model answer:* Consider max_requests=100, window_seconds=60, with a fixed window per minute. A user sends 100 requests at second 59 (end of window 1). The window resets at second 60. They send 100 more requests at second 61 (start of window 2). Both sets are within their respective fixed windows. But in the span of 3 seconds (59–61), the user made 200 requests — twice the limit. A sliding window would catch this; a fixed window does not.

**Q4: How does your sliding window log handle the case where `max_requests` changes dynamically?**
[blank]

*Model answer:* It handles it transparently. The deque stores raw timestamps; the limit is read from `self.max_requests` at call time. Changing `self.max_requests` between calls immediately takes effect on the next `is_allowed` check without any state migration. Fixed-window counters must be reset when the limit changes, since the counter itself encodes the limit.

**Q5: If this rate limiter runs on a single machine, what is the failure mode when the machine crashes?**
[blank]

*Model answer:* All in-memory state (the `user_windows` dict) is lost. After restart, every user's request history is empty. Users who were rate-limited just before the crash can immediately make max_requests new requests. For most rate limiters, this is an acceptable trade-off — brief leniency after a restart. For strict enforcement, persist state to Redis or another external store before responding.

**Checkpoint M5 (Extended):** Describe how you would support TWO rate limits simultaneously: 10 requests per second AND 100 requests per minute.

[blank — your design]

*Model answer:* Compose two `RateLimiter` instances:
```python
class MultiRateLimiter:
    def __init__(self):
        self.per_second = RateLimiter(10, 1)
        self.per_minute = RateLimiter(100, 60)
    
    def is_allowed(self, user_id: str, timestamp: int) -> bool:
        # Both limits must pass; neither records if the other blocks
        # Problem: if per_second passes but per_minute blocks, per_second has already recorded
        # Solution: check both before recording either
        ...
```

The naive composition has a race condition: `per_second.is_allowed` may record the request before `per_minute.is_allowed` rejects it. Fix: separate the "check" and "record" steps, or always check both before recording either. Alternatively, accept the small inconsistency (one limiter may have recorded a request that the other rejected) — in practice, this is tolerable since the request is ultimately blocked.

---

## Part 6 — Curveballs

### Curveball 1 — Memory Constrained

**Interviewer:** "Memory is constrained — you have 1KB per user. With a 60-second window and up to 1000 requests, the deque is too large. What do you do?"

**Your answer:** [blank]

*Things to address:*
- 1000 timestamps × 8 bytes each = 8KB per user. Over budget.
- Option 1: Fixed window counter — O(1) per user, but 2× burst problem. Acceptable if the use case tolerates it.
- Option 2: Sliding window counter — store one counter per second bucket. 60 buckets × 8 bytes = 480 bytes per user. Within budget and more accurate than fixed window.
- Option 3: Approximate counting (Count-Min Sketch) — probabilistic, sublinear memory, some false positives (may rate-limit legitimate users). Use for extremely tight memory budgets.
- The right answer here: sliding window counter with second-granularity buckets. Approximately accurate, memory-bounded at O(W) not O(N).

---

### Curveball 2 — Distributed Rate Limiting

**Interviewer:** "Multiple servers run this rate limiter. A user's requests could hit any server. How do you make it distributed?"

**Your answer:** [blank]

*Things to address:*
- The in-memory approach breaks in distributed setting: each server has its own `user_windows` dict. A user can make max_requests on each server without triggering any single limiter.
- Solution: use Redis as shared state. Redis supports atomic increment (INCR), expiring keys (EXPIRE), and sorted sets (ZADD/ZRANGEBYSCORE for the sliding window log).
- Sliding window log in Redis: use a sorted set (key = user_id, score = timestamp). On each request: ZADD to add the timestamp, ZREMRANGEBYSCORE to remove expired entries, ZCARD to count — all in one Lua script for atomicity.
- Trade-off: Redis adds network latency (~1ms) per rate limit check vs in-memory (~1µs). At millions of requests/second, Redis becomes a bottleneck. Mitigation: shard Redis by user_id, or use a local cache with periodic sync to Redis.

---

### Curveball 3 — Two Simultaneous Limits

**Interviewer:** "You need to support TWO limits: 10 req/sec AND 100 req/min. How do you extend the class?"

**Your answer:** [blank]

*Things to address:*
- Simplest: compose two `RateLimiter` instances (per-second and per-minute). A request is allowed only if BOTH return True.
- Problem: if you call `is_allowed` on each sequentially, the first may record the request before the second blocks it.
- Fix: in `is_allowed`, first do a "check only" pass on both limiters, then "record" on both if both pass. This requires splitting the check and record steps.
- Alternative: accept the minor inconsistency and accept that one limiter may occasionally record a blocked request. In practice, this leads to a slightly conservative limiter (users may be blocked slightly earlier than the strict limit), which is usually acceptable.

---

## Part 7 — SWE Rubric

*Self-grade after completing the lab.*

| Dimension | 5 — Strong | 3 — Adequate | 1 — Weak | Your Score |
|---|---|---|---|---|
| Communication / think-aloud | Named all three approaches before coding; stated the choice and reason; narrated the cleanup loop logic out loud | Coded after naming one approach; some narration | Jumped straight to code; no comparison; interviewer cannot follow reasoning | __ /5 |
| Design / approach comparison | Filled in all table cells correctly; explained why deque beats list for cleanup; explained sliding window log vs counter tradeoff | Filled in most cells; one major gap (e.g., why deque) | Could not compare approaches; did not know difference between fixed and sliding window | __ /5 |
| Correctness | All 5 test cases pass; correct boundary condition (<=, not <) in cleanup; blocked requests not recorded | 3-4 tests pass; off-by-one error in boundary condition or blocks-record-anyway bug | Fails basic allow/block test; cleanup loop incorrect | __ /5 |
| System reasoning (Part 5) | Answered all 5 questions correctly; correctly explained amortized O(1); described 2× burst in fixed window | Answered 3-4 questions; one wrong or missing (e.g., fixed window burst not explained correctly) | Could not explain amortized complexity; did not know fixed window burst problem | __ /5 |
| Extension (M5) | Described two-limiter composition with correct identification of the race condition between check and record | Described composition but missed the race condition | Could not extend to two simultaneous limits | __ /5 |
| Curveballs | Handled all 3 curveballs with specific, correct answers; named Redis ZADD for distributed case | Handled 1-2 curveballs; generic or incomplete | Could not reason about memory constraints or distributed limits | __ /5 |
| Time management | Completed Part 4 and Part 5 within 45 minutes; curveballs in remaining time | Completed Part 4 but rushed on Part 5 | Did not finish implementation within time | __ /5 |

**Total: __ / 35**

---

## You're Ready When...

- You implement `is_allowed` from scratch in under 10 minutes without hints
- You trace Test 1 correctly step by step without running code
- You explain the 2× burst problem in the fixed window approach without hesitation
- You answer Curveball 2 (distributed rate limiting) with specific mention of Redis ZADD
- You self-grade ≥ 28/35 on two separate attempts

**Next lab:** [→ Lab 03: Mock Phone Screen](../lab_03_mock_screen/workbook.md)

---

*Google SWE Lab 02 · Tier 2 (Completion) · Design-a-Data-Structure · v2.0*
