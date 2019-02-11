def palindrome(n):
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
    numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.
    :param n: two n-digit numbers
    :return: the largest palindrome
    reference: https://www.geeksforgeeks.org/largest-palindrome-product-two-n-digit-numbers/
    """
    # 左右对称 且 为两个三位数的乘积

    upper_limit = 0
    # Loop to calculate upper bound , largest number of n-digit
    for i in range(1, n + 1):
        upper_limit = upper_limit * 10
        upper_limit = upper_limit + 9

    # largest number of n-1 digit
    # one plus this number is lower limit which is product of two number
    lower_limit = 1 + upper_limit // 10

    max_product = 0  # Initialize result
    for i in range(upper_limit, lower_limit, -1):
        for j in range(i, lower_limit - 1, -1):
            # calculating product of two n-digit numbers
            product = i * j
            if product < max_product:
                break
            number = product

            # calculating reverse of product to check whether it is palindrome or not
            # reverse = 0
            # while number != 0:
            #    reverse = reverse * 10 + number % 10
            #    number = number // 10
            reverse = int(str(number)[::-1])

            # update new product if exist and if greater than previous one
            if product == reverse and product > max_product:
                max_product = product

    return max_product


if __name__ == "__main__":
    print(palindrome(3))
