def findDuplicates(nums):

    N = len(nums)

    for i in range(N):
        if nums[abs(nums[i]) - 1] > 0:
            nums[abs(nums[i]) - 1] = -nums[abs(nums[i])-1]
        else:
            nums.append(abs(nums[i]))

    return nums[N:]

inputs = [4,3,2,7,8,2,3,1]
outputs = findDuplicates(inputs)
print(outputs)