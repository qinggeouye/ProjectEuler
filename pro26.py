import itertools


def compute():
    ans = max(range(1, 1000), key=reciprocal_cycle_len)
    return str(ans)


def reciprocal_cycle_len(n):
    """
    1/n
    :param n:
    :return: recurring cycle
    """
    seen = {}
    x = 1
    for i in itertools.count():
        if x in seen:  # 余数重复出现: recurring cycle , i 为出现的位置
            return i - seen[x]
        else:
            seen[x] = i  # 余数作为key 除第几次作为value
            x = x * 10 % n  # 取余数


if __name__ == "__main__":
    print(compute())

