from itertools import chain, combinations

from tqdm import tqdm

from challenges.utils import get_puzzle_input, get_test_input


def draw(lines, antenas, antinodes):
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


def solve(puzzle_input: str):
    cache: dict[str, list[tuple[int, int]]] = {}
    rows = len(puzzle_input.splitlines())
    cols = len(puzzle_input.splitlines()[0])

    # get all antenas and coords
    for i, line in tqdm(
        enumerate(puzzle_input.splitlines()), desc="getting all antenas"
    ):
        for char in line:
            if char != ".":
                if char not in cache:
                    # create a list of coordinates for that char
                    cache[char] = [(i, line.index(char))]
                else:
                    cache[char].append((i, line.index(char)))

    all_coords = list(chain(*cache.values()))
    antinodes_list = []
    for key in tqdm(cache, desc="getting all antinodes"):
        for antena1, antena2 in combinations(cache[key], 2):
            diff_x = antena1[0] - antena2[0]
            diff_y = antena1[1] - antena2[1]
            coordinate_antinode1 = (antena1[0] + diff_x, antena1[1] + diff_y)
            coordinate_antinode2 = (antena2[0] - diff_x, antena2[1] - diff_y)

            if not (
                # out of bounds
                coordinate_antinode1 in all_coords
                or coordinate_antinode1[0] > rows - 1
                or coordinate_antinode1[0] < 0
                or coordinate_antinode1[1] > cols - 1
                or coordinate_antinode1[1] < 0
            ):
                antinodes_list.append(coordinate_antinode1)

            if not (
                coordinate_antinode2 in all_coords
                or coordinate_antinode2[0] > rows - 1
                or coordinate_antinode2[0] < 0
                or coordinate_antinode2[1] > cols - 1
                or coordinate_antinode2[1] < 0
            ):
                antinodes_list.append(coordinate_antinode2)
    draw(puzzle_input.splitlines(), list(all_coords), set(antinodes_list))
    return len(set(antinodes_list))


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))
