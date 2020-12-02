def findKthLargest_heap(nums, k):

    import heapq
    h = []

    for num in nums:
        if len(h) < k:
            heapq.heappush(h, num)
        else:
            if h[0] < num:
                heapq.heappop(h)
                heapq.heappush(h, num)

    return h[0]


def findKthLargest_old(nums, k):
    """
    This implementation is written in Jan, 2020
    :param nums:
    :param k:
    :return:
    """
    def partition(select_nums):
        pivot = select_nums[0]
        smaller = []
        larger = []
        for num in select_nums[1:]:
            if num < pivot:
                smaller.append(num)
            else:
                larger.append(num)
        return smaller, pivot, larger


    select = nums
    cur_k = k # The current largest k in the remaining nums
    while True:
        cur_n = len(select)  # The current length of remaining nums
        smaller, pivot, larger = partition(select)
        print(smaller, pivot, larger, cur_k)
        input()

        if len(larger) == cur_k - 1 or len(smaller) == len(nums) - k:
            return pivot
        elif len(larger) < cur_k - 1:
            select = smaller
            cur_k -= len(larger)
        else:
            select = larger
            # cur_k -= len(larger)


def findKthLargest(nums, k):
    """
    This implementation corresponds to solution 2 in readme
    :param nums:
    :param k:
    :return:
    """

    left = 0
    right = len(nums) - 1

    def partition(_nums, _left, _right):
        pivot = _nums[_left]
        i = _left + 1
        j = _right
        while i <= j:
            if _nums[i] < pivot < _nums[j]:
                tmp = _nums[i]
                _nums[i] = _nums[j]
                _nums[j] = tmp
                i += 1
                j -= 1
            if _nums[i] >= pivot:
                i += 1
            if _nums[j] <= pivot:
                j -= 1
        _nums[left] = _nums[j]
        _nums[j] = pivot
        # print(_nums)
        # input()
        return j

    while True:
        mid = partition(nums, left, right)
        if mid == k - 1:
            return nums[mid]
        # pivot is too large, which rank #mid (< k-1), therefore the result is in right lart
        elif mid < k - 1:
            left = mid + 1
        else:
            right = mid - 1

inputs = [3,2,1,5,6,4]
k = 2
print(findKthLargest(inputs, k))
inputs = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(inputs, k))
inputs = [7,6,5,4,3,2,1]
k = 2
print(findKthLargest(inputs, k))
inputs = [-1,2,0]
k = 2
print(findKthLargest(inputs, k))