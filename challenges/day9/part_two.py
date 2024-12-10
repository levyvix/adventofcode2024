from tqdm import tqdm
from collections import OrderedDict

from challenges.utils import get_puzzle_input, get_test_input


def remap_block(block: list[int], length_of_nums: dict[int, int]):
    new_block = block[:]

    # find all groups of empty spaces
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

    # order of decreasing ID
    for n, length in tqdm(reversed(length_of_nums.items()), desc="remapping", total=len(length_of_nums)):
        current_pos = new_block.index(n)

        # find the leftmost valid position
        best_pos = None
        for group in groups:
            if len(group) >= length:  # group is big enough
                if group[0] < current_pos:  # group is to the left
                    best_pos = group
                    break

        # if we found a valid position, move the file
        if best_pos:
            # clear the old position
            new_block[current_pos : current_pos + length] = [-1] * length

            # place in new position
            for i in range(length):
                new_block[best_pos[i]] = n

            # update the groups
            idx = groups.index(best_pos)
            groups[idx] = best_pos[length:]
            if not groups[idx]:  # remove empty group
                groups.pop(idx)

    return new_block


def solve(puzzle_input):
    blocks = []
    file_id = 0
    length_of_nums = OrderedDict()
    for i, char in enumerate(puzzle_input):
        length = int(char)
        if i % 2 == 0:  # file length
            blocks.extend([file_id] * length)
            length_of_nums[file_id] = length
            file_id += 1
        else:  # free space length
            blocks.extend([-1] * length)

    new_block = remap_block(blocks, length_of_nums)
    print(new_block)
    soma_total = 0
    for i, value in tqdm(enumerate(new_block)):
        if value < 0:
            continue
        soma_total += value * i

    return soma_total


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input))

    puzzle_input = get_test_input(__file__)
    print("test: ", solve(puzzle_input))
