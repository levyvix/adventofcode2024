from collections import deque

from challenges.utils import get_puzzle_input, get_test_input


def parse_map(map_str):
    """Parse the input map string into a grid."""
    return [[int(char) for char in line] for line in map_str.strip().splitlines()]


def find_trailheads(grid):
    """Find all positions with height 0."""
    return [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 0]


def calculate_rating(grid, start):
    """Calculate the score of a trailhead using BFS."""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, 0)])  # (position, current height)
    visited = set()
    reachable_nines = []

    while queue:
        (x, y), current_height = queue.popleft()

        visited.add((x, y))

        # if we reach height 9, record it and continue
        if grid[x][y] == 9:
            reachable_nines.append((x, y))
            continue

        # explore valid neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                if grid[nx][ny] == current_height + 1:
                    queue.append(((nx, ny), current_height + 1))

    return len(reachable_nines)


def total_trailhead_ratings(map_str):
    """Compute the sum of scores for all trailheads."""
    grid = parse_map(map_str)
    trailheads = find_trailheads(grid)
    total_score = sum(calculate_rating(grid, trailhead) for trailhead in trailheads)
    return total_score


def solve(puzzle_input):
    return total_trailhead_ratings(puzzle_input)


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input = get_puzzle_input(__file__)
        print("PROD: ", solve(puzzle_input))

    puzzle_input = get_test_input(__file__)
    print("TEST: ", solve(puzzle_input))
