Status: Spec incomplete — fill in all blank fields before implementing

# Scenario

You need to design a Case Management Platform for investigating high-priority operational incidents. 
Users (Analysts) will open cases, attach evidence (links to other systems), change case states, and close cases.
Supervisors must approve closures.

# Part 1: Design

Fill out the templates in the `templates/` folder to design:
- Data model
- State machine
- APIs

# Part 2: Coding Task

Open `api_design.js` and `state_machine.js`. Implement the validation logic and route handlers.

# Part 3: Interview Simulation

Curveball 1: An analyst tries to close a case, but the system crashes halfway through writing the audit log.
Your response (Idempotency / Transactions):
[blank]

Curveball 2: A supervisor needs to see all cases closed in the last 24 hours. How do you index the database?
Your response:
[blank]

# Self-grade

Score 1–5.

Total: __ / 50
