from tqdm import tqdm

from challenges.utils import get_puzzle_input, get_test_input


def solve(puzzle_input):
    # Parse the disk map into blocks
    blocks = []
    file_id = 0
    for i, char in enumerate(puzzle_input):
        length = int(char)
        if i % 2 == 0:  # File length
            blocks.extend([file_id] * length)
            file_id += 1
        else:  # Free space length
            blocks.extend(["."] * length)

    # Compact the disk map
    left = 0
    n_nums = sum(1 for x in blocks if x != ".")
    for right in tqdm(range(len(blocks) - 1, 0, -1), desc="compact", total=n_nums):
        if blocks[right] != ".":
            blocks[blocks.index(".")], blocks[right] = blocks[right], "."
            left += 1

        if right == n_nums:
            break

    # Calculate the checksum
    checksum = sum(i * block for i, block in enumerate(blocks) if block != ".")

    return checksum


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input))

    puzzle_input = get_test_input(__file__)
    print("test: ", solve(puzzle_input))
