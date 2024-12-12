inp = """125 17"""
inp = """554735 45401 8434 0 188 7487525 77 7"""
from tqdm import tqdm


def solve(s: str) -> str:
    ns = []
    for n in s.split():
        if len(n) % 2 == 0:
            left = n[len(n) // 2 :]
            rigth = n[: len(n) // 2]
            if int(left) == 0:
                ns.append("0")
                ns.append(rigth)

            elif int(rigth) == 0:
                ns.append("0")
                ns.append(left)

            else:
                ns.append(str(int(left)))
                ns.append(str(int(rigth)))

        elif int(n) == 0:
            ns.append(str(1))
        else:
            ns.append(str(int(n) * 2024))
    return " ".join(ns)


for i in tqdm(range(25)):
    inp = solve(inp)

print(len(inp.split()))
