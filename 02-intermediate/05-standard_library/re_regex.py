"""
re — Regular Expressions
==========================
Ref: https://docs.python.org/3/tutorial/stdlib.html#string-pattern-matching
     https://docs.python.org/3/library/re.html
     https://docs.python.org/3/howto/regex.html
"""
import re

# ─── 1. Pattern Basics ────────────────────────────────────────────────────────
# .       any character except newline
# \d      digit [0-9]          \D  non-digit
# \w      word char [a-zA-Z0-9_]   \W  non-word
# \s      whitespace            \S  non-whitespace
# \b      word boundary
# ^       start of string       $  end of string
# [abc]   character class       [^abc]  negated class
# a|b     alternation
# (...)   capturing group       (?:...) non-capturing
# *       0 or more (greedy)    +  1 or more    ?  0 or 1
# {n}     exactly n             {n,m}  n to m
# (?P<name>...)  named group

# ─── 2. Core Functions ────────────────────────────────────────────────────────
text = "The price is $42.99 and $7.50"

# re.search — first match anywhere in string
m = re.search(r"\$[\d.]+", text)
if m:
    print(m.group())        # $42.99
    print(m.start(), m.end())

# re.match — only matches at the START of string
m = re.match(r"The", text)
print(bool(m))   # True

m = re.match(r"price", text)
print(bool(m))   # False — 'price' is not at the start

# re.findall — all non-overlapping matches → list of strings
prices = re.findall(r"\$[\d.]+", text)
print(prices)    # ['$42.99', '$7.50']

# re.finditer — all matches → iterator of Match objects
for match in re.finditer(r"\$[\d.]+", text):
    print(f"Found {match.group()} at {match.start()}-{match.end()}")

# re.fullmatch — entire string must match
print(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", "2024-01-15")))  # True
print(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", "2024-1-15")))   # False

# ─── 3. Groups ────────────────────────────────────────────────────────────────
date_str = "2024-01-15"

# Numbered groups
m = re.match(r"(\d{4})-(\d{2})-(\d{2})", date_str)
if m:
    year, month, day = m.groups()
    print(year, month, day)

# Named groups — preferred for readability
m = re.match(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", date_str)
if m:
    print(m.group("year"), m.groupdict())

# ─── 4. Substitution ──────────────────────────────────────────────────────────
# re.sub(pattern, replacement, string)
result = re.sub(r"\s+", " ", "too  many    spaces")
print(result)   # "too many spaces"

# Backreferences in replacement
result = re.sub(r"(\w+)\s+(\w+)", r"\2 \1", "hello world")
print(result)   # "world hello"

# Using a function as replacement
def redact(m: re.Match) -> str:
    return "*" * len(m.group())

result = re.sub(r"\d+", redact, "Call 1800 555 0199")
print(result)

# ─── 5. Compiled Patterns ─────────────────────────────────────────────────────
# Compile when you reuse the same pattern many times
EMAIL = re.compile(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    re.IGNORECASE,
)
emails = EMAIL.findall("Contact alice@example.com or BOB@GMAIL.COM")
print(emails)

# ─── 6. Flags ─────────────────────────────────────────────────────────────────
# re.IGNORECASE  (re.I)  — case-insensitive
# re.MULTILINE   (re.M)  — ^ and $ match start/end of each line
# re.DOTALL      (re.S)  — . matches newline too
# re.VERBOSE     (re.X)  — allow comments and whitespace in pattern

URL = re.compile(r"""
    (?P<scheme>https?)   # http or https
    ://
    (?P<host>[\w.-]+)    # hostname
    (?P<path>/[\w./-]*)? # optional path
""", re.VERBOSE)

m = URL.match("https://docs.python.org/3/library/re.html")
if m:
    print(m.groupdict())

# ─── 7. Common Patterns (interview cheat-sheet) ────────────────────────────────
PATTERNS = {
    "email":    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "url":      r"https?://[^\s]+",
    "phone_IN": r"(\+91|0)?[6-9]\d{9}",
    "date":     r"\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])",
    "ipv4":     r"(?:\d{1,3}\.){3}\d{1,3}",
    "slug":     r"[a-z0-9]+(?:-[a-z0-9]+)*",
}
test = "Email: user@test.com, Date: 2024-03-15, IP: 192.168.1.1"
for name, pat in PATTERNS.items():
    found = re.findall(pat, test)
    if found:
        print(f"{name}: {found}")


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Extract all URLs from a block of HTML text.
# TODO 2: Write a function that validates an Indian phone number (various formats).
# TODO 3: Parse a log line "2024-01-15 10:30:00 ERROR Failed to connect" into a dict.
# TODO 4: Replace all occurrences of profane words (from a list) with asterisks.
# TODO 5: Split a string on any whitespace OR comma OR semicolon using re.split().
