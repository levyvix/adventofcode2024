from challenges.utils import get_puzzle_input, get_test_input
import re


def solve(input):
    line = input.replace("\n", "")

    # Find all multiplications and their positions
    muls = [(m.start(), m.group()) for m in re.finditer(r"mul\((\d+),(\d+)\)", line)]

    # Find positions of don't() and do()
    stops = [m.start() for m in re.finditer(r"don't\(\)", line)]
    starts = [m.start() for m in re.finditer(r"do\(\)", line)]

    # Process each multiplication
    total_sum = 0
    for pos, mul in muls:
        # Find the last stop and start before this position
        last_stop = max([s for s in stops if s < pos], default=-1)
        last_start = max([s for s in starts if s < pos], default=-1)

        # If the last state change was a start, or there were no state changes, this mul is valid
        if last_start > last_stop or (last_stop == -1 and last_start == -1):
            # Extract numbers from mul(x,y)
            numbers = re.findall(r"\d+", mul)
            total_sum += int(numbers[0]) * int(numbers[1])

    return total_sum


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))
