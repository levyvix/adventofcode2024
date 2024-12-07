from challenges.utils import get_puzzle_input, get_test_input
from loguru import logger


class VerificaXMAS:
    def __init__(self, x, y, lines) -> None:
        self.x = x
        self.y = y
        self.lines = lines

    @logger.catch
    def diagonal_direita(self):
        cima = self.lines[self.y - 1][self.x - 1]
        meio = self.lines[self.y][self.x]
        baixo = self.lines[self.y + 1][self.x + 1]

        palavra = f"{cima}{meio}{baixo}"
        if palavra == "SAM" or palavra == "MAS":
            return True

        return False

    @logger.catch
    def diagonal_esquerda(self):
        cima = self.lines[self.y - 1][self.x + 1]
        meio = self.lines[self.y][self.x]
        baixo = self.lines[self.y + 1][self.x - 1]

        palavra = f"{cima}{meio}{baixo}"
        if palavra == "SAM" or palavra == "MAS":
            return True
        return False

    def forma_xmas(self) -> bool:
        # tem que ter 1 em baixo e 1 em cima e 1 pra direita e 1 pra esquerda
        if (
            self.y - 1 < 0
            or self.y + 1 >= len(self.lines)
            or self.x - 1 < 0
            or self.x + 1 >= len(self.lines[0])
        ):
            return False

        if self.diagonal_direita() and self.diagonal_esquerda():
            return True

        return False

    def contagem_xmas(self):
        contagem = 0

        if self.forma_xmas():
            contagem += 1

        return contagem


def solve(input):
    lines = input.splitlines()
    xmas_found = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "A":
                verificaxmas = VerificaXMAS(x, y, lines)
                xmas_found += verificaxmas.contagem_xmas()

    return xmas_found


if __name__ == "__main__":
    run_prod = True

    if run_prod:
        puzzle_input_prod = get_puzzle_input(__file__)
        print("prod: ", solve(puzzle_input_prod))

    puzzle_input_test = get_test_input(__file__)
    print("test: ", solve(puzzle_input_test))
