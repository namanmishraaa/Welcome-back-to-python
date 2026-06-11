# 02-file_handling — Reading, Writing, and Parsing Data

Master file operations and work with different file formats for persistent data storage.

## 📚 Topics Covered

### 1. Basic File I/O
- **Opening files** — `open()` function, modes (r, w, a, x, b, +)
- **Reading files** — `read()`, `readline()`, `readlines()`, iteration
- **Writing files** — `write()`, `writelines()`, overwrite vs append
- **Closing files** — Importance of cleanup, resource management
- **Binary vs text mode** — When to use each
- **File paths** — Absolute vs relative, platform-specific paths

### 2. Context Managers (`with` statement)
- **Why context managers?** — Automatic resource cleanup
- **`with` statement syntax** — Ensuring files are closed
- **Multiple context managers** — Handling multiple files
- **Context manager protocol** — `__enter__` and `__exit__`
- **Creating custom context managers** — For your own resources

### 3. Working with Text Files
- **Line by line processing** — Efficient memory usage
- **String methods for parsing** — split, strip, replace
- **Newline handling** — `\n`, `\r\n` (platform differences)
- **Encoding issues** — UTF-8, ASCII, encoding parameter
- **Large file handling** — Reading chunks instead of entire file

### 4. CSV and Data Formats
- **CSV module** — Reading/writing CSV files correctly
- **CSV reader and writer** — Handling delimiters and quoting
- **CSV DictReader/DictWriter** — Working with headers
- **JSON format** — `json` module for JSON data
- **JSON reading/writing** — `load()`, `dump()`, `loads()`, `dumps()`
- **Parsing different formats** — YAML, TOML, XML basics

### 5. Exception Handling for Files
- **FileNotFoundError** — Handling missing files
- **IOError** — General I/O problems
- **Permissions** — Permission denied errors
- **Encoding errors** — UnicodeDecodeError handling
- **Try-except-finally** — Ensuring cleanup even with errors

### 6. File and Directory Operations
- **`os` module** — File and directory operations
- **`pathlib` module** — Modern path handling (recommended)
- **Checking file existence** — `os.path.exists()`, `Path.exists()`
- **Listing directory contents** — `os.listdir()`, `Path.iterdir()`
- **Creating/deleting files and directories** — Safe operations

## 💡 Learning Objectives

By the end of this section, you should be able to:
- ✅ Read and write files safely with context managers
- ✅ Parse CSV and JSON files effectively
- ✅ Handle file I/O errors gracefully
- ✅ Work with file paths correctly
- ✅ Process large files efficiently
- ✅ Handle different encodings
- ✅ Manipulate file systems programmatically

## 📝 Files in This Section

1. **basic_file_io.py** — Reading, writing, closing files
2. **context_managers.py** — Using `with` statement, creating custom managers
3. **text_file_processing.py** — Line-by-line reading, string parsing
4. **csv_and_json.py** — Working with CSV and JSON formats
5. **exception_handling_files.py** — Error handling in file operations
6. **file_operations.py** — Using `os` and `pathlib` modules
7. **exercises.py** — Practice problems on file handling

## 🎯 Interview Tips

**Common Questions:**
- What's the importance of the `with` statement for files?
- How do you read a large file without loading it all into memory?
- Explain the difference between `json.load()` and `json.loads()`
- How do you handle encoding issues when reading files?
- What's the difference between `os` and `pathlib`?

**Key Points to Master:**
- Always use `with` statement for file operations
- Know when to use different file modes (r, w, a)
- Understand CSV quoting and delimiter issues
- Handle FileNotFoundError and encoding errors
- Prefer pathlib over os.path for modern code

## 🚀 Next Steps

After mastering file handling:
1. Move to `03-oop_basics/` to organize file operations in classes
2. Use these skills in intermediate projects
3. Practice building data processing pipelines

---

**Difficulty: ⭐⭐☆ Essential for real-world programming**
