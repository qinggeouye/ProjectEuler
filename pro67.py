def max_path_sum_ii():
    with open("./pro67_triangle.txt", "r") as f:  # 去掉换行符, 每行文本以空格分割出数字, 作为二维list的一行
        triangle = list(map(lambda x: list(map(int, x)), map(lambda x: x.strip().split(), f.readlines())))
    for i in reversed(range(len(triangle) - 1)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return str(triangle[0][0])


if __name__ == "__main__":
    print(max_path_sum_ii())
