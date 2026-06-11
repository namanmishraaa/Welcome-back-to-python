"""
Design Patterns in Python
===========================
Ref: https://refactoring.guru/design-patterns/python
     Gang of Four (GoF) patterns implemented Pythonically.

Patterns are solutions to recurring design problems — not templates to copy,
but vocabularies to communicate architecture decisions.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Callable, TypeVar
import threading
import copy

T = TypeVar("T")

# ════════════════════════════════════════════════════════════
#  CREATIONAL PATTERNS — object creation
# ════════════════════════════════════════════════════════════

# ─── 1. Singleton — One instance per process ─────────────────────────────────
class Singleton:
    """Thread-safe Singleton using __new__."""
    _instance: Singleton | None = None
    _lock: threading.Lock = threading.Lock()

    def __new__(cls) -> Singleton:
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:   # double-checked locking
                    cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton(); s2 = Singleton()
print(s1 is s2)   # True

# Pythonic alternative: module-level global (modules are singletons by default)

# ─── 2. Factory Method — Delegate object creation to subclasses ───────────────
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> str: ...

class EmailNotification(Notification):
    def send(self, message: str) -> str:
        return f"EMAIL: {message}"

class SMSNotification(Notification):
    def send(self, message: str) -> str:
        return f"SMS: {message}"

class PushNotification(Notification):
    def send(self, message: str) -> str:
        return f"PUSH: {message}"

def notification_factory(channel: str) -> Notification:
    registry: dict[str, type[Notification]] = {
        "email": EmailNotification,
        "sms":   SMSNotification,
        "push":  PushNotification,
    }
    cls = registry.get(channel)
    if cls is None:
        raise ValueError(f"Unknown channel: {channel!r}")
    return cls()

for ch in ("email", "sms", "push"):
    n = notification_factory(ch)
    print(n.send("Hello!"))

# ─── 3. Builder — Construct complex objects step-by-step ─────────────────────
from dataclasses import dataclass, field

@dataclass
class QueryBuilder:
    """SQL-like query builder."""
    _table:   str       = ""
    _selects: list[str] = field(default_factory=list)
    _wheres:  list[str] = field(default_factory=list)
    _limit:   int | None = None

    def from_table(self, table: str) -> QueryBuilder:
        self._table = table
        return self   # return self for chaining

    def select(self, *columns: str) -> QueryBuilder:
        self._selects.extend(columns)
        return self

    def where(self, condition: str) -> QueryBuilder:
        self._wheres.append(condition)
        return self

    def limit(self, n: int) -> QueryBuilder:
        self._limit = n
        return self

    def build(self) -> str:
        cols  = ", ".join(self._selects) or "*"
        sql   = f"SELECT {cols} FROM {self._table}"
        if self._wheres:
            sql += " WHERE " + " AND ".join(self._wheres)
        if self._limit:
            sql += f" LIMIT {self._limit}"
        return sql

query = (
    QueryBuilder()
    .from_table("users")
    .select("name", "email")
    .where("age > 18")
    .where("active = true")
    .limit(10)
    .build()
)
print(query)

# ════════════════════════════════════════════════════════════
#  STRUCTURAL PATTERNS — object composition
# ════════════════════════════════════════════════════════════

# ─── 4. Adapter — Make incompatible interfaces compatible ─────────────────────
class OldPaymentSystem:
    def make_payment(self, amount_cents: int) -> bool:
        print(f"Old API: paying {amount_cents} cents")
        return True

class PaymentAdapter:
    """Adapts OldPaymentSystem to a modern float-based interface."""
    def __init__(self, old_system: OldPaymentSystem):
        self._old = old_system

    def pay(self, amount_dollars: float) -> bool:
        return self._old.make_payment(int(amount_dollars * 100))

payment = PaymentAdapter(OldPaymentSystem())
payment.pay(19.99)

# ─── 5. Decorator Pattern — Wrap objects to extend behaviour ──────────────────
class TextProcessor(ABC):
    @abstractmethod
    def process(self, text: str) -> str: ...

class PlainText(TextProcessor):
    def process(self, text: str) -> str:
        return text

class UpperCaseDecorator(TextProcessor):
    def __init__(self, wrapped: TextProcessor):
        self._wrapped = wrapped
    def process(self, text: str) -> str:
        return self._wrapped.process(text).upper()

class TrimDecorator(TextProcessor):
    def __init__(self, wrapped: TextProcessor):
        self._wrapped = wrapped
    def process(self, text: str) -> str:
        return self._wrapped.process(text).strip()

processor = TrimDecorator(UpperCaseDecorator(PlainText()))
print(processor.process("  hello world  "))   # HELLO WORLD

# ════════════════════════════════════════════════════════════
#  BEHAVIOURAL PATTERNS — communication between objects
# ════════════════════════════════════════════════════════════

# ─── 6. Observer — Notify dependents when state changes ───────────────────────
from collections import defaultdict

class EventBus:
    """Simple publish-subscribe event bus."""
    def __init__(self):
        self._listeners: dict[str, list[Callable[..., None]]] = defaultdict(list)

    def subscribe(self, event: str, callback: Callable[..., None]) -> None:
        self._listeners[event].append(callback)

    def publish(self, event: str, **data: Any) -> None:
        for cb in self._listeners[event]:
            cb(**data)

bus = EventBus()
bus.subscribe("user.registered", lambda name, email: print(f"Welcome email → {email}"))
bus.subscribe("user.registered", lambda name, email: print(f"Analytics → new user: {name}"))
bus.publish("user.registered", name="Alice", email="alice@example.com")

# ─── 7. Strategy — Swap algorithms at runtime ────────────────────────────────
# Pythonic: just pass a function (callable) as the strategy
def sort_by_name(users: list[dict]) -> list[dict]:
    return sorted(users, key=lambda u: u["name"])

def sort_by_age(users: list[dict]) -> list[dict]:
    return sorted(users, key=lambda u: u["age"])

def sort_by_score(users: list[dict]) -> list[dict]:
    return sorted(users, key=lambda u: u["score"], reverse=True)

class UserSorter:
    def __init__(self, strategy: Callable[[list[dict]], list[dict]]):
        self.strategy = strategy

    def sort(self, users: list[dict]) -> list[dict]:
        return self.strategy(users)

users = [
    {"name": "Charlie", "age": 28, "score": 85},
    {"name": "Alice",   "age": 32, "score": 92},
    {"name": "Bob",     "age": 25, "score": 78},
]
sorter = UserSorter(sort_by_score)
print([u["name"] for u in sorter.sort(users)])   # Alice, Charlie, Bob

# ─── 8. Repository — Abstract data access layer ──────────────────────────────
class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, user_id: int) -> dict | None: ...
    @abstractmethod
    def save(self, user: dict) -> None: ...
    @abstractmethod
    def delete(self, user_id: int) -> None: ...

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._store: dict[int, dict] = {}
        self._next_id = 1

    def find_by_id(self, user_id: int) -> dict | None:
        return self._store.get(user_id)

    def save(self, user: dict) -> None:
        if "id" not in user:
            user["id"] = self._next_id; self._next_id += 1
        self._store[user["id"]] = user

    def delete(self, user_id: int) -> None:
        self._store.pop(user_id, None)

repo = InMemoryUserRepository()
repo.save({"name": "Alice", "email": "a@b.com"})
repo.save({"name": "Bob",   "email": "b@c.com"})
print(repo.find_by_id(1))


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Implement a Command pattern for an undo/redo text editor.
# TODO 2: Build a Chain of Responsibility for HTTP request middleware.
# TODO 3: Implement a Proxy pattern that adds caching to any function call.
# TODO 4: Create a State machine for a vending machine (idle, selecting, dispensing, error).
# TODO 5: Implement a Template Method pattern for parsing different file formats.
