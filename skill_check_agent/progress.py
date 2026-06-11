"""
progress.py — Persist and manage user progress across sessions.

State is stored in .skill_check_progress.json at the project root.
"""

import json
import os
from pathlib import Path

from .questions import LEVELS, QUESTIONS

STATE_FILE = Path(__file__).parent.parent / ".skill_check_progress.json"


def _default_state() -> dict:
    """Return a fresh, empty progress state."""
    state: dict = {"current_level": "beginner", "levels": {}}
    for level in LEVELS:
        state["levels"][level] = {}
        for topic in QUESTIONS[level]:
            state["levels"][level][topic] = {
                "attempts": 0,
                "best_score": 0.0,
                "passed": False,
            }
    return state


def load() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, KeyError):
            pass
    return _default_state()


def save(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def reset() -> dict:
    state = _default_state()
    save(state)
    return state


def record_topic_result(state: dict, level: str, topic: str, score: float) -> dict:
    """Update topic stats and check for level advancement."""
    from .questions import PASS_THRESHOLD, LEVEL_PASS_THRESHOLD

    entry = state["levels"][level][topic]
    entry["attempts"] += 1
    if score > entry["best_score"]:
        entry["best_score"] = round(score, 3)
    if score >= PASS_THRESHOLD:
        entry["passed"] = True

    # Check if entire level is passed
    topics = state["levels"][level]
    level_avg = sum(t["best_score"] for t in topics.values()) / len(topics)
    all_passed = all(t["passed"] for t in topics.values())

    if all_passed and level_avg >= LEVEL_PASS_THRESHOLD:
        _try_advance_level(state, level)

    save(state)
    return state


def _try_advance_level(state: dict, completed_level: str) -> None:
    idx = LEVELS.index(completed_level)
    if idx + 1 < len(LEVELS):
        next_level = LEVELS[idx + 1]
        if state["current_level"] == completed_level:
            state["current_level"] = next_level


def get_summary(state: dict) -> str:
    lines = ["\n  Progress Summary", "=" * 50]
    for level in LEVELS:
        topics = state["levels"].get(level, {})
        if not topics:
            continue
        passed = sum(1 for t in topics.values() if t["passed"])
        total = len(topics)
        marker = " [COMPLETE]" if passed == total else ""
        lines.append(f"\n  {level.upper()}{marker}  ({passed}/{total} topics passed)")
        for topic, data in topics.items():
            pct = int(data["best_score"] * 100)
            status = "PASS" if data["passed"] else f"{pct}%"
            tick = "[v]" if data["passed"] else "[ ]"
            lines.append(f"    {tick} {topic:<25} {status}")
    lines.append(f"\n  Current level: {state['current_level'].upper()}")
    return "\n".join(lines)
