# https://blog.dreamshire.com/project-euler-38-solution/
def is_pan_digital(n, s=9):
    n = str(n)
    return len(n) == s and not '1234567890'[:s].strip(n)


def pan_digital_multiples():
    # The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
    # giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
    for n in range(9876, 9213, -1):
        p = str(n * 1) + str(n * 2)
        if is_pan_digital(p):
            return p
    return "None found"


if __name__ == "__main__":
    print(pan_digital_multiples())
