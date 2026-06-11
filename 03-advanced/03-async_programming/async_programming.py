"""
Async Programming — Advanced Python
=====================================
Covers: event loop, async/await, gather, Queue, ThreadPoolExecutor
"""
import asyncio
import time
import concurrent.futures
from typing import Any

# ─── 1. Coroutines and async/await ────────────────────────────────────────────
async def greet(name: str, delay: float) -> str:
    """Async function: suspends with 'await', not blocking."""
    await asyncio.sleep(delay)
    return f"Hello, {name}!"

async def main_basic():
    result = await greet("Alice", 1)
    print(result)

asyncio.run(main_basic())

# ─── 2. Concurrent Execution with gather() ───────────────────────────────────
async def fetch_data(url: str, delay: float) -> dict:
    """Simulate an async HTTP fetch."""
    await asyncio.sleep(delay)
    return {"url": url, "data": f"content from {url}"}

async def main_concurrent():
    start = time.perf_counter()

    # Sequential — total time = sum of delays
    # for url in urls: await fetch_data(url, 1)

    # Concurrent — total time = max(delays)
    results = await asyncio.gather(
        fetch_data("https://api.example.com/users",    1.0),
        fetch_data("https://api.example.com/products", 1.5),
        fetch_data("https://api.example.com/orders",   0.8),
    )

    elapsed = time.perf_counter() - start
    for r in results:
        print(r["url"])
    print(f"Completed in {elapsed:.2f}s")   # ~1.5s, not 3.3s

asyncio.run(main_concurrent())

# ─── 3. asyncio.create_task() ─────────────────────────────────────────────────
async def main_tasks():
    # create_task schedules coroutines immediately; they run concurrently
    task1 = asyncio.create_task(greet("Bob",   0.5))
    task2 = asyncio.create_task(greet("Carol", 0.3))

    result2 = await task2    # Carol is faster
    result1 = await task1
    print(result2, result1)

asyncio.run(main_tasks())

# ─── 4. Timeouts ──────────────────────────────────────────────────────────────
async def slow_operation() -> str:
    await asyncio.sleep(5)
    return "done"

async def main_timeout():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
    except asyncio.TimeoutError:
        print("Operation timed out!")

asyncio.run(main_timeout())

# ─── 5. asyncio.Queue — Producer / Consumer ───────────────────────────────────
async def producer(queue: asyncio.Queue, items: list):
    for item in items:
        await asyncio.sleep(0.1)
        await queue.put(item)
        print(f"Produced: {item}")
    await queue.put(None)   # sentinel

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        await asyncio.sleep(0.05)
        print(f"Consumed: {item}")
        queue.task_done()

async def main_queue():
    queue = asyncio.Queue(maxsize=3)
    await asyncio.gather(
        producer(queue, list(range(5))),
        consumer(queue),
    )

asyncio.run(main_queue())

# ─── 6. Semaphore — Limit Concurrent Connections ─────────────────────────────
async def limited_fetch(sem: asyncio.Semaphore, url: str) -> str:
    async with sem:
        await asyncio.sleep(0.5)
        return f"data from {url}"

async def main_semaphore():
    sem  = asyncio.Semaphore(2)   # max 2 concurrent requests
    urls = [f"url-{i}" for i in range(6)]
    results = await asyncio.gather(*(limited_fetch(sem, u) for u in urls))
    print(results)

asyncio.run(main_semaphore())

# ─── 7. Run Blocking Code in Thread Pool ─────────────────────────────────────
def cpu_bound(n: int) -> int:
    """Blocking / CPU-heavy function."""
    return sum(range(n))

async def main_executor():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound, 10_000_000)
    print(f"Sum: {result}")

asyncio.run(main_executor())

# ─── 8. ThreadPoolExecutor and ProcessPoolExecutor ────────────────────────────
def square(n: int) -> int:
    return n * n

# Threads — I/O-bound
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(square, range(10)))
print(results)

# Processes — CPU-bound (bypasses GIL)
if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(square, n) for n in range(5)]
        for f in concurrent.futures.as_completed(futures):
            print(f.result())


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Fetch 10 URLs concurrently using aiohttp and gather().
# TODO 2: Implement a bounded async worker pool that processes a task queue.
# TODO 3: Use asyncio.wait() to process results as they complete (not in order).
# TODO 4: Benchmark async vs threaded vs sequential for 20 simulated I/O tasks.
# TODO 5: Implement an async rate limiter (max N requests per second).
