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


def findKthLargest(nums, k):

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



# inputs = [3,2,1,5,6,4]
# k = 2
# print(findKthLargest(inputs, k))
# inputs = [3,2,3,1,2,4,5,5,6]
# k = 4
# print(findKthLargest(inputs, k))
# inputs = [7,6,5,4,3,2,1]
# k = 2
# print(findKthLargest(inputs, k))
inputs = [-1,2,0]
k = 2
print(findKthLargest(inputs, k))