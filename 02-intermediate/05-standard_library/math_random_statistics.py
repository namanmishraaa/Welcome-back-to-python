"""
math, random, statistics, decimal, fractions — Numerics
=========================================================
Ref: https://docs.python.org/3/tutorial/stdlib.html#mathematics
     https://docs.python.org/3/tutorial/stdlib2.html#decimal-floating-point-arithmetic
"""
import math
import random
import statistics
from decimal import Decimal, getcontext, ROUND_HALF_UP
from fractions import Fraction

# ─── 1. math ──────────────────────────────────────────────────────────────────
print(math.pi)          # 3.141592653589793
print(math.e)           # 2.718281828459045
print(math.inf)         # inf
print(math.nan)         # nan

print(math.floor(3.7))  # 3
print(math.ceil(3.2))   # 4
print(math.trunc(3.9))  # 3  (towards zero)

print(math.sqrt(16))    # 4.0
print(math.pow(2, 10))  # 1024.0 (float; use ** for int)
print(math.log(100, 10))# 2.0
print(math.log2(8))     # 3.0
print(math.log10(1000)) # 3.0

print(math.factorial(10))  # 3628800
print(math.gcd(48, 36))    # 12
print(math.lcm(4, 6))      # 12  (Python 3.9+)
print(math.comb(10, 3))    # 120  (10 choose 3)
print(math.perm(10, 3))    # 720  (10 permutations 3)

print(math.isfinite(math.inf))   # False
print(math.isnan(math.nan))      # True
print(math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9))  # True — float comparison!

# Trigonometry (radians)
print(math.sin(math.pi / 2))   # 1.0
print(math.degrees(math.pi))   # 180.0
print(math.radians(90))        # 1.5707...

# ─── 2. random ────────────────────────────────────────────────────────────────
random.seed(42)   # reproducible results — always seed for tests!

print(random.random())           # float in [0.0, 1.0)
print(random.uniform(1, 10))     # float in [1, 10]
print(random.randint(1, 100))    # int in [1, 100] inclusive
print(random.randrange(0, 10, 2))# 0, 2, 4, 6, or 8

items = [1, 2, 3, 4, 5]
print(random.choice(items))      # single random element
print(random.choices(items, k=3))# 3 elements WITH replacement
print(random.sample(items, k=3)) # 3 elements WITHOUT replacement

random.shuffle(items)            # in-place shuffle
print(items)

# Weighted choices
population = ["heads", "tails"]
weights    = [70, 30]           # 70% heads, 30% tails
print(random.choices(population, weights=weights, k=10))

# Secure random (for cryptography) — use secrets module instead of random
import secrets
print(secrets.token_hex(16))       # 32-char hex string
print(secrets.token_urlsafe(16))   # URL-safe base64

# ─── 3. statistics ────────────────────────────────────────────────────────────
data = [4, 9, 11, 6, 3, 7, 4, 8, 12, 4]

print(statistics.mean(data))       # 6.8 — arithmetic mean
print(statistics.median(data))     # 7.0 — middle value
print(statistics.mode(data))       # 4   — most common (raises if multimodal pre 3.8)
print(statistics.multimode(data))  # [4]

print(statistics.stdev(data))      # sample standard deviation
print(statistics.pstdev(data))     # population standard deviation
print(statistics.variance(data))   # sample variance

print(statistics.quantiles(data, n=4))  # quartiles

# ─── 4. decimal — Exact Decimal Arithmetic ───────────────────────────────────
# Use when precision matters: money, tax, scientific measurements
# NEVER use float for money!

# Float imprecision
print(0.1 + 0.2 == 0.3)          # False — floating point!
print(0.1 + 0.2)                  # 0.30000000000000004

# Decimal is exact
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True

# Financial calculation example
price    = Decimal("19.99")
quantity = Decimal("3")
tax_rate = Decimal("0.18")

subtotal = price * quantity
tax      = (subtotal * tax_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
total    = subtotal + tax
print(f"Subtotal: {subtotal}, Tax: {tax}, Total: {total}")

# Precision context
getcontext().prec = 50
print(Decimal(1) / Decimal(3))   # 50 significant digits

# ─── 5. fractions — Exact Rational Arithmetic ─────────────────────────────────
print(Fraction(1, 3) + Fraction(1, 6))    # 1/2
print(Fraction(1, 3) * Fraction(3, 4))   # 1/4
print(Fraction("3.14159"))               # 314159/100000
print(float(Fraction(1, 3)))             # 0.333...


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Write a function that checks if two floats are "equal" using math.isclose().
# TODO 2: Simulate rolling two dice 10,000 times; plot (or print) the frequency distribution.
# TODO 3: Calculate the mean, median, and standard deviation of student scores from a CSV.
# TODO 4: Build a tip calculator using Decimal that handles rounding correctly.
# TODO 5: Implement the Monty Hall problem simulation and verify the 2/3 win rate.
