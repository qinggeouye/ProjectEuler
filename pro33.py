import math


# there are exactly four non-trivial examples of this type of fractions,
# less than one in value, and containing two digits in the numerator adn denominator.
# if the product of these four fractions is given in its lowest common terms,
# find the value of the denominator
def digit_cancelling_fractions():
    num = 1
    den = 1
    for d in range(10, 100):
        for n in range(10, d):
            if (str(n)[1] == str(d)[0] and int(str(n)[0]) * d == n * int(str(d)[1])) or \
                    (str(n)[0] == str(d)[1] and int(str(n)[1]) * d == n * int(str(d)[0])):
                num *= n  # 分子乘积
                den *= d  # 分母乘积
    return den // math.gcd(num, den)  # 分母除以最大公约数，约分


if __name__ == "__main__":
    print(digit_cancelling_fractions())
