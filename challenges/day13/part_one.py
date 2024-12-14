import re
from pathlib import Path

import numpy as np
from icecream import ic

file = (Path(__file__).parent / "puzzle_input.txt").read_text()


def get_claws(file: str):
    claws = []
    claw = []
    for i, line in enumerate(file.splitlines()):
        if "Button A" in line:
            button_a_pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
            claw.append(list(map(int, button_a_pattern.findall(line)[0])))

        if "Button B" in line:
            button_b_pattern = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
            claw.append(list(map(int, button_b_pattern.findall(line)[0])))

        if "Prize" in line:
            prize_pattern = re.compile(r"Prize: X=(\d+), Y=(\d+)")
            prize = list(map(int, prize_pattern.findall(line)[0]))
            claw.append(prize)

        if not line or i == len(file.splitlines()) - 1:
            claws.append(claw)
            claw = []
            continue

    return claws


def determine_a_b(a: list[int], b: list[int], target: list[int]):
    A = np.array([[a[0], b[0]], [a[1], b[1]]])

    B = np.array(target)

    res = np.linalg.solve(A, B)

    pressa = round(res[0])
    pressb = round(res[1])

    if pressa * a[0] + pressb * b[0] == target[0] and pressa * a[1] + pressb * b[1] == target[1]:
        return pressa, pressb
    else:
        return 0, 0


def solve(file: str) -> int:
    claws = get_claws(file)
    total_cost = 0
    for claw in claws:
        pressa, pressb = determine_a_b(claw[0], claw[1], claw[2])
        tokens = 3 * pressa + pressb
        total_cost += tokens

    return total_cost


if __name__ == "__main__":
    ic(solve(file))
