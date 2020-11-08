def longestPalindrome(s):

    n = len(s)
    dp = [[0] * n for _ in range(n)]
    # print(dp)

    max_len = 1
    start = 0

    for i in range(n):
        dp[i][i] = 1
        if i + 1 < n and s[i] == s[i + 1]:
            dp[i][i+1] = 1
            start = i
            max_len = 2

    for i in range(n-1, -1, -1):
        for j in range(i + 2, n):
            if dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = 1
                cur_len = j - i + 1
                if max_len < cur_len:
                    max_len = cur_len
                    start = i

    return s[start: start + max_len]

s = "babad"
print(longestPalindrome(s))

s = "cbbd"
print(longestPalindrome(s))

s = "ac"
print(longestPalindrome(s))

s = 'abcdefggfedcba'
print(longestPalindrome(s))