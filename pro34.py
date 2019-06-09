def factorial(n):
    # <=> math.factorial(n)
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_factorial_of_ten_digits():
    return sum(factorial(9) for i in range(1, 10))


def is_equal_factorial_sum(n):
    return sum(factorial(int(i)) for i in str(n)) == n


def sum_of_all_numbers(up_limit):
    return sum(i for i in range(3, up_limit + 1) if is_equal_factorial_sum(i))


if __name__ == "__main__":
    print(sum_of_all_numbers(sum_factorial_of_ten_digits()))
