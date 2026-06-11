"""
quiz.py — Interactive quiz engine for skill-check-agent.
"""

import random
import sys
from typing import Optional

from .questions import QUESTIONS, LEVELS, PASS_THRESHOLD


def _clear_line() -> None:
    print()


def _ask_question(q_dict: dict, number: int, total: int) -> bool:
    """Present a single question and return True if answered correctly."""
    print(f"\n  Q{number}/{total}: {q_dict['q']}")
    choices = q_dict["choices"][:]
    random.shuffle(choices)
    labels = ["A", "B", "C", "D"]

    for label, choice in zip(labels, choices):
        print(f"    {label}) {choice}")

    correct_label = labels[choices.index(q_dict["answer"])]

    while True:
        raw = input("\n  Your answer (A/B/C/D): ").strip().upper()
        if raw in labels[: len(choices)]:
            break
        print("  Please enter A, B, C, or D.")

    if raw == correct_label:
        print("  Correct!")
        print(f"  Tip: {q_dict['explain']}")
        return True
    else:
        print(f"  Wrong. Correct answer: {correct_label}) {q_dict['answer']}")
        print(f"  Tip: {q_dict['explain']}")
        return False


def run_topic_quiz(level: str, topic: str, quick: bool = False) -> float:
    """
    Run a quiz for a specific level/topic.
    Returns the score as a float 0.0–1.0.
    """
    all_questions = QUESTIONS[level][topic]
    sample_size = min(5, len(all_questions)) if quick else len(all_questions)
    questions = random.sample(all_questions, sample_size)

    bar = "─" * 50
    print(f"\n{bar}")
    print(f"  QUIZ: {level.upper()} > {topic.replace('_', ' ').title()}")
    print(f"  {sample_size} questions  |  Pass mark: {int(PASS_THRESHOLD*100)}%")
    print(bar)

    correct = 0
    for i, q in enumerate(questions, 1):
        if _ask_question(q, i, sample_size):
            correct += 1

    score = correct / sample_size
    pct = int(score * 100)
    status = "PASSED" if score >= PASS_THRESHOLD else "NOT PASSED"

    print(f"\n{bar}")
    print(f"  Result: {correct}/{sample_size}  ({pct}%)  —  {status}")
    print(bar)
    return score


def run_level_quiz(level: str) -> dict[str, float]:
    """Run quizzes for all topics in a level. Returns {topic: score}."""
    topics = list(QUESTIONS[level].keys())
    results: dict[str, float] = {}

    print(f"\n{'='*50}")
    print(f"  LEVEL QUIZ: {level.upper()}")
    print(f"  Topics: {', '.join(topics)}")
    print("=" * 50)

    for topic in topics:
        score = run_topic_quiz(level, topic, quick=True)
        results[topic] = score
        input("\n  Press Enter to continue to next topic...")

    _print_level_summary(level, results)
    return results


def run_overall_quiz(current_level: str) -> dict[str, dict[str, float]]:
    """
    Run a mixed overall quiz drawing questions from all levels
    up to and including the user's current level.
    Returns {level: {topic: score}}.
    """
    accessible = LEVELS[: LEVELS.index(current_level) + 1]
    all_results: dict[str, dict[str, float]] = {}

    print(f"\n{'='*50}")
    print("  OVERALL SKILL CHECK")
    print(f"  Levels: {', '.join(l.upper() for l in accessible)}")
    print("=" * 50)

    for level in accessible:
        all_results[level] = {}
        for topic in QUESTIONS[level]:
            score = run_topic_quiz(level, topic, quick=True)
            all_results[level][topic] = score
            input("\n  Press Enter for next topic...")

    _print_overall_summary(all_results)
    return all_results


def _print_level_summary(level: str, results: dict) -> None:
    print(f"\n{'─'*50}")
    print(f"  Level Summary: {level.upper()}")
    passed = 0
    for topic, score in results.items():
        pct = int(score * 100)
        ok = score >= PASS_THRESHOLD
        passed += int(ok)
        tick = "[v]" if ok else "[x]"
        print(f"    {tick} {topic:<25} {pct}%")
    avg = int(sum(results.values()) / len(results) * 100) if results else 0
    print(f"  Average: {avg}%  |  {passed}/{len(results)} topics passed")
    print("─" * 50)


def _print_overall_summary(all_results: dict) -> None:
    print(f"\n{'='*50}")
    print("  OVERALL SUMMARY")
    print("=" * 50)
    for level, topics in all_results.items():
        _print_level_summary(level, topics)
