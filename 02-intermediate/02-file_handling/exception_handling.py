"""
Exception Handling — Complete Guide
=====================================
Ref: https://docs.python.org/3/tutorial/errors.html
Covers: try/except/else/finally, raising, custom exceptions, chaining,
        ExceptionGroup (3.11+), except* (3.11+), add_note() (3.11+)
"""

# ─── 1. Basic try/except ──────────────────────────────────────────────────────
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Catching multiple exceptions
def parse_int(s: str) -> int:
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print(f"Conversion error: {e}")
        return 0

print(parse_int("42"))    # 42
print(parse_int("abc"))   # error message, 0
print(parse_int(None))    # error message, 0

# ─── 2. try / except / else / finally ────────────────────────────────────────
# else  → runs only if try block had NO exception
# finally → ALWAYS runs (cleanup)

def read_file(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File '{path}' not found")
        return ""
    else:
        print("File read successfully")
        return content
    finally:
        print("This always runs")

read_file("nonexistent.txt")

# ─── 3. Raising Exceptions ────────────────────────────────────────────────────
def set_age(age: int) -> int:
    if not isinstance(age, int):
        raise TypeError(f"age must be int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"age {age} is out of range [0, 150]")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"ValueError: {e}")

# ─── 4. Custom Exceptions ────────────────────────────────────────────────────
class AppError(Exception):
    """Base exception for this application."""

class ValidationError(AppError):
    """Raised when user input fails validation."""
    def __init__(self, field: str, message: str):
        self.field   = field
        self.message = message
        super().__init__(f"Validation error on '{field}': {message}")

class NotFoundError(AppError):
    """Raised when a requested resource is not found."""
    def __init__(self, resource: str, resource_id):
        super().__init__(f"{resource} with id={resource_id} not found")

def get_user(user_id: int) -> dict:
    users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    if user_id not in users:
        raise NotFoundError("User", user_id)
    return users[user_id]

try:
    print(get_user(99))
except NotFoundError as e:
    print(e)

# ─── 5. Exception Chaining ────────────────────────────────────────────────────
def connect_db(url: str):
    try:
        raise ConnectionRefusedError("Connection refused")
    except ConnectionRefusedError as e:
        raise RuntimeError("Failed to connect to database") from e

try:
    connect_db("localhost:5432")
except RuntimeError as e:
    print(e)
    print(f"Caused by: {e.__cause__}")

# Suppress original exception (from None)
try:
    int("abc")
except ValueError:
    raise ValueError("Input must be numeric") from None   # hides original traceback

# ─── 6. Context Manager + Exceptions ─────────────────────────────────────────
from contextlib import suppress

# Suppress specific exceptions cleanly
with suppress(FileNotFoundError):
    open("nonexistent.txt")   # silently ignored

# ─── 7. Best Practices ────────────────────────────────────────────────────────
# ✅ Be specific — catch the narrowest exception possible
# ✅ Never use bare 'except:' — catches SystemExit and KeyboardInterrupt too
# ✅ Use 'finally' for cleanup, not for return values
# ✅ Create custom exception hierarchies for your application
# ✅ Use 'raise ... from ...' to preserve exception chains
# ❌ Don't swallow exceptions silently without logging

import logging
logging.basicConfig(level=logging.ERROR)

def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Division by zero: a=%s, b=%s", a, b)
        return None

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # None (logged)


# ─── 8. ExceptionGroup and except* (Python 3.11+) ────────────────────────────
# Ref: https://docs.python.org/3/tutorial/errors.html#raising-and-handling-multiple-unrelated-exceptions
#
# ExceptionGroup bundles multiple unrelated exceptions together.
# except* handles specific exception types from the group while
# letting others propagate — essential for async/concurrent error handling.

import sys

if sys.version_info >= (3, 11):
    # Raise multiple unrelated exceptions at once
    def validate_user(data: dict) -> None:
        errors = []
        if not data.get("name"):
            errors.append(ValueError("name is required"))
        if not isinstance(data.get("age"), int):
            errors.append(TypeError("age must be an integer"))
        if data.get("age", 0) < 0:
            errors.append(ValueError("age must be non-negative"))
        if errors:
            raise ExceptionGroup("validation errors", errors)

    try:
        validate_user({"name": "", "age": "thirty"})
    except* ValueError as eg:
        print(f"Value errors ({len(eg.exceptions)}): {[str(e) for e in eg.exceptions]}")
    except* TypeError as eg:
        print(f"Type errors ({len(eg.exceptions)}): {[str(e) for e in eg.exceptions]}")

    # Nested ExceptionGroups
    nested = ExceptionGroup("outer", [
        ValueError("v1"),
        ExceptionGroup("inner", [TypeError("t1"), KeyError("k1")]),
    ])
    # except* flattens the group and matches by type at any nesting level
    try:
        raise nested
    except* (ValueError, TypeError) as eg:
        print(f"Caught: {eg.exceptions}")

else:
    print("ExceptionGroup requires Python 3.11+")


# ─── 9. Enriching Exceptions with Notes (Python 3.11+) ───────────────────────
# Ref: https://docs.python.org/3/tutorial/errors.html#enriching-exceptions-with-notes
#
# add_note() attaches supplementary context to ANY existing exception.
# Notes appear in the traceback and are stored in exception.__notes__.

if sys.version_info >= (3, 11):
    try:
        try:
            raise ValueError("disk full")
        except ValueError as e:
            e.add_note("Occurred while processing upload: report.csv")
            e.add_note("Free up disk space and retry.")
            raise
    except ValueError as e:
        print(f"Exception: {e}")
        print(f"Notes: {e.__notes__}")   # ['Occurred while...', 'Free up...']

    # Useful pattern: add context in except blocks before re-raising
    def process_batch(items: list) -> None:
        for i, item in enumerate(items):
            try:
                int(item)   # will fail on non-numeric items
            except ValueError as e:
                e.add_note(f"Failed at item index {i}: {item!r}")
                raise

    try:
        process_batch(["1", "2", "abc", "4"])
    except ValueError as e:
        print(e, getattr(e, "__notes__", []))

else:
    print("add_note() requires Python 3.11+")


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Create a custom exception hierarchy for a bank account (InsufficientFunds, etc.)
# TODO 2: Write a retry decorator that catches an exception and retries N times.
# TODO 3: Parse a CSV file and collect ALL errors without stopping; use ExceptionGroup to raise them all.
# TODO 4: Implement safe_cast(value, target_type, default) using exceptions.
# TODO 5: Use add_note() to enrich a FileNotFoundError with the full config path that was attempted.

