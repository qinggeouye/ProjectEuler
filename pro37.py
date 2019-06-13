import itertools

import eulerlib


def is_truncatable_prime(n):
    # test if left-truncatable
    # i = 10
    # while i <= n:
    #     if not eulerlib.is_prime(n % i):
    #         return False
    #     i *= 10
    if any(not eulerlib.is_prime(n % (10 ** i)) for i in range(1, len(str(n)) + 1)):
        return False

    # test if right-truncatable
    # while n > 0:
    #     if not eulerlib.is_prime(n):
    #         return False
    #     n //= 10
    if any(not eulerlib.is_prime(n // (10 ** i)) for i in range(len(str(n)))):
        return False

    return True


def sum_truncatable_primes():
    return sum(itertools.islice(filter(is_truncatable_prime, itertools.count(10)), 11))


if __name__ == "__main__":
    print(sum_truncatable_primes())
