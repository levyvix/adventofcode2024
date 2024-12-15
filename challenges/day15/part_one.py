from pathlib import Path

from icecream import ic


def get_positions(grid: str):
    return [list(line) for line in grid.splitlines()]


def find_arrow(grid) -> tuple[int, int]:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                return r, c
    return (0, 0)


def solve(file: str) -> int:
    top, bottom = file.split("\n\n")
    movements = bottom.replace("\n", "")
    grid = get_positions(top)
    r, c = find_arrow(grid)
    for move in movements:
        dr, dc = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}[move]
        cr, cc = (r, c)
        targets = [(cr, cc)]
        go = True
        while True:
            cr += dr
            cc += dc
            char = grid[cr][cc]
            if char == "#":
                go = False
                break
            if char == "O":
                targets.append((cr, cc))

            if char == ".":
                break

        if not go:
            continue
        grid[r][c] = "."
        grid[r + dr][c + dc] = "@"
        for br, bc in targets[1:]:
            grid[br + dr][bc + dc] = "O"
        r += dr
        c += dc

    return sum(100 * r + c for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == "O")


if __name__ == "__main__":
    file = (Path(__file__).parent / "puzzle_input.txt").read_text()
    ic(solve(file))
