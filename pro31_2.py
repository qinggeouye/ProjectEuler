

def coin_sums(total):

    ways = [1] + [0] * total
    # ways[i] 总额为 i 时，所有硬币的组合（不考虑顺序）
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        for i in range(len(ways) - coin): # 下标相差 coin
            ways[i + coin] += ways[i]  # 下标相差 coin
    return str(ways[-1])


if __name__ == "__main__":
    print(coin_sums(200))
