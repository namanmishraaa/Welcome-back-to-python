# Advanced Level — Progress Tracker

Track your completion of each exercise file.

## 01-decorators
- [ ] `decorators.py` — function decorators, @wraps, parameterized decorators, class decorators,
  retry pattern, LRU cache, timing decorator

## 02-generators
- [ ] `generators.py` — generator functions, yield, generator expressions,
  send(), throw(), close(), yield from, async generators

## 03-async_programming
- [ ] `async_programming.py` — asyncio event loop, async/await, gather, create_task,
  Queue, Semaphore, run_in_executor, aiohttp

## 04-type_hints  ← NEW (PEP 484)
- [ ] `type_hints.py` — basic annotations, Optional/Union (X|Y), List/Dict generics,
  TypeVar, Generic, Protocol, TypedDict, NamedTuple, Literal, Final,
  @overload, mypy --strict, TYPE_CHECKING guard

## 05-dataclasses  ← NEW (PEP 557)
- [ ] `dataclasses_demo.py` — @dataclass, field(), default_factory, frozen=True,
  slots=True (3.10+), kw_only, KW_ONLY sentinel, __post_init__,
  inheritance, asdict(), replace(), comparison methods

## 06-testing  ← NEW
- [ ] `test_examples.py` — pytest basics, fixtures, conftest, parametrize,
  marks (skip, xfail), mocking (unittest.mock), pytest-cov,
  unittest.TestCase, TDD red-green-refactor workflow

## 07-design_patterns  ← NEW
- [ ] `patterns.py` — Singleton, Factory Method, Builder, Adapter,
  Decorator pattern, Observer, Strategy, Repository

## Projects
- [ ] Async web scraper (aiohttp + asyncio)
- [ ] Type-safe config system (dataclasses + type hints)
- [ ] Test suite for a mini library (pytest + mocking)

---
*Ref: PEP 484 (type hints), PEP 557 (dataclasses), PEP 492 (async/await), PEP 654 (ExceptionGroup)*
