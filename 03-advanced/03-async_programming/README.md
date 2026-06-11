# 03-async_programming — Concurrency and Asynchronous Code

Master async programming: write non-blocking, efficient Python programs using asyncio and concurrency tools.

## 📚 Topics Covered

### 1. Concurrency vs Parallelism
- **Concurrency** — Multiple tasks making progress (not necessarily simultaneously)
- **Parallelism** — Multiple tasks running simultaneously (multi-core)
- **GIL (Global Interpreter Lock)** — Why Python threads don't give true parallelism
- **I/O-bound vs CPU-bound** — Which approach suits which workload
- **Threading vs multiprocessing vs asyncio** — Choosing the right tool

### 2. asyncio Fundamentals
- **Event loop** — The core of asyncio, managing coroutines
- **Coroutines** — Functions defined with `async def`
- **`await` keyword** — Suspending coroutine execution
- **`asyncio.run()`** — Entry point for async programs
- **Tasks** — `asyncio.create_task()`, scheduling coroutines
- **Awaitables** — Coroutines, Tasks, Futures

### 3. async/await Patterns
- **Sequential vs concurrent execution** — `await` vs `asyncio.gather()`
- **`asyncio.gather()`** — Running multiple coroutines concurrently
- **`asyncio.wait()`** — Waiting with more control
- **`asyncio.wait_for()`** — Timeouts on coroutines
- **Async context managers** — `async with`
- **Async iterators and generators** — `async for`, `async yield`

### 4. Common asyncio Patterns
- **HTTP requests concurrently** — Using `aiohttp`
- **Async file I/O** — Using `aiofiles`
- **Producer-consumer** — `asyncio.Queue`
- **Semaphores** — Limiting concurrent operations
- **Locks** — Preventing race conditions
- **Event and Condition** — Synchronization primitives

### 5. concurrent.futures
- **`ThreadPoolExecutor`** — Thread pool for I/O-bound tasks
- **`ProcessPoolExecutor`** — Process pool for CPU-bound tasks
- **`submit()` and `map()`** — Submitting work to executors
- **Futures** — Representing pending results
- **`as_completed()`** — Processing results as they finish
- **Executor with asyncio** — `loop.run_in_executor()`

### 6. Threading Module
- **`threading.Thread`** — Creating and managing threads
- **Thread synchronization** — `Lock`, `RLock`, `Semaphore`, `Event`
- **`threading.local()`** — Thread-local storage
- **Daemon threads** — Background threads
- **When to use threads** — I/O-bound tasks only (GIL)

### 7. Multiprocessing Module
- **`multiprocessing.Process`** — Creating processes
- **Process pools** — `multiprocessing.Pool`
- **`map()` and `starmap()`** — Parallel execution
- **Shared memory** — `Value`, `Array`, `Manager`
- **Queues and Pipes** — Inter-process communication
- **When to use multiprocessing** — CPU-bound tasks

## 💡 Learning Objectives

By the end of this section, you should be able to:
- ✅ Understand event loop and coroutine execution model
- ✅ Write async functions and use `await` correctly
- ✅ Run coroutines concurrently with `asyncio.gather()`
- ✅ Use `ThreadPoolExecutor` and `ProcessPoolExecutor`
- ✅ Understand when to use async vs threads vs multiprocessing
- ✅ Implement producer-consumer patterns with `asyncio.Queue`
- ✅ Handle timeouts and cancellation

## 📝 Files in This Section

1. **concurrency_concepts.py** — GIL, I/O vs CPU bound, choosing the right tool
2. **asyncio_basics.py** — Event loop, coroutines, `async def`, `await`, `asyncio.run()`
3. **async_patterns.py** — `gather()`, `wait()`, `wait_for()`, async context managers
4. **async_generators.py** — Async iterators, `async for`, `async yield`
5. **concurrent_futures.py** — `ThreadPoolExecutor`, `ProcessPoolExecutor`, `Future`
6. **threading_module.py** — Threads, locks, synchronization
7. **multiprocessing_module.py** — Processes, pools, shared memory, IPC
8. **exercises.py** — Practice problems on async programming

## 🎯 Interview Tips

**Common Questions:**
- What is the GIL and how does it affect Python concurrency?
- When would you use asyncio vs threading vs multiprocessing?
- Explain the event loop
- What's the difference between a coroutine and a thread?
- How does `asyncio.gather()` work?
- What happens when you `await` a coroutine?
- What's the difference between `asyncio.wait()` and `asyncio.gather()`?

**Key Points to Master:**
- GIL makes threading suitable only for I/O-bound work
- asyncio is single-threaded concurrency — no shared-state race conditions
- Multiprocessing bypasses the GIL for true CPU parallelism
- `async def` defines a coroutine, not a regular function
- `await` suspends the current coroutine, not the whole program
- `asyncio.gather()` runs coroutines concurrently within the event loop

## 🚀 Next Steps

After mastering async programming:
1. Build the advanced projects using async I/O
2. Explore `aiohttp` for async HTTP clients/servers
3. Study `FastAPI` for async web APIs
4. Look into `Celery` for distributed task queues

---

**Difficulty: ⭐⭐⭐ Essential for modern high-performance Python**
