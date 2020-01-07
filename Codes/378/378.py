def kthSmallest_heap(matrix, k):
    import heapq

    heap = []
    for row in matrix:
        for ele in row:
            if len(heap) < k:
                heapq.heappush(heap, -ele)
            else:
                if heap[0] < -ele:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -ele)
    return -heap[0]


def kthSmallest(matrix, k):

    left = matrix[0][0]
    right = matrix[-1][-1]
    if left == right:
        return left

    while left < right:
        mid = (left + right) // 2

        count = 0
        for row in matrix:
            for ele in row:
                if ele < mid:
                    count += 1
        # print(left, mid, right, count)
        if count < k:
            left = mid + 1
        else:
            right = mid

    return mid

inputs = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8

print(kthSmallest(inputs, k))
