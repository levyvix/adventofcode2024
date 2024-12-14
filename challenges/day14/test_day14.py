from challenges.utils import get_puzzle_input


def test_part_one_prod():
    from challenges.day14.part_one import solve

    file = get_puzzle_input(__file__)
    assert solve(file) == 231852216


def test_part_two_prod():
    from challenges.day14.part_two import solve

    file = get_puzzle_input(__file__)
    assert solve(file) == 8159
