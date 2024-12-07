from challenges.utils import get_puzzle_input, get_test_input
from itertools import pairwise


class ValidReport:
    def __init__(self, line: list[int]):
        self.line = line

    def is_valid(self) -> bool:
        if self._report_status():
            return True
        return self._problem_dampener()

    # deve ser reutilizada com argumentos diferentes sem alterar self.line
    def _report_status(self, new_line=None) -> bool:
        if new_line is None:
            new_line = self.line
        order = None
        for a, b in pairwise(new_line):
            delta = abs(a - b)
            if delta == 0 or delta > 3:
                return False
            if order is None:
                order = a < b
            elif order != (a < b):
                return False
        return True

    # para cada elemento da lista, remove ele e chama report_status
    def _problem_dampener(self) -> bool:
        for i in range(len(self.line)):
            new_line = self.line.copy()
            new_line.pop(i)
            if self._report_status(new_line):
                return True
        return False


def solve(input: str):
    safe_lines_count = 0

    for line in input.splitlines():
        validator = ValidReport([int(x) for x in line.split()])
        if validator.is_valid():
            safe_lines_count += 1
    return safe_lines_count


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))
