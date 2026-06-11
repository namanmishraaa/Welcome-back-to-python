# 05-dataclasses — Boilerplate-Free Data Modelling

`@dataclass` auto-generates `__init__`, `__repr__`, `__eq__` — the modern Python way to model data.

**Official Docs:** https://docs.python.org/3/library/dataclasses.html
**PEP 557:** https://peps.python.org/pep-0557/

## 📚 Topics Covered
- `@dataclass` — basic usage, auto-generated methods
- `field()` — default factories, `repr=False`, `compare=False`, `hash`
- `__post_init__` — validation and computed fields
- `frozen=True` — immutable dataclasses (hashable)
- `order=True` — comparison operators
- `ClassVar` — class-level constants
- `slots=True` (Python 3.10+) — memory-efficient instances
- `kw_only` and `KW_ONLY` sentinel (Python 3.10+)
- `asdict()`, `astuple()`, `fields()`, `replace()`
- Inheritance with dataclasses
- Real-world patterns: request/response models, configs

## 💡 Learning Objectives
- ✅ Replace verbose `__init__` / `__repr__` / `__eq__` boilerplate
- ✅ Use `frozen=True` for immutable value objects
- ✅ Validate data in `__post_init__`
- ✅ Apply `slots=True` for performance-sensitive code

## 🎯 Interview Tips
- `field(default_factory=list)` — mutable defaults MUST use `default_factory`
- `frozen=True` makes dataclasses hashable (usable as dict keys / set members)
- `replace()` is the idiomatic way to "update" a frozen dataclass
- `@dataclass` vs `NamedTuple`: dataclasses are mutable by default; NamedTuple is always immutable and a subclass of tuple

## 📝 Files
1. **dataclasses_demo.py** — complete guide from basic to advanced

---
**Difficulty: ⭐⭐☆ Industry standard for data modelling**
