from challenges.utils import get_puzzle_input, get_test_input


run_prod = False


def test_part_one_test():
    test_input = get_test_input(__file__)

    from .part_one import solve

    result = solve(test_input)

    assert result == 10092


def test_part_one_prod():
    puzzle_input = get_puzzle_input(__file__)

    from .part_one import solve

    result = solve(file=puzzle_input)

    assert result == 1371036


def test_part_two_test():
    test_input = get_test_input(__file__)
    from .part_two import solve

    result = solve(test_input)

    assert result == 1392847

def test_part_two_prod():
    puzzle_input = get_puzzle_input(__file__)
    from .part_two import solve

    result = solve(puzzle_input)

    assert result == 1392847



