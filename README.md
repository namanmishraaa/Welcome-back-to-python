# Welcome Back to Python 🐍

A **comprehensive Python skills refresher** designed for intermediate developers who want to strengthen their fundamentals, deepen their understanding of advanced concepts, and **prepare for technical interviews**.

This repository covers **every essential Python topic** needed for interviews and professional development, organized from beginner through advanced levels with exercises and projects.

## 📚 Repository Structure

```
Welcome-back-to-python/
├── 01-beginner/
│   ├── 01-basics/                    # Data types, operators, string manipulation
│   ├── 02-control_flow/              # Conditionals, loops, comprehensions
│   ├── 03-functions/                 # Functions, scope, closures
│   └── projects/                     # Beginner-level projects
├── 02-intermediate/
│   ├── 01-data_structures/           # Lists, dicts, sets, tuples, deque
│   ├── 02-file_handling/             # File I/O, JSON, CSV, context managers
│   ├── 03-oop_basics/                # Classes, inheritance, polymorphism, encapsulation
│   └── projects/                     # Intermediate-level projects
├── 03-advanced/
│   ├── 01-decorators/                # Function decorators, class decorators, parameterized
│   ├── 02-generators/                # Iterators, generators, yield, lazy evaluation
│   ├── 03-async_programming/         # asyncio, async/await, concurrent.futures
│   └── projects/                     # Advanced-level projects
├── pyproject.toml                    # UV project configuration
├── uv.lock                           # Dependency lock file
└── README.md
```

## 🎯 Coverage by Level

### 1️⃣ **Beginner Level** — Python Fundamentals

**Topics:**
- Variables, data types (int, float, str, bool)
- Operators (arithmetic, comparison, logical, assignment)
- String manipulation (formatting, methods, slicing)
- Input/output (print, input, f-strings)
- Conditionals (if/elif/else)
- Loops (for, while, break, continue)
- List/dict comprehensions
- Function basics (def, parameters, return, *args, **kwargs)
- Built-in functions (len, range, enumerate, zip, map, filter)

**Interview Focus:**
- Time/space complexity basics
- String problems (palindromes, anagrams, reversals)
- Number problems (factorials, fibonacci, primes)

**Projects:**
1. **Calculator** — Basic arithmetic and expression evaluation
2. **Number Guesser** — Game with loop logic and conditionals
3. **Todo List** — File persistence and list operations

---

### 2️⃣ **Intermediate Level** — Practical Programming

**Topics:**
- Lists, tuples, sets, dictionaries (operations, methods)
- Collections module (namedtuple, Counter, defaultdict, deque)
- File handling (open, read, write, seek, append)
- JSON/CSV parsing and serialization
- Exception handling (try/except/finally, custom exceptions)
- Context managers (with statement, creating custom)
- Object-Oriented Programming:
  - Classes, constructors, methods
  - Instance vs class variables
  - Inheritance, method overriding
  - Polymorphism, duck typing
  - Abstract base classes
  - `__init__`, `__str__`, `__repr__`, magic methods
- Modules and packages (imports, `__name__`, `__main__`)

**Interview Focus:**
- Data structure operations and trade-offs
- OOP design patterns (singleton, factory, observer)
- Problem solving with dictionaries and sets
- File I/O and data processing
- Exception handling best practices

**Projects:**
1. **Library Management System** — OOP, file persistence, search algorithms
2. **Inventory Manager** — CRUD operations, data validation, CSV handling

---

### 3️⃣ **Advanced Level** — Professional Python

**Topics:**
- Decorators:
  - Function decorators (syntax, use cases)
  - Class decorators
  - Parameterized decorators
  - Built-in decorators (@staticmethod, @classmethod, @property)
  - Decorator patterns (timing, logging, authentication)
- Generators and Iterators:
  - Iterator protocol (`__iter__`, `__next__`)
  - Generator functions (yield, send)
  - Generator expressions
  - Lazy evaluation and memory efficiency
- Async Programming:
  - asyncio basics (event loop, coroutines)
  - async/await syntax
  - Concurrent.futures (ThreadPoolExecutor, ProcessPoolExecutor)
  - Event handling and callbacks
- Advanced Features:
  - Metaclasses (basics)
  - Descriptors (`__get__`, `__set__`, `__delete__`)
  - Context managers (advanced patterns)
  - Closures and scope
  - Lambda and functional programming

**Interview Focus:**
- Design patterns and their implementation
- Performance optimization
- Concurrency and parallelism concepts
- Code maintainability and SOLID principles
- Real-world architectural decisions

**Projects:**
1. **Web Scraper** — Async I/O, decorators, exception handling, data parsing
2. **Data Analyzer** — File processing, generators, comprehensions, visualization

---

## 🛠️ Setup with UV

UV is a fast Python package manager and project manager. [Learn more about UV](https://docs.astral.sh/uv/)

### Installation

**Windows:**
```bash
powershell -ExecutionPolicy BypassCurrentUser -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Project Setup

```bash
# Create and activate virtual environment
uv venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS/Linux)
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

## 📖 How to Use This Repository

### For Learning & Practice
1. **Start at your level** (or begin with beginner for comprehensive review)
2. Read the `README.md` in each topic folder
3. Work through exercises in order
4. Complete projects to integrate learning
5. Refactor earlier code using new techniques

### For Interview Preparation
1. **Focus areas:** Beginner fundamentals + Intermediate data structures/OOP
2. **Mock interview topics:**
   - Data structure operations (lists, dicts, sets)
   - String manipulation
   - Algorithmic thinking (recursion, searching, sorting)
   - OOP design and implementation
   - Code optimization
3. **Advanced topics:** Decorators, generators, async (useful for system design interviews)

### Suggested Progression

**Option A: Complete Refresh (Recommended)**
```
01-beginner → 02-intermediate → 03-advanced
(Thorough review of all concepts)
```

**Option B: Interview Focused**
```
01-beginner/01-basics → 02-intermediate → Review 03-advanced topics selectively
(Prioritize data structures, algorithms, OOP)
```

**Option C: Quick Review**
```
Start at 02-intermediate with spot-checks in 01-beginner
(Only if confident in fundamentals)
```

## 📋 Topic Checklist for Interviews

Use this to track your preparation:

### Core (Must Know)
- [ ] Data types and operations
- [ ] Loops and conditionals
- [ ] Functions and scope
- [ ] Lists and dictionaries
- [ ] Classes and inheritance
- [ ] Exception handling
- [ ] File I/O

### Important (Should Know)
- [ ] List/dict comprehensions
- [ ] Sets and tuples
- [ ] String methods
- [ ] Collections module
- [ ] Decorators (basics)
- [ ] Generators
- [ ] Context managers

### Advanced (Nice to Know)
- [ ] Async programming
- [ ] Metaclasses
- [ ] Descriptors
- [ ] Design patterns
- [ ] Performance optimization

## 💡 Learning Tips

1. **Understand before memorizing** — Know *why* and *when* to use each concept
2. **Write code daily** — Consistency matters more than marathon sessions
3. **Refactor often** — Rewrite earlier solutions with new techniques
4. **Complete projects** — They integrate multiple concepts and build confidence
5. **Time yourself** — Practice problem-solving under time constraints
6. **Explain out loud** — Teaching yourself strengthens understanding
7. **Review frequently** — Revisit earlier topics while learning new ones

## 📚 Interview Preparation Guide

### Week 1-2: Fundamentals
- Cover `01-beginner/` thoroughly
- Focus on problem-solving, not syntax

### Week 3-4: Data Structures & OOP
- Master `02-intermediate/` topics
- Practice with LeetCode-style problems
- Implement data structures from scratch

### Week 5-6: Advanced Topics & System Design
- Cover `03-advanced/` as needed
- Focus on architectural decisions
- Practice design pattern interviews

### Ongoing: Practice
- Complete projects in this repo
- Solve interview problems
- Review weak areas

## 🤖 skill-check-agent — Automated Skill Assessment

Test your Python knowledge interactively, topic by topic, level by level. The agent tracks your progress, enforces a 70% pass threshold per topic, and automatically unlocks the next level when you've mastered the current one.

### Setup

```bash
# Activate your virtual environment first
uv venv && .venv\Scripts\activate   # Windows
# or: source .venv/bin/activate     # macOS/Linux

# Install the package in editable mode (registers the CLI entry point)
uv pip install -e .
```

### Usage

```bash
# Run overall quiz at your current level (default behaviour)
skill-check-agent

# Quiz all topics in a specific level
skill-check-agent --level beginner
skill-check-agent --level intermediate
skill-check-agent --level advanced

# Quiz a single topic within a level
skill-check-agent --level beginner    --topic basics
skill-check-agent --level beginner    --topic control_flow
skill-check-agent --level beginner    --topic functions
skill-check-agent --level intermediate --topic data_structures
skill-check-agent --level intermediate --topic oop_basics
skill-check-agent --level advanced    --topic decorators
skill-check-agent --level advanced    --topic type_hints

# Show your current progress and scores
skill-check-agent --status

# List all available levels and topics
skill-check-agent --list

# Reset all progress and start over
skill-check-agent --reset
```

> You can also invoke it without installing: `python -m skill_check_agent [options]`

### How It Works

| Concept | Detail |
|---|---|
| **Question bank** | 65 MCQ questions across 15 topics and 3 levels |
| **Pass threshold** | 70% per topic to mark it as passed |
| **Level advancement** | All topics in a level must be passed → unlocks next level |
| **Progress persistence** | Scores saved to `.skill_check_progress.json` (gitignored) |
| **Quiz sampling** | 5 questions per topic per session (randomised from full bank) |

### Topics Covered

| Level | Topics |
|---|---|
| **Beginner** | basics, control_flow, functions |
| **Intermediate** | data_structures, file_handling, oop_basics, modules_packages, standard_library |
| **Advanced** | decorators, generators, async_programming, type_hints, dataclasses, testing, design_patterns |

### Advancement Flow

```
BEGINNER (pass all 3 topics at 70%+)
    └── unlocks INTERMEDIATE (pass all 5 topics at 70%+)
            └── unlocks ADVANCED
```

---

## 🔗 Useful Resources

- **Problem Solving:** [LeetCode](https://leetcode.com/), [HackerRank](https://www.hackerrank.com/)
- **Official Docs:** [Python.org](https://docs.python.org/3/)
- **Real-world:** Read open-source Python projects on GitHub
- **Videos:** Tech interview channels for mock interviews

## 🎯 Success Metrics

✅ Can solve problems without looking at solutions
✅ Understand time/space complexity of your solutions
✅ Can explain your code to someone else
✅ Comfortable with OOP and design patterns
✅ Can optimize code for performance
✅ Confident in technical interviews

---

**Start wherever you are. Progress at your own pace. Master Python! 🚀**

Begin with `01-beginner/` or jump to your comfort level. Each topic builds toward interview readiness and professional excellence.
