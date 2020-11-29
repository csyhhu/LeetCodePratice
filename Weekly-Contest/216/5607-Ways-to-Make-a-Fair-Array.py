def waysToMakeFair_TLE(nums):

    n = len(nums)
    n_fair_idx = 0
    for i in range(n):
        left_value = nums.pop(i)
        odd_sum = 0
        even_sum = 0
        for j in range(n-1):
            if j % 2 == 0:
                even_sum += nums[j]
            else:
                odd_sum += nums[j]
        if even_sum == odd_sum:
            n_fair_idx += 1
        nums.insert(i, left_value)
    return n_fair_idx


def waysToMakeFair_prefix_sum(nums):
    n = len(nums)
    even_prefix_sum = [0] * (n + 1) # even_prefix_sum[n] = 0. Adding n+1 here is a trick.
    odd_prefix_sum = [0] * (n + 1)

    for idx, num in enumerate(nums):
        even_prefix_sum[idx] += even_prefix_sum[idx - 1] # even_prefix_sum[1] == even_prefix_sum[0]
        odd_prefix_sum[idx] += odd_prefix_sum[idx - 1] # odd_prefix_sum[2] == even_prefix_sum[1]
        if idx % 2 == 0:
            even_prefix_sum[idx] += num
        else:
            odd_prefix_sum[idx] += num

    # print(even_prefix_sum)
    # print(odd_prefix_sum)

    results = 0
    for idx, num in enumerate(nums):
        # If idx is removed, sum the even(odd) prefix sum before it and odd(even) prefix sum after it.
        # Take idx = 0, sum of even before it should be 0, sum of odd after it should be:
        # odd_prefix_sum[n-1] (sum of all odd numbers) - odd_prefix_sum[idx] (including it)
        even_after_remove = even_prefix_sum[idx - 1] + odd_prefix_sum[n - 1] - odd_prefix_sum[idx]
        odd_after_remove = odd_prefix_sum[idx - 1] + even_prefix_sum[n - 1] - even_prefix_sum[idx]
        results += (even_after_remove == odd_after_remove)

    return results


def waysToMakeFair(nums):
    even_remain = sum(nums[::2])
    odd_remain = sum(nums[1::2])
    even_cur, odd_cur, results = 0, 0, 0
    for idx, num in enumerate(nums):
        # During processing, substract number from even/old_remain as the right sum of even/old list,
        # Add removed number to even/old_cur as the left sum of even/old list
        if idx % 2 == 0:
            even_remain -= num
            even_after_remove = even_cur + odd_remain
            odd_after_remove = odd_cur + even_remain
            results += (even_after_remove == odd_after_remove)
            even_cur += num
        else:
            odd_remain -= num
            even_after_remove = even_cur + odd_remain
            odd_after_remove = odd_cur + even_remain
            results += (even_after_remove == odd_after_remove)
            odd_cur += num
    return results


print(waysToMakeFair(nums = [2,1,6,4]))
print(waysToMakeFair(nums = [1,1,1]))
print(waysToMakeFair(nums = [1,2,3]))