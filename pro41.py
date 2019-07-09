import eulerlib


# https://en.wikipedia.org/wiki/Divisibility_rule#Divisibility_by_3_or_9
# 数字之和能被 3 整除，那么由这些数字组成的数就能被 3 整除，这个数就不是素数。
# the largest n-digit pandigital prime  srats with 7654321


def is_pan_digital(n, s=9):
    n = str(n)
    return len(n) == s and not '1234567890'[:s].strip(n)


def largest_pan_digital_prime():
    n = 7654321
    while not (is_pan_digital(n, 7) and eulerlib.is_prime(n)):
        n -= 2
    return str(n)


if __name__ == "__main__":
    print(largest_pan_digital_prime())
