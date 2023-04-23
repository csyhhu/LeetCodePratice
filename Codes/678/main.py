def checkValidStringWA(s: str):

    n = len(s)
    left_pos_set = ['(', '*']
    right_pos_set = [')', '*']
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    def isValid(l, r, s, dp):

        if dp[l][r] in [0, 1]:
            return dp[l][r]
        if l == r:
            dp[l][r] = 1
            return 1 if s[l] == '*' else 0
        if l > r:
            dp[l][r] = 1
            return 1

        if s[l] in left_pos_set and s[r] in right_pos_set and isValid(l+1, r-1, s, dp):
            dp[l][r] = 1
            return 1

        for k in range(l, r):
            if isValid(l, k, s, dp) and isValid(k + 1, r, s, dp):
                dp[l][r] = 1
                return 1

        dp[l][r] = 0
        return 0

    return True if isValid(0, n-1, s, dp) == 1 else False

# s = "()"
# print(checkValidString(s))
#
# s = "(*)"
# print(checkValidString(s))
#
# s = "(*))"
# print(checkValidString(s))
#
# s = "("
# print(checkValidString(s))

s = "(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((("
print(checkValidString(s))
