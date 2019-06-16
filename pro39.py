# for which value of p<=1000, is the number of solutions maximised?
def integer_right_triangles(p):
    # method 1
    # count = 0
    # for a in range(1, p//2 + 1):
    #     for b in range(a, (p - a) // 2 + 1):
    #         if a ** 2 + b ** 2 == (p - a - b) ** 2:
    #             count += 1

    # method 2
    # a < b + c = p - a
    count = sum(1 for a in range(1, p // 2 + 1) for b in range(a, (p-a)//2 + 1) if a**2 + b**2 == (p - a - b) ** 2)

    return count


def result():
    ans = max(range(1, 1001), key=integer_right_triangles)
    return str(ans)


if __name__ == "__main__":
    print(result())
