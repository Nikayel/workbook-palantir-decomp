<div align="center">
  <h1>🚀 Palantir FDSE / SWE Interview Prep Workbook</h1>
  <p><strong>An interactive, hands-on coding, API, and system design lab for Palantir interviews.</strong></p>
  <img src="https://img.shields.io/badge/Status-Complete-success?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge" alt="Difficulty"/>
  <img src="https://img.shields.io/badge/Language-Python%20%7C%20Node.js%20%7C%20SQL-blue?style=for-the-badge" alt="Language"/>
</div>

---

Welcome to the **Palantir Forward Deployed Software Engineer (FDSE) and Software Engineer (SWE)** interactive interview-practice lab generator. 

Unlike standard "lecture" repos, this is an **interactive workbook + coding lab system**. You will learn by *doing*, simulating the ambiguity, decomposition, and systems thinking required at Palantir.

## 📖 What's Inside?

This repository contains multiple distinct sections modeled after actual Palantir interview rounds.

### 🧪 1. The Core Decomposition Labs (3 Hours Each)
Found in `labs/`, these 8 realistic labs cover the signature Palantir "Open Deployment" or "Decomposition" round:
1. 🚑 **[Lab 1: 911 Dispatch Optimization](./labs/lab_01_911_dispatch)** 
2. 🏥 **[Lab 2: Hospital Discharge Delays](./labs/lab_02_hospital_discharge)**
3. 💳 **[Lab 3: Fraud Investigation](./labs/lab_03_fraud_investigation)**
4. 🚢 **[Lab 4: Supply Chain Risk](./labs/lab_04_supply_chain_risk)**
5. 🏭 **[Lab 5: Factory Predictive Maintenance](./labs/lab_05_factory_maintenance)**
6. 🌪️ **[Lab 6: Disaster Relief](./labs/lab_06_disaster_relief)**
7. 🛠️ **[Lab 7: Learning/Re-engineering](./labs/lab_07_learning_reengineering)**
8. ⚙️ **[Lab 8: System Design Case](./labs/lab_08_system_design_case)**

### 🧩 2. DSA Patterns (`dsa_patterns/`)
Focuses on the exact Data Structures & Algorithms patterns commonly seen in Palantir interviews, complete with Product Lab Ideas for each.
- Arrays & Hash Maps (Duplicate Detection, Frequency Counting)
- Strings & Parsing (Beautiful Indices, Log Parsing)
- Intervals & Timestamps (Min Time Difference, Daily Temperatures)
- Graphs, BFS/DFS (Flood Fill, Accounts Merge, Trapping Rain Water II)
- Design Data Structures (LRU Cache, Session Manager)
- Heap & Priority Queue (Merge K Sorted Lists)
- Basic DP & Backtracking

### 🔌 3. API, Data & SQL (`api_sql_data/`)
Crucial for FDSE prep. Includes realistic tasks for consuming APIs with pagination, implementing CRUD, and writing complex analytical SQL queries (window functions, sessionization).

### 🎯 4. Exact Reported Problems (`exact_reported_problems/`)
A collection of specific scenarios that have been previously reported by candidates:
- Card Game Scorer
- Duplicate Event Detector
- Website User Session Analysis
- Access Control Tree
- Stock Portfolio
- A complete 90-minute **Mock OA** covering DSA, API, and SQL.

### 📝 Templates & Drills
Check out the `templates/` and `drills/` folders for fill-in-the-blank markdown files, flashcards, and behavioral STAR prompts!

---

## 🚀 How to Use This Workbook

Each core lab is designed to take about **3 hours**.

1. **Start the Clock**: Open a lab's `README.md`.
2. **Decompose**: Open `workbook.md`. Fill in the blanks. **Do not look at the solution.**
3. **Code**: Open `starter.py` (or `.js`), read the prompt, and implement the TODOs. 
4. **Test**: Run the tests (`python3 tests.py` or `node tests.js`).
5. **Interview Simulation**: Use the curveballs and talk-track prompts in the workbook to practice *verbalizing* your thoughts.
6. **Review & Reflect**: Only after you have tried, open `solution_reasoning.md` and `reference_solution.*`.
7. **Self-Grade**: Fill out the rubric.

### ⚠️ Golden Rules
- **Ask & Assume**: When gathering requirements in Part 1, always pair your question with an immediate assumption. (e.g., *"What is our scale? I'll assume it fits in memory for now."*) This prevents you from freezing if the interviewer is silent.
- **Write your answer before opening `solution_reasoning.md`**.
- **Explain out loud while coding**.
- **Self-grade after every lab**.

---

## 🗓️ Study Plans

### ⚡ 7-Day Sprint Plan
- **Day 1**: Lab 1 (911 Dispatch) + DSA Arrays/Hash Maps
- **Day 2**: Lab 2 (Hospital Discharge) + DSA Graphs/DFS
- **Day 3**: Lab 3 (Fraud Investigation) + SQL Labs
- **Day 4**: Lab 4 (Supply Chain Risk) + API Labs
- **Day 5**: Exact Reported Problems (Card Game, Access Control)
- **Day 6**: Lab 7 (Learning/Re-engineering)
- **Day 7**: Mock OA (90 minutes)

### 🏋️ 14-Day Deep Dive
- **Week 1**: Do all 8 core labs on the standard 3-hour path.
- **Week 2**: Focus on DSA patterns, API/SQL queries, and repeat core labs with a strict timer. Record your 90-second explanations on video. Track rubric scores to measure improvement!

---

---

## 🧑‍🏫 For Curriculum Creators

This repo started as a **Palantir SWE** workbook. The **[`curriculum_creator_playbook/`](./curriculum_creator_playbook/)** folder is the perfected, generalized system for building workbooks like these across **3 roles (PM · Technical PM · SWE)** and **10 companies** (Google, Meta, Amazon, Microsoft, Apple, Palantir, Nvidia, Uber, Stripe, Atlassian).

It contains the learning-science principles, the authoring standard, role guides, **10 company fact-packs**, how-many-to-build counts, **authoring checklists**, templates, and **3 fully-worked gold-standard sample labs** (one per role). Start at [`curriculum_creator_playbook/README.md`](./curriculum_creator_playbook/README.md). The existing labs here are "v1" — see the [v1 audit](./curriculum_creator_playbook/10_v1_audit_and_gap_analysis.md) for what's kept and what's improved.

---

## 🤝 Contributing
Feel free to fork this repository, add your own labs, or submit PRs with better reference solutions! Star the repo if you found it useful for your Palantir prep. Good luck! 🚀
