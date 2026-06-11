# 02-generators — Lazy Evaluation and Memory Efficiency

Master generators: creating efficient iterables that produce values on-demand instead of all at once.

## 📚 Topics Covered

### 1. Iterator Protocol
- **Iterables vs iterators** — Understanding the distinction
- **Iterator protocol** — `__iter__()` and `__next__()`
- **StopIteration exception** — Signaling end of iteration
- **Creating custom iterators** — Implementing iterator classes
- **Iterator state** — Managing position and data

### 2. Generator Functions
- **Introducing generators** — Functions with `yield`
- **`yield` keyword** — Pausing and resuming execution
- **Generator state** — Maintaining local variables between yields
- **Generator expressions** — List comprehension-like syntax for generators
- **Multiple yields** — Generating multiple values
- **Return from generators** — Using `return` with StopIteration

### 3. Generator Mechanics
- **How generators work** — Behind the scenes execution model
- **Memory efficiency** — Not storing all values in memory
- **Lazy evaluation** — Computing values on demand
- **Generator pipelines** — Chaining generators together
- **Infinite generators** — Generators that never end

### 4. Generator Methods
- **`send()` method** — Sending values into generators
- **`throw()` method** — Injecting exceptions
- **`close()` method** — Terminating generators
- **Generator coroutines** — Using generators as coroutines
- **Two-way communication** — send() for interaction

### 5. Practical Generator Patterns
- **Filtering generators** — Yielding only matching values
- **Transforming generators** — Yielding modified values
- **Combining generators** — Merging multiple generators
- **File processing** — Reading large files efficiently
- **Infinite sequences** — Generating Fibonacci, primes, etc.
- **Range alternatives** — Custom range-like generators

### 6. Generator Expressions and Comprehensions
- **Generator expressions** — `(expr for x in iterable)`
- **vs List comprehensions** — Memory and performance differences
- **When to use each** — Performance vs flexibility tradeoff
- **Nested generators** — Complex generator expressions
- **Generator comprehensions** — Best practices

### 7. Advanced Generator Concepts
- **Delegating to subgenerators** — `yield from` (Python 3.3+)
- **Generator composition** — Combining generators elegantly
- **Coroutines** — Generators as coroutines (basis for async)
- **Contextlib** — `@contextmanager` for generators

## 💡 Learning Objectives

By the end of this section, you should be able to:
- ✅ Understand iterator protocol and implement iterators
- ✅ Write generator functions with `yield`
- ✅ Use generators for lazy evaluation and memory efficiency
- ✅ Implement common generator patterns
- ✅ Use `send()` for two-way generator communication
- ✅ Use `yield from` for delegating to subgenerators
- ✅ Optimize code using generator expressions
- ✅ Understand generators as the basis for async/await

## 📝 Files in This Section

1. **iterators.py** — Iterator protocol, custom iterators
2. **generator_basics.py** — `yield`, simple generators, generator expressions
3. **generator_mechanics.py** — How generators work, lazy evaluation
4. **generator_methods.py** — `send()`, `throw()`, `close()`, coroutines
5. **practical_patterns.py** — Filtering, transforming, combining generators
6. **file_processing.py** — Using generators for efficient file reading
7. **yield_from.py** — Delegating to subgenerators
8. **exercises.py** — Practice problems on generators

## 🎯 Interview Tips

**Common Questions:**
- What's the difference between an iterator and an iterable?
- Explain generators and their benefits
- Why are generators memory-efficient?
- How does `yield` work internally?
- What's the difference between generator and list comprehensions?
- Implement a generator for Fibonacci numbers
- What's `yield from` and when do you use it?
- How do you use `send()` with generators?

**Key Points to Master:**
- Iterables have `__iter__()`, iterators have `__next__()`
- Generators are a simple way to create iterators
- `yield` pauses execution and returns a value
- Generator expressions are lazy (don't compute all values immediately)
- `send()` enables two-way communication with generators
- `yield from` delegates to subgenerators (Python 3.3+)
- Generators are the foundation for async/await

## 🚀 Next Steps

After mastering generators:
1. Move to `03-async_programming/` which uses generators as foundation
2. Apply generators to optimize your existing code
3. Practice with complex generator pipelines
4. Study coroutines and async patterns

---

**Difficulty: ⭐⭐⭐ Advanced Python feature**
