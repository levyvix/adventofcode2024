# from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import cycle

from pathos.multiprocessing import Pool

from challenges.utils import get_puzzle_input, get_test_input


def guards_original_path(guard_location, lines):
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
        if lines[guard_location[0] + current_direction[0]][guard_location[1] + current_direction[1]] == "#":
            next_direction = next(directions)
            current_direction = next_direction
        else:
            # keep moving in the current direction
            guard_location = (
                guard_location[0] + current_direction[0],
                guard_location[1] + current_direction[1],
            )
            locations.add(guard_location)
    print(len(locations))
    return list(locations)


def obstacle_loop(guard_location, lines):
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
    locations = []
    locations.append(guard_location)

    loop = False
    while True:
        # next move is out of bounds? break
        if (
            guard_location[0] + current_direction[0] < 0
            or guard_location[0] + current_direction[0] >= len(lines)
            or guard_location[1] + current_direction[1] < 0
            or guard_location[1] + current_direction[1] >= len(lines[0])
        ):
            break
        if lines[guard_location[0] + current_direction[0]][guard_location[1] + current_direction[1]] == "#":
            next_direction = next(directions)
            current_direction = next_direction
        else:
            # keep moving in the current direction
            previus_location = guard_location
            guard_location = (
                guard_location[0] + current_direction[0],
                guard_location[1] + current_direction[1],
            )
            next_location = guard_location

            # is he going in a direction that he has already been?
            # if tuple (previus_location, next_location) is in locations, one after another
            if previus_location in locations:
                try:
                    if locations[locations.index(previus_location) + 1] == next_location:
                        # he is going in a direction he has already been
                        loop = True
                        break
                except IndexError:
                    pass

            locations.append(guard_location)

    return loop


def solve(puzzle_input: str):
    lines = puzzle_input.splitlines()

    guard_location: tuple[int, int] = (0, 0)
    for i, line in enumerate(lines):
        for j in range(len(line)):
            if lines[i][j] == "^":
                guard_location = (i, j)

    print(guard_location)
    loops = 0
    # put a obstacle in every location the guard has been, minus the first one, because he is already there
    original_path = guards_original_path(guard_location, lines)
    list_of_new_lines = []
    for location in original_path:
        new_lines = lines.copy()
        # change the location to an obstacle
        new_line = list(new_lines[location[0]])
        new_line[location[1]] = "#"
        new_lines[location[0]] = "".join(new_line)
        list_of_new_lines.append(new_lines)

    with Pool() as pool:
        results = pool.starmap(obstacle_loop, [(guard_location, new) for new in list_of_new_lines])

    for result in results:
        if result:
            loops += 1
    return loops


if __name__ == "__main__":
    run_prod = True
    from time import time

    start_time = time()

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))

    print("time: ", time() - start_time)
