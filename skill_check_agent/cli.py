"""
cli.py — Command-line interface for skill-check-agent.

Usage:
    skill-check-agent                          # overall quiz at current level
    skill-check-agent --level beginner         # quiz all topics in a level
    skill-check-agent --level intermediate --topic data_structures  # single topic
    skill-check-agent --status                 # show progress summary
    skill-check-agent --reset                  # reset all progress
    skill-check-agent --list                   # list all levels and topics
"""

import argparse
import sys

from .questions import LEVELS, QUESTIONS
from . import progress as prog
from . import quiz


BANNER = r"""
 _____ _    _ _ _        _____ _               _
/  ___| |  (_) | |      /  __ \ |             | |
\ `--.| | ___| | |      | /  \/ |__   ___  ___| | __
 `--. \ |/ / | | |      | |   | '_ \ / _ \/ __| |/ /
/\__/ /   <| | | |_____ | \__/\ | | |  __/ (__|   <
\____/|_|\_\_|_|______/  \____/_| |_|\___|\___|_|\_\
     ___  ___  _____  ___  _  _____
    / _ \/ _ \| ____|/ _ \| ||_   _|
   / /_\ \ (_| | |__ | | | | |  | |
  |  _  |\__, |  __|| | | | |  | |
  | | | |  / /| |___| |_| | |  | |
  \_| |_/ /_/ \____/ \___/|_|  \_/
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="skill-check-agent",
        description="Python skill assessment tool — tests you level by level, topic by topic.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  skill-check-agent                            Run overall quiz at your current level
  skill-check-agent --level beginner           Quiz all beginner topics
  skill-check-agent --level advanced --topic decorators   Single topic quiz
  skill-check-agent --status                  Show your progress
  skill-check-agent --reset                   Start fresh
  skill-check-agent --list                    List all topics
        """,
    )

    parser.add_argument(
        "--level", "-l",
        choices=LEVELS,
        help="Target a specific level (beginner/intermediate/advanced)",
    )
    parser.add_argument(
        "--topic", "-t",
        help="Target a specific topic within the chosen level",
    )
    parser.add_argument(
        "--status", "-s",
        action="store_true",
        help="Show current progress and scores",
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Reset all progress and start over",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available levels and topics",
    )
    return parser


def list_topics() -> None:
    print("\nAvailable levels and topics:\n")
    for level in LEVELS:
        topics = list(QUESTIONS[level].keys())
        q_count = sum(len(QUESTIONS[level][t]) for t in topics)
        print(f"  {level.upper()}  ({q_count} questions total)")
        for topic in topics:
            n = len(QUESTIONS[level][topic])
            print(f"    --topic {topic:<25} ({n} questions)")
        print()


def main() -> None:
    print(BANNER)
    parser = build_parser()
    args = parser.parse_args()

    state = prog.load()

    # ── --list ──────────────────────────────────────────────────
    if args.list:
        list_topics()
        return

    # ── --reset ─────────────────────────────────────────────────
    if args.reset:
        confirm = input("Reset all progress? This cannot be undone. (yes/no): ").strip().lower()
        if confirm == "yes":
            state = prog.reset()
            print("Progress reset. Starting fresh from beginner level.")
        else:
            print("Cancelled.")
        return

    # ── --status ────────────────────────────────────────────────
    if args.status:
        print(prog.get_summary(state))
        return

    # ── --level + --topic  (single topic quiz) ──────────────────
    if args.level and args.topic:
        level = args.level
        topic = args.topic

        if topic not in QUESTIONS.get(level, {}):
            valid = ", ".join(QUESTIONS[level].keys())
            print(f"Error: '{topic}' is not a valid topic for {level}.")
            print(f"Valid topics: {valid}")
            sys.exit(1)

        score = quiz.run_topic_quiz(level, topic)
        state = prog.record_topic_result(state, level, topic, score)
        _show_advancement(state, level)
        return

    # ── --level only  (full level quiz) ─────────────────────────
    if args.level:
        level = args.level
        results = quiz.run_level_quiz(level)
        for topic, score in results.items():
            state = prog.record_topic_result(state, level, topic, score)
        _show_advancement(state, level)
        return

    # ── default: overall quiz at current level ───────────────────
    current = state["current_level"]
    print(f"\n  Your current level: {current.upper()}")
    print("  Running overall skill check (use --level/--topic to narrow down)\n")

    all_results = quiz.run_overall_quiz(current)
    for level, topics in all_results.items():
        for topic, score in topics.items():
            state = prog.record_topic_result(state, level, topic, score)

    _show_advancement(state, current)
    print(prog.get_summary(state))


def _show_advancement(state: dict, prev_level: str) -> None:
    """Print a congratulations message if the user advanced."""
    new_level = state["current_level"]
    if new_level != prev_level:
        print(f"\n  *** LEVEL UP! ***")
        print(f"  You've completed {prev_level.upper()} and unlocked {new_level.upper()}!")
        print(f"  Run `skill-check-agent --level {new_level}` to start the next level.\n")
