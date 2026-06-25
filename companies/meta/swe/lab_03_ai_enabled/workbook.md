Status: Ready — work through all parts in order

# Meta SWE Lab 03 — AI-Enabled Coding Interview
## Harassment Detector with Sliding Window (Tier 2)

**Tier:** 2 | **Role:** SWE | **Est. time:** 60 min | **Difficulty:** Hard

**Before you start:** Set a timer for 60 minutes. This lab simulates the Meta AI-Enabled Coding Interview format (Oct 2025). You have access to an AI assistant (CoderPad with Claude Sonnet or GPT-4). The interviewer is NOT scoring your ability to use AI — they're scoring whether you DRIVE the solution and CATCH the AI's mistakes. An engineer who submits AI output without review will fail. An engineer who uses AI to accelerate work they fully understand will pass.

---

## Milestones

- [ ] M1 · Designed independently — sketched the algorithm BEFORE using AI
- [ ] M2 · AI prompted effectively — broke the problem into sub-tasks for AI
- [ ] M3 · AI mistakes caught — identified at least 2 issues in AI-generated code
- [ ] M4 · Integrated — your design + AI assistance = working final code
- [ ] M5 · Explained fully — can explain every line of the final solution (AI wrote or not)
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Part 0 — Forethought

**STOP. Do this BEFORE using AI assistance.**

*This step is non-negotiable. In the actual interview, the AI is available from minute 1. The engineers who fail are the ones who open the AI immediately. The engineers who pass design first.*

**Scenario:** Your Meta interviewer says:

> "Implement a function that, given a list of messages in a chat thread, detects whether any user is being harassed based on keyword frequency, message velocity, and sentiment patterns. The function should return flagged users and the evidence. You have 60 minutes, and you have access to an AI assistant. I'm interested in how you use it."

**Your design (fill in before moving to Part 1):**

**Function signature** [design this yourself]:

```python
def detect_harassment(
    [blank — parameters]
) -> [blank — return type]:
```

**The 3 sub-problems you'll ask AI to help with:**
1. [blank — e.g., "implement the sliding window for velocity detection"]
2. [blank — e.g., "implement keyword frequency counting per user across a window"]
3. [blank — e.g., "aggregate evidence per flagged user into the output format"]

**AI verification checklist** (what would a language model be likely to get wrong here?):
- [ ] [blank — e.g., "assumes messages are sorted by timestamp — may not check"]
- [ ] [blank — e.g., "sliding window off-by-one on window boundary inclusion"]
- [ ] [blank — e.g., "sentiment approach may use an unavailable library (TextBlob, NLTK)"]
- [ ] [blank — e.g., "doesn't handle empty messages list"]
- [ ] [blank — e.g., "doesn't handle unicode or special characters in messages"]

**Confidence rating before starting (circle one):** 1 — 2 — 3 — 4 — 5

**What I want to get right this session:** [blank]

---

## Part 1 — Clarifying Questions

*In an AI-enabled interview, clarifying questions are still required — and the AI doesn't ask them for you.*

**Q1 (Goal): "Should the function detect harassment of a SPECIFIC user (they're being targeted) or any user exhibiting harassing BEHAVIOR (they're doing the harassing)?"**

Rationale: A harassment DETECTOR by definition flags the harasser (the one sending harassing messages). But the problem says "detect whether any user IS BEING harassed" — suggesting the victim, not the perpetrator. In practice, you detect by analyzing the sender's behavior. Clarify which user gets flagged: the sender of harassing messages, or the receiver?

*Your assumption:* [blank]

**Q2 (Data): "Are the messages guaranteed to be sorted by timestamp? And can multiple users be harassing the same target simultaneously?"**

Rationale: Sliding window algorithms for velocity assume time-ordered input. Unsorted input requires a sort pass. Your AI assistant will almost certainly assume sorted input without checking — this is one of the bugs to look for.

*Your assumption:* [blank]

**Q3 (Constraints): "Are 'keywords' an exact match list (e.g., ['hate', 'die', 'idiot']), or is it fuzzy/stemmed matching?"**

Rationale: Exact match is O(k) per message where k is keyword count. Fuzzy match requires a different approach (Aho-Corasick, or embedding distance). In an interview, assume exact match unless told otherwise.

*Your assumption:* [blank]

**Q4 (Sentiment): "For sentiment — are we using a library (e.g., VADER, TextBlob) or implementing a keyword-based negative word ratio? What's available in the environment?"**

Rationale: This is a critical clarification for the AI. If the AI uses TextBlob and it's not available in the CoderPad environment, the code will error. In an AI-enabled interview, the correct approach is either: (a) implement a simple keyword-based negative sentiment proxy, or (b) abstract the sentiment function so it can be swapped in later.

*Your assumption:* [blank]

**Checkpoint M1:** Check the box once you've written all assumptions AND your Part 0 design BEFORE using any AI.

---

## Part 2 — Algorithm Design (No AI Yet)

*Design the algorithm yourself. The AI will help you implement it — not design it.*

**Entities:**

```
Message: {user_id: str, text: str, timestamp: float}

HarassmentSignal: {
    keyword_count: int,    # # of banned keywords in this message
    is_high_velocity: bool, # this message pushed velocity over threshold
    sentiment_score: float  # negative = more negative sentiment
}

HarassmentReport: {
    user_id: str,
    evidence: {
        keyword_hits: list[str],    # which keywords
        velocity_burst: float,       # messages/second in worst window
        sentiment_avg: float         # avg sentiment in window
    },
    confidence: float               # 0-1: how many signals fired
}
```

**Algorithm sketch (fill in — your design, not the AI's):**

```
For each message (in time order):
1. Update per-user state:
   - keyword_count[user]: scan text for banned keywords
   - message_window[user]: add timestamp to sliding window, remove timestamps
     older than window_seconds
   - sentiment_running[user]: compute sentiment proxy for this message,
     update per-user running average

2. Check thresholds:
   - if keyword_count[user] >= threshold.keyword_freq: [blank — what happens?]
   - if len(message_window[user]) >= threshold.velocity: [blank — what happens?]
   - if sentiment_running[user] <= threshold.sentiment: [blank — what happens?]

3. Build evidence:
   - Only flag a user if [blank — which threshold combination?]
   - Confidence score = [blank — how do you compute it?]

Return: list of HarassmentReport for flagged users
```

**Data structures:**
- Per-user keyword count: [blank — what structure?]
- Sliding window for velocity: [blank — deque? list? why?]
- Per-user sentiment state: [blank — rolling average approach?]

**Time complexity target:** O([blank]) — explain your reasoning.

**Checkpoint M2:** Check the box once the algorithm sketch is complete and you've chosen your data structures.

---

## Part 3 — Contract

```python
from collections import deque, defaultdict
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Message:
    user_id: str
    text: str
    timestamp: float  # Unix epoch seconds

@dataclass
class HarassmentEvidence:
    keyword_hits: list[str] = field(default_factory=list)
    max_velocity: float = 0.0      # messages per second in worst window
    avg_sentiment: float = 0.0     # negative = more negative

@dataclass
class HarassmentReport:
    user_id: str
    evidence: HarassmentEvidence
    confidence: float              # 0.0 to 1.0

def detect_harassment(
    messages: list[Message],
    window_seconds: int,
    keyword_list: list[str],
    thresholds: dict              # {keyword_freq: int, velocity: int, sentiment: float}
) -> list[HarassmentReport]:
    """
    Detects users exhibiting harassing behavior based on:
    - keyword_freq: minimum banned keyword count to flag
    - velocity: minimum messages in window_seconds to flag (message storm)
    - sentiment: maximum (most negative) sentiment score to flag

    Returns list of HarassmentReport for flagged users, sorted by confidence desc.
    Assumes messages are NOT necessarily sorted by timestamp.
    """
    pass
```

---

## Part 4 — AI Collaboration Exercise

*Now use your AI assistant. Give it the specific sub-tasks you identified in Part 0. Then review the output against your verification checklist.*

**Prompt 1 to AI (keyword frequency sub-problem):**

"I'm implementing a harassment detector. Here's the function signature and data classes: [paste from Part 3]. Please implement ONLY the keyword frequency component: given a message's text and a keyword_list, return a list of keywords found in the text. Use exact case-insensitive matching. The text may contain unicode characters. Handle the empty text case explicitly."

*After AI generates code, check:*
- [ ] Does it handle empty string input? [blank — yes/no and your fix if no]
- [ ] Does it do case-insensitive matching correctly? [blank — e.g., `.lower()` on both text and keyword]
- [ ] Does it handle unicode? (e.g., messages with emojis or accented characters) [blank]
- [ ] Any other issues? [blank]

---

**Prompt 2 to AI (sliding window velocity sub-problem):**

"Now implement the sliding window velocity check. Given: a deque of timestamps for one user (most recent at the right), a new timestamp, and window_seconds, update the deque and return the current message count within the window. Timestamps may arrive out of order — sort the deque after inserting. Handle the edge case where all timestamps in the deque are outside the window."

*After AI generates code, check:*
- [ ] Does the AI handle out-of-order timestamps? (Did your prompt ask for it — if so, does it implement it?) [blank]
- [ ] Is the window boundary inclusive or exclusive? (e.g., is a message exactly `window_seconds` old in or out of the window?) [blank — note the AI's choice and whether it matches your spec]
- [ ] Does the AI handle the empty deque case? [blank]
- [ ] Off-by-one: if window_seconds = 60 and two messages are 60 seconds apart, are both in the window? [blank]
- [ ] Any other issues? [blank]

---

**Prompt 3 to AI (evidence aggregation sub-problem):**

"Now implement the evidence aggregation: given a per-user dict of {user_id: {keyword_hits, velocity_deque, sentiment_sum, message_count}}, and the thresholds dict, return a list of HarassmentReport objects for users who exceed at least one threshold. Confidence score = (signals fired / total signals) where total signals = 3. Sort by confidence descending."

*After AI generates code, check:*
- [ ] Does the AI use floating point division correctly for confidence? (3 / 3 = 1.0, 1 / 3 ≈ 0.33) [blank]
- [ ] Does it handle a user with 0 messages (division by zero in sentiment avg)? [blank]
- [ ] Does it correctly compute average_sentiment from sum/count? [blank]
- [ ] Does it sort by confidence descending correctly? [blank]
- [ ] Any other issues? [blank]

**AI mistakes found and fixed:**

"I found the following issues in the AI's code and fixed them as follows:"

Issue 1: [blank — describe the bug]
Fix: [blank — describe what you changed]

Issue 2: [blank]
Fix: [blank]

Issue 3 (if found): [blank]
Fix: [blank]

**Checkpoint M3 + M4:** Check both boxes once you've reviewed all AI outputs, documented at least 2 issues, and integrated the components into a working solution.

---

## Part 5 — Final Implementation

*Write your final integrated solution here. Every line of code — whether you wrote it, the AI wrote it, or you modified the AI's output — must be explainable by you.*

```python
from collections import deque, defaultdict
from dataclasses import dataclass, field
from typing import Optional

# [Your complete implementation here — fill in after integration]
```

**"Can you explain every line?" self-check:**

Go through your implementation line by line and mark any line you cannot fully explain.

Lines I cannot fully explain: [blank — if any, this is where you study]

---

## Part 5b — Reasoning

**Time complexity of your final solution:**

Walk through: [blank — what is O(?) and why? Consider: n = number of messages, k = keyword_list size, u = number of unique users]

*Model analysis:*
- Sorting messages by timestamp: O(n log n) if needed (if messages are unsorted)
- Per message processing: O(k) for keyword scan + O(W) for window maintenance where W = max messages in window
- Total: O(n log n + n × k) — the keyword scan dominates if k is large
- Space: O(n) for storing per-user deques + O(u × W) for windows — where u = unique users

**What does your solution miss?**

[blank — be honest: false positives? False negatives? Edge cases?]

*Model:*
- **False positives:** A user who sends 10 messages quickly about a legitimate urgent topic (e.g., "help me," "please respond," "are you there") could be flagged for velocity. Velocity alone is a weak signal.
- **False negatives:** Sophisticated harassment that avoids the keyword list (e.g., coded language, abbreviations, misspellings like "h8te" instead of "hate") won't be caught by exact keyword matching.
- **Grouping assumption:** The function detects harassment based on messages in a single thread. A harasser who spams a user across multiple threads won't be detected unless the function is called with all cross-thread messages combined.

**How would you improve the sentiment detection beyond keyword counting?**

[blank — your answer]

*Model:* Replace the keyword-based negative word ratio with a fine-tuned BERT classifier trained on labeled harassment examples. This handles coded language, context-dependent negativity, and cross-language harassment. In an interview environment where libraries are constrained, abstract the sentiment function behind an interface so the keyword approach can be swapped for the model approach post-interview. The key is to design so that swapping the sentiment implementation doesn't require rewriting the core detection logic.

---

## Part 6 — Interview Simulation (Curveballs)

### Curveball 1 — Find the AI Bug

**Interviewer:** "The AI gave you code that passes all visible test cases but fails on an edge case you can spot. Here's the AI-generated sliding window code:"

```python
def update_velocity_window(timestamps: deque, new_ts: float, window_seconds: int) -> int:
    timestamps.append(new_ts)
    # Remove timestamps outside the window
    while timestamps and timestamps[0] < new_ts - window_seconds:
        timestamps.popleft()
    return len(timestamps)
```

**What's the bug?** [blank]

*The bug:* The boundary condition is `< new_ts - window_seconds` (strictly less than), which means a timestamp exactly `window_seconds` old IS included. Whether that's correct depends on the spec: if the window is "messages in the last 60 seconds," a message exactly 60 seconds old is ambiguous (is it "in the last 60 seconds" or has it been exactly 60 seconds?). More importantly: **the function assumes `timestamps` is already sorted.** If messages arrive out of order, `timestamps[0]` may not be the oldest. The correct approach: sort after appending, or use a sorted container.

**Your fix:** [blank]

---

### Curveball 2 — Explain Every Line

**Interviewer:** "Remove the AI and explain every line of your solution."

*This is where the interview is won or lost for AI-enabled format. Narrate your solution now, line by line, without looking at the AI-generated version.*

[blank — write your narration here. If you get stuck on a line, mark it and study it before the real interview.]

---

### Curveball 3 — Multi-Language Fairness

**Interviewer:** "How would you make this harassment detector fair across languages — specifically, for users sending messages in Spanish, Arabic, or Mandarin?"

**Your answer:** [blank]

*Things to address:*
- Keyword list approach is language-specific. A keyword list in English won't catch harassment in Spanish or Arabic. You'd need language-specific keyword lists.
- Language detection is a prerequisite: before applying the keyword list, detect the message language (using a library like `langdetect`, or a lightweight character n-gram classifier) and route to the appropriate keyword list.
- The sentiment model is also language-specific. A BERT model trained on English text doesn't generalize to Arabic without fine-tuning on Arabic data.
- Velocity detection is language-agnostic — it's based on timestamps, not text. This is the one signal that works equally across all languages.
- Fairness concern: if you only have English keyword lists and English sentiment models, the detector will systematically fail for non-English users — meaning harassment in Spanish goes undetected. This is a discriminatory outcome that should be addressed before wide deployment.
- Practical recommendation: MVP with English-only detection (clearly scoped), roadmap includes: (a) language detection, (b) multilingual keyword lists, (c) multilingual harassment classifier. Don't claim the MVP works for all languages if it doesn't.

---

## Part 7 — SWE Rubric (AI-Enabled)

*Self-grade after completing the lab. Score as a Meta AI-enabled interview panel would.*

| Dimension | 5 — Strong | 3 — Adequate | 1 — Weak | Your Score |
|---|---|---|---|---|
| Pre-AI design | Full algorithm sketched before AI assistance: function signature, data structures, sub-tasks, verification checklist | Partial design — sketch started but incomplete before first AI prompt | Went to AI immediately; no independent design phase | __ /5 |
| AI direction | Broke problem into 3 clear sub-tasks with specific constraints for AI (e.g., "handle empty input," "case-insensitive matching," "timestamps may be unsorted") | Used AI with general prompts ("implement keyword detection for harassment") | Single prompt: "Write a harassment detector" — gave AI the whole problem | __ /5 |
| AI error detection | Found 2+ AI mistakes, explained the mechanism (not just "this is wrong"), documented the fix | Found 1 mistake with explanation | Accepted all AI output uncritically; submitted without review | __ /5 |
| Code ownership | Narrated every line of the final solution — AI-written or not — without hesitation; could re-implement without AI if asked | Narrated most lines; 1-2 lines were opaque ("the AI wrote that part") | "The AI wrote that part" on multiple sections | __ /5 |
| Correctness | All visible test cases pass; sliding window boundary is correct; empty input handled; unicode handled | Core logic correct; 1 edge case missed (empty list or out-of-order timestamps) | Fails on empty input or timestamps; sliding window off by one | __ /5 |
| Communication | Narrated the AI interaction strategy aloud: "I'm asking AI to implement X because it's mechanical; I'm keeping the algorithm design to myself because that's what the interviewer is evaluating" | Some narration; clear about what AI helped with | Silent; interviewer couldn't tell what came from the candidate vs. the AI | __ /5 |
| Time management | Working, integrated solution with test cases in < 50 minutes | Working solution in 50-60 minutes | Ran out of time; AI was running when time expired; no integrated solution | __ /5 |

**Total: __ / 35**

---

## Reflection

**Which AI output had the most significant bug?** [blank]

**Which line of the final solution were you least confident explaining?** [blank]

**How long did you spend in the pre-AI design phase? Was it enough?** [blank]

---

## You're Ready When...

- You complete the full implementation (Parts 0–6) with working code in under 50 minutes
- You can narrate every line of the final solution without notes
- You find at least 2 AI bugs in the practice run before the real interview
- You answer Curveball 2 ("remove the AI and explain every line") without hesitation on more than 2 lines
- You self-grade ≥ 28/35 on two separate attempts

**Congratulations:** This is the final lab in the Meta SWE track.

---

*Meta SWE Lab 03 · Tier 2 · v1.0*
