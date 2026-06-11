"""
First-Class Functions — Functions
===================================
Covers: functions as objects, lambda, map/filter/reduce, partial
"""
from functools import reduce, partial
from typing import Callable

# ─── 1. Functions Are First-Class Objects ────────────────────────────────────
# Can be assigned, passed, returned, stored in data structures

def shout(text: str) -> str:
    return text.upper() + "!"

speak = shout           # assign to variable
print(speak("hello"))   # HELLO!

# Store in a list
def whisper(text: str) -> str:
    return text.lower() + "..."

transforms = [shout, whisper, str.title]
for fn in transforms:
    print(fn("Hello World"))

# ─── 2. Functions as Arguments (Higher-Order Functions) ──────────────────────
def apply(func: Callable, value):
    return func(value)

print(apply(len, "hello"))     # 5
print(apply(shout, "world"))   # WORLD!

def apply_twice(func: Callable, value):
    return func(func(value))

print(apply_twice(lambda x: x + 1, 5))   # 7

# ─── 3. Lambda Functions ─────────────────────────────────────────────────────
# Anonymous one-expression functions
# Use when: simple, temporary, used inline

square  = lambda x: x ** 2
add     = lambda x, y: x + y
is_even = lambda n: n % 2 == 0

print(square(5))     # 25
print(add(3, 4))     # 7
print(is_even(4))    # True

# Lambdas are useful as sort keys
students = [("Alice", 92), ("Bob", 55), ("Charlie", 88)]
students.sort(key=lambda s: s[1], reverse=True)
print(students)

# ─── 4. map() ────────────────────────────────────────────────────────────────
# Apply function to every element; returns iterator (lazy)
nums    = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
print(squares)

# map with multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)

# map vs list comprehension
# Prefer list comprehension for readability
comp = [x ** 2 for x in nums]   # usually more Pythonic

# ─── 5. filter() ─────────────────────────────────────────────────────────────
# Keep elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, range(10)))
print(evens)

# filter + None removes falsy values
mixed = [0, 1, "", "hello", None, [], [1, 2], False, True]
truthy = list(filter(None, mixed))
print(truthy)

# ─── 6. reduce() ─────────────────────────────────────────────────────────────
# Cumulatively apply function to reduce iterable to a single value
nums    = [1, 2, 3, 4, 5]
product = reduce(lambda acc, x: acc * x, nums)
print(product)   # 120

# Equivalent manual implementation
result = nums[0]
for n in nums[1:]:
    result *= n
print(result)   # 120

# ─── 7. functools.partial ────────────────────────────────────────────────────
# Pre-fill arguments — create specialised versions of functions
def power(base: float, exp: float) -> float:
    return base ** exp

square  = partial(power, exp=2)
cube    = partial(power, exp=3)
double  = partial(lambda x, n: x * n, n=2)

print(square(5))   # 25
print(cube(3))     # 27
print(double(7))   # 14

# ─── 8. Returning Functions ──────────────────────────────────────────────────
def make_greeting(salutation: str) -> Callable[[str], str]:
    def greet(name: str) -> str:
        return f"{salutation}, {name}!"
    return greet

hello = make_greeting("Hello")
hi    = make_greeting("Hi")

print(hello("Alice"))   # Hello, Alice!
print(hi("Bob"))        # Hi, Bob!


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Use map and filter to get squares of all odd numbers from 1-20.
# TODO 2: Implement your own map() function using a loop.
# TODO 3: Use reduce to find the maximum in a list (without max()).
# TODO 4: Create a compose(f, g) function: compose(f, g)(x) == f(g(x)).
# TODO 5: Use partial to create a base-2 log and base-10 log from math.log.
