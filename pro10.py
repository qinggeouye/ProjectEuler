
def is_prime(n):
    k = 2
    while k <= n // 2:
        if n % k == 0:
            return False
        k = k + 1
    return True


def is_prime2(n):
    k = n // 2
    while k > 1:
        if n % k == 0:
            return False
        k = k - 1
    return True


def sum_primes(natural):
    """
    oh , you do not want this solution ...
    find the sum of all primes below two million
    :param natural:
    :return:
    """
    s = 2
    for n in range(3, natural + 1, 2):
        if is_prime(n):
            s += n
    return s


if __name__ == "__main__":
    print(sum_primes(10))
