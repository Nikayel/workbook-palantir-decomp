<div align="center">
  <h1>🚀 Palantir FDSE / SWE Interview Prep Workbook</h1>
  <p><strong>An interactive, hands-on coding and system design lab for Palantir interviews.</strong></p>
  <img src="https://img.shields.io/badge/Status-Complete-success?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge" alt="Difficulty"/>
  <img src="https://img.shields.io/badge/Language-Python%20%7C%20Node.js-blue?style=for-the-badge" alt="Language"/>
</div>

---

Welcome to the **Palantir Forward Deployed Software Engineer (FDSE) and Software Engineer (SWE)** interactive interview-practice lab generator. 

Unlike standard "lecture" repos, this is an **interactive workbook + coding lab system**. You will learn by *doing*, simulating the ambiguity, decomposition, and systems thinking required at Palantir.

## 📖 What's Inside?

This repository contains **8 realistic labs** modeled after actual Palantir interview rounds. Each lab is designed to take about 3 hours and covers:

* **Decomposition**: Breaking down ambiguous, real-world operational problems.
* **Coding**: Implementing core logic (Python & JS), handling edge cases, and writing tests.
* **System Design**: Designing APIs, data models, state machines, and audit logs.
* **Behavioral**: Handling "curveballs," justifying tradeoffs, and communicating your MVP.

### 🧪 The Labs
1. 🚑 **[Lab 1: 911 Dispatch Optimization](./labs/lab_01_911_dispatch)** - Resource allocation, heuristics, and human-in-the-loop design.
2. 🏥 **[Lab 2: Hospital Discharge Delays](./labs/lab_02_hospital_discharge)** - Workflow bottlenecks and task state machines.
3. 💳 **[Lab 3: Fraud Investigation](./labs/lab_03_fraud_investigation)** - Anomaly scoring and analyst workflows.
4. 🚢 **[Lab 4: Supply Chain Risk](./labs/lab_04_supply_chain_risk)** - DFS/BFS traversal, DAGs, and risk propagation.
5. 🏭 **[Lab 5: Factory Predictive Maintenance](./labs/lab_05_factory_maintenance)** - Time-series anomaly detection and alert fatigue.
6. 🌪️ **[Lab 6: Disaster Relief](./labs/lab_06_disaster_relief)** - Prioritization, offline constraints, and logistics.
7. 🛠️ **[Lab 7: Learning/Re-engineering](./labs/lab_07_learning_reengineering)** - Debugging and extending a flawed legacy system.
8. ⚙️ **[Lab 8: System Design Case](./labs/lab_08_system_design_case)** - Applied API design and state transition validation (JS).

### 📝 Templates & Drills
Check out the `templates/` folder for fill-in-the-blank markdown files to help structure your decomposition, tradeoffs, and system design.
Check out the `drills/` folder for flashcards and coding patterns!

---

## 🚀 How to Use This Workbook

Each lab is designed to take about **3 hours** (flexible from 2 to 5 hours depending on your deep-dive).

1. **Start the Clock**: Open a lab's `README.md` and read the time breakdown.
2. **Decompose**: Open `workbook.md`. Fill in the blanks for the goal, users, workflow, and entities. **Do not look at the solution.**
3. **Code**: Open `starter.py` (or `.js`), read the prompt, and implement the TODOs. 
4. **Test**: Run the tests.
   - For Python: `python3 tests.py`
   - For Node: `node tests.js`
5. **Interview Simulation**: Use the curveballs and talk-track prompts in the workbook to practice *verbalizing* your thoughts.
6. **Review & Reflect**: Only after you have tried, open `solution_reasoning.md` and `reference_solution.*`.
7. **Self-Grade**: Fill out the rubric at the bottom of the workbook.

### ⚠️ Golden Rules
- **Write your answer before opening `solution_reasoning.md`**.
- **Explain out loud while coding**.
- **Self-grade after every lab**.

---

## 🗓️ Study Plans

### ⚡ 7-Day Sprint Plan
- **Day 1**: Lab 1 (911 Dispatch) + 30 min review
- **Day 2**: Lab 2 (Hospital Discharge) + 30 min coding pattern review
- **Day 3**: Lab 3 (Fraud Investigation) + 30 min talk track practice
- **Day 4**: Lab 4 (Supply Chain Risk) 
- **Day 5**: Lab 5 (Factory Maintenance) OR Lab 6 (Disaster Relief)
- **Day 6**: Lab 7 (Learning/Re-engineering)
- **Day 7**: Lab 8 (System Design Mock) + redo your weakest lab

### 🏋️ 14-Day Deep Dive
- **Week 1**: Do all 8 labs on the standard 3-hour path.
- **Week 2**: Repeat each lab once.
  - First attempt without looking at the answer key at all.
  - Second attempt timed (stress test).
  - Record your 90-second explanations on video.
  - Redo the coding tests from scratch.
  - Track rubric scores and measure your improvement!

---

## 🤝 Contributing
Feel free to fork this repository, add your own labs, or submit PRs with better reference solutions! Star the repo if you found it useful for your Palantir prep. Good luck! 🚀
