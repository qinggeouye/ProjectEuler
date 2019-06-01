import itertools
import copy


def fac(n):
    if n <= 1:
        return 1
    return n * fac(n-1)


def lexicographic_permutations():
    """
    What is the millionth lexicographic permutation
    of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    :return:
    """
    ans = list()
    x = copy.copy(MILLIONTH)
    nums = copy.copy(NUMS)
    while nums:
        a = x // fac(len(nums) - 1)
        x = x % fac(len(nums) - 1)
        # 刚好整除 要退一位 不进位
        a = a - 1 if x == 0 else a
        ans.append(nums[a])
        nums.remove(nums[a])
    return ''.join(str(x) for x in ans)


NUMS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
MILLIONTH = 1000000


def compute():
    arr = list(range(len(NUMS)))
    temp = itertools.islice(itertools.permutations(arr), MILLIONTH - 1, None)
    return "".join(str(x) for x in next(temp))


if __name__ == "__main__":
    print(lexicographic_permutations())
    print(compute())

