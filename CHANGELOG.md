# Changelog

All notable changes to this project are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased] — develop

### Added
- `01-beginner/PROGRESS.md` — exercise completion tracker for beginner level
- `02-intermediate/PROGRESS.md` — exercise completion tracker for intermediate level
- `03-advanced/PROGRESS.md` — exercise completion tracker for advanced level

---

## [1.0.0] — 2026-06-12

### Added — Beginner Level
- `01-basics/`: data_types, operators, string_manipulation, input_output, pep8_coding_style
- `02-control_flow/`: conditionals, for_loops, while_loops, comprehensions
- `03-functions/`: function_basics, scope_and_closures, first_class_functions

### Added — Intermediate Level
- `01-data_structures/`: lists_tuples_sets_dicts, collections_module, del_and_comparisons
- `02-file_handling/`: basic_file_io, csv_and_json, exception_handling (+ ExceptionGroup 3.11+)
- `03-oop_basics/`: oop_basics (classes, inheritance, MRO, ABC, magic methods)
- `04-modules_packages/`: modules, packages (import system, __init__.py, relative imports)
- `05-standard_library/`: os/pathlib, re, math/random, datetime, argparse, logging,
  itertools/functools, heapq/bisect

### Added — Advanced Level
- `01-decorators/`: decorators (function, class, parameterized, retry, cache)
- `02-generators/`: generators (yield, send, yield from, async generators)
- `03-async_programming/`: asyncio, gather, Queue, Semaphore, executors
- `04-type_hints/`: typing, Generic, Protocol, TypedDict, overload (PEP 484)
- `05-dataclasses/`: @dataclass, field, frozen, slots, kw_only (PEP 557)
- `06-testing/`: pytest, fixtures, parametrize, mocking, TDD workflow
- `07-design_patterns/`: Singleton, Factory, Builder, Adapter, Observer, Strategy, Repository

### Added — Reference
- `SOURCES.md` — every topic mapped to official Python docs URL + PEP numbers
- `README.md` — comprehensive guide with UV setup, interview prep, topic checklist
- `pyproject.toml` — UV config with pytest, pytest-cov, mypy, ruff, black, aiohttp

### Technical
- Aligned to official Python Tutorial (https://docs.python.org/3/tutorial/) all 16 chapters
- Python 3.11+ features: ExceptionGroup, except*, add_note(), slots=True, kw_only
- Every file: working examples + 5 TODO exercises + interview tips
