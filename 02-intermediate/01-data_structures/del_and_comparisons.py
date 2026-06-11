"""
del Statement and Sequence Comparison
=======================================
Ref: https://docs.python.org/3/tutorial/datastructures.html#the-del-statement
     https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types
"""

# ─── 1. The del Statement ─────────────────────────────────────────────────────
# del removes items from lists, dict keys, or unbinds variable names.
# Unlike pop(), del doesn't return the removed value.

# Delete a list element by index
nums = [10, 20, 30, 40, 50]
del nums[1]
print(nums)   # [10, 30, 40, 50]

# Delete a slice
del nums[1:3]
print(nums)   # [10, 50]

# Delete a dict key
person = {"name": "Alice", "age": 30, "city": "Delhi"}
del person["city"]
print(person)   # {'name': 'Alice', 'age': 30}

# Unbind a variable name — accessing it after raises NameError
x = 42
del x
# print(x)   # NameError: name 'x' is not defined

# del on a slice vs assigning empty list
a = [1, 2, 3, 4, 5]
a[1:3] = []   # also removes elements, but via assignment
print(a)      # [1, 4, 5]

# del is the only way to remove a variable name from scope
# (assigning None just rebinds it to None, doesn't free the name)

# ─── 2. Sequence Comparison ───────────────────────────────────────────────────
# Sequences are compared lexicographically:
# Compare element-by-element; first difference determines the result.
# If all elements equal, the longer sequence is greater.

# Lists
print([1, 2, 3] == [1, 2, 3])   # True
print([1, 2, 4] >  [1, 2, 3])   # True  (4 > 3 at index 2)
print([1, 2]    <  [1, 2, 3])   # True  (shorter is less when prefix matches)
print([1, 2, 3] <  [1, 3])      # True  (2 < 3 at index 1)

# Strings (lexicographic by Unicode code point)
print("apple" < "banana")   # True
print("abc"   < "abd")      # True  (c < d at index 2)
print("Zoo"   < "apple")    # True  (Z=90 < a=97 in Unicode)

# Tuples
print((1, 2, 3)  < (1, 2, 4))   # True
print((1, 2)     < (1, 2, -1))  # True

# Mixed numeric types ARE comparable
print(1 == 1.0)   # True  (int and float)
print(1 <  1.5)   # True

# Comparing different sequence types raises TypeError in Python 3
# print([1, 2] < (1, 2))   # TypeError — can't compare list and tuple

# ─── 3. Sorting Using Comparison ─────────────────────────────────────────────
# sorted() and list.sort() use the same lexicographic rules
words = ["banana", "Apple", "cherry", "apricot"]
print(sorted(words))             # case-sensitive: uppercase before lower
print(sorted(words, key=str.lower))   # case-insensitive

tuples = [(1, 3), (1, 2), (2, 1), (1, 2, 0)]
print(sorted(tuples))   # [(1, 2), (1, 2, 0), (1, 3), (2, 1)]

# ─── 4. The del Built-in vs. Object __del__ ───────────────────────────────────
# del x       — removes the NAME x from the current scope/namespace
# obj.__del__ — a finalizer method called when the object is garbage-collected
#               (avoid relying on __del__ for cleanup; use context managers instead)

class Resource:
    def __init__(self, name: str):
        self.name = name
        print(f"Opened: {self.name}")

    def __del__(self):
        print(f"Closed: {self.name}")   # called by GC — timing is unpredictable

r = Resource("file.txt")
del r   # triggers __del__ immediately here (CPython ref-counting), but not guaranteed


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Remove all even-indexed elements from a list using del in a loop (careful with shifting!).
# TODO 2: Write a function that deletes all dict keys whose values are None.
# TODO 3: Given [("alice", 95), ("bob", 87), ("alice", 92)], sort by name then by score descending.
# TODO 4: Explain why "abc" < "abd" < "b" — trace the comparison step-by-step.
# TODO 5: Use del to implement a simple stack pop without using list.pop().
