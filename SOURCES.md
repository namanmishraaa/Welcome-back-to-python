# SOURCES — Topic to Official Documentation Mapping

Every topic in this project mapped to its authoritative source.

## Official Python Tutorial
https://docs.python.org/3/tutorial/index.html

| Topic | File | Official Doc | PEP |
|---|---|---|---|
| Numbers, strings, lists | `01-beginner/01-basics/` | [Ch 3](https://docs.python.org/3/tutorial/introduction.html) | — |
| Control flow (if, for, while) | `01-beginner/02-control_flow/` | [Ch 4](https://docs.python.org/3/tutorial/controlflow.html) | — |
| PEP 8 / Coding style | `01-beginner/01-basics/pep8_coding_style.py` | [Ch 4.10](https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style) | [PEP 8](https://peps.python.org/pep-0008/) |
| Functions, lambda, annotations | `01-beginner/03-functions/` | [Ch 4.8-4.9](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) | [PEP 526](https://peps.python.org/pep-0526/) |
| Data structures (list, dict, set, tuple) | `02-intermediate/01-data_structures/` | [Ch 5](https://docs.python.org/3/tutorial/datastructures.html) | — |
| `del` and sequence comparison | `02-intermediate/01-data_structures/del_and_comparisons.py` | [Ch 5.2 & 5.8](https://docs.python.org/3/tutorial/datastructures.html#the-del-statement) | — |
| Modules and packages | `02-intermediate/04-modules_packages/` | [Ch 6](https://docs.python.org/3/tutorial/modules.html) | — |
| Input/output, f-strings, file I/O, JSON | `02-intermediate/02-file_handling/` | [Ch 7](https://docs.python.org/3/tutorial/inputoutput.html) | — |
| Exceptions, chaining, custom | `02-intermediate/02-file_handling/exception_handling.py` | [Ch 8](https://docs.python.org/3/tutorial/errors.html) | — |
| ExceptionGroup, `except*` | `02-intermediate/02-file_handling/exception_handling.py` | [Ch 8.9](https://docs.python.org/3/tutorial/errors.html#raising-and-handling-multiple-unrelated-exceptions) | [PEP 654](https://peps.python.org/pep-0654/) |
| `add_note()` on exceptions | `02-intermediate/02-file_handling/exception_handling.py` | [Ch 8.10](https://docs.python.org/3/tutorial/errors.html#enriching-exceptions-with-notes) | — |
| Classes, inheritance, MRO | `02-intermediate/03-oop_basics/` | [Ch 9](https://docs.python.org/3/tutorial/classes.html) | — |
| Iterators and generators | `03-advanced/02-generators/` | [Ch 9.8-9.10](https://docs.python.org/3/tutorial/classes.html#iterators) | — |
| `os`, `sys`, `re`, `math`, `datetime` | `02-intermediate/05-standard_library/` | [Ch 10](https://docs.python.org/3/tutorial/stdlib.html) | — |
| `logging`, `itertools`, `functools`, `decimal`, `heapq` | `02-intermediate/05-standard_library/` | [Ch 11](https://docs.python.org/3/tutorial/stdlib2.html) | — |
| Virtual environments | `pyproject.toml` (UV) | [Ch 12](https://docs.python.org/3/tutorial/venv.html) | — |
| Floating-point issues | `01-beginner/01-basics/data_types.py` | [Ch 15](https://docs.python.org/3/tutorial/floatingpoint.html) | — |

---

## Standard Library Reference
https://docs.python.org/3/library/index.html

| Module | File | Library Doc |
|---|---|---|
| `os` | `os_sys_pathlib.py` | [os](https://docs.python.org/3/library/os.html) |
| `sys` | `os_sys_pathlib.py` | [sys](https://docs.python.org/3/library/sys.html) |
| `pathlib` | `os_sys_pathlib.py` | [pathlib](https://docs.python.org/3/library/pathlib.html) |
| `shutil` | `os_sys_pathlib.py` | [shutil](https://docs.python.org/3/library/shutil.html) |
| `re` | `re_regex.py` | [re](https://docs.python.org/3/library/re.html) |
| `math` | `math_random_statistics.py` | [math](https://docs.python.org/3/library/math.html) |
| `random` | `math_random_statistics.py` | [random](https://docs.python.org/3/library/random.html) |
| `statistics` | `math_random_statistics.py` | [statistics](https://docs.python.org/3/library/statistics.html) |
| `decimal` | `math_random_statistics.py` | [decimal](https://docs.python.org/3/library/decimal.html) |
| `fractions` | `math_random_statistics.py` | [fractions](https://docs.python.org/3/library/fractions.html) |
| `datetime` | `datetime_module.py` | [datetime](https://docs.python.org/3/library/datetime.html) |
| `zoneinfo` | `datetime_module.py` | [zoneinfo](https://docs.python.org/3/library/zoneinfo.html) |
| `argparse` | `argparse_cli.py` | [argparse](https://docs.python.org/3/library/argparse.html) |
| `logging` | `logging_module.py` | [logging](https://docs.python.org/3/library/logging.html) |
| `itertools` | `itertools_functools.py` | [itertools](https://docs.python.org/3/library/itertools.html) |
| `functools` | `itertools_functools.py` | [functools](https://docs.python.org/3/library/functools.html) |
| `heapq` | `heapq_bisect.py` | [heapq](https://docs.python.org/3/library/heapq.html) |
| `bisect` | `heapq_bisect.py` | [bisect](https://docs.python.org/3/library/bisect.html) |
| `csv` | `csv_and_json.py` | [csv](https://docs.python.org/3/library/csv.html) |
| `json` | `csv_and_json.py` | [json](https://docs.python.org/3/library/json.html) |
| `collections` | `collections_module.py` | [collections](https://docs.python.org/3/library/collections.html) |
| `dataclasses` | `03-advanced/05-dataclasses/` | [dataclasses](https://docs.python.org/3/library/dataclasses.html) |
| `typing` | `03-advanced/04-type_hints/` | [typing](https://docs.python.org/3/library/typing.html) |
| `unittest` | `03-advanced/06-testing/` | [unittest](https://docs.python.org/3/library/unittest.html) |
| `abc` | `02-intermediate/03-oop_basics/oop_basics.py` | [abc](https://docs.python.org/3/library/abc.html) |
| `contextlib` | `02-intermediate/02-file_handling/basic_file_io.py` | [contextlib](https://docs.python.org/3/library/contextlib.html) |
| `asyncio` | `03-advanced/03-async_programming/` | [asyncio](https://docs.python.org/3/library/asyncio.html) |
| `concurrent.futures` | `03-advanced/03-async_programming/` | [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) |

---

## Key PEPs

| PEP | Topic | Status |
|---|---|---|
| [PEP 8](https://peps.python.org/pep-0008/) | Style Guide for Python Code | Active |
| [PEP 20](https://peps.python.org/pep-0020/) | The Zen of Python | Active |
| [PEP 484](https://peps.python.org/pep-0484/) | Type Hints | Final |
| [PEP 526](https://peps.python.org/pep-0526/) | Variable Annotations | Final |
| [PEP 544](https://peps.python.org/pep-0544/) | Protocols (Structural Subtyping) | Final |
| [PEP 557](https://peps.python.org/pep-0557/) | Data Classes | Final |
| [PEP 572](https://peps.python.org/pep-0572/) | Walrus Operator `:=` | Final |
| [PEP 585](https://peps.python.org/pep-0585/) | Generic aliases (`list[int]`) | Final |
| [PEP 604](https://peps.python.org/pep-0604/) | Union type `X \| Y` | Final |
| [PEP 634](https://peps.python.org/pep-0634/) | Structural Pattern Matching (`match`) | Final |
| [PEP 654](https://peps.python.org/pep-0654/) | Exception Groups (`ExceptionGroup`, `except*`) | Final |
| [PEP 695](https://peps.python.org/pep-0695/) | Type Parameter Syntax (`type X = ...`) | Final (3.12) |

---

## Third-Party Tools Used in This Project

| Tool | Purpose | Install |
|---|---|---|
| [UV](https://docs.astral.sh/uv/) | Package manager | See README.md |
| [pytest](https://docs.pytest.org/) | Testing framework | `uv add --dev pytest` |
| [pytest-cov](https://pytest-cov.readthedocs.io/) | Coverage reporting | `uv add --dev pytest-cov` |
| [mypy](https://mypy.readthedocs.io/) | Static type checker | `uv add --dev mypy` |
| [ruff](https://docs.astral.sh/ruff/) | Fast linter + formatter | `uv add --dev ruff` |
| [black](https://black.readthedocs.io/) | Code formatter | `uv add --dev black` |
| [click](https://click.palletsprojects.com/) | CLI framework | `uv add click` |
| [aiohttp](https://docs.aiohttp.org/) | Async HTTP | `uv add aiohttp` |
