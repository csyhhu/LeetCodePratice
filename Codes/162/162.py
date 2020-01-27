def findPeakElement(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        # print(left, mid, right)
        # input()
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return right

# inputs = [1,2,3,1]
inputs = [1,2,1,3,5,6,4]
print(findPeakElement(inputs))
        