"""
OOP — Class Basics, Inheritance, Polymorphism, Magic Methods
=============================================================
Covers: classes, inheritance, super(), MRO, duck typing, dunder methods
"""
from abc import ABC, abstractmethod
from functools import total_ordering

# ─── 1. Class Basics ──────────────────────────────────────────────────────────
class BankAccount:
    bank_name = "Python Bank"   # class variable — shared across all instances

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner   = owner           # instance variable
        self._balance = balance        # protected by convention

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    @property
    def balance(self) -> float:        # getter via property
        return self._balance

    @balance.setter
    def balance(self, value: float):   # setter with validation
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    @classmethod
    def from_dict(cls, data: dict) -> "BankAccount":
        """Alternative constructor — creates from dict."""
        return cls(data["owner"], data.get("balance", 0.0))

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        """Validate transaction amount — doesn't need instance or class."""
        return isinstance(amount, (int, float)) and amount > 0

    def __str__(self) -> str:          # human-readable
        return f"{self.owner}'s account (balance: £{self._balance:.2f})"

    def __repr__(self) -> str:         # unambiguous developer repr
        return f"BankAccount(owner={self.owner!r}, balance={self._balance})"


acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc)
print(repr(acc))
print(acc.balance)
acc2 = BankAccount.from_dict({"owner": "Bob", "balance": 2000})
print(BankAccount.is_valid_amount(100))

# ─── 2. Inheritance ────────────────────────────────────────────────────────────
class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.05):
        super().__init__(owner, balance)     # call parent __init__
        self.interest_rate = interest_rate

    def apply_interest(self) -> float:
        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest

    def __str__(self) -> str:
        return f"Savings: {super().__str__()} (rate: {self.interest_rate:.1%})"

savings = SavingsAccount("Bob", 1000, 0.04)
print(savings)
print(savings.apply_interest())

# isinstance checks
print(isinstance(savings, SavingsAccount))  # True
print(isinstance(savings, BankAccount))     # True — inherits

# MRO
print(SavingsAccount.__mro__)

# ─── 3. Abstract Base Classes ─────────────────────────────────────────────────
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"

class Circle(Shape):
    import math
    def __init__(self, radius: float):
        self.radius = radius
    def area(self)      -> float: return self.math.pi * self.radius ** 2
    def perimeter(self) -> float: return 2 * self.math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w, self.h = w, h
    def area(self)      -> float: return self.w * self.h
    def perimeter(self) -> float: return 2 * (self.w + self.h)

# Polymorphism — same interface, different behaviour
shapes: list[Shape] = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.describe())

# ─── 4. Magic Methods ─────────────────────────────────────────────────────────
@total_ordering   # generates missing comparison methods from __eq__ and __lt__
class Temperature:
    def __init__(self, celsius: float):
        self._c = celsius

    @property
    def fahrenheit(self) -> float:
        return self._c * 9/5 + 32

    def __repr__(self)         -> str:  return f"Temperature({self._c}°C)"
    def __str__(self)          -> str:  return f"{self._c}°C"
    def __eq__(self, other)    -> bool: return self._c == other._c
    def __lt__(self, other)    -> bool: return self._c <  other._c
    def __add__(self, other)   -> "Temperature": return Temperature(self._c + other._c)
    def __neg__(self)          -> "Temperature": return Temperature(-self._c)
    def __abs__(self)          -> "Temperature": return Temperature(abs(self._c))
    def __bool__(self)         -> bool: return self._c != 0
    def __len__(self)          -> int:  return int(abs(self._c))   # example only

temps = [Temperature(100), Temperature(0), Temperature(37)]
print(sorted(temps))
print(max(temps))


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Extend BankAccount with a CreditAccount that allows negative balance up to a limit.
# TODO 2: Implement a Vector class with __add__, __mul__, __len__, __repr__.
# TODO 3: Create an Animal hierarchy (Animal → Dog, Cat) with an abstract speak() method.
# TODO 4: Implement __iter__ and __next__ on a class to make it iterable.
# TODO 5: Build a Stack class with __len__, __contains__, __getitem__.
