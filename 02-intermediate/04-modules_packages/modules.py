"""
Modules — The Python Import System
=====================================
Ref: https://docs.python.org/3/tutorial/modules.html
"""
import sys
import importlib

# ─── 1. What is a Module? ─────────────────────────────────────────────────────
# Any .py file is a module. The filename (without .py) is the module name.
# When you import a module, Python executes it top-to-bottom once and caches it.

# ─── 2. Import Styles ─────────────────────────────────────────────────────────
import os                          # import the whole module
import os.path                     # import a sub-module
from pathlib import Path           # import specific names
from pathlib import Path as P      # import with alias
import json as _json               # private alias convention (discouraged for public APIs)

# Avoid: from module import *
# — pollutes namespace, hides where names come from, breaks tools like mypy

# ─── 3. __name__ and if __name__ == "__main__": ───────────────────────────────
# When Python runs a file directly, __name__ is set to "__main__".
# When the file is imported as a module, __name__ is the module name.
# This lets a file work both as a runnable script AND as an importable library.

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    # This block only runs when this file is executed directly:
    #   python modules.py
    # It does NOT run when another file does: import modules
    print("Running as a script")
    print(add(3, 4))

# ─── 4. Module Search Path (sys.path) ─────────────────────────────────────────
# Python searches for modules in this order:
#   1. The directory of the running script (or '' for interactive)
#   2. Directories in the PYTHONPATH environment variable
#   3. Installation-dependent default (site-packages)
print(sys.path[:3])   # first 3 entries

# You can add to sys.path at runtime (use sparingly):
# sys.path.insert(0, "/path/to/my/libs")

# ─── 5. The Module Cache (sys.modules) ────────────────────────────────────────
# Once imported, modules are cached in sys.modules.
# Subsequent imports reuse the cached copy — imports are cheap after the first.
print("os" in sys.modules)          # True (already imported above)
print(sys.modules["os"] is os)      # True — same object

# ─── 6. Reloading a Module ────────────────────────────────────────────────────
# Usually unnecessary. Useful in interactive sessions when you've edited a file.
import json
importlib.reload(json)   # re-executes json/__init__.py

# ─── 7. dir() — Inspect a Module's Contents ──────────────────────────────────
import math
public_attrs = [name for name in dir(math) if not name.startswith("_")]
print(public_attrs[:10])

# ─── 8. __doc__, __file__, __spec__ — Module Metadata ────────────────────────
print(math.__doc__[:80])
print(math.__file__)
print(math.__name__)

# ─── 9. Useful Patterns ───────────────────────────────────────────────────────

# Lazy import — defer a heavy import until it's actually needed
def compress(data: bytes) -> bytes:
    import zlib   # imported here, not at module top
    return zlib.compress(data)

# Type-checking-only import — avoids runtime cost while keeping type hints
from __future__ import annotations   # postpone annotation evaluation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Sequence   # only used by mypy, not at runtime


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Create a utils.py file with 3 helper functions. Import it two ways:
#         a) import utils  b) from utils import <function>
# TODO 2: Add an if __name__ == "__main__": block that runs a self-test.
# TODO 3: Print all modules currently in sys.modules that start with "collections".
# TODO 4: Use dir() and help() to explore the random module without reading the docs.
# TODO 5: Write a function that dynamically imports a module by name string:
#         dynamic_import("json") → returns the json module
