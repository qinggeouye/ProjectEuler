coins = [1, 2, 5, 10, 20, 50, 100, 200]
sums = 200
count = list([0])


# recruit is too slow, not recommended!
# 排列（有顺序），递归层数太多!
def coin_sums(total):
    if total == 0:
        count[0] += 1
        return
    elif total < 0:
        return
    else:
        for coin in coins:
            coin_sums(total - coin)


if __name__ == "__main__":
    coin_sums(sums)
    print(count[0])
