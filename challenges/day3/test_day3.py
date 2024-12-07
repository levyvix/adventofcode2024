from challenges.day3.part_one import solve as part_one_solve
from challenges.day3.part_two import solve as part_two_solve
from challenges.utils import get_test_input, get_puzzle_input


def test_part_one_test():
    puzzle_input_test = get_test_input(__file__)
    result = part_one_solve(puzzle_input_test)

    assert result == 161


def test_part_one_prod():
    puzzle_input_prod = get_puzzle_input(__file__)
    result = part_one_solve(puzzle_input_prod)

    assert result == 173731097


def test_part_two_test():
    puzzle_input_test = get_test_input(__file__)
    result = part_two_solve(puzzle_input_test)

    assert result == 48


def test_part_two_prod():
    puzzle_input_prod = get_puzzle_input(__file__)
    result = part_two_solve(puzzle_input_prod)

    assert result == 93729253
