# 04-type_hints — Static Typing in Python

Add type safety to your Python code using the `typing` module and `mypy`.

**Official Docs:** https://docs.python.org/3/library/typing.html
**PEP 484:** https://peps.python.org/pep-0484/
**mypy docs:** https://mypy.readthedocs.io/

## 📚 Topics Covered
- Variable and function annotations
- Built-in generic types: `list[T]`, `dict[K, V]`, `tuple[T, ...]`
- `X | Y` union syntax (Python 3.10+) vs `Union[X, Y]`
- `Optional[X]` / `X | None`
- `Any`, `Final`, `Literal`
- `TypeVar` — generic functions
- `Generic[T]` — generic classes
- `Protocol` — structural typing (duck typing + static checks)
- `TypedDict` — typed dictionaries
- `NamedTuple` — typed named tuples
- `TypeAlias` — readable type aliases
- `overload` — multiple function signatures
- `Callable`, `Sequence`, `Iterable`, `Iterator`, `Generator`
- `TYPE_CHECKING` — imports only visible to the type checker
- `ParamSpec`, `Concatenate` — typed decorators (advanced)

## 💡 Learning Objectives
- ✅ Add type hints to all your functions and classes
- ✅ Run `mypy --strict` and fix all errors
- ✅ Use `Protocol` for structural typing
- ✅ Create generic, reusable typed abstractions

## 🎯 Interview Tips
- `Optional[X]` is just `Union[X, None]` — same thing
- `Protocol` enables duck typing with static guarantees
- `TypedDict` > plain `dict` for typed data shapes
- Use `from __future__ import annotations` for forward refs

## 🛠️ Setup
```bash
uv add --dev mypy
mypy --strict 04-type_hints/type_hints.py
```

Add to `pyproject.toml`:
```toml
[tool.mypy]
strict = true
python_version = "3.11"
```

## 📝 Files
1. **type_hints.py** — comprehensive type hints guide with working examples

---
**Difficulty: ⭐⭐⭐ Industry essential for professional code**
