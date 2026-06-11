"""
datetime — Dates, Times, and Timezones
=========================================
Ref: https://docs.python.org/3/tutorial/stdlib.html#dates-and-times
     https://docs.python.org/3/library/datetime.html
     https://docs.python.org/3/library/zoneinfo.html
"""
import datetime
from datetime import date, time, datetime as dt, timedelta, timezone
from zoneinfo import ZoneInfo    # Python 3.9+

# ─── 1. date ──────────────────────────────────────────────────────────────────
today = date.today()
print(today)                  # 2024-01-15
print(today.year, today.month, today.day)
print(today.weekday())        # 0=Mon … 6=Sun
print(today.isoweekday())     # 1=Mon … 7=Sun  (ISO standard)
print(today.isoformat())      # "2024-01-15"

# Create a specific date
birthday  = date(1990, 7, 20)
age_days  = today - birthday
print(f"Age: {age_days.days} days")

# ─── 2. time ──────────────────────────────────────────────────────────────────
t = time(14, 30, 45, 123456)  # hour, minute, second, microsecond
print(t.hour, t.minute, t.second, t.microsecond)
print(t.isoformat())           # "14:30:45.123456"

# ─── 3. datetime ──────────────────────────────────────────────────────────────
now = dt.now()
utcnow = dt.now(tz=timezone.utc)    # always use tz-aware for real apps

specific = dt(2024, 3, 15, 9, 30, 0)
print(specific.date())   # 2024-03-15
print(specific.time())   # 09:30:00

# From timestamp (Unix epoch)
ts = dt.fromtimestamp(0)           # 1970-01-01 (local time)
ts_utc = dt.fromtimestamp(0, tz=timezone.utc)
print(ts_utc)

# ─── 4. timedelta — Duration Arithmetic ──────────────────────────────────────
delta = timedelta(days=30, hours=2, minutes=15)
print(delta.days, delta.seconds, delta.total_seconds())

future = now + timedelta(weeks=2)
past   = now - timedelta(days=365)
print(f"Two weeks from now: {future.date()}")
print(f"One year ago: {past.date()}")

# Difference between two datetimes
start = dt(2024, 1, 1)
end   = dt(2024, 12, 31)
diff  = end - start
print(f"Days in 2024: {diff.days}")

# ─── 5. strftime / strptime — Formatting and Parsing ─────────────────────────
# strftime — datetime → string
print(now.strftime("%d %B %Y"))          # "15 January 2024"
print(now.strftime("%I:%M %p"))          # "02:30 PM"
print(now.strftime("%Y-%m-%dT%H:%M:%S")) # ISO 8601

# Key codes:
# %Y=4-digit year  %m=month  %d=day  %H=hour(24)  %M=minute  %S=second
# %A=weekday name  %B=month name  %p=AM/PM  %f=microseconds

# strptime — string → datetime (PARSE)
date_str = "15 January 2024 14:30"
parsed   = dt.strptime(date_str, "%d %B %Y %H:%M")
print(parsed)

# ISO format parsing (Python 3.7+)
iso     = "2024-01-15T14:30:00+05:30"
parsed2 = dt.fromisoformat(iso)
print(parsed2, parsed2.tzinfo)

# ─── 6. Timezones with zoneinfo (Python 3.9+) ────────────────────────────────
IST  = ZoneInfo("Asia/Kolkata")
UTC  = ZoneInfo("UTC")
NY   = ZoneInfo("America/New_York")

now_ist = dt.now(tz=IST)
now_utc = now_ist.astimezone(UTC)
now_ny  = now_ist.astimezone(NY)

print(f"IST: {now_ist.strftime('%H:%M %Z')}")
print(f"UTC: {now_utc.strftime('%H:%M %Z')}")
print(f"NY:  {now_ny.strftime('%H:%M %Z')}")

# ── Interview Tip ─────────────────────────────────────────────────────────────
# Always store datetimes in UTC in databases; convert to local time only for display.
# Use dt.now(tz=timezone.utc) — never naive dt.utcnow() (deprecated 3.12).

# ─── 7. calendar module ───────────────────────────────────────────────────────
import calendar

print(calendar.month(2024, 2))        # prints Feb 2024 calendar
print(calendar.isleap(2024))          # True
print(calendar.monthrange(2024, 2))   # (weekday of 1st, number of days)


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Calculate how many days until your next birthday.
# TODO 2: Given a list of ISO date strings, sort them chronologically.
# TODO 3: Write a function that returns the last day of any given month.
# TODO 4: Convert a naive datetime from "Asia/Kolkata" to UTC and format it.
# TODO 5: Build a simple "time ago" function: humanize(dt) → "3 days ago", "2 hours ago", etc.
