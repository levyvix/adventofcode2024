import time
from itertools import repeat
from pathlib import Path

from icecream import ic

file = (Path(__file__).parent / "puzzle_input.txt").read_text()


def get_positions(grid: str):
    return [list(line) for line in grid.splitlines()]


def is_valid_move(grid, pos):
    rows, cols = len(grid), len(grid[0])
    return 0 <= pos[0] < rows and 0 <= pos[1] < cols and grid[pos[0]][pos[1]] != "#"


def move_box(grid: list[str], boxes, old_pos, new_pos):
    grid[old_pos[0]][old_pos[1]] = "."
    grid[new_pos[0]][new_pos[1]] = "O"
    boxes.remove(old_pos)
    boxes.add(new_pos)


def print_grid(grid, boxes, arrow):
    grid = [list(row) for row in grid]
    for box in boxes:
        grid[box[0]][box[1]] = "O"
    grid[arrow[0]][arrow[1]] = "@"
    for row in grid:
        print("".join(row))
    print()


def find_arrow(grid) -> tuple[int, int]:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                return r, c
    return (0, 0)


def solve(file: str):
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

    ic(sum(100 * r + c for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == "O"))


if __name__ == "__main__":
    ic(solve(file))
