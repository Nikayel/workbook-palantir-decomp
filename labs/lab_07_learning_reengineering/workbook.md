Status: Spec incomplete — fill in all blank fields before implementing

# Scenario

You have inherited a legacy piece of code written by a former intern. It is supposed to assign support tickets to agents. However, users are complaining that tickets are being assigned to agents who are currently on vacation, the highest priority tickets are being ignored, and sometimes the system throws weird errors.

Your job is to read the code, find the bugs, fix them, and add a new feature.

# Part 1: Understand the Code

Read `starter.py`. Without running it, explain what it is *trying* to do:
[blank]
[blank]

# Part 2: Find the Bugs

List the 5 bugs you found in the code.
1. [blank]
2. [blank]
3. [blank]
4. [blank]
5. [blank]

# Part 3: Write Tests

Open `tests.py`. Write tests that trigger the bugs you found.

# Part 4: Fix and Extend

Fix the bugs in `starter.py`.

**New Requirement**:
The business now wants to route tickets based on `language`. If a ticket is marked `es` (Spanish), it MUST go to an agent who has `es` in their `languages` array.

# Part 5: Reasoning

Why did the original code mutate the input array? Why is that bad?
[blank]

How did you preserve the existing behavior while adding the language requirement?
[blank]

# Self-grade

Score 1–5.

Understanding unfamiliar code: __ / 5  
Debugging logic errors: __ / 5  
Writing tests: __ / 5  
Adding requirements cleanly: __ / 5  
Communication of tradeoffs: __ / 5  

Total: __ / 25
