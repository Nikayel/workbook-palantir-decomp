# Lab 01 — Low-Level Debugging in C: Memory Pool Allocator

**Company:** Nvidia
**Role:** SWE (systems)
**Style:** Low-level/debugging — find bugs in C code, pointer semantics, integer arithmetic
**Tier:** 1
**Estimated time:** 45 minutes
**Status: Ready — work through all parts in order**

---

## Milestones

- [ ] M1 · Read — described what the allocator is trying to do before finding any bugs
- [ ] M2 · Found bugs — identified all 3 with line numbers and root cause (mechanism, not just symptom)
- [ ] M3 · Fixed bug 1 — dangerous dangling pointer: `return pool->pool + i * BLOCK_SIZE`
- [ ] M4 · Fixed bug 2 — bounds check before computing block_index in pool_free()
- [ ] M5 · Fixed bug 3 — operator precedence / integer arithmetic order in get_usage_percent()
- [ ] M6 · Intellectual honesty — named at least one thing you'd need to look up (e.g., thread safety, valgrind flags)

---

## Scenario

"You're in an Nvidia technical screen. The interviewer says:

'Here's a ~250-line C program that implements a simple memory pool allocator. It has 3 bugs. Find and fix them. Narrate your reasoning as you go — we care about your process, not just the final answer.'

You have 45 minutes."

**What this tests:** C pointer semantics (stack vs heap lifetime), bounds checking discipline, integer arithmetic order, and — critically at Nvidia — intellectual honesty about what you know vs what you'd need to verify.

---

## Part 0: Forethought (Before Reading the Code)

"What does a memory pool allocator do? Why would you use one instead of malloc()?"
```
[blank — think: pre-allocated block, fixed-size chunks, avoids fragmentation, predictable latency]
```

"Name 3 common bugs in manual memory management C code:"
```
[blank — e.g., dangling pointer, double free, buffer overflow, use-after-free, null dereference]
```

"What tool would you use to find a dangling pointer in C code at runtime?"
```
[blank — valgrind --leak-check=full, or AddressSanitizer (-fsanitize=address)]
```

---

## The Buggy C Code

```c
// memory_pool.c — simple memory pool allocator (has 3 bugs)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define POOL_SIZE 1024
#define BLOCK_SIZE 64
#define NUM_BLOCKS (POOL_SIZE / BLOCK_SIZE)

typedef struct {
    uint8_t pool[POOL_SIZE];      // The actual memory pool
    uint8_t used[NUM_BLOCKS];     // 0 = free, 1 = used
    int num_allocated;
} MemoryPool;

/*
 * pool_create: allocate and initialize a new memory pool.
 * Returns NULL on allocation failure.
 */
MemoryPool* pool_create(void) {
    MemoryPool* pool = malloc(sizeof(MemoryPool));
    if (!pool) return NULL;
    memset(pool->pool, 0, POOL_SIZE);
    memset(pool->used, 0, NUM_BLOCKS);
    pool->num_allocated = 0;
    return pool;
}

/*
 * pool_alloc: allocate one block from the pool.
 * Returns a pointer to the block, or NULL if the pool is full.
 */
void* pool_alloc(MemoryPool* pool) {
    for (int i = 0; i < NUM_BLOCKS; i++) {
        if (!pool->used[i]) {
            pool->used[i] = 1;
            pool->num_allocated++;
            // BUG 1: returns pointer to stack variable instead of pool memory
            int offset = i * BLOCK_SIZE;
            return &offset;  // <-- returns address of local variable (dangling pointer)
        }
    }
    return NULL;  // pool full
}

/*
 * pool_free: release a block back to the pool.
 * ptr must be a pointer previously returned by pool_alloc.
 */
void pool_free(MemoryPool* pool, void* ptr) {
    // BUG 2: doesn't validate that ptr is actually within the pool bounds
    uint8_t* base = pool->pool;
    int offset = (uint8_t*)ptr - base;
    int block_index = offset / BLOCK_SIZE;
    // If ptr is outside the pool, offset can be negative or > POOL_SIZE,
    // causing block_index to be out of bounds — undefined behavior
    pool->used[block_index] = 0;
    pool->num_allocated--;
}

/*
 * pool_get_usage_percent: return the percentage of blocks currently allocated.
 */
int pool_get_usage_percent(MemoryPool* pool) {
    // BUG 3: integer arithmetic order truncates to 0 for small num_allocated
    return pool->num_allocated / NUM_BLOCKS * 100;
    // Example: 1 allocated, NUM_BLOCKS = 16
    // 1 / 16 = 0 (integer division truncates)
    // 0 * 100 = 0  <-- wrong, should be 6 (6.25%)
    // Fix: (pool->num_allocated * 100) / NUM_BLOCKS
}

/*
 * pool_destroy: free the memory pool itself.
 */
void pool_destroy(MemoryPool* pool) {
    free(pool);
    // Note: in debug builds, consider memset(pool, 0xDD, sizeof(*pool))
    // before free() to catch use-after-free sooner
}

int main(void) {
    MemoryPool* pool = pool_create();
    if (!pool) {
        fprintf(stderr, "Failed to create pool\n");
        return 1;
    }
    
    void* block1 = pool_alloc(pool);   // bug 1: block1 is a dangling pointer
    void* block2 = pool_alloc(pool);   // bug 1: same
    
    printf("Usage: %d%%\n", pool_get_usage_percent(pool));  // bug 3: prints 0
    
    pool_free(pool, block1);   // bug 2: block1 is not in pool bounds; UB
    pool_free(pool, block2);   // bug 2: same
    
    pool_destroy(pool);
    return 0;
}
```

---

## Part 1: Read Before Fixing (Intellectual Honesty Signal)

Spend 5 minutes reading only. No fixes yet.

"What is this code trying to do? Describe the intent of each function:"

**pool_create:**
```
[blank]
```

**pool_alloc:**
```
[blank — what is it supposed to return? What does it actually return?]
```

**pool_free:**
```
[blank — what invariant should it maintain?]
```

**pool_get_usage_percent:**
```
[blank — what is the expected output for 1 block allocated out of 16?]
```

**"Where would a memory error first become visible if you ran main()?"**
```
[blank — hint: the dangling pointer from block1 is used immediately in pool_free]
```

**"What would valgrind report if you compiled and ran this?"**
```
[blank — expected output: "invalid read/write" on pool_free, "use of uninitialized value" on &offset usage]
```

---

## Part 2: Bug Audit Table

Fill this in BEFORE writing fixes. Name the mechanism, not just the symptom.

| # | Function | Line(s) | Bug type | Root cause | Severity |
|---|---|---|---|---|---|
| 1 | pool_alloc | `return &offset` | [blank] | [blank — local var on stack; stack frame gone after return] | Critical — undefined behavior every time pool_alloc returns |
| 2 | pool_free | `int offset = ...` | [blank] | [blank — no validation of ptr bounds before computing block_index] | High — out-of-bounds write into used[] array |
| 3 | pool_get_usage_percent | `num_allocated / NUM_BLOCKS * 100` | [blank] | [blank — integer division truncates before multiply] | Low — logic error, wrong answer but no crash |

**What is undefined behavior (UB) in C?**
```
[blank — behavior not defined by the C standard; compiler may do anything: crash, give wrong answer, 
appear to work, or silently corrupt memory. Cannot be reasoned about without knowing the specific 
compiler and optimization level.]
```

**For bug 1: what does "dangling pointer" mean precisely?**
```
[blank — a pointer that refers to memory that has been freed or that no longer belongs to the 
variable it was pointing to. In this case: the stack frame for pool_alloc() is reclaimed after 
return; the address of `offset` is now pointing to whatever the stack happens to hold.]
```

---

## Part 3: Write the Fixes

**Fix 1: pool_alloc — return pointer into the pool, not into a local variable**

```c
void* pool_alloc(MemoryPool* pool) {
    for (int i = 0; i < NUM_BLOCKS; i++) {
        if (!pool->used[i]) {
            pool->used[i] = 1;
            pool->num_allocated++;
            // FIXED: return pointer into the heap-allocated pool array
            return pool->pool + i * BLOCK_SIZE;
        }
    }
    return NULL;
}
```

**Explain in words why `pool->pool + i * BLOCK_SIZE` is correct:**
```
[blank — pool->pool is a uint8_t array inside the heap-allocated MemoryPool struct.
Its lifetime is tied to the MemoryPool struct, which persists until pool_destroy().
Pointer arithmetic: pool->pool is the base address; adding i * BLOCK_SIZE gives the
address of block i within the pool. This is heap memory, not stack memory.]
```

**Fix 2: pool_free — validate bounds before use**

```c
void pool_free(MemoryPool* pool, void* ptr) {
    // FIXED: validate ptr is within pool bounds
    uint8_t* base = pool->pool;
    uint8_t* end = base + POOL_SIZE;
    
    if ((uint8_t*)ptr < base || (uint8_t*)ptr >= end) {
        // ptr is outside the pool — programming error
        // Options: assert(0), return early, fprintf(stderr, ...)
        fprintf(stderr, "pool_free: ptr %p is outside pool bounds [%p, %p)\n",
                ptr, base, end);
        return;
    }
    
    int offset = (uint8_t*)ptr - base;
    
    // Optional: also check alignment (ptr should be at a block boundary)
    if (offset % BLOCK_SIZE != 0) {
        fprintf(stderr, "pool_free: ptr %p is not block-aligned\n", ptr);
        return;
    }
    
    int block_index = offset / BLOCK_SIZE;
    pool->used[block_index] = 0;
    pool->num_allocated--;
}
```

**What additional check would make this even more robust?**
```
[blank — check that pool->used[block_index] == 1 before clearing it; 
otherwise double-free goes undetected and num_allocated becomes negative]
```

**Fix 3: pool_get_usage_percent — multiply before dividing**

```c
int pool_get_usage_percent(MemoryPool* pool) {
    // FIXED: multiply by 100 BEFORE dividing to avoid integer truncation
    return (pool->num_allocated * 100) / NUM_BLOCKS;
}
```

**Trace through both versions with num_allocated=1, NUM_BLOCKS=16:**
```
Buggy:   1 / 16 * 100 = [blank] * 100 = [blank]
Fixed:   1 * 100 / 16 = [blank] / 16  = [blank]
```

**What's the maximum value of num_allocated * 100 for this pool? Could it overflow int?**
```
[blank — NUM_BLOCKS = 16, max num_allocated = 16, 16 * 100 = 1600. 
Well within int range (max ~2 billion). For larger pools: use int64_t or check for overflow.]
```

---

## Part 4: Write the Fixed Version

Write the complete corrected memory_pool.c from scratch. All 3 bugs fixed, all defensive checks added:

```c
// memory_pool_fixed.c — corrected version
// [blank — write the complete file here]
```

---

## Part 5: Intellectual Honesty Reasoning

Answer these directly. If you're unsure, say so and describe how you'd find out.

**What C/C++ tool catches bug 1 (dangling pointer) at runtime?**
```
[blank — valgrind with --tool=memcheck, or compile with -fsanitize=address (AddressSanitizer)]
```

**What would happen if pool_free() is called with a NULL pointer?**
```
[blank — with the fixed version: (uint8_t*)NULL < base is true (NULL = 0x0, base > 0x0), 
so the bounds check catches it. Without the fix: ptr - base is a large positive or negative 
number (implementation-defined for NULL pointer arithmetic), causing OOB write. UB.]
```

**What's the difference between stack and heap memory? Why does bug 1 matter?**
```
Stack: [blank — automatic storage, LIFO, reclaimed when function returns, small (typically 8MB)]
Heap: [blank — dynamic allocation (malloc/new), persists until freed, can be large]
Why bug 1 matters: [blank — the caller receives an address into stack memory that will be 
overwritten by the next function call. Writing to it corrupts the stack. Reading from it 
returns garbage. This is UB and can cause security vulnerabilities (stack smashing).]
```

**What would you add to make pool_alloc and pool_free thread-safe? (If you're unsure, name what you'd research)**
```
Minimal change: [blank — add a pthread_mutex_t to MemoryPool; lock in pool_alloc and pool_free]
What I'd need to look up: [blank — be honest: e.g., "I know I need a mutex but I'd need to 
verify the exact API for static initializer vs PTHREAD_MUTEX_INITIALIZER"]
Lock-free approach: [blank — if you know it: compare-and-swap on used[i], but harder to implement correctly]
```

---

## Part 6: Curveballs

**Curveball 1: Make pool_alloc and pool_free Thread-Safe**
"The pool will now be used from multiple threads simultaneously. What's the minimal change?"

```c
// Modified MemoryPool struct:
typedef struct {
    uint8_t pool[POOL_SIZE];
    uint8_t used[NUM_BLOCKS];
    int num_allocated;
    // TODO: add synchronization primitive
    // [blank — pthread_mutex_t mutex; or std::mutex in C++]
} MemoryPool;

// Modified pool_alloc:
void* pool_alloc(MemoryPool* pool) {
    // TODO: lock before searching, unlock before return
    // [blank]
}
```

What's the performance cost of this approach?
```
[blank — every alloc/free takes the mutex; under heavy contention, threads serialize.
Alternative: per-CPU pools (jemalloc pattern), or lock-free CAS on used[] bits]
```

**Curveball 2: Variable-Size Allocations**
"The pool is 1KB, but now we need to support variable-size allocations (not just 64-byte blocks). How does the allocator design change fundamentally?"

```
Change 1: [blank — need to store block size metadata alongside each allocation]
Change 2: [blank — used[] bitmap no longer sufficient; need a free list or boundary tags]
Challenge: [blank — fragmentation: small freed blocks can't satisfy a large request]
Classic approach: [blank — first-fit, best-fit, buddy allocator, or slab allocator for fixed sizes]
```

**Curveball 3: Intellectual Honesty**
"What don't you know about memory allocators that you'd need to learn if this was your production project?"

```
Write your honest answer here:
[blank — e.g., "I understand the basics of free lists and buddy allocators conceptually, 
but I've never implemented one production-quality. I'd need to study fragmentation handling, 
alignment guarantees, and how real allocators like jemalloc handle size classes."]
```

---

## Part 7: Self-Assessment Rubric

Score yourself honestly. Target >= 28/35 before moving on.

| Dimension | 5 — Strong | 3 — Solid | 1 — Needs Work | Your Score |
|---|---|---|---|---|
| Code reading | Described allocator purpose accurately; identified all 3 bugs with line numbers | Found 2 bugs; purpose mostly correct | 0–1 bugs found or misread intent | __ /5 |
| Root cause analysis | Named mechanism: "dangling pointer to stack variable," "UB from OOB write," "integer truncation before multiply" | Named symptom: "returns wrong pointer," "crashes," "returns wrong number" | "Something is wrong here" with no mechanism | __ /5 |
| Fix quality | All 3 fixes are correct, minimal, and don't introduce new bugs | 2 fixes correct; 1 partial or incomplete | 1 fix correct; others incorrect or missing | __ /5 |
| C/C++ terminology | Correct use of: UB, dangling pointer, stack vs heap, pointer arithmetic, integer truncation | Mostly correct; 1–2 imprecise terms | Incorrect or absent terminology | __ /5 |
| Intellectual honesty | Named gaps proactively ("I'd need to verify thread safety API"); suggested what to research | Some uncertainty acknowledged | Bluffed through unknowns with confidence | __ /5 |
| Narration | Reasoned aloud at each step; named hypothesis before checking line | Narrated some steps | Silent debugging; went straight to fixing without explaining | __ /5 |
| Time management | Found all 3 bugs in < 30 min; time remaining for discussion and curveballs | Found all 3 but used most of 45 min | Ran out of time before fixing all 3 | __ /5 |

**Total: __ / 35**

---

## Reflection

**State bug 1 from memory in one sentence (mechanism, not symptom):**
```
[blank]
```

**What does `-fsanitize=address` do when you compile C code?**
```
[blank]
```

**If you got this problem in a real Nvidia interview, what would you say when you couldn't remember whether integer overflow is defined behavior in C?**
```
[blank — this is the intellectual honesty exercise. Write the exact words you'd say.]
```

---

## Ready-When Checklist

- [ ] I can describe all 3 bugs from memory (type, mechanism, fix) in < 2 minutes
- [ ] I can write the corrected pool_alloc, pool_free, and pool_get_usage_percent without notes
- [ ] I can explain "dangling pointer" and "undefined behavior" in plain language
- [ ] I can explain the thread-safety approach with a mutex at a conceptual level
- [ ] I have an honest "intellectual honesty" statement ready for what I'd need to look up
- [ ] I scored >= 28/35

---

*Next lab: `lab_02_thread_safe_queue` — implement bounded blocking queue in C++ with mutex + condition variables*
