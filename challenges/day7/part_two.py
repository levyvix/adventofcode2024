from itertools import product

from tqdm import tqdm

from challenges.utils import get_puzzle_input, get_test_input


def test_combination(combination, equations, test_value):
    sum_of_combination = int(equations[0])
    for i, op in enumerate(combination):
        next_number = equations[i + 1]
        if op == "+":
            sum_of_combination = int(eval(f"{sum_of_combination} {op} {next_number}"))
        if op == "*":
            sum_of_combination = int(eval(f"{sum_of_combination} {op} {next_number}"))
        if op == "||":
            sum_of_combination = int(f"{sum_of_combination}{next_number}")
        if sum_of_combination == int(test_value):
            return int(test_value)

    return 0


def solve(puzzle_input: str):
    soma_total = 0
    for line in tqdm(puzzle_input.splitlines(), desc="verifying lines..."):
        test_value = line.split(":")[0]
        equations = line.split(":")[1].lstrip().split(" ")

        operations = ["+", "*", "||"]

        combinations = list(product(operations, repeat=len(equations) - 1))
        for comb in tqdm(combinations, desc="testing combinations..."):
            result = test_combination(comb, equations, test_value)
            if result:
                soma_total += int(test_value)
                break

    return soma_total


if __name__ == "__main__":
    run_prod = False

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))
