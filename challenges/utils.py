from pathlib import Path


def get_puzzle_input(current_file=__file__):
    return (Path(current_file).parent / "puzzle_input.txt").read_text()


def get_test_input(current_file=__file__):
    return (Path(current_file).parent / "test_input.txt").read_text()
