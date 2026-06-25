Status: Ready — work through all parts in order

# Lab 01 · Algorithmic + Complexity Narration
**Microsoft SWE · Tier 1 · ~75 minutes**

---

## 🪜 Milestones

- [ ] M1 · Clarified — edge cases named for both problems before coding
- [ ] M2 · Approached — BFS for P1 and stack for P2, both narrated aloud
- [ ] M3 · Coded — both solutions complete and readable
- [ ] M4 · Tested — walked 3 test cases per problem
- [ ] M5 · Growth-mindset check — noted one thing you'd do differently next time
- [ ] M6 · Ready — self-graded ≥ 28/35

---

## Scenario

You're sitting the **Microsoft Codility OA** — 90 minutes, 2 problems. An interviewer is observing your screen (in the Superday version of this round, someone is watching live).

**Problem 1:** Given a binary tree, return the level-order traversal as a list of lists — one sublist per level (BFS).

**Problem 2:** Given a string containing parentheses `()`, brackets `[]`, and braces `{}`, determine if it's valid. A string is valid if every opening bracket has a matching closing bracket in the correct order.

Narrate your thought process as if a Microsoft interviewer is watching. They care about **growth mindset and clear reasoning**, not just whether you get the answer.

---

## Part 0: Forethought

Before reading anything else — spend 3 minutes answering these:

1. What do you already know about BFS? What's the core data structure it uses?
   [blank]

2. What's your first instinct for the valid-parentheses problem?
   [blank]

3. When was the last time you got stuck on a problem? What did you learn from it?
   [blank — this is not throwaway. Microsoft will ask this.]

---

**--- CHECKPOINT: Do not move to Part 1 until Part 0 is filled in. ---**

---

## Part 1: Clarifying Questions

**Skill: Clarifying before coding is a green flag at Microsoft.**

For both problems, write the clarifying questions you'd ask before touching code:

**Problem 1 — Binary Tree Level Order:**

- What should we return for an empty tree (root is None)?
  [blank — your answer]
- Can the tree have only one node?
  [blank]
- Are node values guaranteed to be integers, or could they be any type?
  [blank]
- Is the output expected as a list of lists, or a flat list?
  [blank]

**Problem 2 — Valid Parentheses:**

- Can the string be empty? If so, is it valid?
  [blank]
- Does the string contain only bracket characters, or can it contain letters/spaces too?
  [blank]
- What about `{[}]` — is nesting required to be strict?
  [blank]
- What's the maximum length of the string?
  [blank]

---

**--- CHECKPOINT: Clarifying questions complete. Move to Part 2. ---**

---

## Part 2: Approach (Narrate Aloud)

Write your approach in plain English before writing any code. Pretend you're explaining to a peer who just walked in.

**Problem 1 — BFS Approach:**

"For level-order traversal, I need to visit all nodes on one level before moving to the next. The natural data structure for this is a..."
[blank — continue the narration. What goes into the queue? How do you know when one level ends and the next begins?]

Time complexity: O([blank]) — why? [blank]
Space complexity: O([blank]) — why? [blank]

**Problem 2 — Valid Parentheses Approach:**

"For valid parentheses, I need to match each closing bracket to the most recent unmatched opening bracket. The natural data structure for this is a..."
[blank — continue the narration. What's the invariant? When do you return False?]

Time complexity: O([blank]) — why? [blank]
Space complexity: O([blank]) — why? [blank]

---

**--- CHECKPOINT: Both approaches narrated. Move to Part 3. ---**

---

## Part 3: Implementation

**Now write your solutions from scratch, narrating aloud as you type.**

**Problem 1 — Level Order Traversal:**

```python
# Your implementation here
# Hint: you'll need a queue and a way to track level boundaries



```

**Problem 2 — Valid Parentheses:**

```python
# Your implementation here
# Hint: you'll need a stack and a way to match closing brackets to opening ones



```

---

**--- CHECKPOINT: Both solutions written. Move to Part 4. ---**

---

## Part 4: Worked Solutions

Compare your implementations to these. Do NOT read these before attempting Part 3.

**Problem 1 — BFS Level Order Traversal:**

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)   # Snapshot: how many nodes are on THIS level
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    
    return result
```

Key insight: `level_size = len(queue)` at the start of each while iteration tells you exactly how many nodes belong to the current level. Process exactly that many, then move on. Children added during this loop belong to the NEXT level.

**Problem 2 — Valid Parentheses:**

```python
def is_valid(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
    
    return len(stack) == 0
```

Key insight: the `matching` dict maps each closer to its expected opener. When we see a closing bracket, the top of the stack MUST be its matching opener — otherwise the string is invalid. At the end, the stack must be empty (every opener was closed).

---

## Part 4 Growth Mindset Reflection

**After implementing (this is what Microsoft actually evaluates):**

What was the hardest part of each problem for you?
[blank]

What would you do differently if you started over?
[blank]

If you got stuck at any point, what approach or resource helped you get unstuck?
[blank]

If you got it right away — is there a harder version of either problem that you'd want to try next? What would that be?
[blank]

> Microsoft interviewers are explicitly trained to look for this kind of reflection. "I got it immediately" is a weaker answer than "I made a mistake here and here's what I learned." Authenticity matters.

---

**--- CHECKPOINT: Solutions compared, reflection written. Move to Part 5. ---**

---

## Part 5: Test Cases

Walk through each solution with the following test cases. Write the expected output and trace through the code step by step.

**Problem 1 — Level Order:**

Test 1: Standard tree
```
      1
     / \
    2   3
   / \
  4   5
```
Expected output: [[1], [2, 3], [4, 5]]
Your trace: [blank]

Test 2: Single node
```
Root = Node(42)
```
Expected output: [[42]]
Your trace: [blank]

Test 3: Empty tree (root = None)
Expected output: []
Your trace: [blank]

**Problem 2 — Valid Parentheses:**

Test 1: `"()[]{}"` — Expected: True. Trace: [blank]
Test 2: `"([)]"` — Expected: False. Trace: [blank — why does the matching dict catch this?]
Test 3: `""` — Expected: True (empty stack). Trace: [blank]

---

**--- CHECKPOINT: Test cases traced. Move to Part 6. ---**

---

## Part 6: Curveballs

An interviewer throws these at you after you've solved the main problem. Answer each one aloud (or in writing).

**Curveball 1:**
"What if the tree has 10 million nodes? How does your BFS approach handle memory?"

[blank — consider: at worst, the last level can have n/2 nodes. What's the queue size at that point? Is there a more memory-efficient traversal? When would you accept this trade-off?]

**Curveball 2:**
"Extend Problem 2: now also validate HTML tags. For example, `<div><p></p></div>` is valid, but `<div><p></div></p>` is not."

[blank — how does your stack approach generalize? What changes in your matching logic? What new edge cases emerge with HTML vs simple brackets?]

**Curveball 3:**
"The interviewer says: 'Tell me about a time you had to learn something completely new under pressure.' Connect it to this problem — what did you learn from today's exercise?"

[blank — this is not a throwaway. Write 3-4 sentences using the growth-mindset frame: what was new, what you did under pressure, what you'd carry forward.]

---

**--- CHECKPOINT: Curveballs answered. Move to Part 7. ---**

---

## Part 7: Self-Assessment Rubric

Score yourself honestly. Total = 35 points. Target: ≥ 28 to be ready.

| Dimension | 5 | 3 | 1 | Your Score |
|---|---|---|---|---|
| Communication / Think-Aloud | Narrated approach, trade-offs, and test cases clearly throughout | Narrated most of the process with minor gaps | Coded silently or skipped narration | /5 |
| Problem Solving | Identified BFS + stack immediately, explained the "level_size trick" and the matching dict cleanly | Got to the right approach after some exploration | Needed to see the solution before understanding the approach | /5 |
| Correctness | Both solutions correct and handle all edge cases (empty tree, empty string, mismatched brackets) | One solution correct, one had a bug that was caught in testing | One or both solutions incorrect even after testing | /5 |
| Code Quality | Clean, readable variable names, no unnecessary code, well-structured | Mostly clean with minor issues | Messy, hard to follow, magic numbers | /5 |
| Testing & Edge Cases | Proactively tested: empty inputs, single nodes, deeply nested, mismatched brackets | Tested most cases but missed one edge case | Only tested the happy path | /5 |
| Debugging | Caught and corrected at least one error during implementation or testing | Got confused by an error but eventually resolved it | Could not debug without seeing the solution | /5 |
| Growth Mindset | Reflected authentically on what was hard and what you'd do differently; framed difficulty as learning | Some reflection but mostly "I got it" | No reflection, or claimed no difficulties | /5 |

**Total: /35**

---

### Reflection

What's the one thing you'll do differently in your next Microsoft interview?
[blank]

---

### Ready-When Checklist

- [ ] I can implement BFS level-order from scratch in under 10 minutes
- [ ] I can implement valid parentheses with a stack from scratch in under 8 minutes
- [ ] I can explain the "level_size snapshot trick" in one sentence
- [ ] I can explain why the matching dict works in one sentence
- [ ] I have a genuine growth-mindset story ready that connects to a technical experience
- [ ] Self-score ≥ 28/35
