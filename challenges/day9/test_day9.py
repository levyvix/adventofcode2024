from challenges.day9.part_one import solve as part_one_solve, remap_block
from challenges.day9.part_two import solve as part_two_solve
from challenges.utils import get_puzzle_input, get_test_input
import pytest

run_prod = False


def test_part_one_test():
    puzzle_input_test = get_test_input(__file__)
    result = part_one_solve(puzzle_input_test)

    assert result == 1928


# def test_part_one_prod():
#     if not run_prod:
#         return
#     puzzle_input_prod = get_puzzle_input(__file__)
#     result = part_one_solve(puzzle_input_prod)

#     assert result == 5162


# def test_part_two_test():
#     puzzle_input_test = get_test_input(__file__)
#     result = part_two_solve(puzzle_input_test)

#     assert result == 11387


# def test_part_two_prod():
#     if not run_prod:
#         return
#     puzzle_input_prod = get_puzzle_input(__file__)
#     result = part_two_solve(puzzle_input_prod)

#     assert result == 1909
