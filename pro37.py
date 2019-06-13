import itertools

import eulerlib


def is_truncatable_prime(n):
    # test if left-truncatable
    # i = 10
    # while i <= n:
    #     if not eulerlib.is_prime(n % i):
    #         return False
    #     i *= 10

    all(False for i in range(len(str(n)) + 1) if not eulerlib.is_prime(n % (10 ** i)))

    # test if right-truncatable
    while n > 0:
        if not eulerlib.is_prime(n):
            return False
        n //= 10

    return True


if __name__ == "__main__":
    print(is_truncatable_prime(15))
