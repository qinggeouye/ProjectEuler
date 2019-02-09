def multiples_3_5(n):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
    multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
    :param n: n = 10
    :return: sum = 23
    """
    sum_multi = 0
    while n > 0:
        n = n - 1
        if n % 3 == 0 or n % 5 == 0:
            sum_multi = sum_multi + n
    print(sum_multi)


def multiples_3_5_recruit(n):
    """
    递归层数有限制，数字 n 不宜过大
    :param n:
    :return:
    """
    n = n-1
    if n == 0:
        return 0
    if n % 3 == 0 or n % 5 == 0:
        return n + multiples_3_5_recruit(n)
    else:
        return multiples_3_5_recruit(n)


if __name__ == "__main__":
    multiples_3_5(1000)
    print(multiples_3_5_recruit(10))
