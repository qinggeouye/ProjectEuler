
def difference_sum_squares(n):
    """
    :param n: the first n natural numbers
    :return: Find the difference between the sum of the squares of the first one hundred natural numbers
    and the square of the sum.
    """
    sum1 = 0
    sum2 = 0
    for i in range(1, n+1):
        sum1 += i**2
        sum2 += i
    sum2 = sum2**2
    return sum2 - sum1


if __name__ == "__main__":
    num = 100
    print(difference_sum_squares(num))

