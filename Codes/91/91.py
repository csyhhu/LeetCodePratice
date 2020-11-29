def numDecodings_dfs(s: str):
    result = [0]

    def dfs(sub_s, res):
        # print(sub_s, res)
        if len(sub_s) == 0:
            # print('I am here')
            res[0] += 1
        elif len(sub_s) == 1:
            if sub_s[0] != '0':
                res[0] += 1
        else:
            # For the case of take one character
            if sub_s[0] != '0':
                dfs(sub_s[1:], res)
            # Take two characters
            if 10 <= int(sub_s[0: 2]) <= 26:
                dfs(sub_s[2:], res)

    dfs(s, result)
    return result[0]


def numDecodings(s: str):

    substr_results = dict()

    def dfs(sub_s, sub_s_res):
        if sub_s in sub_s_res:
            return sub_s_res[sub_s]
        if len(sub_s) == 0:
            sub_s_res[sub_s] = 1
            return 1
        if sub_s[0] == '0':
            sub_s_res[sub_s] = 0
            return 0
        if len(sub_s) == 1:
            sub_s_res[sub_s] = 1
            return 1

        # Take one character
        n_way = dfs(sub_s[1:], sub_s_res)

        # Take two characters
        if 10 <= int(sub_s[0: 2]) <= 26:
            n_way += dfs(sub_s[2:], sub_s_res)

        sub_s_res[sub_s] = n_way
        return n_way

    dfs(s, substr_results)
    # print(substr_results)
    return substr_results[s]


def numDecodings_DP(s: str):

    n = len(s)
    dp = [0] * n

    if len(s) == 0:
        return 0
    # Determine for the first element
    if s[0] != '0':
        dp[0] = 1
    # Determine for two elements
    if len(s) >= 2:
        if s[1] != '0':
            dp[1] = dp[0]
        if 10 <= int(s[0: 2]) <= 26:
            dp[1] += 1

    for i in range(2, n):
        take_one_possible = (s[i] != '0')
        take_two_possible = (10 <= int(s[i-1: i+1]) <= 26) # i=2, s[1:3], include s[2]
        if take_one_possible and take_two_possible:
            dp[i] = dp[i-1] + dp[i-2]
        elif take_one_possible and not take_two_possible:
            dp[i] = dp[i-1]
        elif not take_one_possible and take_two_possible:
            dp[i] = dp[i-2]
        else:
            dp[i] = 0

    # print(dp)
    return dp[n-1]

print(numDecodings("1"))
print(numDecodings("12"))
print(numDecodings("226"))
print(numDecodings("00"))
print(numDecodings("10"))
print(numDecodings("1201234"))