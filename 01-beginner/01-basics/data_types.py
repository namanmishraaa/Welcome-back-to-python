"""
Data Types — Python Fundamentals
=================================
Covers: int, float, str, bool, None, type conversion, isinstance
"""

# ─── 1. Integers ──────────────────────────────────────────────────────────────
x = 10
big = 10_000_000   # underscore separator for readability
print(type(x), x, big)

# Arbitrary precision
large = 2 ** 100
print(large)

# ─── 2. Floats ────────────────────────────────────────────────────────────────
pi = 3.14159
sci = 1.5e3      # scientific notation → 1500.0
print(type(pi), pi, sci)

# Floating-point imprecision — important interview topic!
print(0.1 + 0.2)           # 0.30000000000000004  — NOT 0.3
print(round(0.1 + 0.2, 2)) # 0.3

# ─── 3. Strings ───────────────────────────────────────────────────────────────
single = 'hello'
double = "world"
multi  = """This is
a multiline string."""

# Immutability: strings cannot be changed in-place
# single[0] = 'H'  # ← TypeError

# ─── 4. Booleans ──────────────────────────────────────────────────────────────
t = True
f = False
print(type(t), t + 1)   # bool is a subclass of int; True == 1

# Falsy values — know these for interviews
falsy = [False, None, 0, 0.0, "", [], {}, set()]
for val in falsy:
    print(f"{repr(val):10} → {bool(val)}")

# ─── 5. None ──────────────────────────────────────────────────────────────────
nothing = None
print(nothing is None)   # use 'is', not '=='

# ─── 6. Type Conversion (Casting) ─────────────────────────────────────────────
print(int("42"))         # str  → int
print(float("3.14"))     # str  → float
print(str(100))          # int  → str
print(bool(0))           # int  → bool
print(int(True))         # bool → int → 1

# ─── 7. Type Checking ─────────────────────────────────────────────────────────
print(type(42) == int)              # True
print(isinstance(42, int))          # True — preferred
print(isinstance(True, int))        # True — bool IS an int

# ─── 8. Interview Quick-Reference ─────────────────────────────────────────────
# Q: What is the difference between == and is?
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)   # True  — same value
print(a is b)   # False — different objects
print(a is c)   # True  — same object


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Create variables of each data type and print their types.
# TODO 2: Demonstrate the floating-point issue and how to work around it.
# TODO 3: List all falsy values in Python with examples.
# TODO 4: Convert "123.45" to an integer (hint: two-step conversion).
# TODO 5: Explain why isinstance(True, int) returns True.
