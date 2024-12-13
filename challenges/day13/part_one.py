import re
from pathlib import Path

from icecream import ic
from pulp import LpConstraint, LpMinimize, LpProblem, LpSolverDefault, LpVariable, lpSum, value

LpSolverDefault.msg = False

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
        claw.append(prize)

    if not line or i == len(file.splitlines()) - 1:
        claws.append(claw)
        claw = []
        continue


def determine_a_b(a: list[int], b: list[int], target: list[int]):
    # Criação do problema de minimização
    prob = LpProblem("ClawMachine", LpMinimize)

    # Variáveis de decisão (inteiras)
    x = LpVariable("ButtonA", lowBound=0, cat="Integer")
    y = LpVariable("ButtonB", lowBound=0, cat="Integer")

    # Função objetivo: minimizar o custo total
    prob += 3 * x + y

    # Restrições
    # prob += a[0] * x + b[0] * y == target[0]  # X constraint
    prob += LpConstraint(a[0] * x + b[0] * y, sense=0, rhs=target[0])  # X constraint
    # prob += a[1] * x + b[1] * y == target[1]  # Y constraint
    prob += LpConstraint(a[1] * x + b[1] * y, sense=0, rhs=target[1])  # Y constraint

    # the button cant be pressed more than 100 times
    prob += x <= 100
    prob += y <= 100

    # solve
    prob.solve()

    if prob.objective.value() % 1 == 0:
        return int(x.value()), int(value(y)), int(prob.objective.value())
    else:
        return int(x.value()), int(value(y)), 0


total_cost = 0
for claw in claws:
    x, y, cost = determine_a_b(claw[0], claw[1], claw[2])
    if cost:
        total_cost += cost
    # print(f"Button A presses: {x}, Button B presses: {y}, Total Cost: {cost}")

# print(f"Total cost for all claws: {total_cost}")
ic(total_cost)
