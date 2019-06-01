def factorial(n):
    """
    n!
    :param n:
    :return:
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


def digit_sum(n):
    ans = sum(int(d) for d in str(factorial(n)))
    return str(ans)


if __name__ == "__main__":
    print(digit_sum(100))
