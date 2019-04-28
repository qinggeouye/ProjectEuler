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


def find_any_prime(n):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    从第一个素数 2 开始，找到第 n 个素数为止
    :param n: 第 n 个素数
    :return:
    """
    k = 1
    num = 1  # 2 是一个素数，num 从 1 开始计数
    while num != n:
        k += 2  # 2 之后的偶数不可能是素数
        if is_prime(k):
            num += 1
    return k


if __name__ == "__main__":
    print(find_any_prime(10001))
