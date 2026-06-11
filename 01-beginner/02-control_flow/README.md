# 02-control_flow — Conditionals and Loops

Master flow control: making decisions with if/else and repeating actions with loops.

## 📚 Topics Covered

### 1. Conditionals
- **if statement** — Basic conditional execution
- **if-else** — Two-way branching
- **if-elif-else** — Multiple conditions and fallback
- **Nested conditionals** — Conditions inside conditions
- **Ternary operator** — `x if condition else y`
- **Truthiness and falsy values** — Understanding when conditions evaluate to True/False

### 2. Loops

#### For Loops
- **`for` loop syntax** — Iterating over sequences
- **`range()` function** — Generating sequences of numbers
- **Unpacking in loops** — `for x, y in items`
- **`enumerate()`** — Getting both index and value
- **`zip()`** — Iterating over multiple sequences
- **Loop control** — `break` and `continue`
- **`else` clause** — Running code when loop completes normally

#### While Loops
- **`while` loop** — Condition-based repetition
- **Infinite loops** — When to use, how to break out
- **Loop control with while** — `break` and `continue`
- **`else` clause with while** — Difference from break scenarios

### 3. List Comprehensions
- **Basic syntax** — `[expr for item in iterable]`
- **Conditional comprehensions** — `[expr for item if condition]`
- **Nested comprehensions** — Comprehensions within comprehensions
- **Dict and set comprehensions** — Beyond just lists
- **Performance benefits** — Why comprehensions are faster

### 4. Advanced Control Flow
- **`pass` statement** — Placeholder for empty blocks
- **Nested loops** — Loops inside loops (patterns, matrices)
- **Loop efficiency** — Understanding performance implications

## 💡 Learning Objectives

By the end of this section, you should be able to:
- ✅ Write if/elif/else statements for any decision logic
- ✅ Use for loops with range, enumerate, and zip effectively
- ✅ Implement while loops with proper exit conditions
- ✅ Use list comprehensions to generate lists efficiently
- ✅ Control loop flow with break, continue, and else
- ✅ Understand and fix infinite loops

## 📝 Files in This Section

1. **conditionals.py** — if/elif/else, ternary, truthiness
2. **for_loops.py** — for loops, range, enumerate, zip, break/continue
3. **while_loops.py** — while loops, infinite loops, loop control
4. **comprehensions.py** — List, dict, and set comprehensions
5. **exercises.py** — Practice problems on control flow

## 🎯 Interview Tips

**Common Questions:**
- What's the difference between `break` and `continue`?
- Explain list comprehensions and their benefits
- How does `zip()` work with multiple iterables?
- What happens if you use `range(10, 1, -1)`?
- Can you nest list comprehensions? When shouldn't you?

**Key Points to Master:**
- Know when to use for vs while loops
- Understand range() parameters: `range(start, stop, step)`
- Master list comprehensions — they appear in interviews frequently
- Understand the difference between loop `else` and `if else`

## 🚀 Next Steps

After mastering control flow:
1. Move to `03-functions/` to encapsulate logic
2. Combine control flow with functions to solve problems
3. Practice with pattern-printing problems (triangle, diamond, etc.)

---

**Difficulty: ⭐⭐☆ Core programming concepts**
