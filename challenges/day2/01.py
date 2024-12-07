from challenges.utils import get_puzzle_input, get_test_input
from itertools import pairwise


def solve(input):
    safe_lines_count = 0
    for line in input.split("\n"):
        line = line.strip()
        # list of ints
        line = [int(x) for x in line.split(" ")]
        line_order = []
        for a, b in pairwise(line):
            if abs(a - b) <= 3 and a > b:
                line_order.append("desc")
            elif abs(a - b) <= 3 and a < b:
                line_order.append("asc")
            elif abs(a - b) > 3:
                continue
        if len(set(line_order)) == 1 and len(line_order) == (len(line) - 1):
            safe_lines_count += 1

    return safe_lines_count


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))
