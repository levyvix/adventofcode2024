from itertools import chain

from tqdm import tqdm

from challenges.utils import get_puzzle_input, get_test_input


def remap_block(block: list[str | int]):
    new_block = block[:]

    for old_pos, value in tqdm(reversed(list(enumerate(block))), desc="remapping", total=len(block)):
        if value == ".":
            continue

        for dot_pos, n_value in enumerate(new_block):
            if n_value == "." and any(x != "." for x in new_block[dot_pos:]):
                new_block[old_pos], new_block[dot_pos] = ".", value
                break
        else:
            return new_block


def solve(puzzle_input):
    final_block = []
    for line in puzzle_input.splitlines():
        i = 0
        for j, char in enumerate(line):
            if j % 2 == 0:
                final_block.append([i] * int(char))
                i += 1
            else:
                final_block.append("." * int(char))

    final_block = list(chain(*final_block))
    new_block = remap_block(final_block)

    soma_total = 0
    for i, value in tqdm(enumerate(new_block)):
        if value == ".":
            break
        soma_total += int(value) * i

    return soma_total


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input))

    puzzle_input = get_test_input(__file__)
    print("test: ", solve(puzzle_input))
