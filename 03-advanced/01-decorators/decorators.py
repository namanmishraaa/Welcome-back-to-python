"""
Decorators — Advanced Python
==============================
Covers: function decorators, parameterized, class-based, built-in patterns
"""
import time
import functools
import logging
from typing import Callable, Any

logging.basicConfig(level=logging.INFO, format="%(message)s")

# ─── 1. Simple Function Decorator ─────────────────────────────────────────────
def timer(func: Callable) -> Callable:
    """Measure and print function execution time."""
    @functools.wraps(func)          # preserve __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__!r} executed in {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n: int) -> int:
    return sum(range(n))

print(slow_sum(1_000_000))

# ─── 2. Logger Decorator ──────────────────────────────────────────────────────
def log_calls(func: Callable) -> Callable:
    """Log function calls and return values."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str   = ", ".join(repr(a) for a in args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args   = ", ".join(filter(None, [args_str, kwargs_str]))
        logging.info(f"Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@log_calls
def add(a: int, b: int) -> int:
    return a + b

add(3, b=4)

# ─── 3. Parameterized Decorator ───────────────────────────────────────────────
def repeat(n: int):
    """Run the decorated function n times."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name: str) -> str:
    print(f"Hello, {name}!")
    return name

greet("Alice")

# ─── 4. Retry Decorator ───────────────────────────────────────────────────────
def retry(max_attempts: int = 3, exceptions: tuple = (Exception,), delay: float = 0.1):
    """Retry a function on specified exceptions."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed ({e}). Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

import random
@retry(max_attempts=5, exceptions=(ValueError,), delay=0.0)
def flaky_function():
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"

print(flaky_function())

# ─── 5. Caching / Memoize Decorator ──────────────────────────────────────────
def memoize(func: Callable) -> Callable:
    """Cache results keyed by arguments."""
    cache: dict = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.cache = cache
    return wrapper

@memoize
def fib(n: int) -> int:
    if n < 2: return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(10)])

# Built-in: functools.lru_cache
from functools import lru_cache

@lru_cache(maxsize=128)
def fib_lru(n: int) -> int:
    if n < 2: return n
    return fib_lru(n - 1) + fib_lru(n - 2)

# ─── 6. Class-Based Decorator (with state) ────────────────────────────────────
class CallCount:
    """Count how many times a function has been called."""
    def __init__(self, func: Callable):
        functools.update_wrapper(self, func)
        self.func  = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@CallCount
def say_hello():
    print("Hello!")

say_hello(); say_hello(); say_hello()
print(f"Called {say_hello.count} times")

# ─── 7. Stacking Decorators ───────────────────────────────────────────────────
# Applied bottom-up: @timer wraps the result of @log_calls wrapping the function

@timer
@log_calls
def multiply(a: int, b: int) -> int:
    return a * b

multiply(4, 5)


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Write a validate_types decorator that checks argument types match annotations.
# TODO 2: Implement a rate_limit(calls_per_second) decorator.
# TODO 3: Write a singleton decorator that ensures a class has only one instance.
# TODO 4: Build a debug decorator that prints args/kwargs and result only in DEBUG mode.
# TODO 5: Implement a timeout(seconds) decorator using threading.
