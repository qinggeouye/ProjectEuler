

def number_spiral_diagonals(n):
    # 左上对角线 右上对角线 右下岁角线 左下岁角线
    ans = sum((i**2 - (i-1)) + (i**2) + ((i-1)**2-(i-2)) + ((i-1)**2+1) for i in range(1, n+1, 2))
    return str(ans - 1*3)


if  __name__ == "__main__":
    print(number_spiral_diagonals(1001))

