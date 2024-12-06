from challenges.utils import get_puzzle_input, get_test_input


def solve(input):
    numbers_left = []
    numbers_right = []

    # Split the input by lines and process
    for line in input.split("\n"):
        line = line.strip()  # Clean up any trailing or leading spaces
        if line:
            number_a, number_b = line.split(
                "  "
            )  # Assuming two spaces as the delimiter
            numbers_left.append(int(number_a))
            numbers_right.append(int(number_b))

    # Sort the lists
    numbers_left.sort()
    numbers_right.sort()

    # Pair up the numbers and sum the differences
    total_distance = sum(abs(b - a) for a, b in zip(numbers_left, numbers_right))

    return total_distance


if __name__ == "__main__":
    # puzzle_input = get_puzzle_input(__file__)
    puzzle_input = get_test_input(__file__)  # Uncomment for testing
    print(solve(puzzle_input))
