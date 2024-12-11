import sys
from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def show_menu(
    day: int = typer.Option(None, help="Day of the challenge", prompt=False, show_default=False),
    part: int = typer.Option(None, help="Part of the challenge", prompt=False, show_default=False),
):
    """CLI for Advent of Code challenges."""
    typer.echo("Welcome to the Advent of Code 2024 CLI - Made by Levy Nunes")

    if day is None:
        day = typer.prompt("Enter the day of the challenge", type=int)
    if part is None:
        part = typer.prompt("Enter the part of the challenge", type=int)

    typer.echo("Enter the input for the challenge: (Press Enter twice to finish)")

    if not sys.stdin.isatty():
        input_entered = sys.stdin.read().strip()
    else:
        lines = []
        while True:
            line = typer.prompt("", default="", prompt_suffix="")
            if line == "":
                break
            lines.append(line)
        input_entered = "\n".join(lines) if lines else ""

    if not input_entered:
        try:
            input_path = Path(f"challenges/day{day}/puzzle_input.txt")
            input_entered = input_path.read_text()
        except FileNotFoundError:
            typer.echo(f"Error: Input file not found at {input_path}", err=True)
            raise typer.Exit(code=1)

    if part not in (1, 2):
        typer.echo("Error: Invalid part number. Please enter 1 or 2.", err=True)
        raise typer.Exit(code=1)

    part_str = "one" if part == 1 else "two"
    module_name = f"challenges.day{day}.part_{part_str}"

    try:
        solve = __import__(module_name, fromlist=["solve"]).solve
    except ModuleNotFoundError:
        typer.echo(f"Error: Module {module_name} not found.", err=True)
        raise typer.Exit(code=1)

    try:
        result = solve(input_entered)
        typer.echo(f"Result for day {day} part {part}: {result}")
    except Exception as e:
        typer.echo(f"Error while solving: {e}", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
