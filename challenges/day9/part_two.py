from itertools import chain

from tqdm import tqdm
from collections import OrderedDict

from challenges.utils import get_puzzle_input, get_test_input


def remap_block(block: list[int], length_of_nums: dict[int, int]):
    new_block = block[:]

    # Find all groups of empty spaces
    groups: list[list[int]] = []
    current_group: list[int] = []

    for i, value in enumerate(block):
        if value == -1:
            current_group.append(i)
        elif current_group:
            groups.append(current_group)
            current_group = []

    if current_group:
        groups.append(current_group)

    # Process files in order of decreasing ID
    for n, length in tqdm(reversed(length_of_nums.items()), desc="remapping", total=len(length_of_nums)):
        current_pos = new_block.index(n)

        # Find the leftmost valid position
        best_pos = None
        for group in groups:
            if len(group) >= length:  # Group is big enough
                if group[0] < current_pos:  # Group is to the left
                    best_pos = group
                    break

        # If we found a valid position, move the file
        if best_pos:
            # Clear the old position
            new_block[current_pos : current_pos + length] = [-1] * length

            # Place in new position
            for i in range(length):
                new_block[best_pos[i]] = n

            # Update the groups
            idx = groups.index(best_pos)
            groups[idx] = best_pos[length:]
            if not groups[idx]:  # Remove empty group
                groups.pop(idx)

    return new_block


def solve(puzzle_input):
    final_block = []
    length_of_nums = OrderedDict()
    for line in puzzle_input.splitlines():
        i = 0
        for j, char in enumerate(line):
            if j % 2 == 0:
                final_block.append([i] * int(char))
                length_of_nums[i] = int(char)
                i += 1
            else:
                final_block.append([-1] * int(char))

    final_block = list(chain(*final_block))
    new_block = remap_block(final_block, length_of_nums)
    print(new_block)
    soma_total = 0
    for i, value in tqdm(enumerate(new_block)):
        if value < 0:
            continue
        soma_total += int(value) * i

    return soma_total


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input))

    puzzle_input = get_test_input(__file__)
    print("test: ", solve(puzzle_input))
