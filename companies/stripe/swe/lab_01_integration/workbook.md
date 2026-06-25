Status: Ready — work through all parts in order

# Lab 01 · Integration Lab — Process Refund
**Stripe SWE · Tier 1→2 · ~75 minutes**

---

## 🪜 Milestones

- [ ] M1 · Read the codebase — understood the `PaymentProcessor` structure before writing any code
- [ ] M2 · Read the API docs — understood the refund endpoint contract, status codes, and body shape
- [ ] M3 · Implemented — `process_refund()` written and integrated into the existing class
- [ ] M4 · Tested — tested full refund, partial refund, invalid `charge_id`, amount = 0
- [ ] M5 · Production-quality — error handling, logging, clean code with no hacks
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Scenario

You're in a **Stripe integration round**. The interviewer drops you into an unfamiliar payment processing repository and says:

> "The `PaymentProcessor` class processes charges but doesn't support refunds yet. The API you need to call is documented below. Ship a working `process_refund(charge_id, amount_cents)` method that:
> - Calls the Stripe-style API to issue the refund
> - Handles partial refunds (refund less than the full charge)
> - Writes the result to the transaction log
>
> You have 45 minutes. Internet access: YES. AI assistants: NO. Make it production-quality."

**Real Stripe integration round constraint:** Read ALL the existing code before writing a single line. Stripe interviewers watch whether you read first. Writing before reading is a signal of recklessness — not urgency.

---

## Mock API Documentation

Study this before writing any code. Treat it as you would real Stripe docs.

```
# Refund API (Stripe-style mock)

## Create a Refund

POST /v1/refunds
Authorization: Bearer {API_KEY}

Request Body (application/json):
  charge   (string, required)  — The charge ID to refund. Example: "ch_xxx"
  amount   (int, optional)     — Amount in cents to refund. Omit for full refund.

Response 200 — Success:
  {
    "id": "re_xxx",
    "amount": 500,
    "status": "succeeded",
    "charge": "ch_xxx"
  }

Response 400 — Bad Request (invalid parameters):
  {
    "error": {
      "type": "invalid_request_error",
      "message": "No such charge: 'ch_xxx'"
    }
  }

Response 402 — Card Error (e.g., refund exceeds original charge):
  {
    "error": {
      "type": "card_error",
      "message": "Refund amount ($10.00) exceeds the charge amount ($5.00)"
    }
  }

Notes:
  - Amounts are always in the smallest currency unit (cents for USD)
  - Partial refunds: POST with amount < original charge amount
  - Full refund: omit the amount field entirely
  - Idempotency: use Idempotency-Key header to safely retry (optional for this lab)
```

---

## Part 0: Forethought

Before reading the existing code — 3 minutes:

1. What's the difference between a 400 and a 402 in this API? How should your code handle each?
   [blank]

2. What does "production-quality" mean to you in 2-3 bullet points?
   [blank]

3. What's the first thing you'll read in the existing codebase? Why?
   [blank — Stripe specifically evaluates: do you read before you write?]

---

**--- CHECKPOINT: Forethought complete. Move to Part 1. ---**

---

## Part 1: Read the Existing Codebase

Read this code carefully. Do not write any code yet. Understand the structure first.

```python
# payment_processor.py (existing code — read before writing)
import requests
import json

class PaymentProcessor:
    def __init__(self, api_key: str, log_file: str = "transactions.log"):
        self.api_key = api_key
        self.base_url = "https://api.stripe-mock.com/v1"
        self.log_file = log_file
    
    def process_charge(self, amount_cents: int, currency: str, source_token: str) -> dict:
        """Process a new charge. Returns charge dict or raises PaymentError on failure."""
        response = requests.post(
            f"{self.base_url}/charges",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"amount": amount_cents, "currency": currency, "source": source_token}
        )
        if response.status_code != 200:
            raise PaymentError(response.json().get("error", {}).get("message", "Unknown error"))
        
        charge = response.json()
        self._log_transaction("charge", charge["id"], amount_cents)
        return charge
    
    def _log_transaction(self, type: str, id: str, amount_cents: int) -> None:
        """Append a transaction record to the log file."""
        with open(self.log_file, "a") as f:
            f.write(json.dumps({"type": type, "id": id, "amount_cents": amount_cents}) + "\n")


class PaymentError(Exception):
    """Raised when a payment API call fails."""
    pass


# TODO: implement process_refund() as a method of PaymentProcessor
```

After reading, answer these before moving on:

What does `_log_transaction` expect? What arguments does it take?
[blank]

What does `process_charge` raise on failure? How does it get the error message from the response?
[blank]

What URL pattern does this class use for API calls? What will the refund URL be?
[blank]

---

**--- CHECKPOINT: Codebase read and questions answered. Move to Part 2. ---**

---

## Part 2: Clarifying Questions

Even in a timed integration round, good engineers ask 1-2 quick clarifying questions.

What would you ask before implementing `process_refund`?
[blank — write your 2-3 questions here]

Canonical answers to check against:
- If `amount_cents` is None, does that mean a full refund, or is it an error?
  → None = full refund (omit amount from API body)
- Should we log the refund even if it fails?
  → No. Log only on success (follow the pattern of `process_charge`).
- Should `process_refund` return the refund object or just True/False?
  → Return the refund dict (follow the pattern of `process_charge` returning the charge dict)

---

**--- CHECKPOINT: Clarifying questions done. Move to Part 3. ---**

---

## Part 3: Design Before Implementing

Fill in the design sketch before touching code. This is the "Stripe-style rigor" requirement.

API call design:
- Endpoint: [blank — copy from the API docs]
- Method: [blank]
- Headers: [blank — what authorization pattern does the existing code use?]
- Body: [blank — what fields? what's optional?]

Error handling design:
- 400 response: [blank — what should process_refund do?]
- 402 response: [blank — same or different from 400?]
- Network timeout: [blank — should we catch requests.exceptions.Timeout?]
- amount_cents = 0: [blank — validate before calling API or let API reject?]

Logging design:
- When to log: [blank — before or after checking response status?]
- What type string: [blank — "refund" to match convention?]

---

**--- CHECKPOINT: Design complete. Move to Part 4. ---**

---

## Part 4: Implementation

The structure is provided. Fill in all `[blank]` and `pass` statements. This is the "build it" part of the integration round.

```python
def process_refund(self, charge_id: str, amount_cents: int = None) -> dict:
    """
    Issue a refund for a charge.
    
    Args:
        charge_id:    The charge ID to refund (e.g., "ch_xxx")
        amount_cents: Amount in cents to refund. None = full refund.
    
    Returns:
        Refund dict from the API (e.g., {"id": "re_xxx", "amount": 500, ...})
    
    Raises:
        ValueError:    If amount_cents is provided and <= 0
        PaymentError:  If the API call fails (400 or 402)
    """
    # TODO: Validate amount_cents if provided
    # Why validate before calling the API?
    # [blank]
    if amount_cents is not None:
        # [blank — what condition makes amount_cents invalid?]
        pass
    
    # TODO: Build the request body
    # Note: amount is OPTIONAL — only include if amount_cents was provided
    # [blank]
    body = {}
    
    # TODO: Make the API call
    # POST to /v1/refunds with the right headers and body
    # [blank]
    response = None
    
    # TODO: Handle errors
    # Both 400 and 402 should raise PaymentError with the API's error message
    # How do you extract the error message from the response body?
    # [blank]
    
    # TODO: Parse the successful response
    # [blank]
    refund = None
    
    # TODO: Log the transaction
    # Use self._log_transaction() — match the convention from process_charge
    # What type string? What id? What amount?
    # [blank]
    
    # TODO: Return the refund dict
    # [blank]
    pass
```

---

**--- CHECKPOINT: process_refund implemented. Move to Part 5. ---**

---

## Part 5: Stripe-Style Reasoning

Answer each of these as if writing a Stripe engineering memo paragraph:

**Q1: Why validate `amount_cents` before calling the API?**
[blank — think about: API round-trips cost time, user experience, being explicit about preconditions]

**Q2: What's the difference between a 400 and a 402 error? Do you handle them the same way or differently?**
[blank — 400 = bad request (invalid charge_id, bad params); 402 = payment required (e.g., refund > charge). Both raise PaymentError but a production system might want to distinguish them for monitoring]

**Q3: What if the API call times out after 30 seconds? What should `process_refund` do?**
[blank — consider: the refund may or may not have processed. This is the "half-open" problem. What's the safe behavior?]

**Q4: What makes this "production-quality" versus "just working"?**
[blank — Stripe's bar: error handling covers all non-200 cases, validation is explicit, logging follows existing conventions, code is readable, function contract is documented]

---

**--- CHECKPOINT: Reasoning complete. Move to Part 6. ---**

---

## Part 6: Curveballs

**Curveball 1:**
"What if `process_refund` is called twice with the same `charge_id` and same `amount_cents`? Is that safe?"
[blank — hint: is the Stripe refund API idempotent by default, or does it create two separate refunds? What would you add to make it safe to retry?]

**Curveball 2:**
"The API has a 500ms p99 latency. You need to refund 1,000 charges in under 30 seconds. How?"
[blank — hint: sequential calls = 500 seconds. What's the concurrency approach? Python `asyncio` + `aiohttp`? `ThreadPoolExecutor`? What are the trade-offs?]

**Curveball 3:**
"Write a Stripe-style memo (2 paragraphs) explaining this refund feature to a non-technical stakeholder — say, the head of Customer Success."
[blank — practice the writing culture: what problem does refunds solve, what the merchant experience looks like, what guarantees they can rely on. No technical jargon.]

---

**--- CHECKPOINT: Curveballs answered. Move to Part 7. ---**

---

## Part 7: Self-Assessment Rubric

Score yourself honestly. Total = 35 points. Target: ≥ 28 to be ready.

| Dimension | 5 | 3 | 1 | Your Score |
|---|---|---|---|---|
| Communication / Think-Aloud | Explained design decisions and trade-offs clearly throughout; would be clear to a remote interviewer watching | Explained most decisions with some silent gaps | Coded silently; design was opaque | /5 |
| Problem Solving | Read codebase first, matched patterns, built the correct solution systematically | Got there after some backtracking; mostly matched patterns | Started writing before reading, or significant pattern mismatches | /5 |
| Correctness | Feature ships: full refund, partial refund, error cases, logging all correct | Most cases correct; one edge case missed or broken | Core functionality broken or doesn't run | /5 |
| Code Quality | Clean code: clear naming, no hacks, proper use of existing patterns, docstring matches reality | Mostly clean with one or two issues (e.g., inconsistent style, missing error type) | Hacks, unclear naming, or copy-paste errors from existing code | /5 |
| Testing & Edge Cases | Tested: full refund, partial refund, amount_cents=0, invalid charge_id, None amount | Tested most cases, missed one | Only tested the happy path | /5 |
| Works Against Provided API | Integration is correct: right endpoint, right headers, right body shape for optional amount, right error extraction | Mostly correct but one API detail wrong (e.g., wrong status code check) | Integration broken; doesn't run against the mock | /5 |
| Writing Quality | Memo is clear, jargon-free, and explains the feature confidently; code is readable as prose | Memo is adequate; code mostly readable | Memo unclear or missing; code is hard to read | /5 |

**Total: /35**

---

### Reflection

What was the hardest part of reading an unfamiliar codebase under time pressure?
[blank]

What would make you faster at integration rounds in the future?
[blank]

---

### Ready-When Checklist

- [ ] I read the codebase fully before writing any code
- [ ] I understand why `amount_cents` is optional in both my implementation and the API
- [ ] I handle both 400 and 402 errors correctly (raise PaymentError with API message)
- [ ] My logging call matches the `_log_transaction` signature exactly
- [ ] I can explain the idempotency problem with refunds in 2 sentences
- [ ] I wrote the non-technical memo and it's jargon-free
- [ ] Self-score ≥ 28/35
