"""
itertools & functools — Functional Toolbox
==========================================
Ref: https://docs.python.org/3/tutorial/stdlib2.html#tools-for-working-with-lists
     https://docs.python.org/3/library/itertools.html
     https://docs.python.org/3/library/functools.html
"""
import itertools
import functools
from typing import Callable, TypeVar

T = TypeVar("T")

# ════════════════════════════════════════════════════════════
#  itertools — iterator building blocks
# ════════════════════════════════════════════════════════════

# ─── 1. Infinite Iterators ────────────────────────────────────────────────────
counter = itertools.count(10, 2)         # 10, 12, 14, ...
print(list(itertools.islice(counter, 5))) # [10, 12, 14, 16, 18]

cycler = itertools.cycle("ABCD")
print(list(itertools.islice(cycler, 9)))  # ['A','B','C','D','A','B','C','D','A']

repeater = itertools.repeat("go!", 3)
print(list(repeater))   # ['go!', 'go!', 'go!']

# ─── 2. Finite Iterators ──────────────────────────────────────────────────────
# chain — flatten multiple iterables
print(list(itertools.chain([1, 2], [3, 4], [5])))  # [1,2,3,4,5]
print(list(itertools.chain.from_iterable([[1,2],[3,4]])))  # same

# islice — lazy slice
print(list(itertools.islice(range(100), 5, 15, 2)))  # [5,7,9,11,13]

# takewhile / dropwhile — stop/start based on predicate
print(list(itertools.takewhile(lambda x: x < 5, [1,2,3,4,5,6])))  # [1,2,3,4]
print(list(itertools.dropwhile(lambda x: x < 5, [1,2,3,4,5,6])))  # [5,6]

# filterfalse — opposite of filter
print(list(itertools.filterfalse(str.isdigit, "a1b2c3")))  # ['a','b','c']

# compress — filter with selector
data     = ["a", "b", "c", "d", "e"]
selector = [1, 0, 1, 0, 1]
print(list(itertools.compress(data, selector)))   # ['a','c','e']

# accumulate — running totals (or any binary op)
print(list(itertools.accumulate([1, 2, 3, 4, 5])))               # [1,3,6,10,15]
print(list(itertools.accumulate([1,2,3,4,5], func=lambda a,b: a*b)))  # factorials

# pairwise (Python 3.10+)
print(list(itertools.pairwise([1,2,3,4])))  # [(1,2),(2,3),(3,4)]

# ─── 3. Combinatorics ─────────────────────────────────────────────────────────
# product — cartesian product
print(list(itertools.product("AB", [1, 2])))     # [('A',1),('A',2),('B',1),('B',2)]
print(list(itertools.product(range(2), repeat=3))) # all 3-bit binary numbers

# permutations — ordered arrangements
print(list(itertools.permutations("ABC", 2)))    # AB AC BA BC CA CB

# combinations — unordered selections WITHOUT replacement
print(list(itertools.combinations("ABCD", 2)))   # AB AC AD BC BD CD

# combinations_with_replacement — WITH replacement
print(list(itertools.combinations_with_replacement("AB", 2)))  # AA AB BB

# ─── 4. groupby ───────────────────────────────────────────────────────────────
# ⚠️ Input MUST be sorted by the key first!
data = [
    {"name": "Alice", "dept": "Eng"},
    {"name": "Bob",   "dept": "Eng"},
    {"name": "Carol", "dept": "HR"},
    {"name": "Dave",  "dept": "HR"},
    {"name": "Eve",   "dept": "Eng"},  # ← will form a SECOND 'Eng' group (not sorted!)
]
data.sort(key=lambda x: x["dept"])   # sort first!
for dept, members in itertools.groupby(data, key=lambda x: x["dept"]):
    print(dept, [m["name"] for m in members])

# ════════════════════════════════════════════════════════════
#  functools — higher-order functions
# ════════════════════════════════════════════════════════════

# ─── 5. functools.partial ─────────────────────────────────────────────────────
def power(base: float, exp: float) -> float:
    return base ** exp

square = functools.partial(power, exp=2)
cube   = functools.partial(power, exp=3)
print(square(5), cube(3))   # 25.0  27.0

# ─── 6. functools.reduce ──────────────────────────────────────────────────────
import operator
product = functools.reduce(operator.mul, range(1, 6))   # 5! = 120
print(product)

# ─── 7. functools.lru_cache / cache ───────────────────────────────────────────
@functools.lru_cache(maxsize=128)
def fib(n: int) -> int:
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print([fib(i) for i in range(10)])
print(fib.cache_info())   # CacheInfo(hits=..., misses=..., maxsize=128, currsize=9)
fib.cache_clear()

@functools.cache   # Python 3.9+ — unbounded cache (simpler)
def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n-1)

# ─── 8. functools.total_ordering ──────────────────────────────────────────────
@functools.total_ordering
class Version:
    def __init__(self, major, minor, patch):
        self.v = (major, minor, patch)
    def __eq__(self, other): return self.v == other.v
    def __lt__(self, other): return self.v <  other.v  # only need eq + lt

v1, v2 = Version(1,0,0), Version(1,2,0)
print(v1 < v2, v1 <= v2, v1 > v2, v1 >= v2)

# ─── 9. functools.singledispatch ──────────────────────────────────────────────
@functools.singledispatch
def process(value) -> str:
    return f"Unknown type: {type(value).__name__}"

@process.register(int)
def _(v: int) -> str: return f"Integer: {v}"

@process.register(str)
def _(v: str) -> str: return f"String: {v!r}"

@process.register(list)
def _(v: list) -> str: return f"List of {len(v)}"

for val in [42, "hello", [1,2,3], 3.14]:
    print(process(val))


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Use itertools.product to generate all possible 4-digit PINs.
# TODO 2: Use groupby to group a list of transactions by date.
# TODO 3: Use accumulate to compute a running maximum of a list.
# TODO 4: Implement a pipeline() function using functools.reduce and a list of functions.
# TODO 5: Use singledispatch to write a to_json() function handling int, str, list, dict.
