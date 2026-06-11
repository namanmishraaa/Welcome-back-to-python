"""
dataclasses — Boilerplate-Free Data Classes
============================================
Ref: https://docs.python.org/3/library/dataclasses.html
     https://peps.python.org/pep-0557/

@dataclass auto-generates __init__, __repr__, __eq__ and optionally
__lt__, __hash__, __slots__ — the backbone of modern Python data modelling.
"""
from __future__ import annotations
from dataclasses import dataclass, field, fields, asdict, astuple, replace, KW_ONLY
from typing import ClassVar
import datetime

# ─── 1. Basic @dataclass ──────────────────────────────────────────────────────
@dataclass
class Point:
    x: float
    y: float

p1 = Point(3.0, 4.0)
p2 = Point(3.0, 4.0)
print(p1)            # Point(x=3.0, y=4.0)  — auto __repr__
print(p1 == p2)      # True                  — auto __eq__ (by value)
print(p1 is p2)      # False                 — different objects

# ─── 2. Default Values and field() ───────────────────────────────────────────
@dataclass
class Config:
    host:    str  = "localhost"
    port:    int  = 8080
    debug:   bool = False
    tags:    list[str] = field(default_factory=list)   # ✅ mutable default
    timeout: float     = field(default=30.0, repr=False)  # excluded from repr

cfg = Config(host="prod.example.com", tags=["web", "api"])
print(cfg)
cfg.tags.append("cache")
print(cfg.tags)

# ─── 3. Post-Init Validation ──────────────────────────────────────────────────
@dataclass
class User:
    name:  str
    email: str
    age:   int

    def __post_init__(self) -> None:
        if "@" not in self.email:
            raise ValueError(f"Invalid email: {self.email!r}")
        if self.age < 0:
            raise ValueError(f"Age cannot be negative: {self.age}")
        self.name = self.name.strip().title()   # normalise

u = User("alice smith", "alice@example.com", 30)
print(u)

# ─── 4. Frozen Dataclasses (Immutable) ────────────────────────────────────────
@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float

    def distance_to_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

ip = ImmutablePoint(3.0, 4.0)
print(ip.distance_to_origin())  # 5.0
# ip.x = 10  # ← FrozenInstanceError

# Frozen dataclasses are hashable — can be used as dict keys or in sets
print(hash(ip))
point_set = {ImmutablePoint(1, 2), ImmutablePoint(3, 4), ImmutablePoint(1, 2)}
print(len(point_set))  # 2

# ─── 5. Ordering ─────────────────────────────────────────────────────────────
@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

versions = [Version(1, 10, 0), Version(2, 0, 0), Version(1, 2, 3)]
print(sorted(versions))   # [1.2.3, 1.10.0, 2.0.0]

# ─── 6. Class Variables (not included in __init__) ────────────────────────────
@dataclass
class Employee:
    COMPANY: ClassVar[str] = "Acme Corp"   # class variable, NOT an instance field
    name: str
    department: str
    salary: float = field(repr=False)

    @property
    def summary(self) -> str:
        return f"{self.name} @ {self.COMPANY}"

emp = Employee("Alice", "Engineering", 95000)
print(emp.summary)

# ─── 7. slots=True (Python 3.10+) ────────────────────────────────────────────
@dataclass(slots=True)   # uses __slots__ → faster access, less memory
class Vector:
    x: float
    y: float
    z: float = 0.0

    def magnitude(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

v = Vector(1.0, 2.0, 2.0)
print(v.magnitude())   # 3.0

# ─── 8. kw_only (Python 3.10+) ────────────────────────────────────────────────
@dataclass
class APIResponse:
    status_code: int
    KW_ONLY      # all fields after this are keyword-only in __init__
    data: dict   = field(default_factory=dict)
    error: str   = ""
    headers: dict = field(default_factory=dict)

r = APIResponse(200, data={"id": 1}, headers={"content-type": "application/json"})
print(r)

# ─── 9. Utility Functions ─────────────────────────────────────────────────────
print(asdict(emp))      # → dict (deep conversion)
print(astuple(ip))      # → tuple
print(fields(Config))   # → tuple of Field objects with metadata

# replace() — immutable update (like copy with changes)
new_cfg = replace(cfg, port=9090, debug=True)
print(new_cfg)

# ─── 10. Inheritance ──────────────────────────────────────────────────────────
@dataclass
class Animal:
    name:    str
    species: str

@dataclass
class Pet(Animal):
    owner: str
    vaccinated: bool = False

dog = Pet(name="Rex", species="Canis lupus", owner="Alice", vaccinated=True)
print(dog)

# ─── 11. Real-World Pattern: Request/Response Models ─────────────────────────
@dataclass(frozen=True)
class CreateUserRequest:
    name:     str
    email:    str
    role:     str = "user"
    created_at: datetime.datetime = field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc),
        compare=False,
    )

req = CreateUserRequest("Alice", "alice@example.com", role="admin")
print(asdict(req))


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Model a playing card (suit, rank) as a frozen dataclass; sort a hand.
# TODO 2: Create a dataclass for a bank transaction with __post_init__ validation.
# TODO 3: Implement a simple in-memory repository using a list of frozen dataclasses.
# TODO 4: Convert a dataclass to/from JSON using asdict() and the json module.
# TODO 5: Benchmark a regular class vs @dataclass(slots=True) for 1 million instantiations.
