import re
from pathlib import Path

from icecream import ic


def print_grid(grid_size, robots):
    grid = [["." for _ in range(grid_size[1])] for _ in range(grid_size[0])]
    for r, c, _, _ in robots:
        grid[r][c] = "#"
    for row in grid:
        print("".join(row))
    print()


def make_robots_coords(file: str) -> list[tuple[int, int, int, int]]:
    robots = []
    for line in file.split("\n"):
        c, r, vc, vr = map(int, re.findall(r"-?\d+", line))
        robots.append((r, c, vr, vc))
    return robots


def find_tree(robots: list[tuple[int, int, int, int]], grid_size=(103, 101)) -> int:
    for second in range(100_000):
        seen = set()
        for i, robot in enumerate(robots):
            r, c, vr, vc = robot
            r += vr
            c += vc
            # teleport to the other side
            r = r % grid_size[0]
            c = c % grid_size[1]

            robots[i] = (r, c, vr, vc)

            seen.add((r, c))

        if len(seen) == len(robots):
            print_grid(grid_size, robots)
            return second + 1
    return -1


def solve(file: str) -> int:
    GRID_SIZE = (103, 101)
    robots = make_robots_coords(file)
    seconds_to_find_tree = find_tree(robots, grid_size=GRID_SIZE)
    return seconds_to_find_tree


if __name__ == "__main__":
    file = (Path(__file__).parent / "puzzle_input.txt").read_text()

    ic(solve(file=file))
