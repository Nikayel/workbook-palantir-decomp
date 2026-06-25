# Flashcards — Lab 01 Low-Level Debugging in C

**Company:** Nvidia | **Lab:** 01 | **Style:** Dangling pointers, bounds checking, integer arithmetic

---

## Card 1: Dangling Pointer — Definition and Detection

**Q:** What is a dangling pointer? Name two tools that detect it at runtime.

**A:** A dangling pointer is a pointer that refers to memory that is no longer valid — either because it was freed (use-after-free) or because it pointed to a local variable whose stack frame has been reclaimed (as in bug 1 of this lab, where `return &offset` returns the address of a local variable that ceases to exist after the function returns).

Detection tools:
1. **Valgrind** (`valgrind --tool=memcheck ./program`): reports "use of uninitialized value," "invalid read/write"
2. **AddressSanitizer** (compile with `-fsanitize=address`): catches use-after-free and stack-use-after-return at runtime with minimal overhead (~2x slowdown vs 10-20x for valgrind)

---

## Card 2: Stack vs Heap Memory Lifetime

**Q:** What is the difference between stack and heap memory lifetime? Why does returning a pointer to a local variable cause undefined behavior?

**A:**
- **Stack:** Automatic storage duration. Variables exist while their enclosing function is executing. When the function returns, the stack frame is reclaimed — the memory is reused by the next function call.
- **Heap:** Dynamic storage duration. Memory persists until explicitly freed with `free()` (C) or `delete` (C++). Lifetime is programmer-controlled.

When you write `int offset = i * BLOCK_SIZE; return &offset;` in C: you're returning the address of a stack variable. After the function returns, that stack memory is no longer valid — it will be overwritten by the next function call's local variables. Any access via the returned pointer is undefined behavior.

---

## Card 3: Integer Arithmetic Order — Multiply Before Divide

**Q:** Why does `count / total * 100` fail for small `count` in C? What's the correct form?

**A:** In C (and C++, Java, etc.), integer division truncates toward zero. `1 / 16` = `0` (not 0.0625). Then `0 * 100 = 0`. You lose all precision.

**Correct form:** `(count * 100) / total`
- `1 * 100 = 100`
- `100 / 16 = 6` (still truncates, but now correctly rounds the percentage down)

**For exact floating-point result:** cast to double first: `(double)count / total * 100`

**Overflow check:** for large counts, `count * 100` could overflow `int`. For safety: use `int64_t` or check bounds before multiplying.

---

## Card 4: Bounds Checking Best Practice

**Q:** What checks should pool_free() perform before using a user-provided pointer?

**A:** A robust pool_free() should validate:
1. **Not NULL:** `if (ptr == NULL) return;`
2. **Within pool bounds:** `if ((uint8_t*)ptr < base || (uint8_t*)ptr >= base + POOL_SIZE)`
3. **Block-aligned:** `if (offset % BLOCK_SIZE != 0)` — pointer must point to the start of a block, not into the middle
4. **Block is actually allocated:** `if (pool->used[block_index] == 0)` — catches double-free

Without these, a caller passing a garbage pointer causes: out-of-bounds write to `used[]`, corrupting the allocator's metadata. In a real allocator this can be exploited for heap-based code execution attacks.

---

## Card 5: Null Pointer Dereference vs Dangling Pointer

**Q:** What is the difference between a null pointer dereference and a use-after-free (dangling pointer dereference)?

**A:**
- **Null pointer dereference:** `*ptr` where `ptr == NULL` (address 0). Almost always causes a segfault immediately (OS protects the zero page). Easy to detect — crashes at the exact point of error.
- **Dangling pointer dereference (use-after-free):** `*ptr` where `ptr` points to memory that was freed or is no longer valid. May or may not crash immediately — the memory might still contain the old value (appears to work), or it might be reused for something else (data corruption). Much harder to debug because the crash happens far from the error.

Null dereferences are visible. Dangling pointer bugs are sneaky.

---

## Card 6: Undefined Behavior (UB) in C — Definition

**Q:** What is "undefined behavior" in C? Why is it dangerous even if the program appears to work?

**A:** Undefined behavior is any operation whose result the C standard does not specify — the compiler is free to do anything. Examples: dereferencing a dangling pointer, signed integer overflow, reading an uninitialized variable, out-of-bounds array access.

Why dangerous even when "it works": modern C compilers use UB as a license for aggressive optimization. If the compiler proves code is unreachable (because executing it would be UB), it may delete it entirely. Programs that "work" in debug builds may silently malfunction in optimized builds. UB-based security vulnerabilities are common in production code.

Nvidia interview relevance: when you say "this causes UB," you're showing you understand the C memory model at a level beyond syntax.

---

## Card 7: Memory Pool Pattern — Purpose

**Q:** Why use a memory pool instead of calling malloc() directly?

**A:**
1. **Predictable latency:** malloc() may call into the OS (sbrk/mmap), which is slow and non-deterministic. A pool pre-allocates once; subsequent allocations are fast and bounded in time.
2. **No fragmentation:** all blocks are the same size; external fragmentation is impossible.
3. **Cache locality:** all pool blocks are contiguous in memory; better cache behavior than scattered heap allocations.
4. **Debugging:** easier to instrument, detect double-free, and bounds-check.

Used in: game engines (Unity/Unreal allocators), network packet buffers, real-time systems, CUDA memory management.

---

## Card 8: Nvidia "Intellectual Honesty" in Technical Interviews

**Q:** The interviewer asks: "How would you make this allocator thread-safe?" You know a mutex is involved but you've never implemented this exact pattern. What do you say?

**A:** The correct Nvidia answer: "I know a mutex would be the standard approach — you'd add a `pthread_mutex_t` to the MemoryPool struct, lock before searching for a free block in pool_alloc, and unlock before returning. I'd also need to verify whether the mutex should be recursive. For lock-free approaches, you'd use compare-and-swap on the `used` bitmap, but I'd want to look up the exact memory ordering guarantees needed before implementing that in production code."

This is exactly the intellectual honesty Nvidia values: name what you know, name the boundary of your certainty, and describe what you'd verify rather than bluffing.

---

## Card 9: Valgrind Output Interpretation Basics

**Q:** What does a typical valgrind error message look like for a dangling pointer, and what information does it give you?

**A:** Typical valgrind output:
```
==12345== Invalid read of size 4
==12345==    at 0x4005A3: pool_free (memory_pool.c:43)
==12345==    by 0x4005D1: main (memory_pool.c:68)
==12345==  Address 0x7ffd3c4a9b2c is on the stack
==12345==  in frame #0, created by pool_alloc (memory_pool.c:28)
```

Key parts:
- **Invalid read/write:** operation type
- **Size:** how many bytes were accessed
- **Stack trace:** exactly where in the code the bad access happened
- **Address description:** where the address points (stack, heap-freed, heap-uninitialized)

"Address is on the stack in frame created by pool_alloc" directly identifies bug 1: the address came from a stack variable in pool_alloc's frame.

---

## Card 10: Thread-Safe Allocator — Minimal Approach

**Q:** What is the minimal change to make pool_alloc() and pool_free() thread-safe?

**A:** Minimal approach: add a `pthread_mutex_t` to the MemoryPool struct. Lock at the start of pool_alloc and pool_free, unlock before returning.

```c
typedef struct {
    uint8_t pool[POOL_SIZE];
    uint8_t used[NUM_BLOCKS];
    int num_allocated;
    pthread_mutex_t mutex;  // ADD THIS
} MemoryPool;

void* pool_alloc(MemoryPool* pool) {
    pthread_mutex_lock(&pool->mutex);
    // ... existing search logic ...
    pthread_mutex_unlock(&pool->mutex);
    return result;
}
```

Cost: every allocation serializes. Under contention, throughput is limited by the mutex.

Nvidia "speed of light" framing: "The theoretical maximum throughput is one allocation per CPU cycle (no locking). A mutex gives us correctness but ~10-100x slowdown under contention. Lock-free CAS on the used[] bits is the direction to look for high-throughput production allocators."
