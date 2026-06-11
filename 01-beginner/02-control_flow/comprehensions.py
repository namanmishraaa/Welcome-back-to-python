"""
List / Dict / Set Comprehensions — Control Flow
================================================
Covers: list, dict, set comprehensions; generator expressions; performance
"""

# ─── 1. List Comprehensions ───────────────────────────────────────────────────
# Syntax: [expression  for item in iterable  if condition]

# Basic
squares = [x ** 2 for x in range(1, 11)]
print(squares)

# With condition (filter)
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# Transformation
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print(upper_words)

# Nested loops — equivalent of nested for
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
print(pairs)

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [n for row in matrix for n in row]
print(flat)

# ─── 2. Dict Comprehensions ───────────────────────────────────────────────────
# Syntax: {key: value  for item in iterable  if condition}

# Basic
square_map = {x: x ** 2 for x in range(1, 6)}
print(square_map)

# Invert a dict
original  = {"a": 1, "b": 2, "c": 3}
inverted  = {v: k for k, v in original.items()}
print(inverted)

# Filter items
scores  = {"Alice": 92, "Bob": 55, "Charlie": 88, "Dave": 61}
passing = {name: score for name, score in scores.items() if score >= 70}
print(passing)

# ─── 3. Set Comprehensions ────────────────────────────────────────────────────
# Syntax: {expression  for item in iterable  if condition}

# Unique lengths
words   = ["hi", "hello", "hey", "world", "wow"]
lengths = {len(w) for w in words}
print(lengths)

# Unique vowels in a sentence
sentence = "the quick brown fox jumps over the lazy dog"
vowels   = {ch for ch in sentence if ch in "aeiou"}
print(vowels)

# ─── 4. Generator Expressions ────────────────────────────────────────────────
# Like list comprehensions but lazy — don't build a list in memory
# Syntax: (expression  for item in iterable  if condition)

# sum() of squares without storing all squares
total = sum(x ** 2 for x in range(1, 1001))
print(total)

# any() / all() with generator — short-circuits
nums = [2, 4, 7, 8, 10]
print(any(n % 2 != 0 for n in nums))   # True (7 is odd)
print(all(n > 0       for n in nums))   # True

# ─── 5. Performance Comparison ────────────────────────────────────────────────
import timeit

# List comprehension vs for loop
lc   = timeit.timeit("[x**2 for x in range(1000)]",     number=10_000)
loop = timeit.timeit(stmt="""
r = []
for x in range(1000):
    r.append(x**2)
""", number=10_000)

print(f"List comp:  {lc:.3f}s")
print(f"For loop:   {loop:.3f}s")
print(f"Speedup:    {loop/lc:.1f}x")

# ─── 6. When NOT to use comprehensions ────────────────────────────────────────
# Avoid comprehensions for side effects (use a plain loop)
# Bad: [print(x) for x in range(5)]
# Good:
for x in range(5):
    print(x, end=" ")
print()

# Avoid deeply nested comprehensions (> 2 levels is usually unreadable)


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Generate all Pythagorean triples (a,b,c) where a,b,c < 50.
# TODO 2: Flatten a 3D list using comprehension.
# TODO 3: Given a list of words, create a dict {word: word_reversed}.
# TODO 4: Find words that are both in list1 AND list2 using set comprehension.
# TODO 5: Use a generator expression to lazily process lines of a large text.
