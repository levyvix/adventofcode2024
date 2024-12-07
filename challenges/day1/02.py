from collections import Counter
from challenges.utils import get_test_input, get_puzzle_input


class Solver:
    def __init__(self, input: str):
        self.input = input
        self.input = self._format_input()
        self.numbers_left = []
        self.numbers_right = []

    def _format_input(self) -> list[str]:
        return self.input.splitlines()

    def _get_two_lists(self) -> None:
        for line in self.input:
            line = line.strip()
            if line:
                number_a, number_b = line.split("  ")
                self.numbers_left.append(int(number_a))
                self.numbers_right.append(int(number_b))

    def _count_appearances(self) -> int:
        counter_b = Counter(self.numbers_right)

        total_sum = 0

        for left_number in self.numbers_left:
            right_count = counter_b.get(left_number, 0)
            total_sum += left_number * right_count

        return total_sum

    def solve(self) -> int:
        self._get_two_lists()
        return self._count_appearances()


def solve(input):
    solver = Solver(input)
    return solver.solve()


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))
