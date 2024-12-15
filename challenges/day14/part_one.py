import re
from functools import reduce
from pathlib import Path

from icecream import ic


def make_robots_coords(file: str) -> list[tuple[int, int, int, int]]:
    """read the file input and make a list of robot coordinates and velocities

    Args:
                file (str): the file to read

    Returns:
                list[tuple[int, int, int, int]]: the coords of robots and their velocities (row, column, velocity_row, velocity_column)
    """
    robots: list[tuple[int, int, int, int]] = []
    for line in file.split(sep="\n"):
        c, r, vc, vr = map(int, re.findall(r"(-?\d+)", line))
        robots.append((r, c, vr, vc))
    return robots


def next_100_seconds(
    robots: list[tuple[int, int, int, int]], grid_size: tuple[int, int] = (103, 101)
) -> list[tuple[int, int, int, int]]:
    """simulate the next 100 seconds of the robots

    Args:
        robots (list[tuple[int,int,int,int]]): the robots coordinates and velocities
        grid_size (tuple, optional): the size of the grid (rows, columns). Defaults to (103, 101).

    Returns:
        (list[tuple[int,int,int,int]]): the robots coordinates and velocities after 100 seconds
    """
    for _ in range(100):
        for i, robot in enumerate(robots):
            r, c, vr, vc = robot
            r += vr
            c += vc
            # teleport to the other side
            r = r % grid_size[0]
            c = c % grid_size[1]

            robots[i] = (r, c, vr, vc)
    return robots


# calcular o numero em cada quadrante


def sum_quadrants(robots: list[tuple[int, int, int, int]], grid_size: tuple[int, int]) -> int:
    sumir_linha: int = grid_size[0] // 2
    sumir_coluna: int = grid_size[1] // 2
    quadrantes: list[list[tuple[int, int, int, int]]] = [[], [], [], []]

    for i, robot in enumerate(robots):
        if robot[0] == sumir_linha and robot[1] == sumir_coluna:
            del robots[i]
            continue

        if robot[0] < sumir_linha and robot[1] < sumir_coluna:
            quadrantes[0].append(robot)
        elif robot[0] < sumir_linha and robot[1] > sumir_coluna:
            quadrantes[1].append(robot)
        elif robot[0] > sumir_linha and robot[1] < sumir_coluna:
            quadrantes[2].append(robot)
        elif robot[0] > sumir_linha and robot[1] > sumir_coluna:
            quadrantes[3].append(robot)

    return reduce(lambda x, y: x * y, map(len, quadrantes), 1)


def solve(file: str) -> int:
    GRID_SIZE = (103, 101)
    robots = make_robots_coords(file=file)
    robots_future = next_100_seconds(robots=robots, grid_size=GRID_SIZE)
    return sum_quadrants(robots=robots_future, grid_size=GRID_SIZE)


if __name__ == "__main__":
    file: str = (Path(__file__).parent / "puzzle_input.txt").read_text()

    ic(solve(file))
