def firstMissingPositive_AC(nums):
    MAX_VALUE = 1e9
    for idx, num in enumerate(nums):
        if num <= 0:
            nums[idx] = MAX_VALUE

    for idx, num in enumerate(nums):
        num = abs(num)
        if num >= 1 and num <= len(nums) and nums[num - 1] > 0:
            nums[num - 1] *= -1
    print(nums)
    for idx, num in enumerate(nums):
        if num > 0:
            return idx + 1

    return len(nums) + 1


def firstMissingPositive(nums):

    pass

inputs = [501,502,4]
print(firstMissingPositive(inputs))
