def is_pan_digital(n, s=9):
    return len(n) == s and not '1234567890'[:s].strip(n)


# 1 到 9 的 9 位数字，被乘数、乘数、积，可能情况只有：
# 1位 x 4位 = 4位
# 2位 x 3位 = 4位
def compute():
    p = set()
    for i in range(2, 60):  # 被乘数
        start = 1234 if i < 10 else 123
        for j in range(start, 10000 // i):  # 乘数，且乘积不能超出4位数字
            if is_pan_digital(str(i) + str(j) + str(i * j)):
                p.add(i * j)
                print('%s*%s=%s' % (i, j, i * j))
    return sum(p)


if __name__ == "__main__":
    print(compute())
