from challenges.utils import get_puzzle_input, get_test_input
import re


def solve(input):
    line = input.replace("\n", "")

    # everything thats not m, u, l, (,) and numbers
    line = re.sub("[^mul(0-9),]", " ", line)
    valid_calls = re.findall(r"mul\((\d+),(\d+)\)", line)

    total_sum = 0
    for call in valid_calls:
        total_sum += int(call[0]) * int(call[1])

    return total_sum


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))
