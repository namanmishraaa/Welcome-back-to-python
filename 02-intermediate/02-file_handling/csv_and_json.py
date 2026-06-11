"""
CSV and JSON — File Handling
==============================
Covers: csv.reader/writer, DictReader/DictWriter, json.load/dump
"""
import csv
import json
from pathlib import Path

# ─── 1. Writing and Reading CSV ───────────────────────────────────────────────
CSV_FILE = Path("students.csv")
HEADERS  = ["name", "age", "score"]
ROWS     = [
    ["Alice", 22, 95.5],
    ["Bob",   25, 87.0],
    ["Charlie", 23, 91.3],
]

# Write
with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(HEADERS)
    writer.writerows(ROWS)

# Read
with open(CSV_FILE, encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ─── 2. DictReader / DictWriter ──────────────────────────────────────────────
# Rows become dicts keyed by header names — much more readable

# Write
students = [
    {"name": "Alice",   "age": 22, "score": 95.5},
    {"name": "Bob",     "age": 25, "score": 87.0},
    {"name": "Charlie", "age": 23, "score": 91.3},
]

with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=HEADERS)
    writer.writeheader()
    writer.writerows(students)

# Read
with open(CSV_FILE, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: {row['score']}")

# ─── 3. JSON — Read and Write ────────────────────────────────────────────────
JSON_FILE = Path("config.json")

config = {
    "database": {
        "host":     "localhost",
        "port":     5432,
        "name":     "mydb",
    },
    "debug":   True,
    "version": "1.0.0",
    "tags":    ["python", "learning"],
}

# json.dump — write to file
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

# json.load — read from file
with open(JSON_FILE, encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["database"]["host"])

# json.dumps — to string; json.loads — from string
json_str  = json.dumps(config, indent=2)
from_str  = json.loads(json_str)
print(type(json_str))   # str
print(type(from_str))   # dict

# Custom encoder for non-serializable types
import datetime

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        return super().default(obj)

data     = {"date": datetime.date(2024, 1, 15), "value": 42}
encoded  = json.dumps(data, cls=DateEncoder)
print(encoded)

# ─── 4. Practical Pattern: Config File Helper ────────────────────────────────
class JSONConfig:
    def __init__(self, path: Path):
        self.path = path
        self._data = self._load()

    def _load(self) -> dict:
        if self.path.exists():
            return json.loads(self.path.read_text(encoding="utf-8"))
        return {}

    def get(self, key: str, default=None):
        return self._data.get(key, default)

    def set(self, key: str, value) -> None:
        self._data[key] = value
        self.path.write_text(
            json.dumps(self._data, indent=2),
            encoding="utf-8",
        )

cfg = JSONConfig(JSON_FILE)
cfg.set("theme", "dark")
print(cfg.get("theme"))       # dark
print(cfg.get("missing", 42)) # 42

# Cleanup
CSV_FILE.unlink(missing_ok=True)
JSON_FILE.unlink(missing_ok=True)


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Read a CSV and compute the average score.
# TODO 2: Convert a CSV file to a JSON file (list of dicts).
# TODO 3: Filter CSV rows where a column meets a condition and write to new CSV.
# TODO 4: Deep-merge two JSON configs, with the second taking priority.
# TODO 5: Build a tiny CLI tool: python tool.py config.json get database.host
