"""
Question bank for skill-check-agent.

Structure:
    QUESTIONS[level][topic] = list of question dicts

Question dict keys:
    q       : question text
    choices : list of 4 strings  (omit for open-answer questions)
    answer  : correct answer string (must match one choice exactly)
    explain : one-line explanation shown after answering
"""

QUESTIONS: dict = {

    # ─────────────────────────────────────────────────────────────
    # BEGINNER
    # ─────────────────────────────────────────────────────────────
    "beginner": {

        "basics": [
            {
                "q": "What is the output of: type(3 / 2)?",
                "choices": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'number'>"],
                "answer": "<class 'float'>",
                "explain": "Division always returns float in Python 3.",
            },
            {
                "q": "Which of the following is a valid f-string?",
                "choices": ["f'Hello {name}'", "'Hello' + f{name}", "f(Hello {name})", "format('Hello', name)"],
                "answer": "f'Hello {name}'",
                "explain": "f-strings use f'...' syntax with {} for expressions.",
            },
            {
                "q": "What does `bool([])` return?",
                "choices": ["True", "False", "None", "Error"],
                "answer": "False",
                "explain": "Empty containers are falsy in Python.",
            },
            {
                "q": "What is the result of `10 // 3`?",
                "choices": ["3.33", "3", "4", "1"],
                "answer": "3",
                "explain": "// is floor division — truncates toward negative infinity.",
            },
            {
                "q": "Which naming style does PEP 8 recommend for variables?",
                "choices": ["camelCase", "PascalCase", "snake_case", "UPPER_CASE"],
                "answer": "snake_case",
                "explain": "PEP 8: variables and functions use snake_case.",
            },
            {
                "q": "What does `'hello'[1:3]` return?",
                "choices": ["'hel'", "'el'", "'ell'", "'he'"],
                "answer": "'el'",
                "explain": "Slice [1:3] returns index 1 and 2 (end is exclusive).",
            },
            {
                "q": "Which operator is the walrus operator?",
                "choices": [":=", "==", "<=", "=>"],
                "answer": ":=",
                "explain": ":= (PEP 572) assigns and returns a value in expressions.",
            },
            {
                "q": "What does `str(3.14)` return?",
                "choices": ["3", "3.14", "'3.14'", "Error"],
                "answer": "'3.14'",
                "explain": "str() converts to string representation.",
            },
        ],

        "control_flow": [
            {
                "q": "What is the output of: `[x*2 for x in range(3)]`?",
                "choices": ["[0, 2, 4]", "[2, 4, 6]", "[0, 1, 2]", "[1, 2, 3]"],
                "answer": "[0, 2, 4]",
                "explain": "range(3) yields 0,1,2 — each multiplied by 2.",
            },
            {
                "q": "Which Python version introduced `match/case`?",
                "choices": ["3.8", "3.9", "3.10", "3.11"],
                "answer": "3.10",
                "explain": "Structural pattern matching (PEP 634) landed in 3.10.",
            },
            {
                "q": "What does `for i in range(5): pass` — how many iterations?",
                "choices": ["4", "5", "6", "0"],
                "answer": "5",
                "explain": "range(5) yields 0,1,2,3,4 — five values.",
            },
            {
                "q": "What is printed? `x=0\nwhile x<3:\n  x+=1\nelse:\n  print('done')`",
                "choices": ["Nothing", "done", "Error", "0 1 2"],
                "answer": "done",
                "explain": "The else clause on a while runs when the condition becomes False (no break).",
            },
            {
                "q": "What does `{x: x**2 for x in range(3)}` produce?",
                "choices": ["{0:0, 1:1, 2:4}", "[0, 1, 4]", "{0, 1, 4}", "(0, 1, 4)"],
                "answer": "{0:0, 1:1, 2:4}",
                "explain": "Dict comprehension with key:value syntax.",
            },
            {
                "q": "What does `enumerate(['a','b'], start=1)` give on first iteration?",
                "choices": ["(0, 'a')", "(1, 'a')", "('a', 1)", "1"],
                "answer": "(1, 'a')",
                "explain": "start=1 makes the counter begin at 1.",
            },
        ],

        "functions": [
            {
                "q": "What does `*args` capture in a function signature?",
                "choices": [
                    "Keyword arguments as a dict",
                    "Positional arguments as a tuple",
                    "All arguments as a list",
                    "Default values",
                ],
                "answer": "Positional arguments as a tuple",
                "explain": "*args collects extra positional args into a tuple.",
            },
            {
                "q": "What is the LEGB rule?",
                "choices": [
                    "List, Enumerate, Global, Built-in",
                    "Local, Enclosing, Global, Built-in",
                    "Local, External, Global, Base",
                    "Lambda, Enclosing, Global, Built-in",
                ],
                "answer": "Local, Enclosing, Global, Built-in",
                "explain": "Python resolves names in Local → Enclosing → Global → Built-in order.",
            },
            {
                "q": "What does `lambda x: x**2` do?",
                "choices": [
                    "Defines a named function",
                    "Creates an anonymous function that squares x",
                    "Creates a class",
                    "Raises x to the power of 2 immediately",
                ],
                "answer": "Creates an anonymous function that squares x",
                "explain": "lambda creates a small anonymous function inline.",
            },
            {
                "q": "What keyword is needed to modify a variable from an enclosing scope?",
                "choices": ["global", "nonlocal", "extern", "outer"],
                "answer": "nonlocal",
                "explain": "nonlocal binds to the nearest enclosing (non-global) scope.",
            },
            {
                "q": "What does `functools.reduce(lambda a,b: a+b, [1,2,3])` return?",
                "choices": ["[1, 2, 3]", "6", "1", "Error"],
                "answer": "6",
                "explain": "reduce applies the function cumulatively: ((1+2)+3) = 6.",
            },
            {
                "q": "A closure is a function that...",
                "choices": [
                    "Has no parameters",
                    "Remembers values from its enclosing scope",
                    "Is defined inside a class",
                    "Returns None",
                ],
                "answer": "Remembers values from its enclosing scope",
                "explain": "Closures capture free variables from the enclosing function.",
            },
        ],
    },

    # ─────────────────────────────────────────────────────────────
    # INTERMEDIATE
    # ─────────────────────────────────────────────────────────────
    "intermediate": {

        "data_structures": [
            {
                "q": "Which data structure is best for O(1) membership testing?",
                "choices": ["list", "tuple", "set", "dict"],
                "answer": "set",
                "explain": "Sets use hash tables, giving O(1) average-case `in` checks.",
            },
            {
                "q": "What does `collections.Counter('aab')` return?",
                "choices": ["{'a':2,'b':1}", "['a','a','b']", "Counter({'a': 2, 'b': 1})", "{'a','b'}"],
                "answer": "Counter({'a': 2, 'b': 1})",
                "explain": "Counter maps each element to its frequency.",
            },
            {
                "q": "What is the time complexity of `list.append()`?",
                "choices": ["O(n)", "O(log n)", "O(1) amortized", "O(n²)"],
                "answer": "O(1) amortized",
                "explain": "Lists use dynamic arrays — append is amortized O(1).",
            },
            {
                "q": "What does `collections.defaultdict(list)` do when a missing key is accessed?",
                "choices": ["Raises KeyError", "Returns None", "Creates an empty list for that key", "Returns []"],
                "answer": "Creates an empty list for that key",
                "explain": "defaultdict calls the factory (list) to create a default value.",
            },
            {
                "q": "What is the difference between `is` and `==`?",
                "choices": [
                    "No difference",
                    "`is` checks identity (same object); `==` checks equality (same value)",
                    "`is` checks value; `==` checks type",
                    "`is` is faster for strings only",
                ],
                "answer": "`is` checks identity (same object); `==` checks equality (same value)",
                "explain": "`is` compares id(); `==` calls __eq__.",
            },
            {
                "q": "Which collections type provides thread-safe append/pop from both ends in O(1)?",
                "choices": ["list", "deque", "tuple", "array"],
                "answer": "deque",
                "explain": "collections.deque has O(1) appendleft/popleft unlike list.",
            },
        ],

        "file_handling": [
            {
                "q": "What is the safest way to open a file in Python?",
                "choices": [
                    "f = open('f.txt')",
                    "with open('f.txt') as f:",
                    "file = File('f.txt')",
                    "f = read('f.txt')",
                ],
                "answer": "with open('f.txt') as f:",
                "explain": "Context manager ensures the file is closed even on exceptions.",
            },
            {
                "q": "What mode string opens a file for both reading and writing without truncating?",
                "choices": ["'w+'", "'r+'", "'a'", "'x'"],
                "answer": "'r+'",
                "explain": "'r+' opens for read+write; 'w+' truncates first.",
            },
            {
                "q": "Which Python version introduced ExceptionGroup?",
                "choices": ["3.9", "3.10", "3.11", "3.12"],
                "answer": "3.11",
                "explain": "ExceptionGroup and except* landed in Python 3.11 (PEP 654).",
            },
            {
                "q": "What does `json.dumps({'a': 1}, indent=2)` produce?",
                "choices": [
                    "'{\"a\": 1}'",
                    "A pretty-printed JSON string with 2-space indent",
                    "A bytes object",
                    "Error",
                ],
                "answer": "A pretty-printed JSON string with 2-space indent",
                "explain": "indent= enables multi-line pretty formatting.",
            },
            {
                "q": "What does `except*` do (Python 3.11+)?",
                "choices": [
                    "Catches all exceptions",
                    "Catches specific exception types within an ExceptionGroup",
                    "Re-raises all exceptions",
                    "Ignores exceptions",
                ],
                "answer": "Catches specific exception types within an ExceptionGroup",
                "explain": "except* filters ExceptionGroup by type, like a group-aware except.",
            },
        ],

        "oop_basics": [
            {
                "q": "What method is called when an object is created?",
                "choices": ["__new__", "__init__", "__create__", "__start__"],
                "answer": "__init__",
                "explain": "__init__ initialises the object after __new__ creates it.",
            },
            {
                "q": "What does MRO stand for?",
                "choices": [
                    "Method Resolution Order",
                    "Multiple Return Object",
                    "Module Registry Object",
                    "Mutable Reference Object",
                ],
                "answer": "Method Resolution Order",
                "explain": "MRO (C3 linearisation) defines the order Python looks up methods.",
            },
            {
                "q": "Which decorator makes a class method receive the class, not the instance?",
                "choices": ["@staticmethod", "@classmethod", "@property", "@abstractmethod"],
                "answer": "@classmethod",
                "explain": "@classmethod passes `cls` as first arg; used for alternative constructors.",
            },
            {
                "q": "What module provides Abstract Base Classes?",
                "choices": ["abc", "abstract", "base", "interface"],
                "answer": "abc",
                "explain": "from abc import ABC, abstractmethod",
            },
            {
                "q": "What does `__repr__` return?",
                "choices": [
                    "A human-friendly string",
                    "An unambiguous developer-focused representation",
                    "The class name only",
                    "Nothing",
                ],
                "answer": "An unambiguous developer-focused representation",
                "explain": "__repr__ is for debugging; __str__ is for end users.",
            },
        ],

        "modules_packages": [
            {
                "q": "What is the value of `__name__` when a file is run directly?",
                "choices": ["None", "'__main__'", "The filename", "'module'"],
                "answer": "'__main__'",
                "explain": "Python sets __name__='__main__' for the entry-point script.",
            },
            {
                "q": "What does `from package import *` import?",
                "choices": [
                    "Everything",
                    "Only names listed in __all__",
                    "Only functions",
                    "Nothing",
                ],
                "answer": "Only names listed in __all__",
                "explain": "__all__ controls what `import *` exports.",
            },
            {
                "q": "What is a relative import?",
                "choices": [
                    "Importing from the same package using dots",
                    "Importing from the internet",
                    "Importing by file path",
                    "Importing without an alias",
                ],
                "answer": "Importing from the same package using dots",
                "explain": "'from . import sibling' imports from the same package.",
            },
        ],

        "standard_library": [
            {
                "q": "Which module provides `Path` objects for filesystem operations?",
                "choices": ["os", "sys", "pathlib", "shutil"],
                "answer": "pathlib",
                "explain": "pathlib.Path gives an OOP interface over file paths.",
            },
            {
                "q": "What does `itertools.chain([1,2], [3,4])` produce?",
                "choices": ["[[1,2],[3,4]]", "[1,2,3,4]", "(1,2,3,4)", "Error"],
                "answer": "[1,2,3,4]",
                "explain": "chain() concatenates iterables lazily.",
            },
            {
                "q": "What does `@functools.lru_cache(maxsize=128)` do?",
                "choices": [
                    "Limits function calls to 128",
                    "Memoizes results using a least-recently-used cache",
                    "Logs the last 128 calls",
                    "Runs the function 128 times",
                ],
                "answer": "Memoizes results using a least-recently-used cache",
                "explain": "lru_cache stores recent results to avoid redundant computation.",
            },
            {
                "q": "What logging level is ABOVE WARNING?",
                "choices": ["INFO", "DEBUG", "ERROR", "NOTICE"],
                "answer": "ERROR",
                "explain": "Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL.",
            },
            {
                "q": "Which regex flag makes `.` match newlines too?",
                "choices": ["re.MULTILINE", "re.DOTALL", "re.IGNORECASE", "re.VERBOSE"],
                "answer": "re.DOTALL",
                "explain": "re.DOTALL (re.S) makes dot match \\n as well.",
            },
        ],
    },

    # ─────────────────────────────────────────────────────────────
    # ADVANCED
    # ─────────────────────────────────────────────────────────────
    "advanced": {

        "decorators": [
            {
                "q": "Why should decorators use `@functools.wraps(func)`?",
                "choices": [
                    "For performance",
                    "To preserve the original function's __name__ and __doc__",
                    "To allow multiple decorators",
                    "It is required by Python",
                ],
                "answer": "To preserve the original function's __name__ and __doc__",
                "explain": "@wraps copies metadata so introspection tools see the original function.",
            },
            {
                "q": "A parameterized decorator is a decorator that...",
                "choices": [
                    "Takes no arguments",
                    "Returns a decorator factory that accepts arguments",
                    "Only works on classes",
                    "Is applied twice",
                ],
                "answer": "Returns a decorator factory that accepts arguments",
                "explain": "@retry(times=3) is a factory — it returns the actual decorator.",
            },
            {
                "q": "In what order are stacked decorators applied? `@A @B def f(): ...`",
                "choices": ["A then B", "B then A", "Simultaneously", "Randomly"],
                "answer": "B then A",
                "explain": "Bottom-up: B wraps f first, then A wraps the result.",
            },
        ],

        "generators": [
            {
                "q": "What keyword turns a function into a generator?",
                "choices": ["return", "yield", "async", "generate"],
                "answer": "yield",
                "explain": "Any function with yield is a generator function.",
            },
            {
                "q": "What does `yield from iterable` do?",
                "choices": [
                    "Returns the iterable",
                    "Delegates to a sub-generator, yielding each item",
                    "Creates a new generator",
                    "Pauses the generator forever",
                ],
                "answer": "Delegates to a sub-generator, yielding each item",
                "explain": "yield from chains generators and passes send()/throw() through.",
            },
            {
                "q": "What is the memory advantage of generators over lists?",
                "choices": [
                    "No advantage",
                    "Generators produce values lazily — only one at a time in memory",
                    "Generators are faster to create",
                    "Generators are immutable",
                ],
                "answer": "Generators produce values lazily — only one at a time in memory",
                "explain": "A generator of 1M items uses O(1) memory; a list uses O(n).",
            },
        ],

        "async_programming": [
            {
                "q": "What does `await` do?",
                "choices": [
                    "Blocks the entire program",
                    "Suspends the coroutine until the awaitable completes",
                    "Creates a new thread",
                    "Calls a function synchronously",
                ],
                "answer": "Suspends the coroutine until the awaitable completes",
                "explain": "await yields control back to the event loop while waiting.",
            },
            {
                "q": "What does `asyncio.gather(*coros)` do?",
                "choices": [
                    "Runs coroutines sequentially",
                    "Runs coroutines concurrently and waits for all to finish",
                    "Cancels all coroutines",
                    "Creates threads for each coroutine",
                ],
                "answer": "Runs coroutines concurrently and waits for all to finish",
                "explain": "gather() schedules all coroutines on the event loop concurrently.",
            },
            {
                "q": "When should you use `run_in_executor` in asyncio?",
                "choices": [
                    "For all async calls",
                    "To run CPU-bound or blocking I/O code without blocking the event loop",
                    "To create new event loops",
                    "For database queries only",
                ],
                "answer": "To run CPU-bound or blocking I/O code without blocking the event loop",
                "explain": "run_in_executor offloads blocking work to a thread/process pool.",
            },
        ],

        "type_hints": [
            {
                "q": "What is a `Protocol` in Python typing?",
                "choices": [
                    "A strict interface that must be inherited",
                    "A structural subtyping mechanism — any class with matching methods satisfies it",
                    "A way to define abstract classes",
                    "A decorator for type checking",
                ],
                "answer": "A structural subtyping mechanism — any class with matching methods satisfies it",
                "explain": "Protocol enables duck typing with static type checking (PEP 544).",
            },
            {
                "q": "What is the Python 3.10+ syntax for `Optional[str]`?",
                "choices": ["str | None", "str?", "Maybe[str]", "Union[str]"],
                "answer": "str | None",
                "explain": "PEP 604 introduced X|Y union syntax, replacing Union[X, Y].",
            },
            {
                "q": "What does `TypeVar('T', bound=Comparable)` mean?",
                "choices": [
                    "T can be any type",
                    "T must be a subtype of Comparable",
                    "T is exactly Comparable",
                    "T cannot be Comparable",
                ],
                "answer": "T must be a subtype of Comparable",
                "explain": "bound= sets an upper bound — T must be Comparable or a subclass.",
            },
        ],

        "dataclasses": [
            {
                "q": "What does `@dataclass(frozen=True)` do?",
                "choices": [
                    "Makes the class abstract",
                    "Makes instances immutable — raises FrozenInstanceError on assignment",
                    "Prevents inheritance",
                    "Disables __init__",
                ],
                "answer": "Makes instances immutable — raises FrozenInstanceError on assignment",
                "explain": "frozen=True generates __setattr__ and __delattr__ that raise errors.",
            },
            {
                "q": "What does `field(default_factory=list)` solve?",
                "choices": [
                    "Nothing special",
                    "Avoids the mutable default argument trap by calling list() per instance",
                    "Makes the field read-only",
                    "Sets the field to an empty tuple",
                ],
                "answer": "Avoids the mutable default argument trap by calling list() per instance",
                "explain": "default_factory is called fresh for each instance, not shared.",
            },
            {
                "q": "Which Python version added `slots=True` to @dataclass?",
                "choices": ["3.8", "3.9", "3.10", "3.11"],
                "answer": "3.10",
                "explain": "slots=True (PEP 557 extension) was added in Python 3.10.",
            },
        ],

        "testing": [
            {
                "q": "What does `@pytest.mark.parametrize` do?",
                "choices": [
                    "Skips the test",
                    "Runs the test multiple times with different input sets",
                    "Marks a test as expected to fail",
                    "Groups tests into a class",
                ],
                "answer": "Runs the test multiple times with different input sets",
                "explain": "parametrize generates one test case per parameter combination.",
            },
            {
                "q": "What is a pytest fixture?",
                "choices": [
                    "A type of assertion",
                    "A reusable setup/teardown function injected by name into tests",
                    "A mock object",
                    "A test file",
                ],
                "answer": "A reusable setup/teardown function injected by name into tests",
                "explain": "@pytest.fixture functions are discovered and injected automatically.",
            },
            {
                "q": "How do you assert a function raises ValueError in pytest?",
                "choices": [
                    "assert raises(ValueError)",
                    "with pytest.raises(ValueError): ...",
                    "try/except ValueError: pass",
                    "@pytest.expect(ValueError)",
                ],
                "answer": "with pytest.raises(ValueError): ...",
                "explain": "pytest.raises() is a context manager that asserts the exception.",
            },
        ],

        "design_patterns": [
            {
                "q": "Which pattern ensures a class has only one instance?",
                "choices": ["Factory", "Builder", "Singleton", "Prototype"],
                "answer": "Singleton",
                "explain": "Singleton restricts instantiation to one object, e.g., config/logger.",
            },
            {
                "q": "The Strategy pattern is best described as...",
                "choices": [
                    "Creating objects without specifying the exact class",
                    "Defining a family of algorithms and making them interchangeable",
                    "Adding behaviour to objects dynamically",
                    "Providing a simplified interface to a complex subsystem",
                ],
                "answer": "Defining a family of algorithms and making them interchangeable",
                "explain": "Strategy encapsulates behaviour variants behind a common interface.",
            },
            {
                "q": "The Observer pattern is used when...",
                "choices": [
                    "You need a single instance",
                    "One object's state change should notify multiple dependents automatically",
                    "You want to add methods to a class at runtime",
                    "You need lazy initialization",
                ],
                "answer": "One object's state change should notify multiple dependents automatically",
                "explain": "Observer (pub-sub) decouples subject from its subscribers.",
            },
        ],
    },
}

LEVELS = ["beginner", "intermediate", "advanced"]
PASS_THRESHOLD = 0.70  # 70% to pass a topic
LEVEL_PASS_THRESHOLD = 0.70  # 70% average across topics to advance level
