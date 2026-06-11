"""
File I/O and Context Managers — File Handling
===============================================
Covers: open(), modes, read/write, context managers, encoding
"""
import os
from pathlib import Path

SAMPLE_FILE = Path("sample.txt")

# ─── 1. Writing Files ─────────────────────────────────────────────────────────
# Mode 'w' — overwrite; 'a' — append; 'x' — create (fails if exists)
with open(SAMPLE_FILE, "w", encoding="utf-8") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.writelines(["Line 3\n", "Line 4\n"])

# ─── 2. Reading Files ─────────────────────────────────────────────────────────
# Read entire file
with open(SAMPLE_FILE, encoding="utf-8") as f:
    content = f.read()
print(content)

# Read all lines into list
with open(SAMPLE_FILE, encoding="utf-8") as f:
    lines = f.readlines()   # includes \n
print(lines)

# Iterate line by line — memory-efficient for large files
with open(SAMPLE_FILE, encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# ─── 3. File Pointer and Seek ─────────────────────────────────────────────────
with open(SAMPLE_FILE, encoding="utf-8") as f:
    first_10 = f.read(10)
    pos       = f.tell()
    print(f"Read: {first_10!r}, position: {pos}")
    f.seek(0)              # back to start
    again = f.read(10)
    print(f"Again: {again!r}")

# ─── 4. Context Manager Protocol ─────────────────────────────────────────────
# __enter__ → returns resource
# __exit__  → handles cleanup, even if exception occurs

class ManagedFile:
    """Custom context manager example."""

    def __init__(self, path: Path, mode: str = "r"):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.path, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False   # don't suppress exceptions

with ManagedFile(SAMPLE_FILE) as f:
    print(f.readline())

# Using contextlib for simpler context managers
from contextlib import contextmanager

@contextmanager
def open_file(path: Path, mode: str = "r"):
    f = open(path, mode, encoding="utf-8")
    try:
        yield f
    finally:
        f.close()

with open_file(SAMPLE_FILE) as f:
    print(f.readline())

# ─── 5. pathlib — Modern Path Handling ───────────────────────────────────────
p = Path(".")

# Path operations
print(p.resolve())                  # absolute path
print(list(p.iterdir()))            # list directory
print(list(p.glob("*.txt")))        # find files

readme = Path("README.md")
print(readme.exists())
print(readme.suffix)                # .md
print(readme.stem)                  # README
print(readme.name)                  # README.md
print(readme.parent)                # .

# Reading/writing with pathlib
SAMPLE_FILE.write_text("Hello from pathlib!\n", encoding="utf-8")
print(SAMPLE_FILE.read_text(encoding="utf-8"))

# ─── 6. Error Handling for Files ──────────────────────────────────────────────
def safe_read(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except PermissionError:
        print(f"Permission denied: {path}")
        return None
    except UnicodeDecodeError:
        print(f"Encoding error reading: {path}")
        return None

result = safe_read(Path("nonexistent.txt"))
print(result)

# Cleanup
SAMPLE_FILE.unlink(missing_ok=True)


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Write a function to count lines, words, and chars in a file (like wc).
# TODO 2: Copy a file line-by-line, adding line numbers to each line.
# TODO 3: Read a log file and extract all lines containing "ERROR".
# TODO 4: Create a context manager that times the code inside the block.
# TODO 5: Walk a directory tree and list all .py files with their sizes.
