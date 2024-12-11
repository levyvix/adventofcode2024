#!/usr/bin/python3

import re

# simple recursive solution
# target contains the target value
# values contains the values we need to use operators (+ or *) to combine
# part2 is a boolean that allows the concatenation operator
# If only one value left, no more operators -- compare and exit
# our input has no zeroes or negatives, so this is monotonic
# that means we can bail early if we overshoot the target


def solution(target, values, part2=False):
    if len(values) == 1:
        if target == values[0]:
            return True
        return False
    if values[0] > target:
        return False

    # try multiply
    if solution(target, [values[0] * values[1]] + values[2:], part2):
        return True
    # try add
    if solution(target, [values[0] + values[1]] + values[2:], part2):
        return True
    # try concatenation if allowed
    if part2 and solution(target, [int(str(values[0]) + str(values[1]))] + values[2:], part2):
        return True
    return False


with open("puzzle_input.txt") as f:
    lines = f.read().rstrip("\n").split("\n")

# doing part 1 and part two at the same time
part1 = part2 = 0
for line in lines:
    n = [int(x) for x in re.split(":? ", line)]
    if solution(n[0], n[1:]):
        part1 += n[0]
        part2 += n[0]
    else:
        if solution(n[0], n[1:], True):
            part2 += n[0]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
