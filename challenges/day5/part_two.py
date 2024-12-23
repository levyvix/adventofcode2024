from challenges.utils import get_puzzle_input, get_test_input


class Validator:
    def __init__(self, raw_input: str):
        self.puzzle_input = raw_input
        self.afters_before: dict[str, dict[str, list[str]]] = {}
        self.safe_pages: list[str] = []

    def build_hashmap(self):
        """Build hashmsp with all the pages and their orders"""
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

    def is_page_safe(self, page, befores, afters):
        """check if the page follow the hashmap rules"""
        checks_before = [p in self.afters_before[page]["before"] for p in afters]
        checks_after = [p in self.afters_before[page]["after"] for p in befores]

        if all(checks_before) and all(checks_after):
            return True
        return False

    def get_safe_pages(self):
        """
        Get all the safe pages and store them in safe_pages list.
        If a page is not safe, try to find the correct order
        """
        for line in self.puzzle_input.splitlines():
            if "|" in line or line == "":
                continue

            if not self.is_line_safe(line):
                safe_line = self.get_correct_order(line)
                if safe_line:
                    self.safe_pages.append(",".join(safe_line))

    def find_start_number(self, nums):
        # Find a number that has no "after" dependencies or has all its "after" dependencies outside the current line
        for num in nums:
            if not self.afters_before[num]["after"] or all(dep not in nums for dep in self.afters_before[num]["after"]):
                return num
        return None

    def get_correct_order(self, line: str) -> list | None:
        nums = line.split(",")
        result = []
        remaining = set(nums)

        while remaining:
            # Find the next number that can be added
            next_num = None
            for num in remaining:
                # Check if all required "after" numbers are already in result
                if all(after not in remaining for after in self.afters_before[num]["after"]):
                    # Check if all required "before" numbers are still in remaining or not in the line
                    if all(before in remaining or before not in nums for before in self.afters_before[num]["before"]):
                        next_num = num
                        break

            if next_num is None:
                return None  # No valid order found

            result.append(next_num)
            remaining.remove(next_num)

        return result

    def is_line_safe(self, line: str):
        checks: list[bool] = []
        for page in line.split(","):
            befores_raw, afters_raw = line.split(page)
            befores: list[str] = befores_raw.split(",")
            afters: list[str] = afters_raw.split(",")
            # remove empty strings
            befores = [x for x in befores if x != ""]
            afters = [x for x in afters if x != ""]

            page_is_safe = self.is_page_safe(
                page,
                befores,
                afters,
            )

            checks.append(page_is_safe)

        return all(checks)

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
