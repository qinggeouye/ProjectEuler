
def pythagorean_triplet(perimeter):
    """
    毕达哥拉斯三角恒等式（勾股定理）
    a < b < c
    a**2 + b**2 = c**2
    perimeter = a + b + c > a + b + b => b < (perimeter - a)//2
    :param perimeter: 周长
    :return: a*b*c
    """
    for a in range(1, perimeter + 1):
        for b in range(a + 1, (perimeter - a)//2 + 1):
            c = perimeter - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return str(a * b * c)


if __name__ == "__main__":
    print(pythagorean_triplet(1000))
