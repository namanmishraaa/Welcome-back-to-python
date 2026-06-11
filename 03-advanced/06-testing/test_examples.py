"""
Testing with pytest — Professional Test-Driven Development
============================================================
Ref: https://docs.python.org/3/library/unittest.html
     https://docs.pytest.org/

Install: uv add --dev pytest pytest-cov
Run:     pytest                    # all tests
         pytest -v                 # verbose
         pytest -k "test_add"      # filter by name
         pytest --cov=src          # coverage report
"""
# ─── Source code under test (normally in src/mypackage/) ─────────────────────
from __future__ import annotations
from dataclasses import dataclass

def add(a: int, b: int) -> int:
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def is_palindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def fizzbuzz(n: int) -> str:
    if n % 15 == 0: return "FizzBuzz"
    if n % 3  == 0: return "Fizz"
    if n % 5  == 0: return "Buzz"
    return str(n)

@dataclass
class BankAccount:
    owner:   str
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


# ════════════════════════════════════════════════════════════
#  pytest test functions
#  Convention: files named test_*.py or *_test.py
#              functions named test_*
# ════════════════════════════════════════════════════════════

# ─── 1. Basic Assertions ──────────────────────────────────────────────────────
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -2) == -3

def test_add_zero():
    assert add(0, 0) == 0

# ─── 2. Testing Exceptions ────────────────────────────────────────────────────
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_normal():
    assert divide(10, 2) == pytest.approx(5.0)   # ✅ float comparison

def test_bank_deposit_negative():
    acc = BankAccount("Alice", 100)
    with pytest.raises(ValueError, match="positive"):
        acc.deposit(-10)

# ─── 3. Fixtures — Reusable Setup ────────────────────────────────────────────
@pytest.fixture
def account() -> BankAccount:
    """Fresh account with £1000 for each test that requests it."""
    return BankAccount("Alice", 1000.0)

def test_deposit(account: BankAccount) -> None:
    account.deposit(500)
    assert account.balance == 1500.0

def test_withdraw(account: BankAccount) -> None:
    account.withdraw(200)
    assert account.balance == 800.0

def test_insufficient_funds(account: BankAccount) -> None:
    with pytest.raises(ValueError, match="Insufficient"):
        account.withdraw(5000)

# ─── 4. Parametrize — Run One Test with Many Inputs ───────────────────────────
@pytest.mark.parametrize("n,expected", [
    (1,  "1"),
    (3,  "Fizz"),
    (5,  "Buzz"),
    (15, "FizzBuzz"),
    (9,  "Fizz"),
    (10, "Buzz"),
    (7,  "7"),
])
def test_fizzbuzz(n: int, expected: str) -> None:
    assert fizzbuzz(n) == expected

@pytest.mark.parametrize("s,expected", [
    ("racecar",       True),
    ("A man a plan a canal Panama", True),
    ("hello",         False),
    ("Was it a car or a cat I saw", True),
    ("",              True),
])
def test_palindrome(s: str, expected: bool) -> None:
    assert is_palindrome(s) == expected

# ─── 5. Marks — Skip, XFAIL, Custom ──────────────────────────────────────────
@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature() -> None:
    assert False

@pytest.mark.xfail(reason="Known bug #42")
def test_known_bug() -> None:
    assert add(1, 1) == 3   # will fail — but expected

@pytest.mark.skipif(
    condition=True,
    reason="Skipped on this platform"
)
def test_platform_specific() -> None:
    pass

# ─── 6. Mocking — Replace Dependencies ───────────────────────────────────────
from unittest.mock import patch, MagicMock, call

def get_weather(city: str) -> str:
    """Calls an external API — we mock this in tests."""
    import urllib.request
    url = f"https://api.weather.com/{city}"
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode()

def test_get_weather_mocked() -> None:
    with patch("urllib.request.urlopen") as mock_open:
        mock_response = MagicMock()
        mock_response.__enter__ = lambda s: s
        mock_response.__exit__ = MagicMock(return_value=False)
        mock_response.read.return_value = b"Sunny, 28C"
        mock_open.return_value = mock_response

        result = get_weather("Delhi")
        assert result == "Sunny, 28C"
        mock_open.assert_called_once()

# ─── 7. Scope-Controlled Fixtures ────────────────────────────────────────────
@pytest.fixture(scope="module")   # created once per module (expensive setup)
def db_connection():
    """Simulates an expensive DB connection shared across tests."""
    print("\n[Setup] Opening DB connection")
    conn = {"connected": True, "queries": 0}
    yield conn
    print("\n[Teardown] Closing DB connection")
    conn["connected"] = False

# ─── 8. unittest Style (classic) ─────────────────────────────────────────────
import unittest

class TestAdd(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertLess(add(-5, 3), 0)

    def setUp(self):                  # runs before each test
        self.account = BankAccount("Bob", 500)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertAlmostEqual(self.account.balance, 600.0)


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Write tests for the BankAccount covering all edge cases (0 balance, exact withdrawal).
# TODO 2: Use parametrize to test is_palindrome with 10 different inputs.
# TODO 3: Mock the datetime.now() call in a function and test time-dependent logic.
# TODO 4: Write a test that uses a tmp_path fixture to test file I/O.
# TODO 5: Add pytest-cov, run coverage, and get the project to 80%+ coverage.
