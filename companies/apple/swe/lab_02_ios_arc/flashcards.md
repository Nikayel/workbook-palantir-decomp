# Flashcards — Lab 02 iOS ARC Memory Management

**Company:** Apple | **Lab:** 02 | **Style:** Retain cycles, weak references, NSCache

---

## Card 1: ARC Definition — Automatic Reference Counting

**Q:** What is ARC and how does it manage memory in Swift?

**A:** ARC = Automatic Reference Counting. Swift tracks how many strong references point to each class instance. When a new strong reference is created (assignment, stored property, or default closure capture), the count increments. When a reference is cleared or goes out of scope, the count decrements. When the count reaches 0, the instance is deallocated automatically. ARC is compile-time (not runtime like GC) — the compiler inserts retain/release calls. This means there are no GC pauses, but retain cycles can cause permanent leaks.

---

## Card 2: Strong vs Weak vs Unowned

**Q:** What are the three reference types in Swift ARC? When do you use each?

**A:**
- **Strong (default):** Increments reference count. Use for normal ownership. Object lives as long as there's a strong reference.
- **`weak var`:** Does NOT increment reference count. Always Optional — automatically becomes `nil` when the object is deallocated. Use when the referenced object can outlive the reference holder or when there's a cycle. Safe.
- **`unowned`:** Does NOT increment reference count. Non-optional — assumes the object is still alive when accessed. Crashes if the object was deallocated. Use only when you can guarantee the reference holder cannot outlive the referenced object (e.g., a child cannot outlive its parent).

Rule of thumb: when in doubt, use `weak`. Use `unowned` only when you're certain of the lifetime relationship.

---

## Card 3: Retain Cycle Mechanism

**Q:** What exactly is a retain cycle? Why does it cause a leak?

**A:** A retain cycle is when two or more objects hold strong references to each other, forming a circular chain. ARC deallocates objects only when their reference count reaches 0. In a cycle: object A's count stays >= 1 (because B points to A), and B's count stays >= 1 (because A points to B). Neither ever reaches 0. Even when all external references are released, the cycle keeps both objects alive indefinitely. The memory is permanently leaked — not freed until the process exits.

---

## Card 4: [weak self] in Closures — Why and When

**Q:** Why do you use `[weak self]` in async closure callbacks in Swift?

**A:** By default, a closure captures `self` strongly. If:
- `self` holds a strong reference to something that holds the closure
- The closure also holds `self` strongly

...you have a retain cycle. `[weak self]` makes `self` inside the closure Optional and does NOT increment `self`'s reference count. The closure cannot prevent `self` from being deallocated. When the VC is dismissed: the navigation controller releases its reference, count drops to 0, VC is deallocated, and the weak reference in the closure becomes `nil`. The next time the closure fires (if ever), `guard let self = self` catches the nil and bails safely.

---

## Card 5: [unowned self] vs [weak self] Tradeoff

**Q:** When should you use `[unowned self]` instead of `[weak self]`?

**A:**
- Use `[unowned self]` ONLY when you are certain the closure cannot outlive `self`. Example: a closure stored in a lazy property on `self` that is only called while `self` exists.
- Use `[weak self]` for ANY async callback where the completion may fire after `self` is deallocated — network callbacks, timers, NotificationCenter handlers, DispatchQueue.async blocks.

The consequence of using `[unowned self]` incorrectly: `EXC_BAD_ACCESS` crash (accessing a deallocated object). The consequence of using `[weak self]` unnecessarily: you write an extra `guard let`. Always choose safety over brevity in async contexts.

---

## Card 6: NSCache vs Dictionary for Image Caching

**Q:** Why use NSCache instead of a plain Dictionary for an image cache?

**A:**
1. **Memory pressure:** NSCache automatically evicts objects when the system is under memory pressure. Dictionary holds everything forever until you manually remove it.
2. **Thread safety:** NSCache is thread-safe by default. `Dictionary` is not — concurrent reads and writes require a lock or dispatch barrier.
3. **countLimit / totalCostLimit:** NSCache supports policies for how many items to hold and total memory cost. Dictionary has no such concept.
4. **Keys:** NSCache uses reference equality for keys (does not copy). Dictionary copies keys.

The right answer at Apple: "I'd use NSCache because it respects memory pressure from the system, and UIKit apps can receive memory warnings at any time."

---

## Card 7: @escaping vs Non-Escaping Closures

**Q:** What does `@escaping` mean on a closure parameter? What is the default?

**A:** By default, closure parameters are **non-escaping**: the closure must complete before the function returns. The compiler can optimize non-escaping closures because it knows their lifetime is bounded. `@escaping` means the closure may outlive the function call — it can be stored, passed to another function, or called asynchronously after the function returns. Any closure stored in a property or dispatched asynchronously MUST be `@escaping`. Non-escaping closures do NOT need `[weak self]` (the compiler enforces that they complete while self exists).

---

## Card 8: DispatchQueue.global() vs main for UI Updates

**Q:** Why is `DispatchQueue.main.async { }` required for UI updates inside an async callback?

**A:** UIKit is explicitly documented as not thread-safe. All UIKit calls (layout, drawing, view manipulation, tableView.reloadData()) must happen on the main thread. If you call UIKit from a background thread, you get:
- Unpredictable visual glitches
- Hard-to-reproduce crashes
- App Store rejections (Xcode detects many of these in release builds)

Pattern: load on a background queue, then dispatch back to main for UI update:
```swift
DispatchQueue.global().async {
    let image = expensiveLoadOperation()
    DispatchQueue.main.async {
        self.imageView.image = image  // safe: on main thread
    }
}
```

---

## Card 9: guard let with weak self Pattern

**Q:** Why is `guard let self = self else { return }` the standard pattern for `[weak self]` in closures?

**A:** Because `[weak self]` makes `self` Optional inside the closure. Before you can call any method on `self`, you must unwrap it. `guard let self = self else { return }` does two things:
1. Checks if `self` is still alive (not nil)
2. If nil, returns immediately — prevents any further code from executing on a deallocated object
3. If non-nil, "rebinds" `self` to a strong reference for the duration of the closure — prevents `self` from being deallocated mid-closure execution

Swift 5.3+: `guard let self = self` is the idiomatic form. Older Swift: `guard let strongSelf = self else { return }` with `strongSelf.method()`.

---

## Card 10: Memory Profiling in Xcode Instruments

**Q:** What Xcode tools would you use to find and confirm a memory leak from a retain cycle?

**A:**
1. **Debug Memory Graph (Xcode):** Product → Debug → Memory Graph Debugger (or the icon in the debug bar). Shows live object graph with reference arrows. Purple "!" badges indicate leaked objects. You can see retain cycles visually.
2. **Instruments → Leaks:** Records allocations over time; shows objects that are allocated but never freed. Good for reproduce-and-profile workflows.
3. **Instruments → Allocations:** Shows all allocations and their reference counts. "Persistent" category shows objects that were never deallocated.
4. **ASAN (AddressSanitizer):** Catches use-after-free (accessing a deallocated object). Not for finding cycles, but for catching crashes from freed memory.

At Apple: the Debug Memory Graph is typically fastest for retain cycle investigation during development.
