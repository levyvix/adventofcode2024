from collections import deque
from pathlib import Path

from rich import print

with open(Path(__file__).parent / "puzzle_input.txt") as f:
    inp = f.read()


grid = [[char for char in line] for line in inp.strip().splitlines()]


def get_groups(grid):
    rows = len(grid)
    cols = len(grid[0])
    seen = set()
    groups = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue
            seen.add((r, c))
            q = deque([(r, c)])
            region = set()
            region.add((r, c))
            while q:
                cr, cc = q.popleft()

                for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[cr][cc] and (nr, nc) not in region:
                        region.add((nr, nc))
                        q.append((nr, nc))
            seen |= region
            groups.append(region)
    return groups


groups = get_groups(grid)


def perimeter(region):
    total_perimeter = 0
    for r, c in region:
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if (nr, nc) not in region:
                total_perimeter += 1
    return total_perimeter


print(sum(len(g) * perimeter(g) for g in groups))  # 1437300
