from functools import reduce
from math import gcd


def lowest_common_multiple(a, b):
    """
    calculate the lowest common multiple of two integer a and b
    :param a:
    :param b:
    :return:
    reference: https://stackoverflow.com/questions/19348430/project-euler-getting-smallest-multiple-in-python
    """
    # 两个数字相乘后除以最大公约数 = 两个数字的最小公倍数
    return a * b // gcd(a, b)


def smallest_multiple(n):
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    :param n:
    :return:
    """
    return reduce(lowest_common_multiple, range(1, n+1))


if __name__ == "__main__":
    print(smallest_multiple(20))
