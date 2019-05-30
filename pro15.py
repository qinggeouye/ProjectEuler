import eulerlib


def compute(n):
    """
    how many such routes are there through a 20*20 grid ?
    combinatorics problem , binomial
    :param n:
    :return:
    """
    return str(eulerlib.numtheory.nCr(2*n, n))


if __name__ == "__main__":
    print(compute(20))

