# Pn = n(3n-1)/2, 找到 Pi + Pj 与 Pj - Pi 均属于 Pentagon number，且 Pj - Pi 最小的那一种情况
def pentagon_number():
    """
    s is the sum Pk + Pj
    Pj is, well, Pj
    s-Pj is Pk
    D is s-2*Pj which is simplified from (s-Pj)-Pj
    """
    ps = set()
    i = 1
    while True:
        i += 1
        s = (3 * i * i - i) // 2
        ps.add(s)
        for pj in ps:
            if s - pj in ps and s - 2 * pj in ps:
                return s - 2 * pj


if __name__ == "__main__":
    print(pentagon_number())
