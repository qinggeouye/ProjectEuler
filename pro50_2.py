# https://blog.dreamshire.com/project-euler-50-solution/
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5  # prime: 2 3 5 7 11 13 ...
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True


def prime_sieve(n):
    sieve = [True] * int(n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * (int((n - i * i - 1) // (2 * i)) + 1)
    return [2] + [2 * i + 1 for i in range(1, int(n // 2)) if sieve[i]]


def consecutive_sum_primes():
    l = 1000000
    prime_sum = [0]
    for p in prime_sieve(l / 100):
        prime_sum.append(prime_sum[-1] + p)
        if prime_sum[-1] >= l:
            break
    c = len(prime_sum)

    terms = 1
    max_prime = 0
    for i in range(c):
        for j in range(c - 1, i + terms, -1):
            n = prime_sum[j] - prime_sum[i]
            if j - i > terms and is_prime(n):
                terms, max_prime = j - i, n
                break
    print("Project Euler 50 Solution = ", max_prime, " with ", terms, " terms")


if __name__ == "__main__":
    consecutive_sum_primes()
