from typing import List
def minOperations1(nums: List[int], x: int):

    """
    TLE
    :param nums:
    :param x:
    :return:
    """

    def dfs(curX, curNums):

        if curX == 0:
            return 0
        elif curX < 0:
            return 1e9

        if len(curNums) == 0:
            return 1e9

        return min(dfs(curX - curNums[0], curNums[1:]) + 1, dfs(curX - curNums[-1], curNums[:-1]) + 1)

    result = dfs(x, nums)
    if result >= 1e9:
        return -1
    else:
        return result


def minOperations_dp(nums: List[int], x: int):

    n = len(nums)
    dp = [[10e9] * (n) for _ in range(n)]
    # print(dp)
    dp[0][n-1] = x
    dp[1][n-1] = x - nums[0]
    dp[0][n-2] = x - nums[-1]
    # print(dp)
    for i in range(1, n-1):
        for j in range(n-2, i, -1):
            # dp[i][j] = dp[i][j+1] - nums[j+1] or dp[i-1][j] - nums[i]
            cut_left = dp[i-1][j] - nums[i-1] # dp[0][n-2] - nums[0]
            cut_right = dp[i][j+1] - nums[j+1] # dp[1][n-1] - nums[n-1]
            if cut_left < 0 and cut_right < 0:
                break
            elif cut_right * cut_left < 0:
                dp[i][j] = max(cut_left, cut_right)
            else:
                dp[i][j] = min(cut_left, cut_right)
            # dp[i][j] = min(dp[i-1][j] - nums[i], dp[i][j+1] - nums[j])
            # print(i, j, dp[i][j])
            if dp[i][j] == 0:
                return i + (n - 1) - j
            # elif dp[i][j] < 0:
            #     break
    return -1


def minOperations(nums, x):
    """
    Main thing to consider is that it is irrelevant what order you perform the operations.
    It only matters how many come from the left, and how many come from the right.
    So create 2 prefix sum arrays: one from the front, one from the back.
    The ith index of each array represents how much you will remove from x if you remove i elements from the front/back.
    Then, the question is like Two Sum. Iterate through one of the prefix sums, and check if the difference needed for x exists in the other prefix sum.
    :param nums:
    :param x:
    :return:
    """
    n = len(nums)
    left = []
    for idx in range(n):
        left.append(sum(nums[:idx]))
    right = []
    for idx in range(n, 0, -1):
        right.append(sum(nums[idx:]))

    result = 1e9
    for idx_left in range(n):
        for idx_right in range(n):
            if left[idx_left] + right[idx_right] == x:
                result = min(idx_left + idx_right, result)
            elif left[idx_left] + right[idx_right] > x:
                break

    if result == 1e9:
        return -1
    else:
        return result



nums = [1,1,4,2,3]
x = 5
print(minOperations(nums, x))

nums = [5,6,7,8,9]
x = 4
print(minOperations(nums, x))

nums = [3,2,20,1,1,3]
x = 10
print(minOperations(nums, x))