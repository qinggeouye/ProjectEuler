import eulerlib


def compute():
    lim = 10000
    for base in range(1489, lim, 2):
        if eulerlib.is_prime(base):
            a = base + 3330
            b = a + 3330
            if b < lim and eulerlib.is_prime(a) and is_perm(a, base) \
                    and eulerlib.is_prime(b) and is_perm(b, base):
                return str(base) + str(a) + str(b)
    raise RuntimeError("Not found")


def is_perm(x, y):
    return sorted(str(x)) == sorted(str(y))


if __name__ == "__main__":
    print(compute())
