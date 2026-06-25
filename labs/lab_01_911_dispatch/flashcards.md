# Flashcards — 911 Dispatch Optimization

> Review **day 1 → 3 → 7 → 14**. Reset to day 1 on a miss.
> Cover each answer before reading. These are free-recall — no peeking.

---

**Q:** What is the "ask + assume" heuristic and when do you use it in an interview?
**A:** For every ambiguity in the scenario, ask a clarifying question AND state the assumption you'll code against. This proves you know what you don't know and lets you move forward without getting stuck waiting for the interviewer to answer every question.

---

**Q:** Why must core entities be nouns, not properties? Give a counterexample from this lab.
**A:** Entities become database tables (rows of data). Properties become columns inside a table. "Responder" is a correct entity. "responder_location" is a property of Responder, not its own table. Listing properties as entities leads to a broken data model with no clear primary keys.

---

**Q:** What is the difference between a UI state transition and a DB lifecycle state transition? Give an example from the dispatch domain.
**A:** A UI state transition describes what the user sees on screen (e.g., "Loading → Results Shown"). A DB lifecycle state transition describes how the row in the database changes over time: AVAILABLE → DISPATCHED → ON_SCENE → AVAILABLE. Only DB lifecycle states belong in your decomposition.

---

**Q:** What is a fallback design and why is "return nothing" dangerous for dispatch systems?
**A:** A fallback is what your system does when it cannot find a valid result. In dispatch, returning an empty list or crashing means no one responds to the emergency. The correct fallback is to escalate — alert a supervisor, page mutual aid from a neighboring jurisdiction, and never silently fail.

---

**Q:** What is the "filter then sort" ranking strategy and why does order matter?
**A:** First filter to the candidate pool that meets hard constraints (right equipment, not on break, within range), then sort that pool by a scoring function (e.g., distance + ETA). If you sort before filtering, you may rank a closer-but-wrong-equipment responder above a valid one, wasting time and resources.

---

**Q:** What are two concrete ways stale GPS data breaks a dispatch recommendation system?
**A:** (1) You recommend a responder who has already been dispatched — their location moved but the system still shows them as nearby and available. (2) You skip a responder who was on break 5 minutes ago but is now available — you're filtering on outdated status. Both errors send the wrong resource to the wrong place.

---

**Q:** What is human-in-the-loop design and why does a dispatch system need it?
**A:** Human-in-the-loop means the system recommends but a human makes the final decision. Dispatch needs it because edge cases (downed bridge, local knowledge, unit capabilities not in the database) exceed what any algorithm can model. The dispatcher must be able to override and the system must log that override.

---

**Q:** What is an audit trail and what three things must every audit event record?
**A:** An audit trail is an append-only log of every action taken in the system. Every event must record: (1) WHO took the action (user ID), (2) WHAT was done (recommendation accepted / override to unit X), and (3) WHEN it happened (timestamp). This supports post-incident review, liability, and system improvement.

---

**Q:** What is a concurrency boundary and how would you protect it in a Python dispatch function?
**A:** A concurrency boundary is the point where two processes can race to modify the same record. In dispatch, two dispatchers could assign the same responder simultaneously. Protect it with a status check + optimistic lock or a database-level compare-and-swap: only update status to DISPATCHED if current status is still AVAILABLE.

---

**Q:** What is "the simplest version that still helps the user" and why is it a better V1 target than a fully automated system?
**A:** The simplest version is a sorted list of the top 3 available responders on the dispatcher's screen — no auto-assignment, no ML scoring, just filter + sort. It still helps because it eliminates the manual map scan. It is a better V1 target because it keeps the human in control, is easier to trust, and reveals real-world data quality issues before you add automation.
