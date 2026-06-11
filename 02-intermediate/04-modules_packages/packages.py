"""
Packages — Organising Code into Directories
=============================================
Ref: https://docs.python.org/3/tutorial/modules.html#packages

A package is a directory that contains an __init__.py file (or is a
namespace package in Python 3.3+). Packages allow hierarchical module
namespaces: sound.effects.echo, urllib.request, etc.

This file demonstrates the concepts — the actual package structure
lives in the sample_pkg/ directory created below.
"""
import os
from pathlib import Path

ROOT = Path(__file__).parent

# ─── 1. Creating a Package (directory structure) ──────────────────────────────
# A minimal package:
#   mypackage/
#   ├── __init__.py       ← marks directory as a package; runs on import
#   ├── module_a.py
#   └── sub/
#       ├── __init__.py
#       └── module_b.py

# Let's create a demo package programmatically so you can import it
pkg_root = ROOT / "sample_pkg"
(pkg_root).mkdir(exist_ok=True)
(pkg_root / "sub").mkdir(exist_ok=True)

(pkg_root / "__init__.py").write_text('''\
"""sample_pkg: a demo package."""

# __init__.py runs when the package is imported.
# Use it to:
#   1. Expose a clean public API
#   2. Run package-level initialisation
#   3. Control what "from sample_pkg import *" exports

from .module_a import greet          # re-export for convenience
from .module_a import PACKAGE_NAME

__all__ = ["greet", "PACKAGE_NAME"]  # controls "import *"
__version__ = "0.1.0"
''')

(pkg_root / "module_a.py").write_text('''\
"""Module A — part of sample_pkg."""
PACKAGE_NAME = "sample_pkg"

def greet(name: str) -> str:
    return f"Hello from module_a, {name}!"

def _private_helper():
    """Not exported — single underscore signals internal use."""
    pass
''')

(pkg_root / "sub" / "__init__.py").write_text('# sub-package init\n')
(pkg_root / "sub" / "module_b.py").write_text('''\
"""Module B — inside sample_pkg.sub sub-package."""

# Relative import: import from the parent package
from ..module_a import PACKAGE_NAME   # .. means one level up

def info() -> str:
    return f"sub.module_b inside {PACKAGE_NAME}"
''')

# ─── 2. Importing from a Package ─────────────────────────────────────────────
import sys
sys.path.insert(0, str(ROOT))    # ensure sample_pkg is findable

import sample_pkg                               # runs __init__.py
print(sample_pkg.greet("Alice"))               # re-exported by __init__
print(sample_pkg.__version__)

from sample_pkg import module_a                 # import a specific module
print(module_a.PACKAGE_NAME)

from sample_pkg.sub import module_b             # import from sub-package
print(module_b.info())

# ─── 3. __all__ — Controlling "from pkg import *" ────────────────────────────
# If __all__ is defined, "from pkg import *" only imports listed names.
# Without __all__, "import *" imports everything not starting with _.
from sample_pkg import *   # imports only names in __all__: greet, PACKAGE_NAME

# ─── 4. Relative vs Absolute Imports ─────────────────────────────────────────
# Inside a package, prefer RELATIVE imports — they're immune to name shadowing
# and make the package relocatable.
#
# Relative:   from .module_a import greet   (. = current package)
#             from ..utils import helper    (.. = parent package)
#
# Absolute:   from sample_pkg.module_a import greet
#
# Rule of thumb:
#   - Inside a package → relative imports
#   - At the top level of an application → absolute imports

# ─── 5. Namespace Packages (Python 3.3+) ─────────────────────────────────────
# A directory WITHOUT __init__.py is still importable as a "namespace package".
# Useful for splitting a large package across multiple directories/repos.
# Less common; prefer regular packages with __init__.py.

# ─── 6. pyproject.toml / Package Distribution ────────────────────────────────
# To make your package installable:
#   1. Put source in src/mypackage/
#   2. Write pyproject.toml (we already have one)
#   3. uv build  → creates dist/ wheel + sdist
#   4. uv publish → uploads to PyPI

# ─── Cleanup demo package ────────────────────────────────────────────────────
import shutil
shutil.rmtree(pkg_root, ignore_errors=True)
sys.path.pop(0)


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Create a real package 'mathutils' with modules: algebra.py, geometry.py.
#         Each module should have 3 functions. Import them in two different ways.
# TODO 2: Add an __init__.py that re-exports the most useful functions so users
#         can do: from mathutils import area_circle (instead of mathutils.geometry.area_circle).
# TODO 3: Add a __version__ and __author__ to the package's __init__.py.
# TODO 4: Write a relative import inside geometry.py that uses a constant from algebra.py.
# TODO 5: Demonstrate __all__ by trying 'from mathutils import *' and checking what's available.
