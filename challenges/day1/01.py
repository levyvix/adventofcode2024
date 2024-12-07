from typing import List, Tuple, Generator
from challenges.utils import get_test_input, get_puzzle_input


class Solver:
    """Solver for calculating the sum of differences between paired numbers."""

    def __init__(self, input_data: str) -> None:
        """Initialize the solver with input data.

        Args:
            input_data: Raw input string containing pairs of numbers
        """
        self.lines = self._format_input(input_data)
        self.first_numbers: List[int] = []
        self.second_numbers: List[int] = []

    def _format_input(self, input_data: str) -> List[str]:
        """Format the raw input into lines.

        Args:
            input_data: Raw input string

        Returns:
            List of strings, each containing a pair of numbers
        """
        return input_data.splitlines()

    def _parse_number_pairs(self) -> None:
        """Parse and store pairs of numbers from each line."""
        for line in self.lines:
            line = line.strip()
            if not line:
                continue

            try:
                number_a, number_b = line.split("  ")
                self.first_numbers.append(int(number_a))
                self.second_numbers.append(int(number_b))
            except ValueError as e:
                raise ValueError(
                    f"Invalid line format: {line}. Expected two numbers separated by two spaces."
                ) from e

    def _sort_number_lists(self) -> None:
        """Sort both lists of numbers in ascending order."""
        self.first_numbers.sort()
        self.second_numbers.sort()

    def _get_paired_numbers(self) -> Generator[Tuple[int, int], None, None]:
        """Create pairs of numbers from the sorted lists.

        Returns:
            Generator of tuples containing paired numbers
        """
        return zip(self.first_numbers, self.second_numbers)

    def _calculate_total_difference(self) -> int:
        """Calculate the sum of absolute differences between paired numbers.

        Returns:
            Total sum of differences
        """
        return sum(abs(b - a) for a, b in self._get_paired_numbers())

    def solve(self) -> int:
        """Solve the puzzle by calculating the total difference.

        Returns:
            Total difference between paired numbers
        """
        self._parse_number_pairs()
        self._sort_number_lists()
        return self._calculate_total_difference()


def solve(input_data: str) -> int:
    """Main solving function.

    Args:
        input_data: Raw input string containing pairs of numbers

    Returns:
        Solution to the puzzle
    """
    solver = Solver(input_data)
    return solver.solve()


if __name__ == "__main__":
    RUN_PRODUCTION = True

    if RUN_PRODUCTION:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("Production result:", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("Test result:", solve(puzzle_input_test))
