"""
For Loops — Control Flow
=========================
Covers: for, range, enumerate, zip, break, continue, else
"""

# ─── 1. Basic for loop ────────────────────────────────────────────────────────
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating a string
for ch in "Python":
    print(ch, end=" ")
print()

# ─── 2. range() ───────────────────────────────────────────────────────────────
# range(stop)
for i in range(5):
    print(i, end=" ")     # 0 1 2 3 4
print()

# range(start, stop)
for i in range(2, 7):
    print(i, end=" ")     # 2 3 4 5 6
print()

# range(start, stop, step)
for i in range(0, 20, 4):
    print(i, end=" ")     # 0 4 8 12 16
print()

# Counting down
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# ─── 3. enumerate() ───────────────────────────────────────────────────────────
# Gets index AND value — avoids manual index tracking
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Custom start index
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# ─── 4. zip() ─────────────────────────────────────────────────────────────────
names  = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# zip stops at shortest iterable
list_a = [1, 2, 3, 4, 5]
list_b = ["a", "b", "c"]
print(list(zip(list_a, list_b)))   # [(1,'a'), (2,'b'), (3,'c')]

# zip_longest to pad shorter iterables
from itertools import zip_longest
print(list(zip_longest(list_a, list_b, fillvalue="-")))

# ─── 5. break and continue ────────────────────────────────────────────────────
# break — exit loop immediately
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")   # 0 1 2 3 4
print()

# continue — skip current iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")   # 1 3 5 7 9
print()

# ─── 6. for…else ──────────────────────────────────────────────────────────────
# else runs only if loop completed WITHOUT a break
def find_prime(nums):
    for n in nums:
        for divisor in range(2, n):
            if n % divisor == 0:
                break           # not prime
        else:
            print(f"{n} is prime")   # only reached if no break

find_prime(range(2, 15))

# ─── 7. Looping Patterns ──────────────────────────────────────────────────────
# Iterate in reverse
for item in reversed(fruits):
    print(item)

# Iterate sorted
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
for n in sorted(numbers):
    print(n, end=" ")
print()

# Iterate dict items
person = {"name": "Naman", "age": 25, "city": "Delhi"}
for key, value in person.items():
    print(f"{key}: {value}")

# Nested loops — building a matrix
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
for row in matrix:
    print(row)


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Print a multiplication table (1–10) using nested for loops.
# TODO 2: Find all prime numbers up to N using for + else.
# TODO 3: Flatten a 2D list [[1,2],[3,4],[5,6]] into [1,2,3,4,5,6].
# TODO 4: Use zip to transpose a matrix (swap rows and columns).
# TODO 5: Given two lists, create a dict mapping list1[i] → list2[i].
