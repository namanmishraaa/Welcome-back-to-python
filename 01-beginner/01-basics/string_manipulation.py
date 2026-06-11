"""
String Manipulation — Python Fundamentals
==========================================
Covers: indexing, slicing, methods, formatting, f-strings
"""

# ─── 1. String Basics ─────────────────────────────────────────────────────────
s = "Hello, World!"

# Indexing (0-based, negative allowed)
print(s[0])    # H
print(s[-1])   # !
print(s[-6])   # W

# Slicing: s[start:stop:step]  (stop is exclusive)
print(s[0:5])     # Hello
print(s[7:])      # World!
print(s[:5])      # Hello
print(s[::2])     # Hlo ol!
print(s[::-1])    # !dlroW ,olleH  — reverse a string

# ─── 2. Common String Methods ─────────────────────────────────────────────────
text = "  Hello, Python!  "
print(text.strip())         # remove whitespace both ends
print(text.lstrip())        # remove left whitespace
print(text.rstrip())        # remove right whitespace

print("hello".upper())      # HELLO
print("HELLO".lower())      # hello
print("hello world".title())# Hello World
print("hello world".capitalize())  # Hello world

print("banana".count("a"))     # 3
print("banana".find("an"))     # 1  (first occurrence; -1 if not found)
print("banana".index("an"))    # 1  (raises ValueError if not found)
print("banana".replace("a", "o"))  # bonono

# Split and join
words = "one,two,three".split(",")
print(words)               # ['one', 'two', 'three']
print(", ".join(words))    # one, two, three

# Checking contents
print("Hello123".isalnum())   # True
print("Hello".isalpha())      # True
print("123".isdigit())        # True
print("hello".startswith("he")) # True
print("hello".endswith("lo"))   # True

# ─── 3. String Formatting ─────────────────────────────────────────────────────
name = "Naman"
age  = 25
score = 98.765

# f-strings (Python 3.6+) — preferred modern approach
print(f"Name: {name}, Age: {age}")
print(f"Score: {score:.2f}")        # 2 decimal places
print(f"{'left':<10}|{'right':>10}")# alignment
print(f"{1000000:,}")               # 1,000,000 — thousand separator
print(f"{255:#010b}")               # binary with prefix, zero-padded

# str.format()
print("Name: {}, Age: {}".format(name, age))
print("{name} is {age}".format(name=name, age=age))

# % formatting — older style, still seen in codebases
print("Name: %s, Score: %.2f" % (name, score))

# ─── 4. String Immutability ───────────────────────────────────────────────────
original = "hello"
# original[0] = "H"  # ← TypeError: strings are immutable
modified = "H" + original[1:]  # create a new string
print(modified)

# ─── 5. Useful Built-ins ──────────────────────────────────────────────────────
print(len("hello"))         # 5
print(ord("A"))             # 65 — Unicode code point
print(chr(65))              # A  — code point to character
print(sorted("dcba"))       # ['a', 'b', 'c', 'd']
print("".join(sorted("dcba")))  # abcd

# ─── 6. Raw Strings and Escape Sequences ──────────────────────────────────────
print("Line1\nLine2")          # newline
print("Tab\there")             # tab
print("Quote: \"hi\"")         # escaped quote
path = r"C:\Users\naman"       # raw string — no escaping
print(path)

# ─── 7. Interview Patterns ────────────────────────────────────────────────────
# Palindrome check
word = "racecar"
print(word == word[::-1])   # True

# Anagram check
a, b = "listen", "silent"
print(sorted(a) == sorted(b))   # True

# Count character frequency
from collections import Counter
freq = Counter("mississippi")
print(freq)   # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Reverse every word in a sentence without reversing the sentence.
# TODO 2: Check if a string is a pangram (contains every letter a-z).
# TODO 3: Count the number of vowels in a string.
# TODO 4: Format a table with name and score columns, right-align scores.
# TODO 5: Remove all duplicate characters from a string while preserving order.
