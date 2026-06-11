"""
os, sys, pathlib, shutil — OS & File System
=============================================
Ref: https://docs.python.org/3/tutorial/stdlib.html#operating-system-interface
     https://docs.python.org/3/library/pathlib.html
"""
import os
import sys
import shutil
from pathlib import Path

# ─── 1. os — Operating System Interface ──────────────────────────────────────
print(os.getcwd())                    # current working directory
print(os.name)                        # 'nt' (Windows) or 'posix' (Unix)
print(os.sep)                         # '\\' or '/'
print(os.linesep)                     # '\r\n' or '\n'

# Environment variables
path_env = os.environ.get("PATH", "")
print(path_env[:60])

os.environ["MY_VAR"] = "hello"
print(os.environ.get("MY_VAR"))

# File/directory operations
os.makedirs("tmp_demo/sub", exist_ok=True)
os.listdir("tmp_demo")
os.rename("tmp_demo/sub", "tmp_demo/sub2")

# os.path (legacy — prefer pathlib for new code)
p = os.path.join("tmp_demo", "file.txt")
print(os.path.exists(p))
print(os.path.dirname(p))
print(os.path.basename(p))
print(os.path.splitext("report.csv"))  # ('report', '.csv')

# Walk directory tree
for root, dirs, files in os.walk("tmp_demo"):
    for file in files:
        print(os.path.join(root, file))

# ─── 2. sys — Interpreter Internals ──────────────────────────────────────────
print(sys.version)
print(sys.platform)          # 'win32', 'linux', 'darwin'
print(sys.argv)              # ['script.py', 'arg1', 'arg2', ...]
print(sys.executable)        # path to the Python interpreter
print(sys.getrecursionlimit())   # default 1000

# sys.stdin / stdout / stderr
sys.stdout.write("hello from sys.stdout\n")

# Exiting a program
# sys.exit(0)    # 0 = success, non-zero = error (don't call in interactive)

# ─── 3. pathlib — Modern Path Handling (Recommended) ─────────────────────────
base = Path("tmp_demo")

# Construction
config = base / "config" / "settings.json"  # / operator joins paths
print(config)
print(config.parent)        # tmp_demo/config
print(config.name)          # settings.json
print(config.stem)          # settings
print(config.suffix)        # .json
print(config.suffixes)      # ['.json']

# Create and write
config.parent.mkdir(parents=True, exist_ok=True)
config.write_text('{"debug": true}', encoding="utf-8")
print(config.read_text(encoding="utf-8"))

# Glob patterns
py_files = list(Path(".").glob("*.py"))
all_py   = list(Path(".").rglob("*.py"))   # recursive
print(f"Found {len(py_files)} .py files here")

# Checking
print(config.exists())
print(config.is_file())
print(config.is_dir())
print(config.stat().st_size)   # file size in bytes

# Iterate directory
for item in base.iterdir():
    kind = "dir" if item.is_dir() else "file"
    print(f"  {kind}: {item.name}")

# Path comparison and resolution
print(config.resolve())         # absolute path
print(config.relative_to(base)) # config/settings.json

# ─── 4. shutil — High-Level File Operations ──────────────────────────────────
# Copy a file
shutil.copy(config, base / "settings_backup.json")       # copies content + permissions
shutil.copy2(config, base / "settings_backup2.json")     # also copies metadata

# Copy a directory tree
shutil.copytree(str(base / "config"), str(base / "config_bak"))

# Move
shutil.move(str(base / "settings_backup.json"), str(base / "archive.json"))

# Disk usage
total, used, free = shutil.disk_usage("/")
print(f"Disk: {free // (1024**3)} GB free")

# Cleanup
shutil.rmtree("tmp_demo", ignore_errors=True)

# ─── 5. Interview Patterns ────────────────────────────────────────────────────
# Find all Python files larger than 10 KB
large_py = [
    p for p in Path(".").rglob("*.py")
    if p.stat().st_size > 10_240
]
print(large_py)


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Write a function that returns all files in a directory tree, grouped by extension.
# TODO 2: Build a safe_delete(path) that moves files to a Trash/ folder instead of deleting.
# TODO 3: Create a script that accepts a directory via sys.argv and prints a tree view.
# TODO 4: Use pathlib to find and rename all .txt files in a folder to .md.
# TODO 5: Read an environment variable with a default fallback; raise if a required var is missing.
