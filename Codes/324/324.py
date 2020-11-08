def wiggleSort_return(nums):
    n = len(nums)
    nums.sort()
    # mid = nums[n//2]
    result = []
    for i in range(n//2):
        result.append(nums[i])
        result.append(nums[n-i-1])
    if n % 2 == 1:
        result.append(nums[n//2])
    return result
    # nums = result # Assignment does not take effect

def wiggleSort_WA(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    # mid = n // 2
    nums.sort()
    print(nums)
    for i in range(n // 2):
        if i % 2 == 0:
            continue
        # In even position, switch with the even position after n//2
        tmp = nums[i]
        nums[i] = nums[n - i - 1]
        nums[n - i - 1] = tmp

def wiggleSort(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    pass


inputs = [1, 5, 1, 1, 6, 4, 7]
# print(wiggleSort(inputs))
wiggleSort(inputs)
print(inputs)

inputs = [1,3,2,2,3,1]
wiggleSort(inputs)
print(inputs)