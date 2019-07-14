def is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f < r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True


def prime_permutations():
    n, f = 1487, 1
    while n < 10000:
        n += 3 - f  # generates prime candidates faster than checking odd numbers
        f = -f
        b, c = n + 3330, n + 6660
        if is_prime(n) and is_prime(b) and is_prime(c) and is_perm(n, b) and is_perm(b, c):
            return str(n) + str(b) + str(c)
    raise RuntimeError("not found")


if __name__ == "__main__":
    print(prime_permutations())
