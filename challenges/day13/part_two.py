import re
from pathlib import Path

from icecream import ic

file = (Path(__file__).parent / "puzzle_input.txt").read_text()

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
        prize[0] += 10**13
        prize[1] += 10**13
        claw.append(prize)

    if not line or i == len(file.splitlines()) - 1:
        claws.append(claw)
        claw = []
        continue

total = 0
for claw in claws:
    a, b, target = claw
    px = target[0]
    py = target[1]
    ax = a[0]
    ay = a[1]
    bx = b[0]
    by = b[1]

    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx
    if ca % 1 == 0 and cb % 1 == 0:
        ic(int(ca), int(cb), int(ca * 3 + cb))
        total += int(ca * 3 + cb)

ic(total)
