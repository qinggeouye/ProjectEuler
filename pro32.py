def is_pan_digital(n, s=9):
    return len(n) == s and not '1234567890'[:s].strip(n)


def compute():
    p = set()
    for i in range(2, 60):
        start = 1234 if i < 10 else 123
        for j in range(start, 10000 // i):
            if is_pan_digital(str(i) + str(j) + str(i * j)):
                p.add(i * j)
    return sum(p)


if __name__ == "__main__":
    print(compute())
