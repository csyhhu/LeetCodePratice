def threeSum(nums):

    nums = sorted(nums)
    print(nums)
    n = len(nums)
    results = []
    # We first fix one number, and then find two numbers whose sum is the negative value of the fixed number.
    # The fix search range in [0, n-2), for there will not be 3 numbers after n-2
    # During the searching, if nums[i] > 0, stop. For nums is sorted and there will not be values after i (nums[i]) whose sum can be negative.
    # In the meanwhile, skip the same value as fix number to reduce duplicated.
    for i in range(n-2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # Find a fixed number: nums[i], set two search pointer, one from start, one from end
        l = i + 1
        r = n - 1
        target = -nums[i]
        # print(i)
        while l < r:
            cur_sum = nums[l] + nums[r]
            if  cur_sum == target:
                results.append([nums[i], nums[l], nums[r]])
                # If one solution is found, left / right move forward / backward, at the same time, pay attention not to include duplicated result
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
                r -= 1
                while nums[r] == nums[r+1] and l < r:
                    r -= 1

            elif cur_sum < target:
                l += 1
            else:
                r -= 1

    return results

nums = [-1,0,1,2,-1,-4]
# print(threeSum(nums=nums))

nums = [-2,0,0,2,2]
print(threeSum(nums=nums))

nums = [0, 0, 0]
print(threeSum(nums=nums))