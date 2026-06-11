# 01-data_structures — Collections and Their Operations

Master Python's powerful built-in data structures for efficient data organization and manipulation.

## 📚 Topics Covered

### 1. Lists (Advanced)
- **List operations** — append, extend, insert, remove, pop, clear
- **List indexing and slicing** — Negative indices, stride slicing
- **List methods** — sort, reverse, count, index, copy
- **Mutability** — Lists are mutable, implications for references
- **List performance** — O(n) insertion/deletion, O(1) access
- **Shallow vs deep copy** — Understanding copy semantics

### 2. Tuples
- **Tuple basics** — Immutable sequences, syntax with/without parentheses
- **Tuple unpacking** — `a, b, c = (1, 2, 3)`
- **Named tuples** — `collections.namedtuple` for readability
- **Tuple performance** — When and why to use tuples
- **Returning multiple values** — Using tuples effectively
- **Tuple as dictionary keys** — Why tuples but not lists?

### 3. Dictionaries (Advanced)
- **Dictionary operations** — get, setdefault, pop, popitem, update, keys, values, items
- **Dictionary methods** — fromkeys, clear, copy
- **Dictionary iteration** — Iterating keys, values, items
- **Dict comprehensions** — `{k: v for k, v in pairs}`
- **Default values** — `get()` vs direct access
- **Nested dictionaries** — Working with complex data structures
- **Dictionary performance** — O(1) lookup (hash tables)

### 4. Sets
- **Set basics** — Unordered, unique elements, set literals
- **Set operations** — add, remove, discard, pop, clear
- **Set mathematics** — union (`|`), intersection (`&`), difference (`-`), symmetric_difference (`^`)
- **Set methods** — issubset, issuperset, isdisjoint, copy
- **Set comprehensions** — `{expr for x in iterable}`
- **Set use cases** — Membership testing, removing duplicates

### 5. Collections Module
- **Counter** — Count occurrences of elements
- **defaultdict** — Dictionary with default values
- **OrderedDict** — Maintains insertion order (3.7+ default dict behavior)
- **deque** — Efficient append/pop from both ends
- **ChainMap** — Multiple dictionaries as one

### 6. Choosing the Right Data Structure
- **Lists vs Tuples** — Mutability, hashing, performance
- **Sets vs Lists** — Membership testing, uniqueness
- **Dicts vs Lists** — Key-value lookup vs indexed access
- **Performance considerations** — Time complexity for operations

## 💡 Learning Objectives

By the end of this section, you should be able to:
- ✅ Use all built-in data structures appropriately
- ✅ Choose the right data structure for different problems
- ✅ Understand time complexity of different operations
- ✅ Manipulate nested structures efficiently
- ✅ Use collections module for specialized structures
- ✅ Solve problems using data structure properties

## 📝 Files in This Section

1. **lists_advanced.py** — List operations, methods, performance
2. **tuples.py** — Tuples, unpacking, named tuples
3. **dictionaries_advanced.py** — Dictionary operations, methods, nested structures
4. **sets.py** — Set operations, mathematical operations
5. **collections_module.py** — Counter, defaultdict, deque, ChainMap
6. **data_structure_selection.py** — Choosing appropriate structures
7. **exercises.py** — Practice problems on data structures

## 🎯 Interview Tips

**Common Questions:**
- What's the difference between a list and a tuple?
- How do you count element occurrences in a list?
- Explain set operations and their use cases
- When would you use a defaultdict?
- What's the time complexity of dictionary operations?
- How do you handle nested structures in Python?

**Key Points to Master:**
- Know the time complexity of each operation on each structure
- Understand why tuples can be dict keys but lists cannot
- Master dictionary and set operations
- Use Counter, defaultdict for specialized tasks
- Understand shallow copy implications

## 🚀 Next Steps

After mastering data structures:
1. Move to `02-file_handling/` to work with real data
2. Combine data structures with control flow for algorithms
3. Practice LeetCode problems on arrays/hashing

---

**Difficulty: ⭐⭐☆ Essential for practical programming**
