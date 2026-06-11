# 05-standard_library — Python's Batteries-Included

Master the most important modules from the Python Standard Library — the tools every professional uses daily.

**Official Docs:**
- Part I:  https://docs.python.org/3/tutorial/stdlib.html
- Part II: https://docs.python.org/3/tutorial/stdlib2.html

## 📚 Topics Covered

### `os_sys_pathlib.py` — OS & File System
- `os` — environment vars, process info, file/dir operations
- `sys` — interpreter internals (`sys.argv`, `sys.path`, `sys.exit`)
- `pathlib` — modern, OOP path handling (`Path`)
- `shutil` — high-level file operations (copy, move, rmtree)

### `re_regex.py` — Regular Expressions
- Pattern syntax — `.`, `*`, `+`, `?`, `[]`, `^`, `$`, `\d`, `\w`, `\s`
- `re.match` vs `re.search` vs `re.findall` vs `re.finditer`
- Groups — `()`, named groups `(?P<name>...)`
- Flags — `re.IGNORECASE`, `re.MULTILINE`, `re.DOTALL`
- Compiled patterns — `re.compile()`
- Substitution — `re.sub()`, `re.subn()`

### `math_random_statistics.py` — Numerics
- `math` — `floor`, `ceil`, `sqrt`, `log`, `factorial`, `gcd`, `pi`, `inf`
- `random` — `random()`, `randint`, `choice`, `shuffle`, `sample`, `seed`
- `statistics` — `mean`, `median`, `mode`, `stdev`, `variance`
- `decimal` — arbitrary-precision decimal arithmetic
- `fractions` — exact rational arithmetic

### `datetime_module.py` — Dates and Times
- `datetime.date`, `datetime.time`, `datetime.datetime`
- `timedelta` — arithmetic on dates/times
- `strftime` / `strptime` — formatting and parsing
- Timezone-aware datetimes — `datetime.timezone`, `zoneinfo`
- `calendar` module basics

### `argparse_cli.py` — Command-Line Interfaces
- `argparse.ArgumentParser` — building CLI tools
- Positional and optional arguments
- Type conversion, default values, choices
- Subcommands — `add_subparsers()`
- `click` overview (third-party, industry standard)

### `logging_module.py` — Logging
- Log levels — DEBUG, INFO, WARNING, ERROR, CRITICAL
- `logging.basicConfig()` — quick setup
- Loggers, Handlers, Formatters — professional setup
- File handlers, rotating file handlers
- Structured logging best practices

### `itertools_functools.py` — Functional Toolbox
- `itertools`: `chain`, `product`, `permutations`, `combinations`, `groupby`,
               `islice`, `takewhile`, `dropwhile`, `cycle`, `repeat`, `accumulate`
- `functools`: `partial`, `lru_cache`, `reduce`, `wraps`, `total_ordering`,
               `cache` (3.9+), `singledispatch`

### `heapq_bisect.py` — Sorted Structures & Priority Queues
- `heapq` — min-heap, `heappush`, `heappop`, `nlargest`, `nsmallest`
- `bisect` — binary search into sorted lists, `insort`
- Use cases — priority queues, top-K problems

## 💡 Learning Objectives
- ✅ Navigate and use the standard library without third-party dependencies
- ✅ Write production-quality CLI tools with `argparse`
- ✅ Use `re` for text parsing and validation
- ✅ Set up structured logging for an application
- ✅ Apply `itertools` and `functools` for clean, functional code
- ✅ Solve top-K / priority-queue problems with `heapq`

## 🎯 Interview Tips
- Know `os.path` vs `pathlib` (prefer `pathlib` in modern code)
- `re.match()` only matches at the START — common gotcha
- `lru_cache` for memoisation without writing it yourself
- `itertools.groupby` requires the input to be sorted first
- `heapq` in Python is a min-heap — negate values for max-heap

## 🔗 Doc References
- https://docs.python.org/3/tutorial/stdlib.html
- https://docs.python.org/3/tutorial/stdlib2.html
- https://docs.python.org/3/library/ (full index)

---
**Difficulty: ⭐⭐☆ — ⭐⭐⭐ depending on topic**
