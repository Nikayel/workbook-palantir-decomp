# System Design Flashcards

**Q: Why use an audit log?**
A: To track who did what and when, especially for human-in-the-loop overrides.

**Q: Batch vs Real-time?**
A: Real-time is for immediate operational decisions (dispatch). Batch is for reporting or heavy pre-computation.

**Q: How to handle stale data?**
A: Show timestamps to the user, add manual overrides, or use a dead-man's switch to invalidate old data.
