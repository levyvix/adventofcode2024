from typing import List

from loguru import logger

from challenges.utils import get_puzzle_input, get_test_input


class Validator:
    def __init__(self, raw_input: str):
        self.puzzle_input = raw_input
        self.afters_before: dict[str, dict[str, List[str]]] = {}
        self.safe_pages: list[str] = []
        self.middle_numbers: list[int] = []

    def build_hashmap(self):
        for line in self.puzzle_input.splitlines():
            if "," in line or line == "":
                break
            left, right = line.split("|")
            left = left.strip()
            right = right.strip()

            # if number not exist, initialize with two empty lists
            if left not in self.afters_before:
                self.afters_before[left] = {"before": [], "after": []}
            if right not in self.afters_before:
                self.afters_before[right] = {"before": [], "after": []}

            self.afters_before[left]["before"].append(right)
            self.afters_before[right]["after"].append(left)

    def get_safe_pages(self):
        for line in self.puzzle_input.splitlines():
            if "|" in line or line == "":
                continue

            checks = 0
            for page in line.strip().split(","):
                befores, afters = line.split(page)
                befores = befores.strip().split(",")
                # remove empty strings
                befores = [x for x in befores if x != ""]
                afters = afters.strip().split(",")
                # remove empty strings
                afters = [x for x in afters if x != ""]

                checks_before = [p in self.afters_before[page]["before"] for p in afters]
                checks_after = [p in self.afters_before[page]["after"] for p in befores]

                if all(checks_before) and all(checks_after):
                    checks += 1
                else:
                    break

            if checks == len(line.strip().split(",")):
                self.safe_pages.append(line.strip())

    def get_middle_numbers(self):
        middle_numbers = 0
        for page in self.safe_pages:
            all_numbers = [int(x) for x in page.split(",")]
            middle_numbers += all_numbers[len(all_numbers) // 2]

        return middle_numbers

    def validate(self):
        self.build_hashmap()
        self.get_safe_pages()
        return self.get_middle_numbers()


def solve(puzzle_input: str):
    validator = Validator(puzzle_input)
    return validator.validate()


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))
