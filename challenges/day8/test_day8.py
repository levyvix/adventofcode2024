from challenges.day8.part_one import solve as part_one_solve
from challenges.day8.part_two import solve as part_two_solve

# from challenges.day8.part_two import solve as part_two_solve
from challenges.utils import get_puzzle_input, get_test_input


def test_part_one_test():
    puzzle_input_test = get_test_input(__file__)
    result = part_one_solve(puzzle_input_test)

    assert result == 14


def test_part_one_prod():
    puzzle_input_prod = get_puzzle_input(__file__)
    result = part_one_solve(puzzle_input_prod)

    assert result == 228


def test_part_two_test():
    puzzle_input_test = get_test_input(__file__)
    result = part_two_solve(puzzle_input_test)

    assert result == 34


# def test_part_two_prod():
#     puzzle_input_prod = get_puzzle_input(__file__)
#     result = part_two_solve(puzzle_input_prod)

#     assert result == 1919
