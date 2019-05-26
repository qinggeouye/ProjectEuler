import eulerlib


def sum_primes(natural):
    """
    find the sum of all primes below two million
    :param natural:
    :return:
    """
    # https://pythonhosted.org/eulerlib/eulerlib.html
    ans = sum(eulerlib.prime_numbers.primes(natural))
    return str(ans)


if __name__ == "__main__":
    print(sum_primes(2000000))
