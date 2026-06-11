"""
Collections Module — Data Structures
======================================
Covers: Counter, defaultdict, OrderedDict, deque, ChainMap
"""
from collections import Counter, defaultdict, OrderedDict, deque, ChainMap

# ─── 1. Counter ───────────────────────────────────────────────────────────────
text  = "mississippi"
freq  = Counter(text)
print(freq)
print(freq.most_common(3))   # top 3

words = "the quick brown fox jumps over the lazy dog the".split()
word_count = Counter(words)
print(word_count["the"])   # 3

# Arithmetic on Counters
c1 = Counter("aabbc")
c2 = Counter("bccdd")
print(c1 + c2)   # add
print(c1 - c2)   # subtract (keep only positive)
print(c1 & c2)   # intersection (min)
print(c1 | c2)   # union (max)

# ─── 2. defaultdict ───────────────────────────────────────────────────────────
# Like dict but returns default value for missing keys instead of KeyError
word_map = defaultdict(list)
for word in "the quick brown fox".split():
    word_map[word[0]].append(word)   # group by first letter
print(dict(word_map))

# defaultdict(int) for counting
count = defaultdict(int)
for ch in "banana":
    count[ch] += 1
print(dict(count))

# defaultdict(set)
graph = defaultdict(set)
edges = [(1, 2), (1, 3), (2, 3), (3, 4)]
for u, v in edges:
    graph[u].add(v)
    graph[v].add(u)
print(dict(graph))

# ─── 3. OrderedDict ───────────────────────────────────────────────────────────
# Python 3.7+ regular dicts maintain insertion order,
# but OrderedDict has additional methods: move_to_end, popitem(last=True)
od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
od.move_to_end("a")         # move 'a' to end
print(od)
od.move_to_end("c", last=False)  # move 'c' to front
print(od)

# LRU Cache using OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.cache    = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

cache = LRUCache(3)
cache.put(1, 1); cache.put(2, 2); cache.put(3, 3)
cache.get(1)            # access key 1 (moves to end)
cache.put(4, 4)         # key 2 is least recently used → evicted
print(list(cache.cache.keys()))   # [3, 1, 4]

# ─── 4. deque (double-ended queue) ───────────────────────────────────────────
d = deque([1, 2, 3])
d.append(4)         # add right   O(1)
d.appendleft(0)     # add left    O(1)
d.pop()             # remove right O(1)
d.popleft()         # remove left  O(1)
print(d)

# maxlen deque — sliding window
window = deque(maxlen=3)
for n in range(6):
    window.append(n)
    print(list(window))

d.rotate(2)     # rotate right by 2
print(d)

# ─── 5. ChainMap ──────────────────────────────────────────────────────────────
# Multiple dicts viewed as one; lookups search each map in order
defaults = {"color": "red",   "size": 10, "shape": "circle"}
user_cfg = {"color": "blue",  "size": 20}
theme    = {"color": "green"}

# Priority: theme > user_cfg > defaults
cfg = ChainMap(theme, user_cfg, defaults)
print(cfg["color"])   # green  (from theme)
print(cfg["size"])    # 20     (from user_cfg)
print(cfg["shape"])   # circle (from defaults)

# Useful for configuration, scope simulation (e.g., variable lookup)
print(list(cfg.keys()))   # all unique keys across all maps


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Find the 3 most common words in a paragraph using Counter.
# TODO 2: Use defaultdict to group anagrams from a list of words.
# TODO 3: Implement a sliding window maximum using deque.
# TODO 4: Build a simple in-memory cache with OrderedDict (LRU eviction).
# TODO 5: Use ChainMap to implement a simple two-scope variable resolver.
