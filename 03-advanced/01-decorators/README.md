# 01-decorators — Modifying Function Behavior

Master decorators: one of Python's most powerful and elegant features for extending function behavior.

## 📚 Topics Covered

### 1. Function Decorators Basics
- **What is a decorator?** — A function that modifies another function
- **Decorator syntax** — `@decorator` notation
- **Wrapping functions** — The decorator pattern
- **Preserving function metadata** — `functools.wraps`
- **Returning new functions** — Closures and decorators
- **Simple decorators** — Timing, logging, validation

### 2. Decorator Parameters
- **Decorators with arguments** — `@decorator(arg1, arg2)`
- **Parameterized decorators** — Three-layer decorator functions
- **Conditional decorators** — Applying decorators conditionally
- **Multiple decorators** — Stacking decorators, order matters
- **Decorator composition** — Combining decorator effects

### 3. Class-Based Decorators
- **Classes as decorators** — Using `__call__` method
- **Stateful decorators** — Maintaining state across calls
- **Class decorators vs function decorators** — Choosing between them
- **Decorating methods** — Special considerations for class methods
- **Decorating classes** — Modifying entire classes

### 4. Common Decorator Patterns
- **Timing decorator** — Measuring function execution time
- **Logging decorator** — Recording function calls
- **Authentication decorator** — Checking permissions before executing
- **Caching/Memoization** — `functools.lru_cache`, custom caching
- **Retry decorator** — Retrying failed operations
- **Validation decorator** — Checking argument types and values
- **Rate limiting** — Controlling function call frequency

### 5. Built-in Decorators
- **`@property`** — Converting methods to attributes
- **`@staticmethod`** — Methods that don't need instance/class
- **`@classmethod`** — Methods operating on class data
- **`@functools.wraps`** — Preserving function metadata
- **`@functools.lru_cache`** — Automatic memoization
- **`@contextmanager`** — Creating context managers from functions

### 6. Advanced Decorator Concepts
- **Decorator factories** — Creating decorators that create decorators
- **Method decorators** — Special handling for `self` and `cls`
- **Decorating decorators** — Decorators for decorators
- **Performance considerations** — Decorator overhead

## 💡 Learning Objectives

By the end of this section, you should be able to:
- ✅ Understand decorator mechanics (closures, wrapping)
- ✅ Write simple and parameterized decorators
- ✅ Use class-based decorators effectively
- ✅ Implement common decorator patterns
- ✅ Use `functools.wraps` properly
- ✅ Understand decorator order and composition
- ✅ Apply decorators for cross-cutting concerns

## 📝 Files in This Section

1. **function_decorators_basics.py** — Simple decorators, wrapping, @wraps
2. **decorator_parameters.py** — Parameterized decorators, stacking
3. **class_decorators.py** — Using classes as decorators, stateful decorators
4. **common_patterns.py** — Timing, logging, caching, validation decorators
5. **builtin_decorators.py** — @property, @staticmethod, @classmethod, etc.
6. **advanced_decorators.py** — Decorator factories, decorator composition
7. **exercises.py** — Practice problems on decorators

## 🎯 Interview Tips

**Common Questions:**
- Explain how decorators work (the mechanism)
- What does `@functools.wraps` do and why is it important?
- How do you write a parameterized decorator?
- Can you decorate a decorator? How?
- What's the difference between class and function decorators?
- Implement a caching decorator
- How are decorators different from middleware?

**Key Points to Master:**
- Understand the mechanics: decorators are functions that return functions
- Always use `@functools.wraps` to preserve function metadata
- Know the difference between `@decorator` and `@decorator()`
- Understand decorator order matters (bottom decorator applied first)
- Master implementation of common patterns (timing, logging, caching)
- Know when NOT to use decorators (KISS principle)

## 🚀 Next Steps

After mastering decorators:
1. Apply decorators to your existing code
2. Move to `02-generators/` for lazy evaluation
3. Practice implementing decorators for real problems
4. Study advanced design patterns

---

**Difficulty: ⭐⭐⭐ Advanced Python feature**
