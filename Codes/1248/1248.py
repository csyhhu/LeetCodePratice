def numberOfSubarrays_TwoPointer(nums, k):

    n = len(nums)
    start = -1
    end = -1
    n_odd = 0
    ans = 0
    while start < n:
        while end < n:
            end += 1
            if end == n:
                break
            if nums[end] % 2 == 1:
                n_odd += 1
            if n_odd == k:
                ans += 1
                break
            # elif n_odd > k:
            #     break
        # print(start, end, ans)
        while start < end:
            start += 1
            if start == n:
                break
            if nums[start] % 2 == 1:
                n_odd -= 1
            else:
                ans += 1
            if n_odd < k:
                break
        print(start, end, ans)
        # input()
    return ans


def numberOfSubarrays(nums, k):

    # n = len(nums)
    num_odd = {0: 1} # [i]: number of subarray with i odd numbers
    cur_odd_num = 0 # Number of odd number in current search
    ans = 0
    for num in nums:
        cur_odd_num += (num % 2 == 1)
        if cur_odd_num - k in num_odd:
            ans += num_odd[cur_odd_num - k]
        num_odd[cur_odd_num] = num_odd.get(cur_odd_num, 0) + 1
    return ans



print(numberOfSubarrays([1,1,2,1,1], k = 3))
print(numberOfSubarrays(nums = [2,4,6], k = 1))
print(numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))