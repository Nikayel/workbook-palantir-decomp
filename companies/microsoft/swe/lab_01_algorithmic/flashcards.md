# Flashcards — Microsoft SWE Lab 01: Algorithmic + Growth Mindset

---

**Card 01 — BFS Template (Queue + Level Size Trick)**

Q: What's the BFS level-order template and why does `level_size = len(queue)` matter?

A:
```python
from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)   # snapshot: nodes on THIS level
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```
`level_size` captures the queue length BEFORE processing any children. Children added inside the loop belong to the NEXT level — so processing exactly `level_size` nodes guarantees correct level boundaries.

---

**Card 02 — Valid Parentheses Stack Invariant**

Q: What is the core invariant for the valid-parentheses stack solution?

A: When you encounter a **closing bracket**, the **top of the stack must be its matching opener**. If the stack is empty or the top doesn't match, return False immediately. At the end, the stack must be empty (every opener was closed). The matching dict `{')':'(', ']':'[', '}':'{'}` makes the check O(1).

---

**Card 03 — Growth Mindset Framing**

Q: How do you frame a coding difficulty using Microsoft's growth mindset language?

A: Use "I learned..." not "I knew..."

Bad: "I already knew BFS so this was straightforward."
Good: "I hadn't used the level-size snapshot trick before. I initially looped without capturing the count and got confused when the queue grew mid-loop. I realized I needed to snapshot the size first — that was the key insight I'll carry forward."

Microsoft explicitly trains interviewers to look for authentic learning framing.

---

**Card 04 — Microsoft STAR Structure**

Q: How does Microsoft's STAR behavioral structure differ from standard STAR?

A: Microsoft STAR has a mandatory fifth element:

- **S**ituation — set the scene
- **T**ask — what was your role
- **A**ction — what you did (specific, not "we")
- **R**esult — measurable outcome
- **L**earned — what you'd do differently / what you grew from

The "L" (Learned) is non-negotiable. Omitting it signals a fixed mindset.

---

**Card 05 — Codility OA Format**

Q: What is the Microsoft Codility OA format?

A:
- Duration: 90 minutes
- Problems: 2 problems (typically easy + medium difficulty)
- Environment: Codility platform, auto-graded, not proctored live
- Problem types: Trees, strings, arrays, graphs — clean algorithmic problems
- Superday version: same type of problem but with a live interviewer watching
- Tip: submit early if confident; the timer counts down visibly

---

**Card 06 — "Learn-It-All vs Know-It-All"**

Q: What does Satya Nadella mean by "learn-it-all beats know-it-all"?

A: Nadella's thesis: fixed mindset = "I already know this"; growth mindset = "I can learn anything." In practice, this means Microsoft interviewers prefer candidates who:
1. Acknowledge gaps honestly
2. Describe how they filled those gaps
3. Extrapolate learning to future situations

An interviewer who asks "Tell me about a time you failed" is not looking for perfection. They're looking for evidence that you process failure into growth.

---

**Card 07 — OOD in Microsoft Culture**

Q: Why does OOP/LLD appear more at Microsoft than at Google or Meta?

A: Microsoft's engineering culture is rooted in C#/.NET, which emphasizes object-oriented design principles. Microsoft products (Office, Azure, Windows) are built on large, long-lived class hierarchies. Interviewers — many of whom work on these products — naturally gravitate toward LLD questions like: "Design this class," "Make it extensible," or "How would you add a new type without modifying existing code?"

---

**Card 08 — Tree Traversal Variants**

Q: Name the four main binary tree traversal orders and when to use each.

A:
- **In-order (L-Root-R)**: gives sorted output for BSTs
- **Pre-order (Root-L-R)**: good for copying/serializing a tree
- **Post-order (L-R-Root)**: good for deleting a tree (process children before parent)
- **Level-order (BFS)**: processes nodes level by level; use when you care about depth or tree layers

---

**Card 09 — When to Use BFS vs DFS**

Q: BFS vs DFS — when do you pick each?

A:
- **BFS**: shortest path in unweighted graph, level-by-level processing, "closest X to source," finding nearby nodes first
- **DFS**: cycle detection, topological sort, connected components, exhaustive path search, tree height/depth problems
- Memory: BFS uses O(width) space; DFS uses O(height) space. For wide shallow trees → DFS; for tall narrow trees → BFS.
- Both are O(V + E).

---

**Card 10 — Superday Format (15 Min Behavioral Per Round)**

Q: Describe the Microsoft Superday format and how behavioral fits in.

A:
- 3-4 rounds, back-to-back
- Each round: **~15 minutes behavioral first**, then ~30-35 minutes coding or product question
- The behavioral happens at the START of each round, not the end
- Each round uses a different behavioral question (not the same STAR story)
- Prepare at least 4-5 distinct STAR+L stories covering: failure, learning, conflict, impact, teamwork
- After Superday: hiring committee review, offer decision typically within 1-2 weeks
