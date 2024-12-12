from functools import cache

# stones = map(int, """125 17""".split())
stones = map(int, """554735 45401 8434 0 188 7487525 77 7""".split())


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


print(sum(count(stone, 75) for stone in stones))
