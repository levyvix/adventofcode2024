from itertools import cycle

from challenges.utils import get_puzzle_input, get_test_input


def solve(puzzle_input: str):
    lines = puzzle_input.splitlines()

    guard_location = (0, 0)
    for i, line in enumerate(lines):
        for j in range(len(line)):
            if lines[i][j] == "^":
                guard_location = (i, j)

    print(guard_location)

    directions = cycle(
        [
            (-1, 0),  # up
            (0, 1),  # right
            (1, 0),  # down
            (0, -1),  # left
        ]
    )

    current_direction = next(directions)  # up

    # need to keep track of every location the guard was
    locations = set()
    locations.add(guard_location)

    while True:
        # next move is out of bounds? break
        if (
            guard_location[0] + current_direction[0] < 0
            or guard_location[0] + current_direction[0] >= len(lines)
            or guard_location[1] + current_direction[1] < 0
            or guard_location[1] + current_direction[1] >= len(lines[0])
        ):
            break
        if (
            lines[guard_location[0] + current_direction[0]][
                guard_location[1] + current_direction[1]
            ]
            == "#"
        ):
            next_direction = next(directions)
            current_direction = next_direction
        else:
            # keep moving in the current direction
            guard_location = (
                guard_location[0] + current_direction[0],
                guard_location[1] + current_direction[1],
            )
            locations.add(guard_location)

    return len(locations)


if __name__ == "__main__":
    run_prod = False

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))
