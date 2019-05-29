import itertools
import math


def triangle_num(natural):
    """
    :param natural: 500
    :return: the value of the first triangle number to have over five hundred divisors
    """
    triangle = 0
    for i in itertools.count(1):
        # this is the ith triangle number, i.e. num = 1+2+...+i
        triangle += i
        if num_divisors(triangle) > natural:
            return str(triangle)


def num_divisors(n):
    end = math.floor(math.sqrt(n))
    # 2 means 1 and itself divisor
    result = sum(2 for i in range(1, end + 1) if n % i == 0)
    if end ** 2 == n:
        result -= 1
    return result


if __name__ == "__main__":
    print(triangle_num(500))
