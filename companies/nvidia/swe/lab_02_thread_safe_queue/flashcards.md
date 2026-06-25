# Flashcards — Lab 02 Thread-Safe Bounded Queue

**Company:** Nvidia | **Lab:** 02 | **Style:** mutex + condition_variable, RAII, producer-consumer

---

## Card 1: Mutex vs Semaphore vs Condition Variable

**Q:** What are the differences between a mutex, a semaphore, and a condition variable? When do you use each?

**A:**
- **Mutex (mutual exclusion):** Binary lock. One thread owns it at a time. Used to protect a critical section — shared state that only one thread should modify at once. pthread_mutex / std::mutex.
- **Semaphore:** Counter-based. Can be acquired by multiple threads up to a count. Signaling primitive. sem_post() / sem_wait(). Used for: limiting concurrent access (connection pool), signaling between threads (producer increments, consumer decrements).
- **Condition variable:** Allows a thread to sleep until a condition is true. Always used WITH a mutex. cv.wait(lock, predicate) atomically releases the lock and sleeps; when notified, reacquires the lock and re-checks the predicate. Used for: blocking until state changes (queue not empty, queue not full).

Use mutex for protection. Use CV for waiting on a changing condition. Use semaphore for counting/signaling.

---

## Card 2: RAII lock_guard Pattern

**Q:** What is RAII and how does lock_guard implement it?

**A:** RAII = Resource Acquisition Is Initialization. Resources (memory, locks, file handles) are tied to object lifetime: acquired in the constructor, released in the destructor. This guarantees cleanup even on exception.

`std::lock_guard<std::mutex> lock(mutex_)`:
- Constructor: calls `mutex_.lock()` — acquires the lock
- Destructor: calls `mutex_.unlock()` — releases the lock automatically when the lock_guard goes out of scope (end of block, early return, OR exception)

Without RAII: if you forget to call mutex_.unlock() (or an exception is thrown), the mutex stays locked. All other threads waiting for it deadlock forever. RAII makes this impossible.

---

## Card 3: Spurious Wakeup — Why `while` Not `if`

**Q:** What is a spurious wakeup? Why must you use a while loop (not if) with condition_variable.wait()?

**A:** A spurious wakeup is when a thread blocked on a condition_variable wakes up without being explicitly notified. The POSIX standard and C++ standard allow this — it's an implementation artifact of how condition variables are built on top of OS primitives.

If you write:
```cpp
if (!predicate()) cv.wait(lock);
// proceed assuming predicate is now true -- WRONG
```
...a spurious wakeup would proceed even when the predicate is still false (queue still empty, queue still full), causing incorrect behavior.

Correct form:
```cpp
while (!predicate()) cv.wait(lock);
// OR: cv.wait(lock, [this] { return predicate(); });
```
The lambda form is idiomatic C++11: it loops internally, re-checking the predicate after every wakeup (spurious or real).

---

## Card 4: notify_one vs notify_all

**Q:** When do you use notify_one() vs notify_all()? What is the "thundering herd" problem?

**A:**
- **notify_one():** Wakes exactly one thread waiting on the CV. Use when only one thread can make progress. For the bounded queue: after enqueue, only one consumer can take the new item — notify_one() is correct and efficient.
- **notify_all():** Wakes ALL threads waiting on the CV. All threads reacquire the mutex, re-check their predicate, and all but one go back to sleep. Use when: multiple threads might be able to make progress (e.g., capacity expands dramatically), or when you're not sure which thread to wake.

**Thundering herd:** With notify_all(), 100 sleeping consumers all wake, compete for the mutex, re-check, 99 go back to sleep. 100 mutex acquisitions, 1 does useful work. Under heavy contention, this is expensive. notify_one() avoids this.

---

## Card 5: Producer-Consumer Pattern

**Q:** Describe the producer-consumer pattern and where the bounded queue fits.

**A:** Producer-consumer is a classic concurrency pattern where producers generate items and put them on a shared buffer, and consumers take items and process them. The buffer decouples producer speed from consumer speed.

A **bounded queue** adds a capacity constraint:
- If producers are faster than consumers: queue fills up; producers block (natural backpressure)
- If consumers are faster than producers: queue empties; consumers block (no busy-waiting)

Real-world uses at Nvidia: GPU command queues (CPU produces GPU commands; GPU consumes them), network packet buffers, video frame pipelines, DMA ring buffers.

---

## Card 6: Bounded Queue vs Unbounded Queue

**Q:** When is an unbounded queue preferable to a bounded queue? What are the risks of each?

**A:**
- **Bounded queue:**
  - Pro: natural backpressure; limits memory use; prevents producers from running away
  - Con: producers can block, potentially causing upstream stalls
  - Use when: memory is precious; consumer slowness should propagate as pressure to producers

- **Unbounded queue:**
  - Pro: producers never block; simple to implement
  - Con: if consumers are slow, queue grows without bound; can exhaust memory and crash the process
  - Use when: producers must not block AND you have a bounded-in-practice workload

At Nvidia: for GPU command submission, bounded queues are used — if the GPU can't keep up, the CPU should slow down, not submit an infinite backlog.

---

## Card 7: Deadlock Conditions and Prevention

**Q:** Name the 4 conditions required for deadlock and how the BoundedQueue avoids it.

**A:** Coffman conditions (all 4 must hold simultaneously for deadlock):
1. **Mutual exclusion:** Thread holds a resource others can't use simultaneously
2. **Hold and wait:** Thread holds a resource while waiting for another
3. **No preemption:** Resources can't be forcibly taken
4. **Circular wait:** Thread A waits for B's resource; B waits for A's resource

BoundedQueue avoids deadlock because:
- **Only one mutex.** There is no circular wait — no thread holds this mutex and waits for a different mutex. Without two mutexes, circular wait is impossible.
- condition_variable.wait() atomically releases the mutex while sleeping and reacquires it on wake. It never holds the mutex and sleeps waiting for another resource.

Lock ordering rule: if you ever need multiple mutexes, always acquire them in the same global order. Violating this causes deadlock.

---

## Card 8: Lock Ordering Rule

**Q:** What is the lock ordering rule and why does it prevent deadlock?

**A:** When multiple mutexes must be acquired simultaneously:
- Always acquire them in the same fixed order, globally across all threads
- Thread A and Thread B always acquire mutex_1 first, then mutex_2 — never in reverse order

Without this rule: Thread A holds mutex_1, waits for mutex_2. Thread B holds mutex_2, waits for mutex_1. Circular wait = deadlock.

C++17 provides `std::scoped_lock(mutex_1, mutex_2)` which acquires multiple mutexes atomically without deadlock risk.

For BoundedQueue: only one mutex, so this rule is trivially satisfied.

---

## Card 9: C++11 Threading Basics

**Q:** Name the 4 key C++11 threading primitives and what each does.

**A:**
1. **`std::thread`:** Creates a new thread. `std::thread t(func, args...)`. Call `t.join()` to wait for it; `t.detach()` to let it run independently.
2. **`std::mutex`:** Mutual exclusion lock. `lock()` / `unlock()`. Use with lock_guard or unique_lock, never raw.
3. **`std::lock_guard<M>`:** RAII wrapper for mutex. Acquires on construction, releases on destruction. Non-movable, non-copyable.
4. **`std::unique_lock<M>`:** RAII wrapper with manual lock/unlock capability. Required for `condition_variable.wait()` because wait() needs to release the lock temporarily.
5. **`std::condition_variable`:** `wait(unique_lock, predicate)`, `notify_one()`, `notify_all()`.

---

## Card 10: Nvidia "Speed of Light" — Maximum Queue Throughput

**Q:** What is the theoretical maximum throughput of a mutex-protected bounded queue? How do you reason about it in an Nvidia interview?

**A:** The "speed of light" framing: what's the theoretical maximum if we removed all overhead?

**Theoretical maximum:** the rate at which items can be moved through memory — bounded by memory bandwidth (on a modern machine: ~100-1000 GB/s depending on cache effects).

**Actual bottleneck with mutex:** the mutex itself. Under heavy contention:
- Each acquire/release takes ~50-100ns (L3 cache line bounce between CPU cores)
- Maximum throughput: ~10M ops/sec per thread pair under contention

**Lock-free alternative:** An atomic ring buffer with CAS (compare-and-swap) on head/tail indices can approach cache-line-bandwidth limits — ~100-500M ops/sec.

Nvidia interview answer: "My mutex implementation is correct, but the speed of light for this problem is a lock-free SPSC (single-producer single-consumer) queue using atomics and a ring buffer, which would approach the memory bandwidth limit. The mutex is the right starting point; I'd profile before optimizing."
