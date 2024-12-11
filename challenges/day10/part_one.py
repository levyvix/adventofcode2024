from collections import deque

from ..utils import get_puzzle_input, get_test_input


def parse_map(map_str: str) -> list[list[int]]:
    """
    Parse the input map string into a grid.

    Args:
        map_str (str): A string representation of the map.

    Returns:
        list[list[int]]: A 2D grid of integers.
    """
    return [[int(char) for char in line] for line in map_str.strip().splitlines()]


def find_trailheads(grid: list[list[int]]) -> list[tuple[int, int]]:
    """
    Find all zeros positions [(x0,y0), (x0, y0)].

    Args:
        grid (list[list[int]]): A 2D grid of integers.

    Returns:
        list[tuple[int, int]]: A list of positions with height

    """
    return [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 0]


def calculate_score(grid: list[list[int]], start: tuple[int, int]) -> int:
    """
    Calculate the score of a trailhead using BFS.

    Args:
        grid (list[list[int]]): A 2D grid of integers.
        start (tuple[int, int]): The starting position, zero position (x,y).

    Retunrs:
        int: The score of the trailhead.
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, 0)])  # (position, current height)
    visited = set()
    reachable_nines = set()

    while queue:
        (x, y), current_height = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # If we reach height 9, record it and continue
        if grid[x][y] == 9:
            reachable_nines.add((x, y))
            continue

        # Explore valid neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                if grid[nx][ny] == current_height + 1:
                    queue.append(((nx, ny), current_height + 1))

    return len(reachable_nines)


def total_trailhead_scores(map_str: str) -> int:
    """
    Compute the sum of scores for all trailheads

    Args:
        map_str (str): A string representation of the map.

    Returns:
        int: The sum of scores for all trailheads.
    """
    grid = parse_map(map_str)
    trailheads = find_trailheads(grid)
    total_score = sum(calculate_score(grid, trailhead) for trailhead in trailheads)
    return total_score


def solve(puzzle_input: str) -> int:
    """
    Receive the puzzle input and return the answer

    Args:
        puzzle_input (str): A string representation of the map.

    Returns:
        int: The sum of scores for all trailheads.
    """
    return total_trailhead_scores(puzzle_input)


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input = get_puzzle_input(__file__)
        print("PROD: ", solve(puzzle_input))

    puzzle_input = get_test_input(__file__)
    print("TEST: ", solve(puzzle_input))
