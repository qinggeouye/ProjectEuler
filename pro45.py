# find the next triangle number that is also pentagonal and hexagonal
def triangular_pentagonal_hexagonal():
    t = 286
    p = 166
    h = 144
    while True:
        triangle = t * (t + 1) // 2
        pentagonal = p * (3 * p - 1) // 2
        hexagnoal = h * (2 * h - 1)
        min_num = min(triangle, pentagonal, hexagnoal)
        max_num = max(triangle, pentagonal, hexagnoal)
        if min_num == max_num:
            return str(triangle)
        if min_num == triangle:
            t += 1
        if min_num == pentagonal:
            p += 1
        if min_num == hexagnoal:
            h += 1


if __name__ == "__main__":
    print(triangular_pentagonal_hexagonal())
