"""
heapq & bisect — Priority Queues and Sorted Structures
=======================================================
Ref: https://docs.python.org/3/tutorial/stdlib2.html#tools-for-working-with-lists
     https://docs.python.org/3/library/heapq.html
     https://docs.python.org/3/library/bisect.html

Industry use: top-K problems, priority queues, efficient sorted insertion.
"""
import heapq
import bisect
from dataclasses import dataclass, field

# ════════════════════════════════════════════════════════════
#  heapq — Min-Heap in Python
# ════════════════════════════════════════════════════════════
# Python's heapq is a MIN-heap. For max-heap: negate the values.

# ─── 1. Basic heap operations ────────────────────────────────────────────────
heap: list[int] = []
for val in [5, 3, 8, 1, 9, 2]:
    heapq.heappush(heap, val)    # O(log n)

print("heap:", heap)             # stored as array but heap-ordered
print(heapq.heappop(heap))       # 1 — smallest  O(log n)
print(heapq.heappop(heap))       # 2

# heapify — convert an existing list IN-PLACE  O(n)
data = [5, 3, 8, 1, 9, 2]
heapq.heapify(data)
print(data)            # [1, 3, 2, 5, 9, 8]  — valid heap

# peek at smallest without popping
print(data[0])         # 1  — always the smallest

# heapreplace — pop smallest and push new value  O(log n), faster than pop+push
heapq.heapreplace(data, 0)
print(data[0])         # 0

# ─── 2. nlargest / nsmallest — Top-K ──────────────────────────────────────────
scores = [85, 92, 78, 95, 61, 88, 73, 99, 55, 84]
print(heapq.nlargest(3, scores))    # [99, 95, 92]
print(heapq.nsmallest(3, scores))   # [55, 61, 73]

# With key function
students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob",   "score": 55},
    {"name": "Carol", "score": 88},
    {"name": "Dave",  "score": 99},
]
top2 = heapq.nlargest(2, students, key=lambda s: s["score"])
print([s["name"] for s in top2])   # ['Dave', 'Alice']

# ─── 3. Max-Heap (negate values) ─────────────────────────────────────────────
max_heap: list[int] = []
for v in [5, 3, 8, 1, 9]:
    heapq.heappush(max_heap, -v)   # negate to simulate max-heap

print(-heapq.heappop(max_heap))    # 9 — largest

# ─── 4. Priority Queue with dataclass ────────────────────────────────────────
@dataclass(order=True)
class Task:
    priority: int
    name: str = field(compare=False)   # exclude name from comparison

pq: list[Task] = []
heapq.heappush(pq, Task(priority=3, name="Low priority task"))
heapq.heappush(pq, Task(priority=1, name="High priority task"))
heapq.heappush(pq, Task(priority=2, name="Medium priority task"))

while pq:
    task = heapq.heappop(pq)
    print(f"P{task.priority}: {task.name}")

# ─── 5. Merge sorted iterables ────────────────────────────────────────────────
sorted1 = [1, 3, 5, 7]
sorted2 = [2, 4, 6, 8]
sorted3 = [0, 9, 10]
merged  = list(heapq.merge(sorted1, sorted2, sorted3))
print(merged)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ════════════════════════════════════════════════════════════
#  bisect — Binary Search on Sorted Lists
# ════════════════════════════════════════════════════════════

# ─── 6. bisect_left / bisect_right ────────────────────────────────────────────
sorted_list = [1, 3, 3, 5, 7, 9, 11]

# bisect_left → insertion point where list stays sorted; ties go LEFT
print(bisect.bisect_left(sorted_list, 3))    # 1 (before existing 3s)
print(bisect.bisect_left(sorted_list, 4))    # 3 (between 3 and 5)

# bisect_right → ties go RIGHT
print(bisect.bisect_right(sorted_list, 3))   # 3 (after existing 3s)
print(bisect.bisect_right(sorted_list, 4))   # 3 (same for non-existent)

# Check if value is in sorted list  O(log n)
def contains_sorted(lst: list, val) -> bool:
    i = bisect.bisect_left(lst, val)
    return i < len(lst) and lst[i] == val

print(contains_sorted(sorted_list, 5))    # True
print(contains_sorted(sorted_list, 6))   # False

# ─── 7. insort — Keep List Sorted on Insert ───────────────────────────────────
live = [1, 3, 5, 7]
bisect.insort(live, 4)    # insort_right
print(live)               # [1, 3, 4, 5, 7]
bisect.insort(live, 3)
print(live)               # [1, 3, 3, 4, 5, 7]

# ─── 8. Grade bucketing with bisect ──────────────────────────────────────────
def letter_grade(score: int) -> str:
    breakpoints = [60, 70, 80, 90]
    grades      = ["F", "D", "C", "B", "A"]
    return grades[bisect.bisect(breakpoints, score)]

for s in [45, 65, 75, 85, 95]:
    print(f"{s} → {letter_grade(s)}")

# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Implement a median-of-stream algorithm using two heaps (max-heap + min-heap).
# TODO 2: Find the K closest points to the origin from a list of (x, y) tuples using heapq.
# TODO 3: Use bisect to implement an O(n log n) longest increasing subsequence.
# TODO 4: Simulate a task scheduler: tasks arrive with priority; always process highest-priority first.
# TODO 5: Given a sorted list of event timestamps, use bisect to efficiently query events in a range.
