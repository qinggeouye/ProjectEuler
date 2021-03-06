# https://blog.dreamshire.com/project-euler-47/
def distinct_primes_factors(lim, nf, ns):
    """
    find the first four consecutive integers to have four distinct prime factors
    :param lim: predefined limit digit
    :param nf: a number of distinct prime factors
    :param ns: the desired sequence length
    :return:
    """
    lim += ns
    f = [0] * lim
    c = 0  # counter
    for n in range(2, lim):  # n is the number, eg 644
        if f[n] == nf:
            c += 1  # increment a counter by 1
            if c == ns:
                print(n - ns + 1)
                c -= 1
        else:
            c = 0  # reset to zero
            if f[n] == 0:
                # eg：644 = (2x2) x 7 x 23, distinct prime factors are 2, 7, 23
                # sieving the number of distinct prime factors
                f[n::n] = [x + 1 for x in f[n::n]]
    return


if __name__ == "__main__":
    distinct_primes_factors(300000, 4, 4)
