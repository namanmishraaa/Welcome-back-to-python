"""
Type Hints — Static Typing in Python
========================================
Ref: https://docs.python.org/3/library/typing.html
     https://peps.python.org/pep-0484/  (Type Hints)
     https://peps.python.org/pep-0526/  (Variable Annotations)
     https://mypy.readthedocs.io/

Type hints don't affect runtime behaviour — Python remains dynamically typed.
They are used by static analysers (mypy, pyright) and IDEs to catch bugs early.
Run: uv add --dev mypy && mypy type_hints.py
"""
from __future__ import annotations   # PEP 563: postpone evaluation of annotations

import sys
from typing import (
    Any, Union, Optional, Final, Literal,
    TypeVar, Generic, Protocol,
    overload, cast, TYPE_CHECKING,
    NamedTuple, TypedDict,
)
from collections.abc import Callable, Sequence, Iterable, Iterator, Generator
from typing import TypeAlias   # Python 3.10+

if TYPE_CHECKING:
    pass  # expensive imports here — skipped at runtime

# ─── 1. Basic Variable and Function Annotations ───────────────────────────────
name: str = "Alice"
age:  int = 30
ratio: float = 0.5
active: bool = True

def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()

print(greet("Bob"))

# ─── 2. Built-in Generics (Python 3.9+) ──────────────────────────────────────
# Python 3.9+ — use built-in types directly as generics (no need to import from typing)
def first(items: list[int]) -> int | None:
    return items[0] if items else None

def count_words(text: str) -> dict[str, int]:
    return {w: text.count(w) for w in text.split()}

def zip_two(a: list[int], b: list[str]) -> list[tuple[int, str]]:
    return list(zip(a, b))

# ─── 3. Union, Optional, Any ─────────────────────────────────────────────────
# Python 3.10+: X | Y instead of Union[X, Y]
def parse_id(value: str | int) -> int:
    return int(value)

# Optional[X] == X | None
def find_user(user_id: int) -> dict[str, str] | None:
    db = {1: {"name": "Alice"}}
    return db.get(user_id)

# Any — opt-out of type checking (use sparingly)
def debug_print(value: Any) -> None:
    print(repr(value))

# ─── 4. Callable, Sequence, Iterable ─────────────────────────────────────────
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def sum_all(nums: Iterable[float]) -> float:
    return sum(nums)

def get_first(seq: Sequence[str]) -> str:
    return seq[0]   # Sequence supports indexing; Iterable doesn't

# ─── 5. TypeVar — Generic Functions ──────────────────────────────────────────
T = TypeVar("T")
S = TypeVar("S", bound="Comparable")

def first_item(items: list[T]) -> T | None:
    return items[0] if items else None

def max_of(a: T, b: T) -> T:
    return a if a > b else b   # type: ignore[operator]

# ─── 6. Generic Classes ───────────────────────────────────────────────────────
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def __len__(self) -> int:
        return len(self._items)

int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())   # 2

# ─── 7. Protocol — Structural Typing (Duck Typing + Types) ───────────────────
class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...

def minimum(items: Iterable[Comparable]) -> Comparable:
    return min(items)   # works with any type that has __lt__

print(minimum([3, 1, 4, 1, 5]))   # 1
print(minimum(["banana", "apple", "cherry"]))   # apple

# ─── 8. TypedDict — Typed Dictionaries ────────────────────────────────────────
class UserDict(TypedDict):
    name: str
    age:  int
    email: str

class PartialUser(TypedDict, total=False):   # all keys optional
    name: str
    age:  int

user: UserDict = {"name": "Alice", "age": 30, "email": "a@b.com"}
print(user["name"])

# ─── 9. NamedTuple — Typed Named Tuples ───────────────────────────────────────
class Point(NamedTuple):
    x: float
    y: float
    label: str = "point"

p = Point(3.0, 4.0)
print(p.x, p.label)
print(p._asdict())

# ─── 10. Literal, Final, TypeAlias ────────────────────────────────────────────
Direction: TypeAlias = Literal["north", "south", "east", "west"]

def move(direction: Direction) -> None:
    print(f"Moving {direction}")

move("north")   # ✅ type-checked
# move("up")    # ❌ mypy error

MAX_WORKERS: Final = 8   # cannot be reassigned — mypy will flag it

# ─── 11. overload — Multiple Signatures ───────────────────────────────────────
@overload
def double(x: int) -> int: ...
@overload
def double(x: str) -> str: ...

def double(x: int | str) -> int | str:
    return x * 2

print(double(5))       # 10
print(double("hi"))    # hihi

# ─── 12. Running mypy ──────────────────────────────────────────────────────────
# uv add --dev mypy
# mypy --strict type_hints.py
# Add to pyproject.toml:
#   [tool.mypy]
#   strict = true
#   python_version = "3.11"


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Add complete type hints to oop_basics.py; run mypy --strict on it.
# TODO 2: Create a generic Result[T, E] type that can hold either a value or an error.
# TODO 3: Define a Protocol for "Serializable" objects that have a to_dict() method.
# TODO 4: Use TypedDict to type the response from a mock REST API.
# TODO 5: Write a typed decorator that preserves the signature of the wrapped function using ParamSpec.
