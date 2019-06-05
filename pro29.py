

def distinct_powers(k, s):
    ans = set(a**b for a in range(2, k+1) for b in range(2, s+1))
    return str(len(ans))


if __name__ == "__main__":
    print(distinct_powers(100, 100))

