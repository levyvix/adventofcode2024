from pathlib import Path


def get_puzzle_input(current_file=__file__):
    with open(Path(current_file).parent / "puzzle_input.txt", "r") as f:
        return f.read()


def get_test_input(current_file=__file__):
    with open(Path(current_file).parent / "test_input.txt", "r") as f:
        return f.read()
