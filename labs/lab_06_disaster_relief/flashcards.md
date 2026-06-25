# Flashcards — Disaster Relief: Supply Allocation Coordinator

> Review **day 1 → 3 → 7 → 14**. Reset to day 1 on a miss.
> Cover each answer before reading. Free-recall — no peeking.

---

**Q:** What does "offline-first design" mean, and why is it non-negotiable in a disaster relief coordination system?
**A:** Offline-first means the app remains fully functional with no network connection — it reads from and writes to a local store, then syncs when connectivity is restored. In disaster scenarios, cell towers and internet infrastructure are often damaged or overloaded. A system that requires constant connectivity will fail exactly when lives are at stake. The app must queue writes locally and merge them on reconnect.

---

**Q:** Two field workers, both offline, each claim the last pallet of water at the same timestamp. When they sync, who wins?
**A:** "Last write wins" by timestamp is unsafe if clocks are unsynchronized (common in disaster conditions). Better options: (1) reserve inventory with a soft lock before dispatching — first sync wins, second gets a conflict error and must re-request; (2) use a version vector or logical clock to detect the conflict and surface it to a human dispatcher for manual resolution; (3) treat inventory as a decrement counter with floor at 0 — both writes go through but the floor prevents negative stock.

---

**Q:** What is eventual consistency, and what is the specific risk of using it in a life-safety system?
**A:** Eventual consistency means all nodes will converge to the same state *eventually*, but reads may return stale data in the interim. In a life-safety system, stale data can mean a shelter that has already received supplies appears to still need them — causing a second truck to be dispatched while a shelter with zero supplies gets nothing. Mitigation: use a "last-known-update" timestamp on every record; surface data age prominently in the UI so dispatchers can make informed decisions.

---

**Q:** How do you rank competing supply requests when a truck can only carry a subset of what is needed?
**A:** Score each request by: (1) supply criticality (medical > water > food > blankets), (2) shelter vulnerability (children, elderly, injured), (3) time since last resupply, and (4) quantity deficit as a fraction of need. Sort descending by score. Greedy-fill the truck by score until capacity is exhausted. Document the scoring formula so dispatchers can override and explain it.

---

**Q:** What geospatial data do you need to route a relief truck, and how do road closures change your routing algorithm?
**A:** You need: depot coordinates, shelter coordinates, road network graph (edges with distance/time weights), and a real-time road closure feed. Road closures are edge deletions from the graph. Re-run shortest-path (Dijkstra or A*) on each closure update. For V1, treat closures as binary (open/closed); for V2, add time-varying weights (roads may reopen). Cache routes and invalidate on closure changes to avoid recomputing from scratch every minute.

---

**Q:** What is the difference between triage-based prioritization and first-come-first-served in resource allocation, and which is correct for disaster relief?
**A:** First-come-first-served gives resources to whoever requests first — fair in normal queuing but catastrophic in disaster relief because a shelter that submits requests quickly may have minor needs while a shelter that can't communicate may be in crisis. Triage-based prioritization allocates based on severity of need, not order of request. Disaster relief always requires triage. The system must support dispatchers overriding algorithmic rankings.

---

**Q:** How fresh does supply inventory data need to be in a disaster relief system, and what happens if a shelter's reported need is 6 hours stale?
**A:** Needs data more than 1–2 hours old is operationally unreliable in a fast-moving disaster — shelter populations shift, supplies are consumed, conditions change. A 6-hour-stale need report could mean the shelter is now fine (over-dispatch risk) or has deteriorated further (under-dispatch risk). The system must display a "last updated" timestamp prominently and flag stale records. Dispatchers must be able to mark a record as "unverified" to trigger a check-in attempt.

---

**Q:** What states should a volunteer or truck go through in a relief coordination state machine?
**A:** For a truck: AVAILABLE → LOADED (inventory assigned) → EN_ROUTE → DELIVERED (confirmation from shelter) → RETURNING → AVAILABLE. Key guards: a truck cannot be LOADED if depot inventory is insufficient; DELIVERED requires a confirmation event (GPS arrival + dispatcher confirmation OR shelter check-in); RETURNING triggers a depot inventory update.

---

**Q:** What is an Incident Command Structure (ICS) and why does it matter when modeling a disaster relief coordination system?
**A:** ICS is a standardized management hierarchy used by emergency responders: Incident Commander → Section Chiefs (Operations, Logistics, Planning, Finance) → Branch Directors → Units. In a software model, ICS tells you who has authority to make which decisions — only Logistics can authorize supply dispatch, only Operations can redirect trucks. Modeling permission and approval flows without understanding ICS leads to systems that don't match how relief organizations actually work.

---

**Q:** What does "failing safe" mean in a humanitarian system, and give one concrete example from disaster relief supply allocation.
**A:** Failing safe means that when the system encounters an error or uncertainty, it defaults to the outcome that causes less harm. Example: if the routing algorithm cannot find a valid route to a shelter (network error, data gap), the system should NOT silently drop the request. It should flag the shelter as "unrouted" and surface it to a human dispatcher for manual handling — rather than losing the request or sending a truck into a closed road.
