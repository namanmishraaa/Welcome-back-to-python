"""
While Loops — Control Flow
===========================
Covers: while, loop control, do-while pattern, else clause
"""

# ─── 1. Basic while loop ──────────────────────────────────────────────────────
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# ─── 2. Common while patterns ────────────────────────────────────────────────
# Input validation loop
def read_positive() -> int:
    """Keep asking until a positive integer is given."""
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n > 0:
                return n
            print("Must be positive.")
        except ValueError:
            print("Not an integer.")

# Do-while equivalent (Python has no do-while keyword)
while True:
    # ... do work ...
    user_input = "q"        # simulated input
    if user_input == "q":
        break

# ─── 3. break and continue in while ──────────────────────────────────────────
i = 0
while i < 20:
    i += 1
    if i % 2 == 0:
        continue    # skip even numbers
    if i > 10:
        break       # stop after 10
    print(i, end=" ")   # 1 3 5 7 9
print()

# ─── 4. while…else ────────────────────────────────────────────────────────────
# else runs only if condition became False (no break)
n = 10
while n > 0:
    n -= 3
else:
    print(f"Loop ended naturally; n = {n}")   # n = -2

# With break — else does NOT run
n = 10
while n > 0:
    if n == 7:
        print("Breaking at 7")
        break
    n -= 1
else:
    print("This won't print")

# ─── 5. Practical Examples ────────────────────────────────────────────────────
# Binary search using while
def binary_search(arr: list, target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(nums, 7))    # 3
print(binary_search(nums, 6))    # -1

# Digit sum
def digit_sum(n: int) -> int:
    total = 0
    n = abs(n)
    while n:
        total += n % 10
        n //= 10
    return total

print(digit_sum(12345))   # 15

# ─── 6. Infinite Loops (intentional) ─────────────────────────────────────────
# Common pattern for event loops, servers, and interactive CLIs
COMMANDS = {"help": "Show help", "quit": "Exit program"}

running = True
inputs  = ["help", "unknown", "quit"]   # simulated user inputs
idx = 0

while running:
    cmd = inputs[idx]; idx += 1
    if cmd == "quit":
        print("Goodbye!")
        running = False
    elif cmd in COMMANDS:
        print(COMMANDS[cmd])
    else:
        print(f"Unknown command: {cmd}")


# ─── Exercises ────────────────────────────────────────────────────────────────
# TODO 1: Implement a number-guessing game using while (random number 1-100).
# TODO 2: Compute n! (factorial) iteratively with while.
# TODO 3: Reverse a number's digits using while (e.g., 1234 → 4321).
# TODO 4: Simulate a simple ATM: balance, deposit, withdraw, quit.
# TODO 5: Find the first power of 2 that exceeds 1_000_000 using while.
