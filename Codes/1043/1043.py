def maxSumAfterPartitioning(A, K):
    """
    Time Limit Exceededme
    :param A:
    :param K:
    :return:
    """
    A.append(0)
    dp = [0] * (len(A)-1)
    dp[0] = A[0]

    for i in range(1, len(A)-1):
        max_value = float('-inf')
        for k in range(1, K + 1):
            max_value = max(max_value, A[i-k+1])
            if i-k >= 0:
                # dp[i] = max(dp[i], dp[i-k] + k * max(A[i-k+1: i+1]))
                dp[i] = max(dp[i], dp[i-k] + k * max_value)
            elif i-k == -1:
                # dp[i] = k * max(A[i-k+1: i+1])
                dp[i] = k * max_value
            else:
                continue
    print(dp)
    return dp[-1]

# A = [1,15,7,9,2,5,10]
# A = [1,15]
# A = [1, 15, 7]
A = [1, 15, 7, 9, 2, 5, 10]
K = 3
output = maxSumAfterPartitioning(A, K)
print(output)