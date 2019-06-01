LIMIT = 28124


def non_abundant_sums():
    """
    find the sum of all the positive integers
    which cannot be written as the sum of two abundant numbers.
    :return:
    """
    # the sum of divisors of every number
    divisor_sum = [0] * LIMIT
    for i in range(1, LIMIT):
        for j in range(i * 2, LIMIT, i):
            divisor_sum[j] += i
    # abundant numbers
    abundant_nums = [i for (i, x) in enumerate(divisor_sum) if x > i]

    expressible = [False] * LIMIT
    for i in abundant_nums:
        for j in abundant_nums:
            if i + j < LIMIT:
                expressible[i + j] = True
            else:
                break
    ans = sum(i for (i, x) in enumerate(expressible) if not x)
    return str(ans)


if __name__ == "__main__":
    print(non_abundant_sums())
