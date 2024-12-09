from collections import defaultdict
from itertools import chain, combinations

from tqdm import tqdm

from challenges.utils import get_puzzle_input, get_test_input


def draw(lines, antenas: list[tuple[int, int]], antinodes: set) -> None:
    """Draw a grid with antenas and antinodes.

    Args:
        lines (list[str]): the original grid
        antenas (list[tuple[int, int]]): the coordinates of the antenas
        antinodes (set): the antinodes coordinates
    """
    grid = [["." for _ in range(len(lines[0]))] for _ in range(len(lines))]

    for x, y in antenas:
        grid[x][y] = "A"

    for x, y in antinodes:
        grid[x][y] = "X"

    print("    ", end="")
    for i in range(len(grid[0])):
        print(f"{i % 10}", end="")
    print()

    for i, line in enumerate(grid):
        print(f"{i:>2}: {''.join(line)}")


def solve(puzzle_input: str) -> int:
    cache: dict[str, list[tuple[int, int]]] = defaultdict(list)
    rows = len(puzzle_input.splitlines())
    cols = len(puzzle_input.splitlines()[0])

    for i, line in tqdm(
        enumerate(puzzle_input.splitlines()), desc="getting all antenas"
    ):
        for char in line:
            if char != ".":
                cache[char].append((i, line.index(char)))

    all_coords = list(chain(*cache.values()))
    antinodes_list = []
    for key in tqdm(cache, desc="getting all antinodes"):
        for antena1, antena2 in combinations(cache[key], 2):
            diff_x = antena1[0] - antena2[0]
            diff_y = antena1[1] - antena2[1]
            coordinate_antinode1 = [
                (antena1[0] + diff_x * t, antena1[1] + diff_y * t) for t in range(50)
            ]
            coordinate_antinode2 = [
                (antena2[0] - diff_x * t, antena2[1] - diff_y * t) for t in range(50)
            ]
            for c1 in coordinate_antinode1:
                if not (c1[0] > rows - 1 or c1[0] < 0 or c1[1] > cols - 1 or c1[1] < 0):
                    antinodes_list.append(c1)

            for c2 in coordinate_antinode2:
                if not (c2[0] > rows - 1 or c2[0] < 0 or c2[1] > cols - 1 or c2[1] < 0):
                    antinodes_list.append(c2)
    draw(puzzle_input.splitlines(), all_coords, set(antinodes_list))
    return len(set(antinodes_list))


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))
