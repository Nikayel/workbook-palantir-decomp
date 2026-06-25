# Lab 02 — LLD: Notification System

**Company:** Atlassian
**Role:** SWE
**Style:** LLD / Code Design — Observer pattern, Open/Closed Principle
**Tier:** 2
**Estimated time:** 50 minutes
**Status: Ready — work through all parts in order**

---

## Milestones

- [ ] M1 · Clarified — asked about delivery guarantee (at-least-once?), batching, max channels per user, priority levels
- [ ] M2 · Designed — class diagram: Event, Subscriber, Channel (abstract), NotificationService mapped out before coding
- [ ] M3 · OCP applied — a new EventType and new Channel can be added without modifying NotificationService or any existing class
- [ ] M4 · Coded — working implementation with Observer/Pub-Sub pattern
- [ ] M5 · Write-your-own-tests — wrote 3+ tests covering new subscriber, unsubscribe, and channel failure
- [ ] M6 · Ready — self-graded >= 28/35

---

## Scenario

"You're in the Atlassian onsite Code Design round. The interviewer says:

'Design a notification system for Jira. Users can subscribe to issue events (created, updated, assigned, commented). When an event fires, the system notifies all subscribers via their preferred channel (email, Slack, in-app). The system should be extensible for new event types and new channels without modifying existing code.'

You have 50 minutes."

**What this tests:** OOD principles (specifically Open/Closed Principle), Observer/Pub-Sub pattern, abstract interfaces for extensibility, and whether you write tests for the system you design.

---

## Part 0: Forethought (5 min — before designing)

Write down your clarifying questions before looking at the design scaffold below. What don't you know?

**Delivery guarantee questions:**
```
[blank — e.g., what if the Slack API is down? Do we retry? Is at-least-once delivery required?]
```

**Volume and performance questions:**
```
[blank — e.g., how many subscribers per event? Is emit() synchronous or async?]
```

**User preference questions:**
```
[blank — e.g., can a user want Slack for one event type and email for another?]
```

**Scope questions:**
```
[blank — e.g., are we designing the channel implementations or just the routing layer?]
```

---

## Part 1: Clarifying Questions (simulate asking the interviewer)

**Standard clarifications for a notification system:**

| Question | Reasonable default assumption |
|---|---|
| Delivery guarantee? | At-least-once; failures should be logged, not silently swallowed |
| Synchronous or async emit? | Synchronous for this exercise; async is a follow-up |
| Max channels per user? | No limit in this design |
| Priority levels? | Not in scope for this design |
| Batching (digest mode)? | Not in scope for this design |
| Unsubscribing from specific events? | Yes, must support |
| Channel failures crash emit()? | No — emit() should be resilient to individual channel failure |

**Your additional questions:**
```
[blank]
```

---

## Part 2: Design — Class Diagram

Before writing any code, sketch the class relationships. Fill in the blanks:

```
EventType (Enum)
    └── ISSUE_CREATED, ISSUE_UPDATED, ISSUE_ASSIGNED, ISSUE_COMMENTED

Event
    └── fields: [blank — what does an event need to carry?]

NotificationChannel (abstract)
    └── send(user_id, event) -> bool
    └── concrete subclasses: [blank — name them]

NotificationService
    └── fields: [blank — what data structures does it need?]
    └── methods: subscribe(), unsubscribe(), emit()
```

**Key design decision:** What data structure maps a user to their channel preferences?
```
[blank — dict? dict of lists? dict of dicts keyed by EventType?]
```

**Key design decision:** What data structure maps an EventType to its subscribers?
```
[blank — dict from EventType -> set of user_ids?]
```

---

## Part 3: Implementation Scaffold

Fill in all `[blank]` sections. The structure is provided — your job is to reason about the choices and implement the TODOs.

```python
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict, Set

class EventType(Enum):
    ISSUE_CREATED = "issue_created"
    ISSUE_UPDATED = "issue_updated"
    ISSUE_ASSIGNED = "issue_assigned"
    ISSUE_COMMENTED = "issue_commented"

class Event:
    def __init__(self, event_type: EventType, issue_id: str, data: dict):
        self.event_type = event_type
        self.issue_id = issue_id
        self.data = data
    
    def __repr__(self):
        return f"Event({self.event_type.value}, issue={self.issue_id})"


class NotificationChannel(ABC):
    """
    Abstract base class — extend to add new channels without modifying
    NotificationService or any existing channel class.
    This is the Open/Closed Principle in practice.
    """
    
    @abstractmethod
    def send(self, user_id: str, event: Event) -> bool:
        """
        Send a notification to the user about the event.
        Returns True if sent successfully, False if failed.
        Should NOT raise exceptions — return False instead.
        """
        pass
    
    @property
    @abstractmethod
    def channel_name(self) -> str:
        """Human-readable name for logging."""
        pass


class EmailChannel(NotificationChannel):
    
    @property
    def channel_name(self) -> str:
        return "email"
    
    def send(self, user_id: str, event: Event) -> bool:
        # TODO: implement email sending simulation
        # In real code: call email service API
        # [blank]
        pass


class SlackChannel(NotificationChannel):
    
    @property
    def channel_name(self) -> str:
        return "slack"
    
    def send(self, user_id: str, event: Event) -> bool:
        # TODO: implement Slack notification simulation
        # [blank]
        pass


class InAppChannel(NotificationChannel):
    
    @property
    def channel_name(self) -> str:
        return "in_app"
    
    def send(self, user_id: str, event: Event) -> bool:
        # TODO: store the notification in a user's in-app inbox
        # [blank]
        pass


class NotificationService:
    """
    Orchestrates subscriptions and event routing.
    Does NOT know about specific channels — only the abstract interface.
    Does NOT know about specific event business logic — only the routing.
    """
    
    def __init__(self):
        # Maps: user_id -> set of EventTypes they subscribed to
        # TODO: initialize this data structure
        # [blank]
        self._subscriptions: Dict[str, Set[EventType]] = {}
        
        # Maps: user_id -> list of NotificationChannel instances
        # TODO: initialize this data structure
        # [blank]
        self._channels: Dict[str, List[NotificationChannel]] = {}
    
    def subscribe(self, user_id: str, event_type: EventType, channel: NotificationChannel) -> None:
        """
        Subscribe user to an event type with a specific channel.
        Multiple calls can add multiple channels for the same event.
        """
        # TODO: implement subscribe
        # Consider: what if user_id doesn't exist yet in _subscriptions?
        # [blank]
    
    def unsubscribe(self, user_id: str, event_type: EventType) -> None:
        """
        Remove user's subscription to a specific event type.
        Their channels are NOT removed — they can re-subscribe.
        """
        # TODO: implement unsubscribe
        # Edge case: what if user_id doesn't exist?
        # [blank]
    
    def add_channel(self, user_id: str, channel: NotificationChannel) -> None:
        """
        Add a notification channel for a user (separate from event subscription).
        This allows user to subscribe to events after setting up channels.
        """
        # TODO: implement add_channel
        # [blank]
    
    def emit(self, event: Event) -> None:
        """
        Fire an event. Notify all subscribers who subscribed to this EventType.
        MUST be resilient to channel failures — one failing channel should not
        prevent other channels from being notified.
        """
        # TODO: implement emit
        # Steps:
        # 1. Find all users subscribed to event.event_type
        # 2. For each user, send via all their channels
        # 3. Handle channel failures gracefully (catch exception, log, continue)
        # [blank]
    
    def get_subscriber_count(self, event_type: EventType) -> int:
        """Return number of users subscribed to this event type."""
        # TODO: implement
        # [blank]
```

---

## Part 4: Voluntary Tests (Write These — Atlassian Rewards It)

```python
import unittest

class TestNotificationService(unittest.TestCase):
    
    def setUp(self):
        self.service = NotificationService()
        self.email = EmailChannel()
        self.slack = SlackChannel()
    
    def test_new_subscriber_receives_event(self):
        """Subscribing then emitting should trigger channel send."""
        # TODO
        # [blank]
    
    def test_unsubscribed_user_does_not_receive_event(self):
        """After unsubscribe, user should not be notified."""
        # TODO
        # [blank]
    
    def test_channel_failure_does_not_crash_emit(self):
        """
        If one channel raises an exception, emit() should continue
        notifying other subscribers/channels.
        """
        # TODO: create a BrokenChannel that always raises, subscribe it,
        # then verify emit() does not propagate the exception
        # [blank]
    
    def test_subscriber_count_updates_on_subscribe_unsubscribe(self):
        # TODO
        # [blank]
    
    # Voluntary bonus tests — add at least 2 more:
    # What if the same user subscribes twice to the same event?
    # What if emit() is called for an EventType with zero subscribers?
    # What if a new channel type (PagerDutyChannel) is added — does anything break?
    # [blank]
```

---

## Part 5: Design Reasoning

**Why abstract NotificationChannel as an ABC?**
```
[blank — hint: what would happen if NotificationService had if/elif chains for email vs Slack?]
```

**What pattern does this implement?**
```
[blank — Observer pattern: EventType is the "subject"; subscribers are "observers"]
```

**How do you add a PagerDutyChannel without modifying NotificationService?**
```
[blank — this is the Open/Closed Principle test. Write the answer as a procedure: "I would..."]
```

**What happens if a channel's send() raises an exception instead of returning False?**
```
[blank — what does your emit() implementation do? Should it re-raise? Swallow? Log?]
```

**What's the tradeoff between Observer (push) and Pub/Sub (intermediary broker)?**
```
[blank — hint: Observer is direct coupling; Pub/Sub uses a message bus. When does each win?]
```

---

## Part 6: Curveballs

**Curveball 1: Scale**
"10,000 users subscribed to ISSUE_UPDATED. An issue is updated and emit() blocks for 30 seconds. What do you do?"

```
Technical approach: [blank — async dispatch, message queue (Kafka/SQS), worker pool]
Design change required: [blank — emit() puts message on queue, workers consume it]
Tradeoff: [blank — at-least-once delivery, ordering guarantees, latency vs reliability]
```

**Curveball 2: Priority Routing**
"A user wants Slack notifications for CRITICAL issues but email for normal ones. How does your design handle this?"

```
What needs to change: [blank — channel subscription needs to carry metadata about priority/filter]
Which class changes: [blank]
Which classes stay the same (OCP check): [blank]
```

**Curveball 3: "Mute for 1 Hour" Feature**
"Product wants to add a 'mute all notifications for 1 hour' feature. Where does that state live? What's the minimal change to your design?"

```
Where the state lives: [blank — NotificationService._muted_users with expiry timestamps?]
Which method checks it: [blank — emit() before calling channels?]
Which class changes: [blank]
Which classes are untouched (OCP): [blank]
```

**Curveball 4: Testing the Untestable**
"EmailChannel calls a real email API. How do you test the subscribe/emit pipeline without sending real emails?"

```
Approach: [blank — dependency injection + mock channel, or test doubles]
Code change required: [blank — none if channel is abstract; just pass MockChannel in tests]
```

---

## Part 7: Self-Assessment Rubric

Score yourself honestly. Target >= 28/35 before moving on.

| Dimension | 5 — Strong | 3 — Solid | 1 — Needs Work | Your Score |
|---|---|---|---|---|
| Clarifying questions | Asked about delivery guarantee, failure behavior, async, and priority before designing | Asked about 2–3 of these | Jumped straight to code | __ /5 |
| OCP application | New channel and new EventType can be added without touching NotificationService | New channel works but requires small NotificationService change | Service has if/elif chains for channels | __ /5 |
| Observer pattern | Correctly identified Observer/Pub-Sub; explained push vs pull | Named the pattern; explanation imprecise | Did not recognize the pattern | __ /5 |
| Implementation | emit() is resilient to channel failures; subscribe/unsubscribe work correctly | Core functionality works; edge cases missed | Crashes on channel failure or missing users | __ /5 |
| Voluntary testing | Wrote 3+ tests including channel failure test; volunteered tests beyond the ask | Wrote 2 required tests | Wrote 0 tests | __ /5 |
| Curveball handling | Addressed scale (async) and mute feature with minimal design change | Addressed one curveball well | Could not extend the design | __ /5 |
| Code quality | Clean abstractions, well-named, type-hinted, no leaking concrete types | Functional but rough | NotificationService knows too much about channels | __ /5 |

**Total: __ / 35**

---

## Reflection

**Which OOD principle did this lab primarily exercise?**
```
[blank]
```

**What would you change if you had to make this production-ready?**
```
[blank]
```

**Which Atlassian value maps best to the Open/Closed Principle?**
```
[blank — "Play, as a team" — designing systems others can extend without asking you]
```

---

## Ready-When Checklist

- [ ] I can explain the Observer pattern vs Pub/Sub in 60 seconds
- [ ] I can add a PagerDutyChannel from scratch without opening the NotificationService file
- [ ] I can explain why emit() must not crash on channel failure
- [ ] I wrote 3+ tests including a channel failure scenario
- [ ] I addressed the async scale curveball with a concrete approach
- [ ] I scored >= 28/35

---

*Previous lab: `lab_01_craft_coding`*
