from challenges.utils import get_puzzle_input, get_test_input

run_prod = True


def test_part_one_test():
    from challenges.day13.part_one import solve

    file = get_test_input(__file__)
    assert solve(file) == 480


def test_part_one_prod():
    from challenges.day13.part_one import solve

    file = get_puzzle_input(__file__)
    assert solve(file) == 33427


def test_part_two_test():
    from challenges.day13.part_two import solve

    file = get_test_input(__file__)
    assert solve(file) == 875318608908


def test_part_two_prod():
    from challenges.day13.part_two import solve

    file = get_puzzle_input(__file__)
    assert solve(file) == 91649162972270
