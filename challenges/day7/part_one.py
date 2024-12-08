from itertools import product

from challenges.utils import get_puzzle_input, get_test_input


def solve(puzzle_input: str):
    safe_lines = []
    for line in puzzle_input.splitlines():
        test_value = line.split(":")[0]
        equations = line.split(":")[1].lstrip().split(" ")

        operations = ["+", "*"]

        for combination in product(operations, repeat=len(equations) - 1):
            sum_of_combination = equations[0]
            for i, op in enumerate(combination):
                next_number = equations[i + 1]
                if op == "+":
                    sum_of_combination = eval(f"{sum_of_combination} {op} {next_number}")
                if op == "*":
                    sum_of_combination = eval(f"{sum_of_combination} {op} {next_number}")

            if sum_of_combination == int(test_value):
                safe_lines.append(test_value)
                break

    return sum([int(str_v) for str_v in safe_lines])


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))
