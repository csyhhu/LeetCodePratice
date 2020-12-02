def findMaxForm(strs, m: int, n: int):
    """

    :param strs:
    :param m: Number of 0
    :param n: Number of 1
    :return:
    """
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    def count(_str):
        _n_one, _n_zero = 0, 0
        for _s in _str:
            if _s == '1':
                _n_one += 1
            else:
                _n_zero += 1
        return _n_one, _n_zero

    # This loop for strs make sure that st is chosen for only one time
    for st in strs:
        n_one, n_zero = count(st)
        for i in range(m, n_zero - 1, -1):
            for j in range(n, n_one - 1, -1):
                # dp[i-n_zero][j-n_one]: Number of strs that can be reached after taking st
                dp[i][j] = max(dp[i][j], dp[i-n_zero][j-n_one] + 1)
        # print(dp)

    return dp[m][n]

print(findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3))
# print(findMaxForm(["10","0","1"], m = 1, n = 1))