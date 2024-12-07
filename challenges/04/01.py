from challenges.utils import get_puzzle_input, get_test_input


class VerificaXMAS:
    def __init__(self, x, y, lines) -> None:
        self.x = x
        self.y = y
        self.lines = lines

    def diagonal_superior_esquerda(self) -> bool:
        """verifica se a diagonal superior esquerda forma a palavra XMAS"""

        if self.y - 3 < 0 or self.x - 3 < 0:
            return False
        try:
            return (
                "".join([self.lines[self.y - i][self.x - i] for i in range(4)])
                == "XMAS"
            )
        except IndexError:
            return False

    def diagonal_superior_direita(self) -> bool:
        """verifica se a diagonal superior direita forma a palavra XMAS"""

        # deve ter 3 linhas pra cima e 3 colunas pra direita

        if self.y - 3 < 0 or self.x + 3 > len(self.lines[0]):
            return False
        try:
            return (
                "".join([self.lines[self.y - i][self.x + i] for i in range(4)])
                == "XMAS"
            )
        except IndexError:
            return False

    def diagonal_inferior_esquerda(self) -> bool:
        """verifica se a diagonal inferior esquerda forma a palavra XMAS"""

        # deve ter 4 linhas pra baixo e 4 colunas pra esquerda
        if self.y + 3 > len(self.lines) or self.x - 3 < 0:
            return False
        try:
            return (
                "".join([self.lines[self.y + i][self.x - i] for i in range(4)])
                == "XMAS"
            )
        except IndexError:
            return False

    def diagonal_inferior_direita(self) -> bool:
        """verifica se a diagonal inferior direita forma a palavra XMAS"""
        # deve ter 3 linhas pra baixo e 3 colunas pra direita
        if self.y + 3 > len(self.lines) or self.x + 3 > len(self.lines[0]):
            return False
        try:
            return (
                "".join([self.lines[self.y + i][self.x + i] for i in range(4)])
                == "XMAS"
            )
        except IndexError:
            return False

    def vertical_cima(self) -> bool:
        """verifica se a vertical cima forma a palavra XMAS"""
        if self.y - 3 < 0:
            return False
        try:
            return "".join([self.lines[self.y - i][self.x] for i in range(4)]) == "XMAS"

        except IndexError:
            return False

    def vertical_baixo(self) -> bool:
        """verifica se a vertical baixo forma a palavra XMAS"""
        if self.y + 3 > len(self.lines):
            return False
        try:
            return (
                True
                if "".join(
                    list(
                        map(
                            lambda lista: lista[self.x], self.lines[self.y : self.y + 4]
                        )
                    )
                )
                == "XMAS"
                else False
            )
        except IndexError:
            return False

    def horizontal_esquerda(self) -> bool:
        """verifica se a horizontal esquerda forma a palavra XMAS"""
        if self.x - 3 < 0:
            return False

        return True if self.lines[self.y][self.x - 3 : self.x + 1] == "SAMX" else False

    def horizontal_direita(self) -> bool:
        """verifica se a horizontal direita forma a palavra XMAS"""
        if self.x + 3 > len(self.lines[0]):
            return False

        return True if self.lines[self.y][self.x : self.x + 4] == "XMAS" else False

    def contagem_xmas(self) -> int:
        """Verifica todas as condicoes e retorna a quantidade de vezes que a
        palavra XMAS aparece"""
        contagem = 0
        if self.horizontal_direita():
            contagem += 1
        if self.horizontal_esquerda():
            contagem += 1
        if self.vertical_baixo():
            contagem += 1
        if self.vertical_cima():
            contagem += 1
        if self.diagonal_inferior_direita():
            contagem += 1
        if self.diagonal_inferior_esquerda():
            contagem += 1
        if self.diagonal_superior_direita():
            contagem += 1
        if self.diagonal_superior_esquerda():
            contagem += 1
        return contagem


def solve(input):
    lines = input.splitlines()
    xmas_found = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "X":
                verificaxmas = VerificaXMAS(x, y, lines)
                xmas_found += verificaxmas.contagem_xmas()

    return xmas_found


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)
    # puzzle_input = get_test_input(__file__)
    print(solve(puzzle_input))
