def sortColors_twoIteration(nums):

    n =  len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp

    print(nums)

def sortColors(nums):

    n = len(nums)
    head = 0
    tail = n-1
    i = 0
    while i <= tail:
        if nums[i] == 0:
            tmp = nums[head]
            nums[head] = nums[i]
            nums[i] = tmp
            head += 1
            i += 1
        elif nums[i] == 2:
            tmp = nums[tail]
            nums[tail] = nums[i]
            nums[i] = tmp
            tail -= 1
        else:
            i += 1
        # print(nums)
    # print(nums)

inputs = [2,0,2,1,1,0]
# print(inputs)
sortColors(inputs)