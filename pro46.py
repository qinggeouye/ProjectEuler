# Goldbach's other conjecture
def smallest_odd_composite():
    n = 5
    f = 1
    primes = set()
    while True:
        if all(n % p for p in primes):
            primes.add(n)
        else:
            if not any((n - 2 * i * i) in primes for i in range(1, n // 2 + 1)):
                break
        n += 3 - f
        f = -f
    return n


if __name__ == "__main__":
    print(smallest_odd_composite())

