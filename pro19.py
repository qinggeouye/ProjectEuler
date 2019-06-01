import datetime


def counting_sundays():
    """
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    每月 1 日是周日的有几个？
    :return:
    """
    ans = sum(1
              for y in range(1901, 2001)
              for m in range(1, 13)
              if datetime.date(y, m, 1).weekday() == 6)
    return str(ans)


if __name__ == "__main__":
    print(counting_sundays())
