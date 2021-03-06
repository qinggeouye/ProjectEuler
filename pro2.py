def fib(n):
    """
    递归有深度限制
    :param n:
    :return:
    """
    if n == 0 or n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


def fib2(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n = n - 1
    return b


def fib_sum(max_fib):
    """
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
    the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci
    sequence whose values do not exceed four million, find the sum of the even-valued terms.
    :param max_fib: four million
    :return: sum_fib
    """
    n, a, b = 0, 0, 1
    sum_fib = 0
    while b <= max_fib:
        a, b = b, a + b
        n = n + 1
        if b % 2 == 0:
            sum_fib = sum_fib + b
    return sum_fib


if __name__ == "__main__":
    print(fib(10))
    print(fib2(10))
    print(fib_sum(4000000))
