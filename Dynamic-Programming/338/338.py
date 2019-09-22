def countBits(num):
    """
    The number of 1s in num is the corresponding number of num - 2**int(log2(num)) + 1
    :param num:
    :return:
    """

    import math

    dp = [0] * (num + 1)

    dp[0] = 0
    dp[1] = 1
    dp[2] = 1

    for i in range(3, num + 1):

        low_level = 2 ** math.floor(math.log2(i))
        dp[i] = dp[i - low_level] + 1

    return dp

def countBits2(num):

    dp = [0] * (num + 1)

    dp[0] = 0
    if num >= 1:
        dp[1] = 1

    for i in range(2, num + 1):

        dp[i] = dp[i>>1] + (i & 1)

    return dp

inputs = 8
print(countBits2(inputs))