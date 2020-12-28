def numberOfArithmeticSlices_1(A: list):

    n = len(A)
    if n < 3:
        return 0
    # base = 0
    dp = [0] * n
    base = [0] * n
    idx = 2
    diff = A[1] - A[0]
    succession = 1
    min_n_succession = 2
    # Find out the first arithmetic slices
    while succession < min_n_succession and idx < n:
        this_diff = A[idx] - A[idx - 1]
        if this_diff == diff:
            succession += 1
        else:
            diff = this_diff
        idx += 1
    # print(idx)
    if succession == min_n_succession:
        dp[idx - 1] = 1
    else:
        return 0
    # print(idx)
    for i in range(idx, n):
        # If the previous slides are arithmetic slices,
        # we first check whether A[i] contributes the current arithmetic slices.
        # If yes, simple way.
        # If no, we stash the base as the addition of dp[i-1] and base[i-1] and renew the diff
        if succession == min_n_succession:
            # print('I am here')
            if A[i] - A[i-1] == diff:
                dp[i] = dp[i-1] * 2 - dp[i-2] + 1
                base[i] = base[i - 1]
            else:
                # Stash the base, representing the number of arithmetic slices for A[0:i-1]
                base[i] = dp[i - 1] + base[i - 1]
                dp[i] = 0
                diff = A[i] - A[i-1]
                succession = 1
        else:
            dp[i] = dp[i-1]
            base[i] = base[i-1]
            if A[i] - A[i-1] == diff:
                succession += 1
                # If it reaches the minimal number of succession, it should start
                if succession == min_n_succession:
                    dp[i] = 1
                    base[i] = base[i - 1]
            else:
                diff = A[i] - A[i-1]
                succession = 1
        # print(i, A[i], diff, succession)
    print(dp)
    print(base)
    return dp[n-1] + base[n-1]


def numberOfArithmeticSlices(A: list):

    n = len(A)
    if n < 3:
        return 0
    a = [0] * n # Number of arithmetic slices ending with A[i]
    for i in range(2, n):
        if (A[i] - A[i-1]) == (A[i-1] - A[i-2]):
            a[i] = a[i-1] + 1
    return sum(a)

print(numberOfArithmeticSlices([1, 2, 3, 4]))
print(numberOfArithmeticSlices([1, 2, 3]))
print(numberOfArithmeticSlices([1, 2, 3, 5, 6, 7]))
print(numberOfArithmeticSlices([1, 2, 3, 5, 6, 6, 7, 8, 9]))
print(numberOfArithmeticSlices([1,2,3,4,5]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))