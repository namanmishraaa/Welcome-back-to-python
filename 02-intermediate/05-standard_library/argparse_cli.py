"""
argparse — Command-Line Interfaces
====================================
Ref: https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments
     https://docs.python.org/3/library/argparse.html
"""
import argparse
import sys

# ─── 1. Why argparse? ─────────────────────────────────────────────────────────
# sys.argv gives you raw strings. argparse provides:
#   - Type conversion and validation
#   - Auto-generated --help
#   - Positional and optional arguments
#   - Subcommands (like git commit, git push)

# ─── 2. Basic Parser ──────────────────────────────────────────────────────────
def demo_basic():
    parser = argparse.ArgumentParser(
        prog="greet",
        description="Greet a user from the command line.",
        epilog="Example: python argparse_cli.py Alice --count 3 --upper",
    )

    # Positional argument — required, no --prefix
    parser.add_argument("name", type=str, help="Name to greet")

    # Optional argument — --count / -c
    parser.add_argument(
        "--count", "-c",
        type=int,
        default=1,
        metavar="N",
        help="Number of greetings (default: 1)",
    )

    # Flag (store_true / store_false)
    parser.add_argument(
        "--upper", "-u",
        action="store_true",
        help="Print greeting in uppercase",
    )

    # choices restriction
    parser.add_argument(
        "--lang",
        choices=["en", "hi", "fr"],
        default="en",
        help="Language for greeting",
    )

    # Parse args (pass list to test without real sys.argv)
    args = parser.parse_args(["Alice", "--count", "2", "--upper"])

    greetings = {"en": "Hello", "hi": "Namaste", "fr": "Bonjour"}
    msg = f"{greetings[args.lang]}, {args.name}!"
    if args.upper:
        msg = msg.upper()
    for _ in range(args.count):
        print(msg)

demo_basic()

# ─── 3. Multiple Values (nargs) ───────────────────────────────────────────────
def demo_nargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="Files to process")  # 1 or more
    parser.add_argument("--nums", nargs="*", type=int)                # 0 or more
    parser.add_argument("--pair", nargs=2, type=float)                # exactly 2

    args = parser.parse_args(["a.txt", "b.txt", "--nums", "1", "2", "3"])
    print(args.files, args.nums)

demo_nargs()

# ─── 4. Subcommands (like git) ────────────────────────────────────────────────
def demo_subcommands():
    parser = argparse.ArgumentParser(prog="todo")
    sub    = parser.add_subparsers(dest="command", required=True)

    # 'add' subcommand
    add_p = sub.add_parser("add", help="Add a todo item")
    add_p.add_argument("text", help="Todo text")
    add_p.add_argument("--priority", choices=["low", "med", "high"], default="med")

    # 'list' subcommand
    list_p = sub.add_parser("list", help="List todos")
    list_p.add_argument("--all", action="store_true", dest="show_all")

    # 'done' subcommand
    done_p = sub.add_parser("done", help="Mark todo as done")
    done_p.add_argument("id", type=int, help="Todo ID")

    # Parse and dispatch
    for cmd_args in [
        ["add", "Buy groceries", "--priority", "high"],
        ["list", "--all"],
        ["done", "1"],
    ]:
        args = parser.parse_args(cmd_args)
        if args.command == "add":
            print(f"Adding: {args.text!r} [{args.priority}]")
        elif args.command == "list":
            print(f"Listing {'all' if args.show_all else 'active'} todos")
        elif args.command == "done":
            print(f"Marking todo #{args.id} as done")

demo_subcommands()

# ─── 5. Argument Groups and Mutual Exclusion ─────────────────────────────────
def demo_groups():
    parser = argparse.ArgumentParser()

    # Mutually exclusive — can't use both --verbose and --quiet
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--verbose", "-v", action="store_true")
    group.add_argument("--quiet",   "-q", action="store_true")

    args = parser.parse_args(["--verbose"])
    print(f"verbose={args.verbose}, quiet={args.quiet}")

demo_groups()

# ─── 6. Custom Types ──────────────────────────────────────────────────────────
def positive_int(value: str) -> int:
    """Argparse type that only accepts positive integers."""
    n = int(value)
    if n <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return n

parser = argparse.ArgumentParser()
parser.add_argument("count", type=positive_int)
args = parser.parse_args(["5"])
print(args.count)

# ─── 7. click — Industry-Standard Alternative ─────────────────────────────────
# click is simpler, more composable, and widely used in industry.
# Install: uv add click
#
# Example (not runnable without click installed):
# import click
#
# @click.command()
# @click.argument("name")
# @click.option("--count", default=1, help="Number of greetings")
# @click.option("--upper/--no-upper", default=False)
# def greet(name, count, upper):
#     """Greet NAME from the command line."""
#     msg = f"Hello, {name}!"
#     if upper: msg = msg.upper()
#     for _ in range(count): click.echo(msg)
#
# if __name__ == "__main__":
#     greet()


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Build a "word count" CLI: wc.py file.txt --lines --words --chars
# TODO 2: Build a file renamer CLI: rename.py src_dir --prefix "2024-" --dry-run
# TODO 3: Build a CSV filter CLI: filter.py data.csv --column age --gt 18
# TODO 4: Add --config FILE argument that loads defaults from a JSON file.
# TODO 5: Recreate the same CLI using click and compare the code.
