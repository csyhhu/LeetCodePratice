def findDuplicate_LinkList(nums):

    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        # print(slow, fast)

        if slow == fast:
            break

    t = nums[0]
    while slow != t:
        slow = nums[slow]
        t = nums[t]

    return slow

def findDuplicate(nums):

    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        # print(left, mid, right)
        count = 0
        for num in nums:
            if num <= mid:
                count += 1
        if count <= mid:
            left = mid + 1
        else:
            right = mid
    return left

inputs = [3,1,3,4,2]
print(findDuplicate(inputs))
inputs = [1,3,4,2,2]
print(findDuplicate(inputs))
inputs = [2,5,9,6,9,3,8,9,7,1]
print(findDuplicate(inputs))