def longestSubarray_1(nums):
    """
    Two pointers
    :param nums:
    :return:
    """
    n = len(nums)
    if sum(nums) == n:
        return n-1
    start, end = 0, 0
    exist_only_one_zero = -1
    ans = 0
    ans_start, ans_end = 0, 0
    while start < n:
        while exist_only_one_zero in [-1, 0] and end < n:
            if nums[end] == 0:
                exist_only_one_zero += 1
            if exist_only_one_zero in [-1, 0]:
                end += 1
        # ans = max(ans, end - start - 1)
        # print(start, end)
        if end - start - 1 > ans:
            ans = end - start - 1
            ans_end = end
            ans_start = start
            # print(ans, ans_start, ans_end)
        if exist_only_one_zero in [-1, 0]:
            break
        while exist_only_one_zero == 1 and start <= end:
            if nums[start] == 0:
                exist_only_one_zero -= 1
            start += 1
        end += 1
        # print(start, end, exist_only_one_zero)
        # input()
    # return ans, ans_start, ans_end
    return ans


def longestSubarray(nums):
    n = len(nums)
    start, end = 0, 0
    num_zero = 0
    ans = 0
    while start < n and end < n:
        if nums[end] == 0:
            num_zero += 1
        while num_zero > 1 and start < n:
            if nums[start] == 0:
                num_zero -= 1
            start += 1
        ans = max(ans, end - start)
        end += 1
    return ans

print(longestSubarray([1,1,0,1]))
print(longestSubarray([0,1,1,1,0,1,1,0,1]))
print(longestSubarray([1,1,1]))
print(longestSubarray(nums = [1,1,0,0,1,1,1,0,1]))
print(longestSubarray(nums = [0,0,0]))