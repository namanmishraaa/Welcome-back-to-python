"""
Generators and Iterators — Advanced Python
==========================================
Covers: iterator protocol, yield, send(), yield from, generator pipelines
"""
from typing import Generator, Iterator

# ─── 1. Iterator Protocol ─────────────────────────────────────────────────────
class Countdown:
    """Custom iterator counting down from n to 1."""
    def __init__(self, start: int):
        self.current = start

    def __iter__(self) -> "Countdown":
        return self           # the iterator IS the iterable

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        value         = self.current
        self.current -= 1
        return value

for n in Countdown(5):
    print(n, end=" ")
print()

# ─── 2. Generator Functions ───────────────────────────────────────────────────
def countdown_gen(start: int) -> Generator[int, None, None]:
    """Same as Countdown but as a generator — much simpler."""
    while start > 0:
        yield start
        start -= 1

for n in countdown_gen(5):
    print(n, end=" ")
print()

# Generators are lazy — values computed on demand
def infinite_counter(start: int = 0) -> Generator[int, None, None]:
    n = start
    while True:
        yield n
        n += 1

gen = infinite_counter()
print([next(gen) for _ in range(5)])   # [0, 1, 2, 3, 4]

# ─── 3. Generator Expressions ─────────────────────────────────────────────────
# Lazy equivalent of list comprehension
squares_gen  = (x ** 2 for x in range(10))   # not yet computed
squares_list = [x ** 2 for x in range(10)]   # computed immediately

print(next(squares_gen))   # 0 — compute on demand
print(sum(x**2 for x in range(1001)))  # memory-efficient sum

# ─── 4. Practical Generator Patterns ─────────────────────────────────────────
def read_large_file(path: str) -> Generator[str, None, None]:
    """Yield lines one at a time — never loads full file in memory."""
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line.strip()

def filter_gen(predicate, iterable):
    """Lazy filter — generator version."""
    for item in iterable:
        if predicate(item):
            yield item

def map_gen(transform, iterable):
    """Lazy map — generator version."""
    for item in iterable:
        yield transform(item)

# Generator pipeline — compose lazy transformations
def pipeline_demo():
    nums    = range(1, 21)
    evens   = filter_gen(lambda n: n % 2 == 0, nums)
    squares = map_gen(lambda n: n ** 2, evens)
    for s in squares:
        print(s, end=" ")
    print()

pipeline_demo()

# ─── 5. send() — Two-Way Communication ───────────────────────────────────────
def accumulator() -> Generator[float, float, str]:
    """Receive values via send() and yield running total."""
    total = 0.0
    while True:
        value = yield total     # yield sends total out, receives new value
        if value is None:
            break
        total += value
    return f"Final total: {total}"

acc = accumulator()
next(acc)          # prime the generator (advance to first yield)
print(acc.send(10))   # 10.0
print(acc.send(20))   # 30.0
print(acc.send(5))    # 35.0

# ─── 6. yield from — Delegating to Sub-Generators ────────────────────────────
def chain(*iterables):
    """Flat-chain multiple iterables together."""
    for iterable in iterables:
        yield from iterable

print(list(chain([1, 2], [3, 4], [5, 6])))   # [1, 2, 3, 4, 5, 6]

def flatten(nested):
    """Recursively flatten nested lists."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

print(list(flatten([1, [2, [3, 4]], [5, 6]])))   # [1, 2, 3, 4, 5, 6]

# ─── 7. Fibonacci Generator ───────────────────────────────────────────────────
def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

from itertools import islice
print(list(islice(fibonacci(), 10)))   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Implement a generator that yields primes (Sieve of Eratosthenes).
# TODO 2: Write a generator pipeline: read CSV → filter rows → transform columns → write output.
# TODO 3: Create a generator that batches items: batch([1..10], 3) → [1,2,3], [4,5,6], [7,8,9], [10].
# TODO 4: Implement coroutine-style grep: a generator that receives text and yields matching lines.
# TODO 5: Write a generator-based round-robin scheduler over multiple iterables.
