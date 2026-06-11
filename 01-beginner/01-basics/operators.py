"""
Operators — Python Fundamentals
================================
Covers: arithmetic, comparison, logical, assignment, membership, identity
"""

# ─── 1. Arithmetic Operators ──────────────────────────────────────────────────
print(10 + 3)   # 13  — addition
print(10 - 3)   # 7   — subtraction
print(10 * 3)   # 30  — multiplication
print(10 / 3)   # 3.333... — true division (always returns float)
print(10 // 3)  # 3   — floor division (integer result)
print(10 % 3)   # 1   — modulus (remainder)
print(2 ** 10)  # 1024 — exponentiation

# Interview: difference between / and //
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(-7 // 2)  # -4  — floors towards negative infinity!

# ─── 2. Comparison Operators ──────────────────────────────────────────────────
print(5 == 5)   # True
print(5 != 4)   # True
print(5 > 3)    # True
print(5 < 3)    # False
print(5 >= 5)   # True
print(5 <= 4)   # False

# Chained comparisons — Pythonic and readable
x = 5
print(1 < x < 10)    # True
print(1 < x < 3)     # False

# ─── 3. Logical Operators ─────────────────────────────────────────────────────
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Short-circuit evaluation — important for interviews
def side_effect():
    print("Called!")
    return True

# 'and' short-circuits on first False
False and side_effect()  # side_effect NOT called

# 'or' short-circuits on first True
True or side_effect()    # side_effect NOT called

# Practical: default value pattern using short-circuit
name = "" or "Anonymous"
print(name)   # Anonymous

# ─── 4. Assignment Operators ──────────────────────────────────────────────────
n = 10
n += 5;  print(n)   # 15
n -= 3;  print(n)   # 12
n *= 2;  print(n)   # 24
n //= 5; print(n)   # 4
n **= 3; print(n)   # 64
n %= 10; print(n)   # 4

# Walrus operator := (Python 3.8+) — assign and return in expression
import re
text = "Hello, World!"
if m := re.search(r"\w+", text):
    print(m.group())   # Hello

# ─── 5. Membership Operators ──────────────────────────────────────────────────
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)       # True
print("mango" not in fruits)   # True
print("a" in "banana")         # True — works on strings too
print(2 in {1, 2, 3})          # True — works on sets (O(1) lookup)

# ─── 6. Identity Operators ────────────────────────────────────────────────────
a = [1, 2]
b = [1, 2]
c = a

print(a == b)   # True  — equal values
print(a is b)   # False — different objects
print(a is c)   # True  — same object

# None check — always use 'is', not '=='
val = None
print(val is None)     # Correct ✅
print(val == None)     # Works but not idiomatic ⚠️

# ─── 7. Operator Precedence (high → low) ──────────────────────────────────────
# ()  →  **  →  +x -x ~x  →  * / // %  →  + -  →  comparisons  →  not  →  and  →  or
print(2 + 3 * 4)       # 14, not 20
print((2 + 3) * 4)     # 20


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: What does -9 // 2 equal? Explain why.
# TODO 2: Use walrus operator to simplify reading lines from a file.
# TODO 3: Demonstrate short-circuit evaluation with a function that has side effects.
# TODO 4: What's the result of: True + True + False? Why?
# TODO 5: Write a one-liner that returns x if x > 0, else returns 0 (use 'or').
