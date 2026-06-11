"""
Exception Handling — File Handling / General
=============================================
Covers: try/except/else/finally, raising, custom exceptions, chaining
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


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Create a custom exception hierarchy for a bank account (InsufficientFunds, etc.)
# TODO 2: Write a retry decorator that catches an exception and retries N times.
# TODO 3: Parse a CSV file and collect ALL errors without stopping (collect errors, report at end).
# TODO 4: Implement safe_cast(value, target_type, default) using exceptions.
# TODO 5: Write a context manager that suppresses only specific exceptions.
