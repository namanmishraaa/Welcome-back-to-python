"""
logging — Professional Logging
================================
Ref: https://docs.python.org/3/tutorial/stdlib2.html#logging
     https://docs.python.org/3/library/logging.html
     https://docs.python.org/3/howto/logging.html
"""
import logging
import logging.handlers
import sys
from pathlib import Path

# ─── 1. Why logging instead of print()? ──────────────────────────────────────
# print()   → no level, no timestamp, no easy on/off, hard to redirect
# logging   → levels, timestamps, file output, configurable, zero-cost when off

# ─── 2. Log Levels (low → high severity) ─────────────────────────────────────
# DEBUG    10  — detailed diagnostic info (dev only)
# INFO     20  — normal events, progress
# WARNING  30  — something unexpected but recoverable
# ERROR    40  — serious problem, some functionality lost
# CRITICAL 50  — program may not continue

# ─── 3. Quick Setup (for scripts) ─────────────────────────────────────────────
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout,
)

log = logging.getLogger(__name__)   # always use __name__, not root logger
log.debug("Debug message")
log.info("Info message")
log.warning("Warning message")
log.error("Error message")
log.critical("Critical message")

# ─── 4. Production Setup — Logger + Handlers + Formatter ─────────────────────
def setup_logger(name: str, log_file: Path | None = None) -> logging.Logger:
    """
    Create a properly configured logger.

    - Console handler: WARNING and above
    - File handler (optional): DEBUG and above, rotating at 5 MB
    """
    logger    = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    fmt       = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler — WARNING+
    ch = logging.StreamHandler(sys.stderr)
    ch.setLevel(logging.WARNING)
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    # File handler — DEBUG+ with rotation (5 MB, keep 3 backups)
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        fh = logging.handlers.RotatingFileHandler(
            log_file, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
        )
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(fmt)
        logger.addHandler(fh)

    return logger

app_log = setup_logger("myapp")   # console-only for demo
app_log.info("App started")       # won't show (below WARNING for console)
app_log.warning("Low memory")     # shown on stderr
app_log.error("Connection failed")

# ─── 5. Logging Exceptions ────────────────────────────────────────────────────
try:
    1 / 0
except ZeroDivisionError:
    log.exception("Division failed")   # logs ERROR + full traceback automatically

# ─── 6. Lazy % Formatting (performance) ──────────────────────────────────────
# ✅ Use % placeholders — the string is NOT formatted if the level is off
log.debug("Processing item %d of %d: %s", 1, 100, "user.csv")

# ❌ Avoid f-strings in log calls — the string is ALWAYS formatted
# log.debug(f"Processing item {1} of {100}: {'user.csv'}")

# ─── 7. Structured Logging (JSON) ─────────────────────────────────────────────
# For services / log aggregators (ELK, CloudWatch, Datadog), emit JSON:
import json

class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "time":    self.formatTime(record),
            "level":   record.levelname,
            "logger":  record.name,
            "line":    record.lineno,
            "message": record.getMessage(),
        }
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(payload)

json_handler = logging.StreamHandler(sys.stdout)
json_handler.setFormatter(JSONFormatter())
json_log = logging.getLogger("json_demo")
json_log.addHandler(json_handler)
json_log.warning("Disk usage high", extra={"disk_pct": 92})

# ─── 8. Best Practices ────────────────────────────────────────────────────────
# ✅ One logger per module: log = logging.getLogger(__name__)
# ✅ Never call logging.basicConfig() inside a library — only in __main__
# ✅ Use log.exception() inside except blocks (captures traceback)
# ✅ Use % formatting, not f-strings, in log messages
# ✅ Set level per handler, not just on the logger
# ✅ Use RotatingFileHandler or TimedRotatingFileHandler for production
# ❌ Never log sensitive data (passwords, tokens, PII)


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Add logging to csv_and_json.py — log every file read/write with timing.
# TODO 2: Create a decorator @log_calls that logs function name, args, result, and duration.
# TODO 3: Set up a logger that writes DEBUG to a file and WARNING+ to the console.
# TODO 4: Implement a context manager that temporarily sets log level to DEBUG.
# TODO 5: Write a JSONFormatter that includes the hostname and process ID in every log record.
