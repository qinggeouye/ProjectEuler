import eulerlib
import itertools


def count_consecutive_primes(ab):
    a, b = ab
    for i in itertools.count():
        n = i * i + i * a + b
        if n < 0:
            return i
        elif not eulerlib.is_prime(n):
            return i


def quadratic_primes():
    # produces the maximum number of primes
    ans = max(((a, b) for a in range(-999, 1000) for b in range(2, 1000)),
              key=count_consecutive_primes)
    return str(ans[0] * ans[1])


if __name__ == "__main__":
    print(quadratic_primes())
