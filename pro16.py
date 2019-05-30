

def power_digit_sum(n):
    """
    what is sum of the digits is 3+2+7+6+8=26
    :param n:
    :return:
    """
    ans = sum(int(c) for c in str(n))
    return str(ans)


if __name__ == "__main__":
    print(power_digit_sum(2**1000))

