"""
Conditionals — Control Flow
=============================
Covers: if/elif/else, ternary, truthiness, nested conditionals
"""

# ─── 1. Basic if/elif/else ────────────────────────────────────────────────────
score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} → Grade {grade}")

# ─── 2. Ternary (Conditional Expression) ─────────────────────────────────────
age = 20
status = "adult" if age >= 18 else "minor"
print(status)

# Nested ternary — use sparingly (readability suffers)
n = 0
sign = "positive" if n > 0 else ("negative" if n < 0 else "zero")
print(sign)

# ─── 3. Truthiness and Falsy Values ──────────────────────────────────────────
# Falsy: False, None, 0, 0.0, 0j, "", [], {}, set(), ()
# Everything else is truthy

def check(val):
    if val:
        print(f"{repr(val):20} → Truthy")
    else:
        print(f"{repr(val):20} → Falsy")

check(0);     check(1)
check("");    check("hello")
check([]);    check([0])
check(None);  check(0.0)

# ─── 4. Comparison Chains ────────────────────────────────────────────────────
x = 5
print(1 <= x <= 10)      # True  — Pythonic range check
print(x == 5 == 5)       # True  — chaining works with ==

# ─── 5. Nested Conditionals ───────────────────────────────────────────────────
def classify(n: int) -> str:
    """Classify a number."""
    if n > 0:
        if n % 2 == 0:
            return "positive even"
        else:
            return "positive odd"
    elif n < 0:
        return "negative"
    else:
        return "zero"

for num in [-3, 0, 4, 7]:
    print(f"{num:4} → {classify(num)}")

# ─── 6. match/case (Python 3.10+) — structural pattern matching ───────────────
def http_status(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown"

print(http_status(200))
print(http_status(404))

# Pattern matching on types
def describe(value):
    match value:
        case int(n) if n > 0:
            return f"positive int: {n}"
        case str(s):
            return f"string: '{s}'"
        case [first, *rest]:
            return f"list starting with {first}"
        case _:
            return "something else"

print(describe(42))
print(describe("hi"))
print(describe([1, 2, 3]))


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Write a function that returns the largest of three numbers without max().
# TODO 2: FizzBuzz — print Fizz (div by 3), Buzz (div by 5), FizzBuzz (both).
# TODO 3: Classify a triangle as equilateral, isosceles, or scalene given 3 sides.
# TODO 4: Implement a simple login: check username and password, 3 attempts max.
# TODO 5: Use match/case to parse a simple command ("quit", "help", "go north", etc.)
