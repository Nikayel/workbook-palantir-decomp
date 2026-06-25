# Lab 02 — Implement a Primitive: Thread-Safe Bounded Queue

**Company:** Nvidia
**Role:** SWE (systems)
**Style:** Implement-a-primitive — thread-safe bounded queue in C++ with mutex + condition variables
**Tier:** 2
**Estimated time:** 45 minutes
**Status: Ready — work through all parts in order**

---

## Milestones

- [ ] M1 · Clarified — asked about: blocking vs non-blocking variants, timeout on block, FIFO guaranteed, exception safety
- [ ] M2 · Named the primitives — identified mutex + condition variables (not spin lock, not semaphore) before coding
- [ ] M3 · Coded — working C++ implementation with proper RAII locking (lock_guard or unique_lock)
- [ ] M4 · No deadlock — reasoned through the locking protocol; verified only one lock acquired per operation
- [ ] M5 · Tested reasoning — traced through: single producer/consumer, multiple producers racing, capacity=1
- [ ] M6 · Ready — self-graded >= 28/35

---

## Scenario

"You're in an Nvidia technical round. The interviewer says:

'Implement a thread-safe bounded queue in C++. It should support:
- `enqueue(item)` — blocks if the queue is full, until space is available
- `dequeue()` — blocks if the queue is empty, until an item is available
- Maximum capacity is set at construction time.
This is a classic producer-consumer queue.'

You have 45 minutes."

**What this tests:** C++ concurrency primitives (mutex, condition_variable), RAII locking discipline, spurious wakeup handling, deadlock avoidance, and — at Nvidia — "speed of light" reasoning about maximum throughput.

---

## Part 0: Forethought (Before Looking at Starter Code)

"What are the 3 classic concurrency problems?"
```
[blank — race condition, deadlock, starvation]
```

"What is a race condition?"
```
[blank — two threads access shared state without synchronization; result depends on thread scheduling]
```

"Why would you block on enqueue() instead of returning false when the queue is full?"
```
[blank — blocking enables the producer-consumer pattern: producers don't need to poll; 
they block automatically when consumers are behind, creating natural backpressure]
```

"Name the primitives you'll need:"
```
[blank — std::mutex, std::condition_variable, std::unique_lock]
```

---

## Part 1: Clarifying Questions

Simulate asking these before writing code:

| Question | Assumption for this exercise |
|---|---|
| Blocking or non-blocking enqueue/dequeue? | [blank — blocking (the interesting case)] |
| Timeout support needed? | [blank — not required for this implementation] |
| FIFO order guaranteed? | [blank — yes, std::queue gives FIFO] |
| Exception safety? | [blank — basic guarantee: if exception thrown, queue is valid but operation may not complete] |
| Multiple producers and consumers? | [blank — yes, must support arbitrary N producers + M consumers] |
| What T can be stored? | [blank — any type for this template; assume copyable for simplicity] |

---

## Part 2: Design Before Coding

"Which synchronization primitives do you need and why?"

**Mutex:**
```
Purpose: [blank — protects shared state: data_, size count. Only one thread modifies at a time.]
```

**Condition variable "not_full":**
```
Purpose: [blank — enqueue() waits on this when queue is full. notify called after dequeue removes an item.]
```

**Condition variable "not_empty":**
```
Purpose: [blank — dequeue() waits on this when queue is empty. notify called after enqueue adds an item.]
```

"Why two condition variables instead of one?"
```
[blank — with one CV, a producer could accidentally wake another producer instead of a consumer.
With two CVs: producers wait on not_full (woken by consumers); consumers wait on not_empty (woken by producers).]
```

"Why condition_variable instead of a spin lock?"
```
[blank — spin lock burns CPU cycles while waiting. condition_variable blocks the thread and yields 
the CPU to other work. For a bounded queue where waits can be long (producer far ahead of consumer),
spinning is wasteful. condition_variable is the correct primitive.]
```

---

## Part 3: Starter Code — Fill in the TODOs

```cpp
#include <queue>
#include <mutex>
#include <condition_variable>
#include <stdexcept>

template<typename T>
class BoundedQueue {
private:
    std::queue<T> data_;
    size_t capacity_;
    std::mutex mutex_;
    std::condition_variable not_full_;   // TODO: was declared here as a blank
    std::condition_variable not_empty_;  // TODO: was declared here as a blank

public:
    explicit BoundedQueue(size_t capacity) : capacity_(capacity) {
        if (capacity == 0) {
            throw std::invalid_argument("BoundedQueue: capacity must be > 0");
        }
    }
    
    // enqueue: add item to the back. Blocks if queue is full.
    void enqueue(T item) {
        // TODO: acquire lock, wait while full, push, notify
        // [blank]
    }
    
    // dequeue: remove and return item from the front. Blocks if queue is empty.
    T dequeue() {
        // TODO: acquire lock, wait while empty, pop front, notify, return
        // [blank]
    }
    
    // size: thread-safe snapshot of current queue size.
    size_t size() {
        // TODO: acquire lock, return size, release
        // [blank]
    }
    
    // empty: thread-safe check.
    bool empty() {
        std::lock_guard<std::mutex> lock(mutex_);
        return data_.empty();
    }
    
    // Disallow copying (mutex and cv are not copyable).
    BoundedQueue(const BoundedQueue&) = delete;
    BoundedQueue& operator=(const BoundedQueue&) = delete;
};
```

---

## Part 4: Reference Solution (Study, Then Implement from Scratch)

Read this solution carefully. Then close it and implement it yourself in the "Your Implementation" section.

```cpp
#include <queue>
#include <mutex>
#include <condition_variable>
#include <stdexcept>

template<typename T>
class BoundedQueue {
private:
    std::queue<T> data_;
    size_t capacity_;
    std::mutex mutex_;
    std::condition_variable not_full_;
    std::condition_variable not_empty_;

public:
    explicit BoundedQueue(size_t capacity) : capacity_(capacity) {
        if (capacity == 0) {
            throw std::invalid_argument("BoundedQueue: capacity must be > 0");
        }
    }
    
    void enqueue(T item) {
        // Step 1: Acquire the lock using unique_lock (required for condition_variable.wait())
        std::unique_lock<std::mutex> lock(mutex_);
        
        // Step 2: Wait while the queue is full.
        // IMPORTANT: use while loop, NOT if. Spurious wakeups can occur — the thread
        // can wake even when the condition is still false. The while loop re-checks.
        not_full_.wait(lock, [this] { return data_.size() < capacity_; });
        // Equivalent to:
        // while (data_.size() >= capacity_) { not_full_.wait(lock); }
        
        // Step 3: Push the item (we hold the lock, size is < capacity)
        data_.push(std::move(item));
        
        // Step 4: Notify ONE waiting consumer that the queue is now non-empty.
        // lock is still held here (released when unique_lock goes out of scope).
        not_empty_.notify_one();
        
        // Step 5: unique_lock destructor releases the lock automatically (RAII).
    }
    
    T dequeue() {
        std::unique_lock<std::mutex> lock(mutex_);
        
        // Wait while queue is empty (while loop handles spurious wakeups).
        not_empty_.wait(lock, [this] { return !data_.empty(); });
        
        // Retrieve the front item.
        T item = std::move(data_.front());
        data_.pop();
        
        // Notify ONE waiting producer that there is now space.
        not_full_.notify_one();
        
        return item;
    }
    
    size_t size() {
        // lock_guard is fine here — no condition_variable.wait() needed.
        std::lock_guard<std::mutex> lock(mutex_);
        return data_.size();
    }
    
    bool empty() {
        std::lock_guard<std::mutex> lock(mutex_);
        return data_.empty();
    }
    
    BoundedQueue(const BoundedQueue&) = delete;
    BoundedQueue& operator=(const BoundedQueue&) = delete;
};
```

---

## Your Implementation (Write from Scratch)

```cpp
// Implement BoundedQueue from memory here:
// [blank]
```

---

## Part 5: Concurrency Reasoning

**Why `while` loop (or the lambda form of wait()) instead of `if`?**
```
[blank — spurious wakeups: POSIX condition variables can wake a waiting thread even when 
the condition was not signaled. This is implementation-defined behavior. The standard C++
condition_variable is allowed to have spurious wakeups. The while loop re-checks the 
predicate after every wakeup, spurious or not. The lambda form of wait() does this automatically:
cv.wait(lock, predicate) is equivalent to: while (!predicate()) cv.wait(lock);]
```

**What is RAII and how does lock_guard use it?**
```
[blank — RAII: Resource Acquisition Is Initialization. Resources are tied to object lifetime.
lock_guard<mutex> acquires the lock in its constructor and releases it in its destructor.
This means the lock is released automatically when the lock_guard goes out of scope —
even if an exception is thrown. You cannot forget to unlock.]
```

**What happens if you forget to call notify_one() after enqueue()?**
```
[blank — consumers that called dequeue() and are blocked on not_empty_.wait() will 
sleep forever (or until another producer happens to notify). The queue will have items 
in it but consumers won't know. This is a liveness failure (starvation/deadlock depending 
on whether producers are also blocked).]
```

**notify_one() vs notify_all() — when to use each?**
```
notify_one(): [blank — wake one waiting thread. Use when only one thread can make progress 
(bounded queue: only one consumer can dequeue the one item added). Preferred for performance.]
notify_all(): [blank — wake ALL waiting threads. Use when multiple threads may be able to 
make progress, or when waking the wrong one would cause starvation. Cost: thundering herd — 
all wake, re-check condition, all but one go back to sleep. Expensive under high contention.]
For this bounded queue: notify_one() is correct. Only one consumer can use the one slot opened.]
```

**Why does unique_lock work with condition_variable but lock_guard does not?**
```
[blank — condition_variable.wait() must temporarily release the lock while sleeping and 
re-acquire it before returning. lock_guard does not expose unlock()/lock() operations — 
you can't temporarily release it. unique_lock does expose these operations, which is what 
condition_variable.wait() needs internally.]
```

---

## Part 6: Trace Through Scenarios

**Scenario A: Single producer, single consumer, capacity=2**

```
Initial state: queue = [], size = 0, capacity = 2

Producer calls enqueue("A"):
  - acquires lock
  - size (0) < capacity (2): no wait
  - pushes "A"
  - calls not_empty_.notify_one()
  - releases lock
  queue = ["A"], size = 1

Consumer calls dequeue():
  - acquires lock
  - queue not empty: no wait
  - removes "A"
  - calls not_full_.notify_one()
  - releases lock, returns "A"
  queue = [], size = 0
```

Trace the scenario where capacity=1 and the producer gets there first:
```
Producer calls enqueue("X") — what happens? [blank]
Producer calls enqueue("Y") immediately after (queue is full) — what happens? [blank]
Consumer calls dequeue() — what happens, and what does the producer do? [blank]
```

**Scenario B: Deadlock check**

"Can this implementation deadlock?"
```
[blank — single mutex, acquired once per operation. No nested locking. 
Deadlock requires circular wait: thread A holds lock A waiting for lock B, 
thread B holds lock B waiting for lock A. We have one lock — no circular wait possible.
Conclusion: deadlock-free by construction.]
```

**Scenario C: Multiple producers race on capacity=1**

```
Producer 1 and Producer 2 both call enqueue() simultaneously, queue is empty, capacity=1.

- Both call lock()
- Only one acquires the lock (P1 wins)
- P1: size=0 < 1, no wait. Pushes item. notify_one(). unlock.
- P2: lock acquired. size=1 == capacity. Waits on not_full_.

Consumer dequeues:
- acquires lock, size=1, dequeues, calls not_full_.notify_one(), unlock.
- P2 wakes, re-checks: size=0 < 1 (predicate true). Pushes item. notify_one(). unlock.

Correct behavior achieved. [verify your reasoning matches this]
```

---

## Part 7: Curveballs

**Curveball 1: try_enqueue (Non-Blocking Variant)**
"Add a `try_enqueue(item)` method that returns false immediately if the queue is full instead of blocking."

```cpp
bool try_enqueue(T item) {
    std::lock_guard<std::mutex> lock(mutex_);
    if (data_.size() >= capacity_) {
        return false;  // non-blocking: return immediately
    }
    data_.push(std::move(item));
    not_empty_.notify_one();
    return true;
}
```

"Why lock_guard instead of unique_lock here?"
```
[blank — no condition_variable.wait() call needed; lock_guard is simpler and sufficient]
```

**Curveball 2: Speed of Light**
"What is the theoretical maximum throughput of your BoundedQueue? What limits you?"

```
Theoretical max (no synchronization): [blank — the memory bandwidth to copy T items]
Actual limit: [blank — mutex acquisition cost, cache line bouncing between threads, 
condition_variable syscalls when blocking]
Nvidia framing: [blank — "If I could avoid the mutex entirely and use a lock-free circular 
buffer with atomic compare-and-swap on head/tail indices, I could approach the memory bandwidth 
limit. That's the speed of light for this problem."]
```

**Curveball 3: Implement with Semaphores Instead**
"How would you implement this using semaphores instead of condition variables?"

```
Design: [blank — two semaphores: 'slots' (count = capacity, decremented by producer, 
incremented by consumer) and 'items' (count = 0, incremented by producer, decremented by consumer)]
Mutex still needed?: [blank — yes, to protect the queue data structure itself; semaphores 
don't protect shared state, they only count]
Tradeoff vs condition_variable: [blank — semaphores are simpler to reason about; 
condition_variable is more flexible (arbitrary predicates) but harder to implement correctly]
```

**Curveball 4: What if T's Copy Constructor Throws?**
"enqueue() calls `data_.push(std::move(item))`. What if the move constructor throws?"

```
[blank — with std::move, if T's move constructor throws, the exception propagates from enqueue().
The lock is still released (RAII unique_lock). The item was never successfully added.
std::queue::push() provides strong exception safety if T's constructor provides it.
This is the "basic guarantee" mentioned in our clarifying questions: queue is valid, 
item not added.]
```

---

## Part 7: Self-Assessment Rubric

Score yourself honestly. Target >= 28/35 before moving on.

| Dimension | 5 — Strong | 3 — Solid | 1 — Needs Work | Your Score |
|---|---|---|---|---|
| Clarifying questions | Asked about blocking behavior, timeout, multiple producers/consumers, exception safety | Asked about 2–3 of these | Jumped straight to code | __ /5 |
| Primitives selection | Named mutex + condition_variable; explained why not spin lock; named two CVs correctly | Named mutex + CV; unsure why two CVs | Chose semaphore or spin lock without reasoning | __ /5 |
| Implementation correctness | enqueue/dequeue both correct; while loop for wait; RAII locking; notify_one correctly placed | Core logic correct; spurious wakeup or notify missed | Deadlock risk or incorrect blocking | __ /5 |
| RAII / unique_lock | Correctly used unique_lock for CV; lock_guard for simple lock; explained why unique_lock is needed | Used correctly; could not explain why | Used lock_guard with CV (compile error) | __ /5 |
| Concurrency reasoning | Traced spurious wakeup scenario; deadlock proof; multiple producers race scenario | Explained most scenarios; missed one | Could not reason about thread interleaving | __ /5 |
| Speed of light framing | Named theoretical max (memory bandwidth); identified mutex as bottleneck; mentioned lock-free as direction | Named some limits | No throughput reasoning | __ /5 |
| Curveball handling | Implemented try_enqueue; addressed semaphore approach; exception safety | One curveball handled | Could not handle curveballs | __ /5 |

**Total: __ / 35**

---

## Reflection

**What's the one-sentence explanation of why `while` not `if` for condition_variable.wait()?**
```
[blank]
```

**Draw the lock acquisition order for enqueue() and dequeue(). Is there a deadlock risk?**
```
[blank]
```

**What would you say to an Nvidia interviewer who asks: "What's the speed of light for throughput on a 16-core machine with your queue?"**
```
[blank — write the exact answer, including what you know and what you'd need to measure]
```

---

## Ready-When Checklist

- [ ] I can implement BoundedQueue from scratch in < 20 minutes without notes
- [ ] I can explain spurious wakeups and why the while loop (or lambda form of wait) handles them
- [ ] I can explain why unique_lock is required (vs lock_guard) for condition_variable
- [ ] I can trace the multiple-producers race and show it's correct
- [ ] I can state the speed-of-light throughput argument for this queue
- [ ] I scored >= 28/35

---

*Previous lab: `lab_01_debugging_c`*
