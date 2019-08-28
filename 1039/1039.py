inputs = [1,3,1,4,1,5]

def minScoreTriangulation(A):
    
    n = len(A)
    dp = [[0]*n for _ in range(n)]
    
    for length in range(n):
        i = 0
        for j in range(length, n):
            # if i == j - 1:
            if j < i + 2:
                dp[i][j] = 0
            else:
                dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[k] * A[i] * A[j])
            i += 1

    return dp[0][n-1]
    
    """
    n = len(A)
    dp = [[0]*n for _ in range(n)]
    for length in range(n):
        index_i = 0
        for index_j in range(length, n):
            if index_j < index_i+2:
                dp[index_i][index_j] = 0
            else:
                dp[index_i][index_j] = float('inf')
                for index_k in range(index_i+1, index_j):
                    val = dp[index_i][index_k] + dp[index_k][index_j] + (A[index_i]*A[index_k]*A[index_j])
                    dp[index_i][index_j] = min(dp[index_i][index_j], val)
            index_i += 1
    return dp[0][n-1]
    """

outputs = minScoreTriangulation(inputs)
print(outputs)