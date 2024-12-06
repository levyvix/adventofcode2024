from challenges.utils import get_puzzle_input, get_test_input
from itertools import pairwise


def report_status(line):
    """Return True if the line is in ascending or descending order, and the
    difference between any two adjacent elements is at least one and at most three.
    """
    order = None
    for a, b in pairwise(line):
        delta = abs(a - b)
        if delta == 0 or delta > 3:
            return False
        if order is None:
            order = a < b
        elif order != (a < b):
            return False
    return True


def solve(input):
    safe_lines_count = 0
    for line in input.splitlines():
        if line:
            line = [int(x) for x in line.split()]
            if report_status(line):
                safe_lines_count += 1
            elif problem_dampener(line):
                safe_lines_count += 1
    return safe_lines_count


def problem_dampener(line: list[int]):
    for i, value in enumerate(line):
        # remove i and see if safe
        new_line = line.copy()
        new_line.pop(i)
        if report_status(new_line):
            return True
    return False


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)
    # puzzle_input = get_test_input(__file__)
    print(solve(puzzle_input))
