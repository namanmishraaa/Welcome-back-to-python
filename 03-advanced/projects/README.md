# Advanced Projects

Apply decorators, generators, and async programming with these complex, real-world projects.

## 📋 Project Overview

These projects combine multiple advanced concepts to solve real problems.

### Project 1: Web Scraper 🕷️
**Topics Used:** Async programming (`aiohttp`), Decorators (retry, logging, rate-limit), Generators (streaming results), File I/O

**Difficulty:** ⭐⭐⭐

**Description:**
Build an async web scraper that:
- Fetches multiple URLs concurrently with `asyncio`
- Implements retry logic with exponential backoff (decorator)
- Rate-limits requests (decorator)
- Logs all requests and errors (decorator)
- Streams results with generators
- Saves output to CSV/JSON

**Learning Goals:**
- Async HTTP requests with `aiohttp`
- Decorator composition for cross-cutting concerns
- Generator pipelines for data processing
- Concurrency control with semaphores
- Robust error handling

**Suggested Enhancements:**
- Support for following links (crawling)
- Robots.txt compliance
- Progress bar with `tqdm`
- Configurable concurrency limit
- Data deduplication using sets

---

### Project 2: Data Analyzer 📊
**Topics Used:** Generators (large file processing), Decorators (timing, caching), File I/O (CSV/JSON), Data Structures, OOP

**Difficulty:** ⭐⭐⭐

**Description:**
Build a data analysis pipeline that:
- Loads large CSV/JSON datasets using generators (memory-efficient)
- Applies transformations as a generator pipeline
- Caches expensive computations with decorators
- Times all major operations
- Generates summary statistics and reports
- Exports results to different formats

**Learning Goals:**
- Generator pipelines for large data processing
- Caching/memoization with decorators
- Performance measurement with timing decorators
- Memory-efficient data processing
- Building extensible pipelines

**Suggested Enhancements:**
- Support multiple file formats (CSV, JSON, YAML)
- Add filtering and aggregation operations
- Visualize results with `matplotlib`
- Support for streaming data
- Configurable output formats

---

## 🏆 Project Completion Checklist

For each project:
- ✅ Apply at least 2 decorators (logging, timing, retry, or caching)
- ✅ Use generators for data streaming or lazy evaluation
- ✅ Use async where I/O operations are involved
- ✅ Implement comprehensive error handling
- ✅ Write docstrings for all public APIs
- ✅ Measure and discuss performance
- ✅ Test edge cases (empty input, network failure, large files)

## 🎯 Focus Areas

### Decorator Application
- Wrap all I/O operations with retry decorator
- Add timing to all major functions
- Use logging decorator for debugging
- Implement caching for repeated operations

### Generator Usage
- Stream data instead of loading all at once
- Build composable generator pipelines
- Use generator expressions for simple transformations

### Async Patterns
- Use `asyncio.gather()` for concurrent I/O
- Control concurrency with `asyncio.Semaphore`
- Handle timeouts with `asyncio.wait_for()`

### Code Quality
- Clean, readable code with type hints
- Proper error messages and logging
- Configurable via arguments or config files

## 💡 Tips

1. **Profile before optimising** — Measure where time is actually spent
2. **Generators for large data** — Never load a full dataset into memory if avoidable
3. **Async for I/O** — Network requests should almost always be async
4. **Decorator order matters** — Think carefully when stacking decorators
5. **Test with realistic data** — Use actual-sized datasets
6. **Handle failures gracefully** — Network errors, file not found, invalid data

## 🚀 Next Steps

After completing advanced projects:
1. Refactor your beginner/intermediate projects using advanced techniques
2. Explore web frameworks — Flask, FastAPI, Django
3. Study databases — SQLAlchemy, async DB drivers
4. Contribute to open-source Python projects
5. Build your own Python packages and publish to PyPI

---

**Completed all projects? You are now a proficient Python developer!** 🎉🐍
