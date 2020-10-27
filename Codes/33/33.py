def search(nums, target: int):
    """
    [0,1,2,4,5,6,7] => [4,5,6,7,0,1,2]
    Find target in nums
    :param nums:
    :param target:
    :return:
    """
    def binSearch(nums, start, end, target):

        mid = (start + end) // 2
        print(start, mid, end)

        if start > end:
            return -1

        if nums[mid] == target:
            return mid

        if nums[start] <= nums[mid]: # [start, mid] is ordered. Attention here, less or equal for mid may be equal to start
            if nums[start] <= target < nums[mid]: # target is within a order list
                return binSearch(nums, start, mid - 1, target)
            else:
                return binSearch(nums, mid + 1, end, target)
        else: # [mid, end] is ordered
            if nums[end] >= target > nums[mid]: # target is within a order list
                return binSearch(nums, mid + 1, end, target)
            else: # target is outside a order list, direct it to another list
                return binSearch(nums, start, mid - 1, target)

    return binSearch(nums, 0, len(nums) - 1, target)

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))

nums = [4,5,6,7,0,1,2]
target = 3
print(search(nums, target))

nums = [1]
target = 0
print(search(nums, target))

nums = [3,1]
target = 1
print(search(nums, target))