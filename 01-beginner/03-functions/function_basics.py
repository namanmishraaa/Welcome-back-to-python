"""
Function Basics — Functions
============================
Covers: def, parameters, return, docstrings, type hints, scope
"""

# ─── 1. Defining and Calling Functions ───────────────────────────────────────
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

print(greet("Naman"))

# ─── 2. Parameters and Arguments ─────────────────────────────────────────────
# Positional arguments
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 4))
print(add(b=4, a=3))   # keyword arguments — order doesn't matter

# Default parameter values
def power(base: float, exponent: float = 2) -> float:
    return base ** exponent

print(power(3))      # 9   — uses default exponent=2
print(power(2, 10))  # 1024

# ⚠️ Mutable default argument trap — common interview question!
def append_item_bad(item, lst=[]):
    lst.append(item)
    return lst

print(append_item_bad(1))   # [1]
print(append_item_bad(2))   # [1, 2]  ← BUG: shared across calls

def append_item_good(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(append_item_good(1))  # [1]
print(append_item_good(2))  # [2]  ← correct

# ─── 3. *args and **kwargs ────────────────────────────────────────────────────
def total(*args: float) -> float:
    """Sum any number of positional arguments."""
    return sum(args)

print(total(1, 2, 3))        # 6
print(total(10, 20, 30, 40)) # 100

def profile(**kwargs):
    """Print keyword arguments as a profile."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

profile(name="Alice", age=30, city="Delhi")

# Combining all parameter types
def full_func(pos1, pos2, *args, kw_only, **kwargs):
    print(f"pos: {pos1}, {pos2}")
    print(f"args: {args}")
    print(f"kw_only: {kw_only}")
    print(f"kwargs: {kwargs}")

full_func(1, 2, 3, 4, 5, kw_only="K", extra="E")

# ─── 4. Return Values ─────────────────────────────────────────────────────────
def min_max(nums: list) -> tuple[int, int]:
    """Return (minimum, maximum) of a list."""
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"min={lo}, max={hi}")

# Functions return None implicitly
def no_return():
    x = 1 + 1

result = no_return()
print(result)   # None

# Early return
def abs_val(n: float) -> float:
    if n < 0:
        return -n
    return n

# ─── 5. Variable Scope (LEGB) ────────────────────────────────────────────────
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)   # local

    inner()
    print(x)   # enclosing

outer()
print(x)   # global

# global keyword
counter = 0
def increment():
    global counter
    counter += 1

increment(); increment()
print(counter)   # 2

# ─── 6. Docstrings and Type Hints ─────────────────────────────────────────────
def divide(a: float, b: float) -> float:
    """
    Divide a by b.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient a / b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

help(divide)


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Write a function that checks if a number is prime.
# TODO 2: Write a function accepting *args that returns mean, median, mode.
# TODO 3: Demonstrate the mutable default argument bug and the fix.
# TODO 4: Write a function using **kwargs to build an HTML tag: tag("p", id="1", class_="note").
# TODO 5: Implement a simple calculator function: calculate(op, *nums).
