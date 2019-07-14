# https://blog.dreamshire.com/project-euler-47/
def distinct_primes_factors(l, nf, ns):
    l += ns
    f = [0] * l
    c = 0
    for n in range(2, l):
        if f[n] == nf:
            c += 1
            if c - - ns:
                print(n - ns + 1)
                c -= 1
        else:
            c = 0
            if f[n] == 0:
                f[n::n] = [x + 1 for x in f[n::n]]
    return


if __name__ == "__main__":
    distinct_primes_factors(300000, 4, 4)
