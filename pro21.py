def divisor_sum(n):
    ans = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            ans += i
    return ans


def amicable_numbers(n):
    """

    :param n:
    :return:
    """
    ans = 0
    visited = list()
    for i in range(2, n + 1):
        if i not in visited:
            visited.append(i)
            amicable1 = divisor_sum(i)
            amicable2 = divisor_sum(amicable1)
            if amicable2 == i and amicable2 != amicable1:
                ans += amicable1 + amicable2
                visited.append(amicable1)
    return str(ans)


if __name__ == "__main__":
    print(amicable_numbers(10000))
