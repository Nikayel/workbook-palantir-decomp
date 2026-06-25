# Lab 02 — iOS ARC: Retain Cycles and Weak References

**Company:** Apple
**Role:** SWE (iOS/macOS teams)
**Style:** Low-level / debugging — find and fix a retain cycle in Swift, implement image caching
**Tier:** 2
**Estimated time:** 45 minutes
**Status: Ready — work through all parts in order**

---

## Milestones

- [ ] M1 · Spotted the retain cycle — drew the reference graph showing who points to whom
- [ ] M2 · Explained why it leaks — both objects keep each other alive, reference count never reaches 0
- [ ] M3 · Fixed with [weak self] — rewrote the closure capture list correctly
- [ ] M4 · Implemented NSCache-based image cache with appropriate reference semantics
- [ ] M5 · Edge cases handled — nil self in async callback, cache eviction, thread safety awareness
- [ ] M6 · Ready — self-graded >= 28/35

---

## Scenario

"You're in an Apple iOS team technical screen. The interviewer says:

'Here's a Swift class for a photo feed view controller. There's a memory leak caused by a retain cycle. Find it, explain why it happens, and fix it. Then implement a simple image caching mechanism using weak references.'

You have 45 minutes."

**What this tests:** Understanding of ARC (Automatic Reference Counting), retain cycle mechanics, `[weak self]` vs `[unowned self]` tradeoffs, and NSCache for caching with proper memory management. This is real iOS engineering work — not algorithm trivia.

---

## Part 0: Forethought (Before Looking at the Code)

"In iOS, what are the 3 most common causes of memory leaks?"
```
[blank — hint: retain cycles, timer retention, notification center observers not removed]
```

"What is a retain cycle? Define it in one sentence:"
```
[blank]
```

"Draw what a retain cycle between a ViewController and an ImageLoader would look like:"
```
[blank — draw: ViewController --strong--> ImageLoader --strong--> ViewController]
```

---

## The Buggy Swift Code

```swift
// PhotoFeedViewController.swift — has a retain cycle (find it)

import UIKit

class ImageLoader {
    var completion: ((UIImage?) -> Void)?  // Stores a strong reference to the closure
    
    func loadImage(url: String, completion: @escaping (UIImage?) -> Void) {
        self.completion = completion  // ImageLoader holds strong reference to closure
        
        // Simulate async image load
        DispatchQueue.global().async {
            // In real code: URLSession.shared.dataTask...
            let image = UIImage(systemName: "photo")
            self.completion?(image)  // self (ImageLoader) captured strongly in the async block
        }
    }
}

class PhotoFeedViewController: UIViewController {
    var imageLoader = ImageLoader()  // ViewController holds strong reference to ImageLoader
    var images: [UIImage] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        loadNextBatch()
    }
    
    func loadNextBatch() {
        imageLoader.loadImage(url: "https://example.com/photo.jpg") { [strong self] image in
            // BUG: "[strong self]" is not valid Swift — but the intent is wrong:
            // this closure captures self (PhotoFeedViewController) strongly
            // ViewController holds ImageLoader (strong)
            // ImageLoader holds closure (strong)
            // Closure holds ViewController (strong)
            // = cycle: none of the three can ever be deallocated
            guard let image = image else { return }
            self.images.append(image)
            self.tableView.reloadData()
        }
    }
}
```

Note: `[strong self]` is not valid Swift syntax — it's written this way to make the intent visible. In real Swift, the default capture is strong (no annotation needed), which is exactly the bug.

---

## Part 1: Read Before Fixing

"Describe what this code is trying to do (without fixing anything):"
```
[blank]
```

"Who points to whom? Draw the reference graph:"
```
PhotoFeedViewController  ---[ strong ]-->  ?
?                        ---[ strong ]-->  ?
?                        ---[ strong ]-->  ?

[blank — complete the graph]
```

"What is the reference count of PhotoFeedViewController when loadNextBatch() is called?"
```
[blank — it should be 1 (from the navigation controller or parent), but what does the closure add?]
```

---

## Part 2: Bug Analysis

**The retain cycle — step by step:**

1. `PhotoFeedViewController` holds a **strong** reference to `imageLoader` (via `var imageLoader = ImageLoader()`)
2. `imageLoader.loadImage()` stores the completion closure as `self.completion` — `ImageLoader` holds a **strong** reference to the closure
3. The closure captures `self` (PhotoFeedViewController) strongly — the closure holds a **strong** reference to `PhotoFeedViewController`

The cycle: `VC -> ImageLoader -> closure -> VC`

**What happens when the VC is dismissed?**
```
[blank — navigation controller releases its reference, but the internal cycle keeps all three alive]
```

**How would you detect this leak in Xcode?**
```
[blank — Instruments → Leaks; or Allocations → Persistent Objects; or Debug Memory Graph in Xcode]
```

---

## Part 3: Fix the Retain Cycle

**Fix 1: Use `[weak self]` in the closure capture list**

```swift
func loadNextBatch() {
    imageLoader.loadImage(url: "https://example.com/photo.jpg") { [weak self] image in
        // weak self: closure does NOT increment VC's reference count
        // self is now Optional<PhotoFeedViewController>
        guard let self = self else { return }  // bail if VC was deallocated
        guard let image = image else { return }
        self.images.append(image)
        self.tableView.reloadData()
    }
}
```

**Why does `guard let self = self` matter?**
```
[blank — the async callback can complete after the VC is dismissed and deallocated.
Without the guard, accessing self would be accessing a deallocated object — crash or UB]
```

**Fix 2: Also clean up the stored closure in ImageLoader**

The secondary issue: `ImageLoader.completion` stores the closure indefinitely. This means the closure (and its strong captures) lives until `ImageLoader` itself is deallocated.

```swift
class ImageLoader {
    var completion: ((UIImage?) -> Void)?
    
    func loadImage(url: String, completion: @escaping (UIImage?) -> Void) {
        self.completion = completion
        
        DispatchQueue.global().async { [weak self] in
            guard let self = self else { return }
            let image = UIImage(systemName: "photo")
            self.completion?(image)
            // TODO: what should we do with self.completion after calling it?
            // [blank — clear it: self.completion = nil]
        }
    }
}
```

**Why clear `self.completion = nil` after calling it?**
```
[blank — break the ImageLoader -> closure -> VC reference chain as soon as the callback fires]
```

---

## Part 4: Implement Image Caching with NSCache

"Now implement a simple image caching mechanism. The requirements: (1) load images from URL asynchronously, (2) cache them so the same URL doesn't trigger a network request twice, (3) the cache should release memory automatically under memory pressure."

```swift
class ImageCache {
    // NSCache is preferred over Dictionary for caching because:
    // 1. It automatically evicts entries under memory pressure
    // 2. Thread-safe by default (unlike Dictionary)
    // 3. Does not copy keys/values (stores references)
    
    private let cache = NSCache<NSString, UIImage>()
    
    // TODO: implement load(url:completion:)
    // If cached: call completion immediately with cached image
    // If not cached: load async, cache result, call completion
    func load(url: String, completion: @escaping (UIImage?) -> Void) {
        // Step 1: Check cache
        // [blank]
        
        // Step 2: Not in cache — load async
        // [blank — DispatchQueue.global().async { ... }]
        
        // Step 3: On load success, cache and call completion on main thread
        // [blank — DispatchQueue.main.async { ... }]
    }
    
    func clearCache() {
        cache.removeAllObjects()
    }
}
```

**Your implementation:**

```swift
class ImageCache {
    private let cache = NSCache<NSString, UIImage>()
    
    func load(url: String, completion: @escaping (UIImage?) -> Void) {
        // [blank — implement here]
    }
    
    func clearCache() {
        cache.removeAllObjects()
    }
}
```

---

## Part 5: Design Reasoning

**`[weak self]` vs `[unowned self]` — when to use each:**

| | `[weak self]` | `[unowned self]` |
|---|---|---|
| Type of self inside closure | `Optional<Self>` (can be nil) | `Self` (implicitly unwrapped) |
| Self can be nil when closure fires? | Yes | No — crash if nil |
| When to use | Async callbacks, timers, any closure that may fire after VC dismissal | When the closure CANNOT outlive self (e.g., in-object lazy property) |
| Safety | Safer — guard let handles nil | Dangerous if used wrong — crash |

"For an async image load callback, which should you use and why?"
```
[blank — weak self: the callback can fire after the VC is popped off the navigation stack]
```

**NSCache vs Dictionary for image caching:**

| | NSCache | Dictionary |
|---|---|---|
| Thread safety | Yes (built-in) | No (must add locks) |
| Memory pressure | Auto-evicts objects | Holds forever |
| Key copying | No (uses reference equality) | Yes |
| Suitable for cache | Yes | Only with manual eviction logic |

**@escaping vs non-escaping closures:**

"What does `@escaping` mean on the completion parameter?"
```
[blank — the closure may outlive the function call. Without @escaping, Swift assumes
the closure completes before the function returns. With @escaping, the closure can
be stored and called later (e.g., after async network call completes)]
```

**DispatchQueue.global() vs main for UI updates:**

"Why call completion on DispatchQueue.main.async inside the image cache?"
```
[blank — UIKit is not thread-safe. All UI updates must happen on the main thread.
Loading on a background thread, then dispatching back to main for the UI update,
is the correct pattern]
```

---

## Part 6: Curveballs

**Curveball 1: Double-Load Race Condition**
"Two cells request the same image URL at the same time. Your cache returns nil for both (not cached yet). Both fire network requests. Both receive the image and cache it. What problem does this cause and how do you fix it?"

```
Problem: [blank — duplicate network requests, possible double-write to cache]
Fix: [blank — in-progress tracking: if a request for URL is already in flight, 
queue the completion and notify all waiting callers when it completes]
Data structure: [blank — Dictionary<String, [(UIImage?) -> Void]> mapping URL to pending callbacks]
```

**Curveball 2: Memory Warning**
"UIKit sends `didReceiveMemoryWarning` to your ViewController. What should happen to your image cache?"

```swift
override func didReceiveMemoryWarning() {
    super.didReceiveMemoryWarning()
    // TODO: what do you do here?
    // [blank — imageCache.clearCache() or set cache count/size limits via cache.countLimit]
}
```

**Curveball 3: Notification Center Leak**
"You add an observer to NotificationCenter in viewDidLoad. Where is the leak?"

```swift
class BadViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        NotificationCenter.default.addObserver(
            self,
            selector: #selector(handleNotification),
            name: .UIApplicationDidBecomeActive,
            object: nil
        )
        // BUG: observer never removed
    }
    
    @objc func handleNotification() { /* ... */ }
}
```

```
The leak: [blank — NotificationCenter holds strong reference to self (the VC). VC can't be deallocated.]
Fix: [blank — remove observer in deinit or viewWillDisappear]
Swift 4+ approach: [blank — use addObserver(forName:object:queue:using:) which returns a token; 
store the token and cancel it in deinit]
```

---

## Part 7: Self-Assessment Rubric

Score yourself honestly. Target >= 28/35 before moving on.

| Dimension | 5 — Strong | 3 — Solid | 1 — Needs Work | Your Score |
|---|---|---|---|---|
| Retain cycle identification | Drew the reference graph accurately; identified all 3 edges in the cycle | Found the cycle but missed one edge | Said "there's a leak" without tracing the cycle | __ /5 |
| ARC mechanics | Explained reference count, why count never hits 0, how weak fixes it | Correct but imprecise | Described symptoms without mechanism | __ /5 |
| [weak self] fix | Correct implementation with guard let, nil check, main thread awareness | Fixed the cycle but missed edge cases | Used [unowned self] incorrectly or missing guard | __ /5 |
| NSCache implementation | Working implementation; explained NSCache vs Dictionary; thread safety mentioned | Working implementation; did not explain choices | Used Dictionary without justification | __ /5 |
| Edge cases | Handled: nil self, main thread for UI, memory warning, double-load race | 2 of 3 edge cases | Did not consider edge cases | __ /5 |
| Terminology precision | Correct use of: ARC, retain cycle, weak, unowned, @escaping, reference type | Some correct terminology | Vague or incorrect terminology | __ /5 |
| Curveball handling | Addressed race condition + memory warning with concrete approaches | One curveball handled | Could not handle curveballs | __ /5 |

**Total: __ / 35**

---

## Reflection

**Explain the retain cycle from memory in 3 sentences:**
```
[blank]
```

**When would you choose [unowned self] over [weak self]?**
```
[blank]
```

**What Xcode tool would you use first if you suspected a memory leak?**
```
[blank]
```

---

## Ready-When Checklist

- [ ] I can draw the VC -> ImageLoader -> closure -> VC reference graph from memory
- [ ] I can explain why [weak self] breaks the cycle and what guard let self = self does
- [ ] I can implement NSCache-based caching and explain why NSCache > Dictionary for this use case
- [ ] I can handle the double-load race condition with a pending-callbacks dictionary
- [ ] I know when to use [unowned self] vs [weak self]
- [ ] I scored >= 28/35

---

*Previous lab: `lab_01_implement_ds`*
