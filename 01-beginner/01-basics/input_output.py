"""
Input / Output — Python Fundamentals
======================================
Covers: print(), input(), type conversion, f-string output
"""

# ─── 1. print() ───────────────────────────────────────────────────────────────
print("Hello, World!")
print("Multiple", "args", "separated", "by", "space")   # default sep=" "
print("Custom", "sep", sep="-")                          # Custom-sep
print("No newline at end", end="")
print(" — continued on same line")

# Pretty-printing data structures
data = {"name": "Naman", "age": 25, "skills": ["Python", "SQL"]}
import pprint
pprint.pprint(data)

# ─── 2. input() ───────────────────────────────────────────────────────────────
# input() ALWAYS returns a string — remember this in interviews
# name = input("Enter your name: ")   # uncomment to run interactively
# print(f"Hello, {name}!")

# ─── 3. Type Conversion from Input ───────────────────────────────────────────
# age_str = input("Enter your age: ")   # returns str
# age     = int(age_str)                # convert to int
# height  = float(input("Height (m): "))

# Safe conversion with error handling
def get_int(prompt: str) -> int:
    """Prompt user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

# ─── 4. Formatted Output Patterns ────────────────────────────────────────────
name   = "Alice"
score  = 95.678
passed = True

# f-strings with format specs
print(f"{'Name':<15} {'Score':>8} {'Passed':>8}")
print(f"{name:<15} {score:>8.2f} {str(passed):>8}")

# Aligning a report
students = [("Alice", 95.5), ("Bob", 87.3), ("Charlie", 92.0)]
print(f"\n{'Student':<12} {'Score':>7}")
print("-" * 20)
for student, s in students:
    print(f"{student:<12} {s:>7.1f}")

# ─── 5. Reading from stdin (for scripts) ─────────────────────────────────────
import sys
# for line in sys.stdin:      # read line by line
#     print(line.strip())

# ─── 6. File-like output ─────────────────────────────────────────────────────
print("This goes to stderr", file=sys.stderr)
print("Normal stdout message")


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Write a program that reads name and age, then prints a greeting.
# TODO 2: Build a function that safely reads a float from the user.
# TODO 3: Print a multiplication table (1–10) in aligned columns.
# TODO 4: Read comma-separated integers from input and print their sum.
# TODO 5: Create a "receipt" output with item names and prices, totalled at the bottom.
