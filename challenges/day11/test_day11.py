inp_test = """125 17"""
inp_prod = """554735 45401 8434 0 188 7487525 77 7"""


def test_part_one_test():
    from .part_one import solve

    result = solve(inp_test)

    assert result == 55312


def test_part_one_prod():
    from .part_one import solve

    result = solve(inp_prod)

    assert result == 209412


def test_part_two_test():
    from .part_two import solve

    result = solve(inp_test)

    assert result == 65601038650482


def test_part_two_prod():
    from .part_two import solve

    result = solve(inp_prod)

    assert result == 248967696501656
