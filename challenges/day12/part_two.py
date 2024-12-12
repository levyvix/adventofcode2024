from collections import deque
from pathlib import Path

from rich import print


def get_groups(grid):
    rows = len(grid)
    cols = len(grid[0])

    regions = []
    seen = set()

    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue
            seen.add((r, c))
            region = {(r, c)}
            q = deque([(r, c)])
            crop = grid[r][c]
            while q:
                cr, cc = q.popleft()
                for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                    if grid[nr][nc] != crop:
                        continue
                    if (nr, nc) in region:
                        continue
                    region.add((nr, nc))
                    q.append((nr, nc))
            seen |= region
            regions.append(region)
    return regions


def sides(region):
    corner_candidates = set()
    for r, c in region:
        for cr, cc in [(r - 0.5, c - 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5), (r - 0.5, c + 0.5)]:
            corner_candidates.add((cr, cc))
    corners = 0
    for cr, cc in corner_candidates:
        config = [
            (sr, sc) in region
            for sr, sc in [(cr - 0.5, cc - 0.5), (cr + 0.5, cc - 0.5), (cr + 0.5, cc + 0.5), (cr - 0.5, cc + 0.5)]
        ]
        number = sum(config)
        if number == 1:
            corners += 1
        elif number == 2:
            if config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
        elif number == 3:
            corners += 1
    return corners


def solve(inp: str) -> int:
    grid = [list(line.strip()) for line in inp.splitlines()]
    regions = get_groups(grid)
    return sum(len(region) * sides(region) for region in regions)


if __name__ == "__main__":
    with open(Path(__file__).parent / "puzzle_input.txt") as f:
        inp = f.read()

    print(solve(inp))
