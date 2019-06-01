import re


def names_scores():
    """
    For example, when the list is sorted into alphab etical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
    is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714. :return:
    """
    ans = 0
    odom = list()
    with open("./pro22_names.txt", "r") as f:
        for line in f.readlines():
            # 正则匹配解决一切（txt 文件多行，分割去掉空串，去掉字符串两边的引号）
            # 多个列表可以用 '+' 合并为一个
            odom += re.findall('[A-Za-z0-9]+', line)
    for i, name in enumerate(sorted(odom)):
        ans += sum(ord(c) - ord('A') + 1 for c in name) * (i + 1)
    return str(ans)


if __name__ == "__main__":
    print(names_scores())
