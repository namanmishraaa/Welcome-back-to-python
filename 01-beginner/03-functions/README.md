# 03-functions — Modular Code and Reusability

Master functions: the building blocks of reusable, organized code.

## 📚 Topics Covered

### 1. Function Basics
- **Defining functions** — `def` keyword, indentation, naming conventions
- **Parameters** — Positional, keyword, default values
- **Return statements** — Returning values, multiple returns, implicit None
- **Docstrings** — Documenting functions with `"""..."""`
- **Function scope** — Local vs global variables
- **LEGB rule** — Local, Enclosing, Global, Built-in scope resolution

### 2. Advanced Parameters
- **`*args`** — Variable number of positional arguments
- **`**kwargs`** — Variable number of keyword arguments
- **Argument unpacking** — `func(*list_args, **dict_args)`
- **Positional-only parameters** — `/` separator (Python 3.8+)
- **Keyword-only parameters** — `*` separator
- **Parameter order** — Standard order for function definitions

### 3. First-Class Functions
- **Functions as objects** — Assigning functions to variables
- **Passing functions as arguments** — Callbacks, functional programming
- **Returning functions** — Functions that create functions
- **Lambda functions** — Anonymous functions, when to use `lambda`
- **Functional tools** — `map()`, `filter()`, `reduce()` (with `functools`)

### 4. Closures and Advanced Concepts
- **Closures** — Functions that access outer scope variables
- **`nonlocal` keyword** — Modifying variables in enclosing scope
- **Closure use cases** — Decorators, factory functions

### 5. Function Best Practices
- **Single Responsibility Principle** — One function, one job
- **Pure functions** — No side effects, deterministic output
- **DRY (Don't Repeat Yourself)** — Using functions to avoid repetition
- **Type hints** — Function annotations for clarity (Python 3.5+)

## 💡 Learning Objectives

By the end of this section, you should be able to:
- ✅ Define functions with appropriate parameters
- ✅ Use `*args` and `**kwargs` effectively
- ✅ Write and use lambda functions appropriately
- ✅ Understand function scope and closures
- ✅ Use functions to reduce code duplication
- ✅ Write clean, well-documented functions
- ✅ Apply functional programming concepts

## 📝 Files in This Section

1. **function_basics.py** — Defining, calling, returning
2. **parameters.py** — Default values, `*args`, `**kwargs`
3. **scope_and_closures.py** — Scope rules, closures, `nonlocal`
4. **first_class_functions.py** — Functions as objects, lambda, map/filter
5. **exercises.py** — Practice problems on functions

## 🎯 Interview Tips

**Common Questions:**
- What are `*args` and `**kwargs`? When do you use each?
- Explain function scope and the LEGB rule
- What's a closure? Give an example
- When should you use `lambda` vs `def`?
- What's the difference between default arguments and `*args`?

**Key Points to Master:**
- Master parameter ordering: positional → *args → keyword → **kwargs
- Understand mutable default arguments problem: `def func(x, lst=[])`
- Know the difference between passing by value vs reference
- Understand when to use lambdas (should be simple, single expression)

## 🚀 Next Steps

After mastering functions:
1. Move to `02-intermediate/03-oop_basics/` to package functions into classes
2. Practice writing utility functions and modules
3. Start using type hints in your code

---

**Difficulty: ⭐⭐☆ Essential for writing organized code**
