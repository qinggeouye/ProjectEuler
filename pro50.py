import eulerlib


# too slow
def consecutive_prime_sum():
    ans = 0
    primes = eulerlib.prime_numbers.primes(999999)
    consecutive = 0
    for i, v in enumerate(primes):
        sum_ = v
        consecutive_tmp = 1
        for j, val in enumerate(primes[i + 1:]):
            sum_ += val
            consecutive_tmp += 1
            if sum_ >= primes[-1]:
                break
            # the sum of the most consecutive primes
            if sum_ in primes and consecutive_tmp > consecutive:
                ans = sum_
                consecutive = consecutive_tmp
    return str(ans)


if __name__ == "__main__":
    print(consecutive_prime_sum())
