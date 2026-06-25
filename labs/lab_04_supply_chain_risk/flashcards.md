# Flashcards — Supply Chain Risk

> Review **day 1 → 3 → 7 → 14**. Reset to day 1 on a miss.
> Cover each answer before reading. These are free-recall — no peeking.

---

**Q:** What is a risk scoring system and what three inputs does a supply chain risk score typically aggregate?
**A:** A risk scoring system combines multiple signals into a single number (e.g., 0–100) representing the likelihood or severity of a disruption. For supply chain, the three common inputs are: (1) supplier financial health (late payments, credit rating), (2) geographic risk (proximity to disaster zone, port congestion), and (3) delivery history (on-time rate over the last 90 days).

---

**Q:** What are early warning signals in supply chain risk, and name three leading indicators (not lagging ones)?
**A:** Early warning signals are indicators that predict a disruption before it happens, rather than confirming it after (lagging). Leading indicators: (1) a supplier's payment defaults or late filings in public records, (2) satellite imagery showing reduced activity at a manufacturing site, (3) shipping container rates spiking on a specific trade lane. Lagging indicators (avoid for early warning): missed delivery, invoice dispute, formal complaint.

---

**Q:** Why is multi-source data aggregation for supply chain harder than a single database query?
**A:** Supplier data comes from incompatible sources — ERP systems, third-party data providers, government filings, logistics APIs — each with different schemas, update frequencies, and reliability. Aggregating them requires normalization, conflict resolution (which source wins when they disagree on a supplier's address?), and staleness tracking per source.

---

**Q:** When should supply chain risk calculations run as batch vs streaming, and what drives that choice?
**A:** Batch (nightly or hourly) for full graph re-scoring — propagating risk across thousands of suppliers is compute-intensive and most supplier risk doesn't change minute-to-minute. Streaming (near real-time) for high-severity event ingestion — a port closure or earthquake notification should trigger an immediate targeted re-score of affected nodes, not wait for the next batch window. The decision criterion is: "How quickly does a human need to act?"

---

**Q:** How do you represent supplier dependencies as a graph and what Python data structure is most practical for in-memory traversal?
**A:** Model suppliers as nodes and dependencies as directed edges (supplier A → sub-assembly B → final product C). Use a dict of adjacency lists: `{node_id: [dependent_node_ids]}`. This gives O(1) neighbor lookup and works well for graphs that fit in memory (tens of thousands of nodes). For larger graphs, use a graph database (e.g., Neo4j) or a sparse matrix.

---

**Q:** What is threshold-based alerting in supply chain risk, and what is the failure mode of setting the threshold too low?
**A:** Threshold-based alerting fires a notification when a supplier's risk score exceeds a set value (e.g., score > 70). Setting the threshold too low produces alert fatigue — supply chain managers receive hundreds of alerts and begin ignoring them. The failure mode is that a genuinely critical alert (score = 95) goes unnoticed because it appears alongside 200 routine ones.

---

**Q:** What is a lead time buffer and how does it change the urgency calculation in a risk system?
**A:** Lead time is how many days in advance a supplier must ship to meet a production deadline. A lead time buffer is the slack added on top (e.g., 10 days buffer on a 30-day lead time). A risk system uses the buffer to calculate how much time is left before a disruption becomes unrecoverable: `days_until_critical = lead_time_buffer - days_since_disruption_started`. If this number turns negative, the impact is already locked in.

---

**Q:** What is the difference between an operational view and a strategic view of supply chain data, and who uses each?
**A:** An operational view shows the current state of active orders and in-flight shipments — used by supply chain coordinators making same-day decisions (reroute this shipment now). A strategic view shows aggregated trends across quarters — used by procurement leadership deciding which suppliers to qualify, dual-source, or exit. The same underlying data supports both, but the aggregation level and latency requirements are completely different.

---

**Q:** How do you detect and handle cycles in a supplier dependency graph during traversal?
**A:** Cycles (A depends on B, B depends on A) cause infinite loops in naive DFS/BFS. Handle them by maintaining a `visited` set of node IDs. Before enqueuing or recursing into a node, check if it is already in `visited`. If it is, skip it. After traversal, log any cycle detected — a cycle in a real supply graph is itself a data quality problem worth surfacing.

---

**Q:** How do you aggregate risk scores from multiple upstream suppliers into a single risk score for a downstream product?
**A:** Three common strategies: (1) Max — the product inherits the risk of its riskiest supplier (conservative; use when any single failure blocks production). (2) Weighted average — weight each supplier by how much of the component they supply (use when substitution is possible). (3) Multiplicative — `1 - product(1 - risk_i)` represents the probability that at least one supplier fails (use when independence can be assumed). Name your choice and justify it — the interviewer is testing whether you know these tradeoffs exist.
