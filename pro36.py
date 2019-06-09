def is_decimal_binary_palindromic(n):
    s = str(n)
    if s == s[::-1]:
        t = bin(n)[2:]
        return t == t[::-1]
    else:
        return False


def sum_all_numbers(n):
    return str(sum(i for i in range(n) if is_decimal_binary_palindromic(i)))


if __name__ == "__main__":
    print(sum_all_numbers(1000000))
