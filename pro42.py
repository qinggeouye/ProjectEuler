import math
import re
from functools import reduce


def is_triangle_number(n):
    return any(2 * n == x * (x + 1) for x in range(1, math.ceil(math.sqrt(2 * n))))


def coded_triangle_numbers():
    with open("./pro42_words.txt", "r") as f:
        words = reduce(lambda x, y: x + y, map(lambda line: re.findall("[A-Za-z0-9-_]+", line), f.readlines()))
    return sum(1 for i, word in enumerate(words) if is_triangle_number(sum(ord(c) - ord('A') + 1 for c in word)))


if __name__ == "__main__":
    print(coded_triangle_numbers())
