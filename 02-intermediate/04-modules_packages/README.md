# 04-modules_packages — The Python Import System

Understand how Python organises code into modules and packages — essential for any real project.

**Official Docs:** https://docs.python.org/3/tutorial/modules.html

## 📚 Topics Covered

### 1. Modules (`modules.py`)
- What is a module? — Any `.py` file is a module
- `import module` — importing an entire module
- `from module import name` — importing specific names
- `from module import *` — why you should avoid it
- `import module as alias` — aliasing
- `__name__` and `if __name__ == "__main__":`
- Module search path — `sys.path`
- The module cache — `sys.modules`
- Reloading modules — `importlib.reload()`

### 2. Packages (`packages.py`)
- What is a package? — A directory with `__init__.py`
- `__init__.py` — initialising a package, controlling exports
- Sub-packages — nested directories
- Relative imports — `from . import sibling`, `from .. import parent`
- `__all__` — controlling `from package import *`
- Namespace packages (Python 3.3+) — packages without `__init__.py`

### 3. Standard vs Third-Party vs Local
- How Python resolves import order
- Virtual environment isolation
- `importlib` — programmatic import

## 💡 Learning Objectives
- ✅ Write importable modules with `if __name__ == "__main__":`
- ✅ Organise a project into packages
- ✅ Use relative imports correctly inside a package
- ✅ Control the public API of a module via `__all__`
- ✅ Understand module search path and caching

## 🎯 Interview Tips
- **Q:** What does `if __name__ == "__main__":` do?
- **Q:** What's the difference between `import x` and `from x import y`?
- **Q:** Why are wildcard imports (`from x import *`) discouraged?
- **Q:** What is `__all__`?
- **Q:** How do relative imports work?

## 📝 Files
1. **modules.py** — import mechanics, `__name__`, `sys.path`, aliases
2. **packages.py** — `__init__.py`, sub-packages, relative imports, `__all__`

## 🔗 Doc References
- https://docs.python.org/3/tutorial/modules.html
- https://docs.python.org/3/reference/import.html

---
**Difficulty: ⭐⭐☆ Essential for every multi-file Python project**
