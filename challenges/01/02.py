from pathlib import Path
from collections import Counter


def get_puzzle_input():
    with open(Path(__file__).parent / "puzzle_input.txt", "r") as f:
        return f.read()


def get_test_input():
    with open(Path(__file__).parent / "test_input.txt", "r") as f:
        return f.read()


def solve(input):
    numbers_left = []
    numbers_right = []

    for line in input.split("\n"):
        line = line.strip()
        if line:
            number_a, number_b = line.split("  ")
            numbers_left.append(int(number_a))
            numbers_right.append(int(number_b))

    counter_b = Counter(numbers_right)

    total_sum = 0

    for left_number in numbers_left:
        right_count = counter_b.get(left_number, 0)
        total_sum += left_number * right_count

    return total_sum


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)
    # puzzle_input = get_test_input(__file__)
    print(solve(puzzle_input))
