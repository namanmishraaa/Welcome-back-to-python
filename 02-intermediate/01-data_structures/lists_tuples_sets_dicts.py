"""
Lists, Tuples, Sets, Dicts — Data Structures (Advanced)
=========================================================
Covers: list/tuple/set/dict operations, namedtuple, performance
"""
from collections import namedtuple

# ─── 1. Lists (Advanced) ──────────────────────────────────────────────────────
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Sorting
print(sorted(nums))             # new list
nums.sort()                     # in-place
print(nums)

# sort with key
words = ["banana", "fig", "apple", "date", "elderberry"]
print(sorted(words, key=len))
print(sorted(words, key=lambda w: w[-1]))  # by last char

# Slicing tricks
print(nums[2:7:2])     # every 2nd from index 2 to 7
nums2 = nums[:]        # shallow copy
nums[::] = sorted(nums, reverse=True)   # in-place reverse-sort via slice assignment

# List as stack (LIFO)
stack = []
stack.append(1); stack.append(2); stack.append(3)
print(stack.pop())    # 3

# List as queue — inefficient (use deque instead)
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
print(queue.popleft())  # 1  O(1) vs list.pop(0) which is O(n)

# ─── 2. Tuples ────────────────────────────────────────────────────────────────
point = (3, 4)
x, y  = point             # unpacking
print(x, y)

# Single-element tuple needs trailing comma
single = (42,)
print(type(single))       # <class 'tuple'>

# Named tuples — readable, lightweight objects
Point  = namedtuple("Point",  ["x", "y"])
Person = namedtuple("Person", ["name", "age", "city"])

p  = Point(3, 4)
me = Person("Naman", 25, "Delhi")
print(p.x, p.y)
print(me.name, me.age)
print(me._asdict())    # OrderedDict

# Tuples as dict keys (immutable → hashable)
grid = {}
grid[(0, 0)] = "start"
grid[(3, 4)] = "end"
print(grid)

# ─── 3. Dictionaries (Advanced) ───────────────────────────────────────────────
person = {"name": "Alice", "age": 30, "city": "Delhi"}

# Safe access
print(person.get("name"))          # Alice
print(person.get("email", "N/A"))  # N/A — default

# Merging dicts
extra  = {"email": "alice@example.com", "age": 31}  # age updated
merged = {**person, **extra}    # Python 3.5+
print(merged)

# Python 3.9+ merge operator
# merged = person | extra

# setdefault
person.setdefault("email", "unknown@example.com")
print(person["email"])

# Nested dict access safely
config = {"db": {"host": "localhost", "port": 5432}}
print(config.get("db", {}).get("host", "unknown"))

# Dict comprehension to count chars
text  = "mississippi"
freq  = {ch: text.count(ch) for ch in set(text)}
print(freq)

# ─── 4. Sets ──────────────────────────────────────────────────────────────────
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a | b)   # union
print(a & b)   # intersection
print(a - b)   # difference (in a but not b)
print(a ^ b)   # symmetric difference (in a or b, not both)

print(a.issubset({1, 2, 3, 4, 5, 6}))    # True
print(a.issuperset({1, 2}))               # True

# Fastest way to deduplicate a list (order not preserved)
nums_dup = [1, 3, 2, 1, 4, 3, 5]
unique   = list(set(nums_dup))
print(unique)

# Preserve order while deduplicating
seen   = set()
unique_ordered = [x for x in nums_dup if not (x in seen or seen.add(x))]
print(unique_ordered)


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Given a list of dicts (students), sort by score then by name.
# TODO 2: Find all common elements across 3 different lists using sets.
# TODO 3: Implement a word-frequency counter using a dict (no Counter).
# TODO 4: Create a namedtuple for a playing card (suit, rank) and sort a hand.
# TODO 5: Merge two dicts, summing values for overlapping keys.
