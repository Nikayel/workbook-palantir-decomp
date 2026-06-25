# Flashcards — Lab 02 LLD Notification System

**Company:** Atlassian | **Lab:** 02 | **Style:** LLD / Observer pattern / Open/Closed Principle

---

## Card 1: Observer vs Pub-Sub Pattern

**Q:** What is the difference between the Observer pattern and Pub/Sub?

**A:**
- **Observer (direct):** Subject maintains a list of observers and calls them directly when state changes. Tight coupling — observer and subject reference each other. Works well in a single process.
- **Pub/Sub (brokered):** Publisher emits to a topic/bus; subscribers listen to the bus. The publisher and subscriber don't know about each other. Works well across services and processes.

In this lab: NotificationService is effectively the broker, making it closer to Pub/Sub. The pattern name to use in an Atlassian interview: "I'm using an Observer/Pub-Sub hybrid — the service acts as the event bus."

---

## Card 2: Open/Closed Principle (OCP)

**Q:** State the Open/Closed Principle and give a concrete example from the notification system.

**A:** "Software entities should be open for extension, but closed for modification."

Concrete example: Adding `PagerDutyChannel` requires:
- Creating a new class that inherits from `NotificationChannel` and implements `send()`
- Zero changes to `NotificationService`
- Zero changes to `EmailChannel` or `SlackChannel`

Violation of OCP: If `emit()` had `if channel_type == "email": ... elif channel_type == "slack": ...` — adding PagerDuty would require modifying `emit()`.

---

## Card 3: Abstract Base Class vs Interface

**Q:** What is an ABC in Python? How does it differ from a Java interface?

**A:** Python's `abc.ABC` provides:
- `@abstractmethod` decorator forces subclasses to implement the method
- Python has no `interface` keyword — ABC is the closest equivalent
- A class with any unimplemented `@abstractmethod` cannot be instantiated (raises `TypeError`)

Java interface: pure contract, no implementation. Python ABC: can mix abstract methods with concrete implementation. In this lab, `NotificationChannel` is an ABC — you can't instantiate it directly, only subclasses that implement `send()`.

---

## Card 4: Why Channel Failures Shouldn't Crash emit()

**Q:** Why should emit() catch exceptions from individual channel sends instead of letting them propagate?

**A:** If one channel fails and emit() propagates the exception:
- User A's Slack being down prevents User B from getting their email
- The caller of emit() must now handle channel-specific exceptions it knows nothing about
- A single flaky third-party API brings down the notification system

Correct approach: each channel call is wrapped in try/except; failure is logged and returns False; emit() continues with remaining channels. This is resilience — "Don't #@!% the customer" means other users' notifications are not held hostage by one channel's failure.

---

## Card 5: Async Dispatch for High-Volume Events

**Q:** ISSUE_UPDATED fires 10,000 notifications. Synchronous emit() takes 30 seconds. How do you fix this?

**A:** Two main approaches:

1. **Thread pool:** `executor.submit(channel.send, user_id, event)` — parallel I/O, simple, bounded by thread count
2. **Message queue (Kafka/SQS/RabbitMQ):** emit() writes event to queue; worker pool consumes and sends — decoupled, scalable, durable

Design change required: emit() signature stays the same; implementation switches to enqueue. Callers don't notice. This is the OCP at the system level: extend behavior (async) without modifying the contract.

Tradeoffs: At-least-once delivery, message ordering, dead-letter queues for failures.

---

## Card 6: "Play, as a Team" in Code Design

**Q:** How does the Open/Closed Principle embody the Atlassian value "Play, as a team"?

**A:** When you design a system where teammates can add new channels without modifying your core class, you are making the team win collectively. No one needs to wait for you to add PagerDuty — they can extend your work without touching it. A design that requires you to be involved in every extension is anti-team. OCP is not just good engineering — it's collaboration architecture.

---

## Card 7: Voluntary Tests in Atlassian Interviews (LLD Style)

**Q:** In a Code Design round, you've implemented the notification system. What voluntary tests would you add to signal craft?

**A:** Strong candidates add:
1. Test that a channel failure does not prevent other channels from being notified
2. Test that emit() on an EventType with zero subscribers does not crash
3. Test that unsubscribing works atomically (immediate effect)
4. Test with a mock channel that counts `send()` calls — verifies correct fanout
5. Test that adding a new channel type (defined inline in the test) works without modifying NotificationService

The last test is the most powerful: it's a live OCP proof.

---

## Card 8: SOLID Principles — Focus on S and O

**Q:** Briefly define the S and O in SOLID and identify where each appears in this notification lab.

**A:**
- **S — Single Responsibility:** Each class has one reason to change. `EmailChannel` only knows how to send email. `NotificationService` only knows routing logic. They don't mix.
- **O — Open/Closed:** `NotificationChannel` is abstract. New channels extend, not modify. `NotificationService.emit()` never needs to change when you add channels.

The other three (Liskov, Interface Segregation, Dependency Inversion) also apply but are less central to this lab's evaluation criteria.

---

## Card 9: Notification System Failure Modes

**Q:** Name 4 realistic failure modes in a notification system and how to handle each.

**A:**
1. **Channel API down (e.g., Slack outage):** Return False from send(); log; emit() continues with other channels. Add retry with exponential backoff for transient failures.
2. **User unsubscribes mid-emit():** Race condition. Use a snapshot of subscribers at emit() start (copy the set before iterating).
3. **Duplicate notifications:** Idempotency key on each notification event; check before sending.
4. **Notification storm (10k users, 1 event):** Message queue with worker pool; rate-limiting per channel.

---

## Card 10: Batching vs Immediate Delivery Tradeoff

**Q:** When should a notification system use batching (digest) vs immediate delivery?

**A:**
- **Immediate:** High-priority events (ISSUE_ASSIGNED to you, P0 incidents). User needs to act now.
- **Batching/digest:** Low-priority, high-volume events (ISSUE_UPDATED for a watched project). User prefers a daily email over 50 real-time pings.

Design implication: subscription must carry a preference field (immediate vs digest). Digest requires a scheduler that aggregates and sends on a schedule. Immediate goes through emit() directly. Both paths can use the same `NotificationChannel` abstraction — the routing layer changes, not the delivery abstraction.
