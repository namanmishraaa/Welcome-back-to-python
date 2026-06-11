# 07-design_patterns — GoF Patterns in Python

Proven solutions to recurring software design problems, implemented Pythonically.

**Reference:** https://refactoring.guru/design-patterns/python
**Book:** Design Patterns (Gang of Four — Gamma, Helm, Johnson, Vlissides)

## 📚 Patterns Covered

### Creational — *How objects are created*
| Pattern | When to Use | Python Idiom |
|---|---|---|
| **Singleton** | One instance per process (config, DB pool) | module-level global or `__new__` |
| **Factory Method** | Create objects without specifying class | function + registry dict |
| **Builder** | Construct complex objects step-by-step | method chaining |
| **Prototype** | Clone existing objects | `copy.deepcopy()` |

### Structural — *How objects are composed*
| Pattern | When to Use | Python Idiom |
|---|---|---|
| **Adapter** | Wrap incompatible interface | class wrapping |
| **Decorator** | Add behaviour without subclassing | class wrapping or `@functools.wraps` |
| **Facade** | Simple interface to complex subsystem | wrapper class |
| **Proxy** | Control access to an object | `__getattr__` forwarding |

### Behavioural — *How objects communicate*
| Pattern | When to Use | Python Idiom |
|---|---|---|
| **Observer** | Notify dependents of state change | callbacks / event bus |
| **Strategy** | Swap algorithms at runtime | pass callables |
| **Command** | Encapsulate actions as objects | callable objects |
| **Repository** | Abstract data storage | ABC + concrete implementation |
| **State** | Object behaviour changes with state | enum + dispatch |
| **Template Method** | Define skeleton; subclasses fill in | abstract methods |
| **Chain of Responsibility** | Pass request through handler chain | list of callables |

## 💡 Learning Objectives
- ✅ Recognise which pattern solves which problem
- ✅ Implement the most common patterns in Python idiomatically
- ✅ Know when NOT to use a pattern (over-engineering)
- ✅ Articulate pattern names and tradeoffs in interviews

## 🎯 Interview Tips
- "What pattern would you use to…?" is a common system design question
- Python's first-class functions make Strategy trivial — just pass a callable
- Singleton is often an anti-pattern — prefer dependency injection
- Repository pattern makes swapping DB backends trivial (tests use in-memory)
- Observer = pub/sub = event bus — same concept, different names

## 📝 Files
1. **patterns.py** — Singleton, Factory, Builder, Adapter, Decorator, Observer, Strategy, Repository

---
**Difficulty: ⭐⭐⭐ Essential for system design interviews**
