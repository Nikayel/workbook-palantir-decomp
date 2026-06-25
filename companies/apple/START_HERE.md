# Apple — Interview Prep START HERE

Status: Ready — work through all parts in order

---

## Snapshot

**Roles:** SWE Intern (team-specific), Hardware Intern, Design Intern, ML/AI Intern, AP

**Critical distinction:** Apple does NOT have a generalist intern rotation. You are matched to a SPECIFIC team during application. The interview process, questions, and expectations differ substantially by domain:
- iOS/macOS SWE teams → Swift, ARC, UIKit/SwiftUI, Obj-C runtime
- Embedded/silicon SWE teams → C/C++, memory management, implement malloc/allocator, bit manipulation
- ML/AI teams → PyTorch, model deployment, Core ML
- Hardware teams → digital design, verification, Verilog/SystemVerilog

**Timing:** Team-specific — no unified recruiting calendar. Most SWE intern cycles: Jan–Mar (summer start), Sep–Nov (January start). Full-time recruiting is rolling.

---

## Culture

### Secrecy and Need-to-Know

Apple's organizational culture is built on compartmentalization. Employees don't discuss projects outside their team, even internally. In interviews:
- Don't ask what your specific project will be (even if you're curious)
- Don't ask about unannounced products
- Do ask about the team's general domain, engineering challenges, and what success looks like in the role

### Craft and Quality

Apple culture prizes attention to detail above speed. "It just works" is not marketing — it is an internal engineering standard. What this means in interviews:
- Prefer correct and readable over clever and fast
- Name your edge cases explicitly
- If you're unsure of something, say so precisely — not vaguely

### Functional Organization

Apple is organized by function (all iOS engineers report up through one structure, not product teams). This means engineers work across many products over time. Domain depth within a function is more valued than product breadth.

### DRI — Directly Responsible Individual

Every decision at Apple has exactly one named DRI. No "the team decided" — someone is accountable. In interviews: when asked how you'd make a decision, name who should own it and why. When recounting past projects, be clear about what YOU specifically decided and did, not "we."

---

## What's Distinctive About Apple Interviews

### Team/Domain Depth Over Generic LeetCode

Apple interviewers care deeply about whether you actually understand their domain. An iOS interviewer who asks about retain cycles is not running LeetCode — they are checking whether you could contribute to a real iOS codebase on day one.

### No Standardized OA

Unlike Google, Amazon, and Meta, Apple typically does NOT use a standardized online assessment as the primary gate. The process varies by team:
- Some teams do a phone screen directly
- Some teams send a take-home
- Some teams start with a HireVue video screen

### Resume Deep-Dive is a Hallmark Round

Apple interviewers frequently spend 15–20 minutes asking detailed technical questions about your past projects. They want specifics: what was the bottleneck, why did you pick that data structure, what would you do differently. Have two or three projects you can discuss at implementation depth.

### Swift/ARC for iOS Teams

If you're targeting iOS/macOS:
- Know Automatic Reference Counting (ARC) mechanically: what counts as a strong reference, what creates a retain cycle, how `weak` and `unowned` prevent leaks
- Know closures as reference types and the `[weak self]` capture list pattern
- Know the difference between `@escaping` and non-escaping closures

### C/C++ for Embedded/Silicon Teams

If you're targeting embedded, silicon, or systems:
- Know pointers and pointer arithmetic cold
- Be prepared to implement malloc or a memory allocator from scratch
- Know bit manipulation: masking, shifting, two's complement
- Know the difference between stack and heap allocation and why it matters

---

## Lab Menu

### SWE Labs

| Lab | Style | Tier | Domain | Description |
|---|---|---|---|---|
| Lab 01 | Implement-a-data-structure | Tier 1 | All SWE | MinStack with O(1) getMin/getMax — Apple's practical implement-from-scratch approach |
| Lab 02 | iOS-skin (ARC + retain cycles) | Tier 2 | iOS/macOS | Swift retain cycle in PhotoFeedViewController — find it, fix it, implement NSCache |
| Lab 03 | Embedded-skin (pointers/malloc in C) | Tier 2 | Embedded/silicon | Implement a memory allocator; bit manipulation exercises |
| Lab 04 | Resume deep-dive + behavioral | Tier 2 | All roles | Guided deep-dive prep for 2–3 past projects; DRI framing |

### PM/PMM Labs

| Lab | Style | Tier | Description |
|---|---|---|---|
| Lab 01 | Teardown + improve an Apple product | Tier 1 | Pick an Apple product; identify what's wrong; propose one measurable improvement |
| Lab 02 | Product tradeoffs case | Tier 2 | Build vs buy, privacy vs personalization, feature cuts — Apple-specific tradeoffs |

### EPM Labs

| Lab | Style | Tier | Description |
|---|---|---|---|
| Lab 01 | Program execution + dependency/risk | Tier 2 | Multi-team hardware-software program; build RACI + risk register |
| Lab 02 | Technical presentation prep | Tier 2 | Explain a complex system to a non-technical executive; rehearse the DRI framing |

---

## Before You Start

1. **Know which Apple team you're targeting.** iOS vs embedded vs ML is a fundamentally different interview. The labs in this package are separated by domain — do the labs that match your team.

2. **Respect secrecy culture.** You will be signing an NDA before starting. In interviews, don't probe for project details. Signal that you understand compartmentalization is how Apple operates.

3. **Think DRI.** In every behavioral story, name what YOU decided. "We decided" is a red flag. Apple wants to know what you owned.

4. **Practice the resume deep-dive.** Pick 2–3 projects. For each:
   - What was the hardest technical decision you made?
   - What data structure or algorithm choice did you make and why?
   - What would you do differently now?
   - What tradeoff did you accept and what did you give up?

5. **If you're an iOS candidate:** Run through ARC/retain cycles until you can draw the reference graph from memory. Lab 02 covers this.

6. **If you're an embedded candidate:** Practice implement-malloc cold. Be able to describe what `malloc()` does at the OS level (sbrk/mmap, heap bookkeeping). Lab 03 covers this.

---

## Quick Reference: Apple Interview Signals

| Signal | Positive | Negative |
|---|---|---|
| Domain knowledge | Knows Swift/ARC or C pointers deeply, domain-specific | Generic answers that could apply to any company |
| DRI framing | "I decided X because..." | "We decided X..." |
| Craft | Names edge cases proactively, handles None/nil defensively | Ships working-but-fragile code |
| Secrecy awareness | Doesn't ask about unreleased products | Probes for project details |
| Attention to detail | Catches the off-by-one, handles the empty state | Misses corner cases that affect real users |
| Resume depth | Can discuss implementation details for any line on resume | Vague about own work: "I worked on performance" |
