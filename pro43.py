import itertools

divisor = [2, 3, 5, 7, 11, 13, 17]


def is_substring_divisibility(num):
    return all((num[i + 1] * 100 + num[i + 2] * 10 + num[i + 3]) % d == 0 for (i, d) in enumerate(divisor))


def sum_sub_string():
    return sum(int("".join(map(str, num))) for num in itertools.permutations(list(range(10)))
               if is_substring_divisibility(num))


if __name__ == "__main__":
    print(sum_sub_string())
