
def self_powers(n, k):
    """
    find the last ten digits of the series 1**1 + 2**2 + 3**3 + ... + 1000**1000
    :param n: n**n
    :param k: the last k digits
    :return:
    """
    mod = 10 ** k
    # 余数求和，对 10 的 k 次幂再求余，余数即为最后 k 位数字
    ans = sum(pow(i, i, mod) for i in range(1, n + 1)) % mod
    return str(ans)


if __name__ == "__main__":
    print(self_powers(1000, 10))
