from functools import reduce
from operator import mul


def champernowne_constant():
    s = "".join(str(i) for i in range(1, 1000000))
    ans = reduce(mul, [int(s[10 ** i - 1]) for i in range(7)])
    return str(ans)


if __name__ == "__main__":
    print(champernowne_constant())
