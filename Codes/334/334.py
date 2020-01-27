def increasingTriplet_(nums):
    """
    Comes from the tricky solution from LeetCode 300
    :param nums:
    :return:
    """
    if len(nums) < 3:
        return False
    LIS = [nums[0]]
    for num in nums[1:]:
        print(num, LIS)
        if num > LIS[-1]:
            LIS.append(num)
            if len(LIS) == 3:
                return True
        else:
            for idx, lis in enumerate(LIS):
                if lis >= num:
                    LIS[idx] = num
                    break
    return False

def increasingTriplet(nums):
    """
    Comes from https://www.cnblogs.com/grandyang/p/5194599.html
    :param nums:
    :return:
    """
    if len(nums) < 3:
        return False
    forward = [1e9] * len(nums) # f[i]: The minimal elements in nums[0: i-1]
    backward = [0] * len(nums)  # f[i]: The maximal elements in nums[i+1: ]
    for idx in range(1, len(nums)):
        forward[idx] = min(forward[idx - 1], nums[idx - 1])
    for idx in range(len(nums)-2, -1, -1):
        backward[idx] = max(backward[idx + 1], nums[idx + 1])
    # print(forward)
    # print(backward)
    for idx in range(1, len(nums)-1):
        if nums[idx] > forward[idx] and nums[idx] < backward[idx]:
            return True
    return False

inputs = [1,2,3,4,5]
print(increasingTriplet(inputs))
inputs = [5,4,3,2,1]
print(increasingTriplet(inputs))
inputs = [2,1,5,0,3]
print(increasingTriplet(inputs))
inputs = [1,2,1,2,1,2,1,2,1,2]
print(increasingTriplet(inputs))
inputs  = [0,4,2,1,0,-1,-3]
print(increasingTriplet(inputs))