import eulerlib

is_prime = list(map(str, eulerlib.prime_numbers.primes(999999)))  # int to str


def is_circular_prime(s):
    return all(s[i:] + s[:i] in is_prime for i in range(len(s)))


def count():
    ans = sum(1 for i in range(len(is_prime)) if is_circular_prime(is_prime[i]))
    return str(ans)


# second method 第二种计算
is_prime_tmp = list(map(str, eulerlib.prime_numbers.primes(999999)))


def is_circular_prime2(s):
    return all(s[i:] + s[:i] in is_prime_tmp for i in range(len(s)))


def count2():
    ans = 0
    while len(is_prime_tmp):
        s_ = is_prime_tmp[0]
        if is_circular_prime2(s_):
            for i in range(len(s_)):
                if s_[i:] + s_[:i] in is_prime_tmp:
                    is_prime_tmp.remove(s_[i:] + s_[:i])
                    ans += 1
        else:
            [is_prime_tmp.remove(s_[i:] + s_[:i]) for i in range(len(s_)) if s_[i:] + s_[:i] in is_prime_tmp]

    return str(ans)


if __name__ == "__main__":
    # print(count())
    print(count2())
