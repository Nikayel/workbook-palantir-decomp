# Flashcards — Meta SWE Lab 03: AI-Enabled Coding

*8 cards for spaced repetition. Study 24–48 hours after completing the workbook.*

---

## Card 1 — Meta AI-Enabled Interview Format (Oct 2025)

**Q:** Describe the Meta AI-Enabled Coding Interview format as of late 2025. What is the interviewer specifically scoring?

**A:** Format: 60 minutes in CoderPad with access to an AI assistant (typically Claude Sonnet or GPT-4). One complex problem requiring multiple algorithmic components. The interviewer watches you interact with AI in real time.

**What the interviewer scores:**
1. **Do you design before using AI?** Engineers who open AI immediately fail. Engineers who sketch the algorithm independently first — then use AI for mechanical implementation — pass.
2. **Do you give the AI useful, scoped prompts?** "Write a harassment detector" fails. "Implement only the sliding window velocity component, assuming timestamps may arrive out of order; handle the empty deque case explicitly" passes.
3. **Do you catch AI mistakes?** AI commonly: assumes sorted input, misses edge cases (empty input, unicode, off-by-one on window boundaries), uses unavailable libraries. The interviewer expects you to find at least one bug.
4. **Do you own every line?** "The AI wrote that part" is a disqualifying answer. Every line in the final submission must be explainable by the candidate.

**What the interviewer does NOT score:** How many AI prompts you used, whether you used the AI at all, or whether your final code matches the AI's first output.

---

## Card 2 — What Interviewers Score (Driving vs. Pure Prompting)

**Q:** What is the difference between "driving the solution" and "pure prompting" in an AI-enabled interview? Why does only the first one pass?

**A:**
**Pure prompting (fails):**
- Gives AI the complete problem statement: "Write a harassment detector that takes messages and returns flagged users based on keyword frequency, velocity, and sentiment."
- Accepts AI output without review
- Submits the AI's code as-is
- Can't explain lines the AI wrote
- Result: The interviewer sees a code-paste engineer, not a problem-solver. The AI could fail silently (wrong boundary conditions, missing edge cases) and the candidate wouldn't know.

**Driving the solution (passes):**
- Designs the algorithm independently: sketches entities, data structures, sub-problems, and algorithm flow before touching AI
- Decomposes the problem into scoped sub-tasks for AI
- Reviews every AI output against a pre-written checklist
- Integrates AI components into the human-designed architecture
- Can narrate every line, AI-written or not
- Result: The interviewer sees an experienced engineer using AI as a power tool — amplifying speed without losing ownership.

The meta-point: AI-enabled interviews test engineering judgment, not AI skill. The AI is the tool; you are the engineer.

---

## Card 3 — Sliding Window for Velocity Detection

**Q:** Implement the sliding window velocity check: given a deque of message timestamps for one user, a new timestamp, and window_seconds, return the message count within the window.

**A:**
```python
from collections import deque

def update_velocity_window(
    timestamps: deque,
    new_ts: float,
    window_seconds: int
) -> int:
    """
    Adds new_ts to the window and removes timestamps outside the window.
    Handles out-of-order timestamps by sorting after insert.
    Window is inclusive: timestamp >= new_ts - window_seconds is IN the window.
    Returns current count of messages in the window.
    """
    timestamps.append(new_ts)

    # Handle out-of-order timestamps
    # Convert to sorted list, update deque
    sorted_ts = sorted(timestamps)
    timestamps.clear()
    timestamps.extend(sorted_ts)

    # Remove timestamps outside the window (older than window_seconds)
    cutoff = new_ts - window_seconds
    while timestamps and timestamps[0] < cutoff:
        timestamps.popleft()

    return len(timestamps)
```

**Common AI bugs in this function:**
1. Missing sort (assumes input is already ordered)
2. Wrong boundary: `<` vs `<=` on the cutoff check — determines whether a message exactly `window_seconds` old is included
3. Not handling empty deque before `timestamps[0]` access
4. Using `timestamps[0]` after modifying the deque in the same loop iteration

---

## Card 4 — Common AI Code Errors (What to Look For)

**Q:** Name 5 common mistakes that AI code generators make when implementing algorithmic problems. Give a concrete example of each.

**A:**
1. **Assumes sorted input:** AI often writes `while queue and queue[0] < cutoff` assuming the earliest element is at index 0. If messages arrive out of order (a realistic scenario), this silently fails by expiring the wrong timestamps.

2. **Off-by-one on window boundaries:** AI frequently uses `< cutoff` when the spec means `<= cutoff` or vice versa. Whether the boundary is inclusive or exclusive changes which messages get counted — subtle and easy to miss in test cases that don't test the boundary exactly.

3. **Unavailable library imports:** AI commonly imports `textblob`, `nltk`, `spacy`, or `transformers` for sentiment analysis without knowing the interview environment's available packages. These will cause `ImportError` at runtime.

4. **Missing empty input guard:** AI often skips `if not messages: return []` at the function entry, causing `IndexError` or `ZeroDivisionError` when the list is empty.

5. **Wrong complexity class:** AI sometimes generates O(n²) solutions for problems that have O(n log n) or O(n) solutions — e.g., re-scanning all previous messages on each new message instead of maintaining a running state.

---

## Card 5 — Pre-AI Design Discipline

**Q:** What are the 4 elements of the pre-AI design phase? Why does each one matter?

**A:**
1. **Function signature:** Forces you to define the interface before implementation. You decide: what are the inputs, what are the outputs, what are the types? This prevents designing a function that the AI misunderstands because the interface was implicit.

2. **Sub-problem decomposition:** Identify the 3-4 independent algorithmic components (e.g., keyword scan, sliding window, sentiment aggregation, evidence collection). Each sub-problem gets its own AI prompt. This forces you to think about the architecture before the AI influences it.

3. **Data structure selection:** Decide: what data structures does each sub-problem require? (deque for sliding window; defaultdict for per-user state; Counter for keyword frequency.) Choosing data structures before AI involvement means you'll recognize if the AI uses a worse structure.

4. **AI verification checklist:** Write down what bugs you'll check for before seeing any AI output. If you write the checklist before the AI generates code, you'll find bugs you'd miss if you reviewed the code cold. The checklist items should match the hardest edge cases: empty input, out-of-order data, boundary conditions, unavailable libraries.

Why each matters: The pre-AI design phase is the only part of the AI-enabled interview where you're purely being evaluated as an engineer. The AI can't do this for you without turning the interview into a pure prompting exercise.

---

## Card 6 — "Can You Explain Every Line" Ownership Test

**Q:** An interviewer says "the AI is gone now — explain every line of your solution." What does this reveal about the candidate, and how do you prepare for it?

**A:** This question is the AI-enabled interview's equivalent of "now code it from memory" in a traditional interview. It reveals:

- **Real ownership:** If the candidate designed the algorithm before using AI, they can explain the structure from memory because it's their structure. The AI only implemented sub-tasks within that structure.
- **Understanding vs. pasting:** A candidate who accepted AI output without review can't explain the control flow of the AI's implementation. They can read it, but they can't reason about it.

**How to prepare:**
1. After integrating AI components, read the final code line by line and ensure you can explain each one before submitting.
2. Re-implement the sliding window and keyword scan from memory (without AI) in your preparation. If you can implement it from memory, you own it.
3. For any AI-generated helper function, ask yourself: "If this function had a subtle off-by-one, would I catch it?" If no, you don't own that code yet.

The preparation that makes this question easy: design the algorithm yourself, use AI only for the mechanical implementation of sub-tasks you already know how to implement, and review every line before integrating.

---

## Card 7 — Harassment Detection: False Positive Costs

**Q:** A harassment detector flags a user incorrectly (false positive). What are the real-world costs of a false positive in a consumer platform context?

**A:** False positive costs in harassment detection:

1. **User harm (to the incorrectly flagged user):** Account suspension, content removal, or warning messages for a user who did nothing wrong. This is a direct harm to a real person. In severe cases (wrongful permanent ban), it destroys their online social graph, which can have significant personal and professional consequences.

2. **Trust erosion:** Users who are falsely flagged — and their friends who see their account restricted — lose trust in the platform's fairness. At scale, a high false positive rate creates a narrative ("the system flags innocent people") that undermines trust in legitimate enforcement actions.

3. **Moderation overload:** If false positives are high, human moderators spend time reviewing flagged cases that turn out to be clean, wasting capacity that should be spent on real harassment.

4. **Chilling effect:** If users believe they might be falsely flagged, they may self-censor legitimate speech — a structural harm to the platform's value as a communication medium.

**Design implication:** Harassment detection systems at consumer platforms are typically designed with high recall (catch most real harassment) but lower precision (some false positives), with the balance adjusted based on: the severity of the enforcement action (a warning has a lower cost than a permanent ban), the strength of the evidence (single signal vs. multiple signals), and whether there's human review in the loop.

---

## Card 8 — Multi-Language NLP Challenges

**Q:** A harassment detector is deployed globally. What are the 3 main challenges in extending it to non-English languages, and what is the correct engineering approach for each?

**A:**
**Challenge 1 — Keyword list coverage:**
English keyword lists don't apply to Spanish, Arabic, Mandarin, etc. Maintaining 100+ language-specific lists is operationally expensive and never fully up-to-date with slang, coded language, or neologisms.
*Engineering approach:* Use multilingual embeddings (mBERT, XLM-RoBERTa) trained on harassment data across languages. The model learns cross-lingual patterns rather than relying on language-specific keyword lists.

**Challenge 2 — Language detection:**
Before applying language-specific signals, you must detect the message language. Misdetection (classifying a Spanish message as Portuguese) routes to the wrong model.
*Engineering approach:* Use a fast, accurate language classifier (e.g., fastText's `lid.176.bin`, which handles 176 languages in < 1ms) as a routing layer before the harassment detector.

**Challenge 3 — Training data imbalance:**
Most labeled harassment data is in English. Models fine-tuned primarily on English data exhibit significantly worse performance on lower-resource languages — meaning harassment in Arabic or Swahili is less likely to be detected.
*Engineering approach:* Zero-shot cross-lingual transfer from multilingual base models, combined with targeted data collection programs for lower-resource languages (paid annotation programs for labeled harassment examples in target languages). Track precision/recall by language in production metrics — if a language shows significantly worse recall, it becomes a data collection priority.

---

*8 cards · Meta SWE Lab 03 · Review 24–48 hrs after completing workbook*
