# Company Pack — Nvidia

## 1. Snapshot
| Program | For | Length / timeline |
|---|---|---|
| **SWE / Systems SWE / AI-Tools Intern** | BS/MS/PhD, enrolled through internship | **min 12 wk**, year-round (summer largest) |
| **Hardware Intern** (ASIC/DV/arch/physical) | BS/MS/PhD | 12 wk |
| **AI/ML/Deep-Learning + PhD Research** | grad-skewed; publications valued | 12 wk; research → publishable |
| **Ignite** (pre-internship) | freshmen/sophomores | 12 wk, on-site Santa Clara |
> Apps open late Aug–early Sept; ~60%+ offers by end Nov. Comp $18–54/hr.

## 2. Culture & values (hiring signal)
Five values (Code of Conduct): **Innovation** ("Dream big, start small. Take risks, learn fast") · **Intellectual Honesty** ("Seek truth, learn from mistakes, share learnings") · **Speed and Agility** · **Excellence and Determination** · **One Team** ("Do what's best for the company"). Jensen layer: **"Speed of light"** (benchmark against the *physical limit*, not competitors); flat org (~60 directs, group feedback, "the mission is the boss"); failures broadcast company-wide; "profanity in service of intellectual honesty."

## 3. What's distinctive
- **Deep GPU / accelerated-computing / systems fundamentals** are weighted heavily — Nvidia rewards **hardware-software co-design** thinking, not app-level coding.
- **Intellectual honesty:** admit gaps, reason aloud, don't bluff. Bake into behavioral keys.

## 4. Assessment artifacts to replicate
- **HackerRank OA — gated** (portal applicants get it; **referral/career-fair often skip**). US ≈ 2–3 coding ~70–90 min DSA. India "SSE" ≈ 60-min HackerRank: ~25–28 MCQ (½ aptitude prob/perms/speed-distance; ½ technical OS/DSA/C-C++ guess-output) + 2 coding, COA-heavy, ~60% bar. ChatGPT banned.
- **Short, phone/virtual-only intern loop** — recruiter/HM → 1–2 technical with engineers from the team (~1–2 h). Ignite can be a single 30-min round. No full onsite for interns.
- **Practical/low-level rounds:** debugging/code-reading (bugs in a ~250-line C program; constructor/destructor leak), **implement-a-primitive** (thread-safe queue, **shared_ptr with refcount**, memory allocator, in-memory filesystem). Process + tradeoff narration > raw correctness.

## 5. Role tracks
**SWE.** Algorithmic baseline (LeetCode-Medium) **with a low-level skin**. Over-index: **pointers & memory** (signature — output prediction, signed/unsigned, value-vs-reference), C/C++ internals (vtables/virtual, smart pointers, function pointers), **OS** (threads/virtual-memory/deadlocks/IPC), bit manipulation & math/aptitude, **parallelism/CUDA** (team-gated). DP/Trie/graphs favorites. Languages: **C/C++ expected** (systems/CUDA/compiler/driver); Python for ML/DL.
**PM / Technical PM.** Higher technical bar than peers. Know the product lines (data center, gaming RTX, robotics, automotive) + stack (**CUDA / TensorRT / cuDNN**); explain how GPUs accelerate training/inference via parallel matrix ops; **HW-SW constraint tradeoffs** (memory bandwidth, training-vs-inference economics) + "explain deep learning to a non-technical audience."

## 6. Lab build list
- SWE *workbooks*: `01` **pointers/memory output-prediction + debugging** lab (C/C++) (Tier 1) · `02` **implement-a-primitive** (thread-safe queue / shared_ptr) (Tier 2) · `03` OS/concurrency reasoning (Tier 2) · `04` **CUDA kernel-optimization** lab (Tier 2, team-gated stretch) · `05` **timed mock-OA** (Tier 3). All low-level/system-building; pure DSA + aptitude grinding → shared **drill kit**, *not* workbooks.
- Technical PM: `01` HW-SW constraint tradeoff lab (Tier 2) · `02` "explain deep learning simply" + GPU-product sense (Tier 2).

## 7. Authenticity notes
Use **C/C++** for systems labs and CUDA pseudocode for GPU labs. Real surfaces: GeForce/RTX, CUDA, Tensor Cores, DGX/data-center, Jetson/robotics, DRIVE/automotive. Model **Intellectual Honesty** ("I don't know X, here's how I'd reason about it") in keys. **2025–26 context:** AI-boom hiring expansion; internships are the **primary new-grad pipeline** (bar stays high).

## 8. Sources & confidence
SWE deep-dive + TPM + company briefs; nvidia careers/Code-of-Conduct, igotanoffer, interviewing.io, linkjob HackerRank, GeeksforGeeks SSE. **Confidence:** high on C++/pointers/systems over-index + gated OA + phone-only loop; **medium** on exact problem counts (candidate-reported).
