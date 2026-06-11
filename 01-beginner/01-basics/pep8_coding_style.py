"""
PEP 8 — Python Coding Style Guide
===================================
Ref: https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style
     https://peps.python.org/pep-0008/

PEP 8 is the official style guide for Python. Following it makes your
code consistent, readable, and professional — interviewers notice.
"""

# ─── 1. Indentation ───────────────────────────────────────────────────────────
# ✅ 4 spaces per indent level (NEVER tabs)
def good_indent():
    if True:
        return 42

# ─── 2. Line Length ───────────────────────────────────────────────────────────
# ✅ Max 79 chars for code, 72 for docstrings/comments
# Use implicit continuation inside brackets, or backslash

result = (
    "first part "
    "second part "
    "third part"
)

long_list = [
    "item_one", "item_two", "item_three",
    "item_four", "item_five",
]

# ─── 3. Blank Lines ───────────────────────────────────────────────────────────
# 2 blank lines around top-level functions and classes
# 1 blank line between methods inside a class


class MyClass:

    def method_one(self):
        pass

    def method_two(self):
        pass


def top_level_function():
    pass


# ─── 4. Imports ───────────────────────────────────────────────────────────────
# Order: stdlib → third-party → local (alphabetical within each group)
# ✅ One import per line
import os
import sys
from pathlib import Path
from typing import Optional

# ❌ Bad
# import os, sys
# from os import *   ← wildcard imports are discouraged

# ─── 5. Naming Conventions ────────────────────────────────────────────────────
# Variables and functions: snake_case
user_name = "Alice"
total_score = 0

def calculate_average(numbers: list) -> float:
    return sum(numbers) / len(numbers)

# Classes: PascalCase (CapWords)
class BankAccount:
    pass

class HTTPSConnection:   # acronyms stay uppercase
    pass

# Constants: UPPER_SNAKE_CASE (module level)
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30.0
PI = 3.14159

# Private: single leading underscore (convention)
_internal_cache = {}

# Name-mangled: double leading underscore (used in classes)
class Example:
    def __init__(self):
        self.__private = 42   # becomes _Example__private

# "Dunder" (magic) methods: double underscore both sides
# __init__, __str__, __repr__, __len__ — never invent your own dunders

# ─── 6. Whitespace in Expressions ────────────────────────────────────────────
# ✅ Spaces around operators
x = 1 + 2
y = x * 3 - 1

# ❌ No spaces inside brackets
# ✅ Correct
my_list = [1, 2, 3]
my_dict = {"key": "value"}
func_call = max(1, 2)

# ❌ Bad
# my_list = [ 1, 2, 3 ]
# func_call = max( 1 , 2 )

# ✅ No space before colon in slices
print(my_list[1:3])      # not [1 : 3]
print(my_list[::2])      # not [:: 2]

# ─── 7. Comments ──────────────────────────────────────────────────────────────
# Inline comment: 2 spaces before #, 1 space after
total = 100  # running total (not: total = 100  #running total)

# Block comment: full sentence, starts with capital letter
# This block processes each item in the input list
# and appends the result to the output.

def public_function(arg: int) -> str:
    """
    One-line summary.

    Extended description if needed. Args section uses Google style.

    Args:
        arg: Description of the argument.

    Returns:
        Description of the return value.

    Raises:
        ValueError: If arg is negative.
    """
    if arg < 0:
        raise ValueError("arg must be non-negative")
    return str(arg)

# ─── 8. Type Hints (PEP 484, now standard practice) ──────────────────────────
def greet(name: str, times: int = 1) -> str:
    return (name + " ") * times

def process(items: list[int]) -> dict[str, int]:
    return {"sum": sum(items), "count": len(items)}

# Optional (Python 3.10+ can use X | None instead of Optional[X])
def find_user(user_id: int) -> dict | None:
    return None

# ─── 9. Common PEP 8 Violations to Avoid ─────────────────────────────────────
# ❌  l, O, I as single-letter variable names (look like 1, 0, l)
# ❌  Mutable default arguments: def f(lst=[])
# ❌  Comparing to None with ==: use 'is None'
# ❌  Bare except: always catch a specific exception
# ❌  Shadowing built-ins: list = [1,2,3] (overwrites built-in list)
# ❌  Too-long lines, deeply nested logic

# ─── 10. Automated Tools ──────────────────────────────────────────────────────
# These enforce PEP 8 automatically — use them in every project:
#   ruff        — ultra-fast linter + formatter (replaces flake8 + isort)
#   black       — opinionated formatter (just run it, no config needed)
#   mypy        — static type checker
#   pre-commit  — run all tools automatically before every git commit
#
# Install with UV:
#   uv add --dev ruff black mypy pre-commit
#
# Run:
#   ruff check .       # lint
#   black .            # format
#   mypy src/          # type-check


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Take the 5 violations below and fix them according to PEP 8:
#         a) def Calculate_Total(X,Y): return X+Y
#         b) import os,sys
#         c) myList=[ 1,2,3 ]
#         d) if x == None: ...
#         e) except: pass

# TODO 2: Run `ruff check .` on this repo and fix all warnings.
# TODO 3: Add type hints to all functions in function_basics.py.
# TODO 4: Write a docstring (Google style) for the calculate_average function above.
# TODO 5: Install pre-commit and add ruff + mypy hooks to .pre-commit-config.yaml.
