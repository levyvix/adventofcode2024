from itertools import product

from challenges.utils import get_puzzle_input, get_test_input
from tqdm import tqdm


def test_combination(combination: tuple[str, ...], equations: list[int], test_value: int) -> bool:
    result = equations[0]
    for i, op in enumerate(combination):
        next_number = equations[i + 1]
        if op == "+":
            result += next_number
        elif op == "*":
            result *= next_number

        if result > test_value:
            return False

    return result == test_value


def solve(puzzle_input: str) -> int:
    soma_total = 0
    for line in tqdm(puzzle_input.splitlines(), desc="verifying lines..."):
        test_value = int(line.split(":")[0])
        equations = line.split(":")[1].lstrip().split(" ")
        equations = [int(x) for x in equations]

        operations = ["+", "*"]
        found_valid = False

        combinations = list(product(operations, repeat=len(equations) - 1))
        for comb in combinations:
            if test_combination(comb, equations, test_value):
                found_valid = True
                break

        if found_valid:
            soma_total += test_value

    return soma_total


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))
