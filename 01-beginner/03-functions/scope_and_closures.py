"""
Scope and Closures — Functions
================================
Covers: LEGB rule, global, nonlocal, closures, factory functions
"""

# ─── 1. LEGB Scope Resolution ────────────────────────────────────────────────
# L — Local (inside the function)
# E — Enclosing (outer function's scope)
# G — Global (module level)
# B — Built-in (Python built-ins like len, print)

x = "global x"

def outer():
    x = "enclosing x"

    def inner():
        x = "local x"
        print(x)          # L: local x

    inner()
    print(x)              # E: enclosing x

outer()
print(x)                  # G: global x
print(len("hello"))       # B: built-in len

# ─── 2. global keyword ───────────────────────────────────────────────────────
total = 0

def add_to_total(n: int) -> None:
    global total           # modify module-level variable
    total += n

add_to_total(10)
add_to_total(20)
print(total)   # 30

# Without global, assignment creates a LOCAL variable
count = 100
def wrong():
    count = 0    # creates local 'count', doesn't touch module-level
wrong()
print(count)     # still 100

# ─── 3. nonlocal keyword ─────────────────────────────────────────────────────
def make_counter(start: int = 0):
    """Return a counter function."""
    current = start

    def increment(step: int = 1) -> int:
        nonlocal current       # modify enclosing variable
        current += step
        return current

    return increment

counter = make_counter(10)
print(counter())    # 11
print(counter(5))   # 16
print(counter())    # 17

# ─── 4. Closures ─────────────────────────────────────────────────────────────
# A closure is an inner function that "closes over" variables from its enclosing scope

def make_multiplier(factor: int):
    """Factory: return a function that multiplies by factor."""
    def multiply(n: float) -> float:
        return n * factor    # 'factor' is captured from enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))    # 10
print(triple(5))    # 15

# Inspect closure cells
print(double.__closure__[0].cell_contents)   # 2

# ─── 5. Factory Functions ────────────────────────────────────────────────────
def make_power(exp: int):
    return lambda base: base ** exp

square = make_power(2)
cube   = make_power(3)

print(square(4))   # 16
print(cube(3))     # 27

# ─── 6. Closure Pitfall — Late Binding ───────────────────────────────────────
# ⚠️ Classic interview trap: closures capture the variable, not its value

# BAD — all functions use the same 'i' from loop
funcs_bad = [lambda: i for i in range(5)]
print([f() for f in funcs_bad])   # [4, 4, 4, 4, 4]  ← same 'i'

# GOOD — capture value at creation time with default argument
funcs_good = [lambda i=i: i for i in range(5)]
print([f() for f in funcs_good])  # [0, 1, 2, 3, 4]  ← correct

# ─── 7. Practical Closure Patterns ───────────────────────────────────────────
def make_validator(min_val: float, max_val: float):
    """Return a validator for a range."""
    def validate(n: float) -> bool:
        return min_val <= n <= max_val
    return validate

is_percentage = make_validator(0, 100)
is_byte       = make_validator(0, 255)

print(is_percentage(85))    # True
print(is_percentage(110))   # False
print(is_byte(200))         # True


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Create a make_adder(n) factory returning a function that adds n.
# TODO 2: Demonstrate the late-binding closure problem and fix it.
# TODO 3: Implement a memoize function using closures (no functools).
# TODO 4: Create a once() function: wraps a function so it only runs once.
# TODO 5: Build a running average function using nonlocal state.
