def findPeakElement(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        