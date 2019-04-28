def is_prime(n):
    k = 2
    while k <= n // 2:
        if n % k == 0:
            print("no")
            return False
        k = k + 1
    print("yes")
    return True


def is_prime2(n):
    k = n // 2
    while k > 1:
        if n % k == 0:
            return False
        k = k - 1
    return True


def prime_factor(num):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    reference: https://math.stackexchange.com/questions/389675/largest-prime-factor-of-600851475143
    :param num:
    :return:
    """
    factor, k = num, 2
    largest_factor = 2
    while factor >= k:
        if factor % k == 0:
            largest_factor = factor
            factor, k = factor//k, 2
        else:
            k = k + 1
    return largest_factor


if __name__ == "__main__":
    print(prime_factor(600851475143))
