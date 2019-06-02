def fib_num(n):
    """
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
    :param n:
    :return:
    """
    index, a, b = 2, 1, 1
    while len(str(b)) < n:
        index += 1
        a, b = b, a + b
    return index, b


if __name__ == "__main__":
    print(fib_num(1000))
