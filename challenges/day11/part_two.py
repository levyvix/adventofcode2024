from functools import cache

# stones = map(int, """125 17""".split())

inp = """125 17"""


@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[: length // 2]), steps - 1) + count(int(string[length // 2 :]), steps - 1)
    return count(stone * 2024, steps - 1)


def solve(inp: str) -> int:
    stones = map(int, inp.split())
    return sum(count(stone, 75) for stone in stones)


print(solve(inp))
