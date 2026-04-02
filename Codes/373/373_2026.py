"""
[373] Find K Pairs with Smallest Sums  ← 热身关联题
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

⚡ 面试真题关联：
    你遇到的面试题：给定 NxN 整型数组，每行已从小到大排列，返回整个数组排序后的结果。
    核心算法完全一致：K 路归并 (Min-Heap)

    面试题解法思路：
        - 把每一行看作一路有序序列，共 N 路
        - 用最小堆维护每路当前最小值，堆元素为 (val, row, col)
        - 每次弹出最小值后，将该行的下一个元素加入堆
        - 时间复杂度：O(N^2 * log N)，空间复杂度：O(N)

    面试题直接代码：
        import heapq
        def sort_matrix(matrix):
            n = len(matrix)
            heap = [(matrix[i][0], i, 0) for i in range(n)]
            heapq.heapify(heap)
            result = []
            while heap:
                val, row, col = heapq.heappop(heap)
                result.append(val)
                if col + 1 < n:
                    heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
            return result

关联题目 373 描述：
    You are given two integer arrays nums1 and nums2 sorted in non-decreasing order
    and an integer k.

    Define a pair (u, v) which consists of one element from the first array and
    one element from the second array.

    Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
    Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
    Output: [[1,2],[1,4],[1,6]]
    Explanation: The first 3 pairs are returned from the sequence:
                 [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
    Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
    Output: [[1,1],[1,1]]

Example 3:
    Input: nums1 = [1,2], nums2 = [3], k = 3
    Output: [[1,3],[2,3]]

Constraints:
    - 1 <= nums1.length, nums2.length <= 10^5
    - -10^9 <= nums1[i], nums2[i] <= 10^9
    - nums1 and nums2 both are sorted in non-decreasing order
    - 1 <= k <= 10^4
    - k <= nums1.length * nums2.length

Key Insights (关键洞察):
    - 把 nums1 的每个元素与 nums2 配对，形成 len(nums1) 路有序序列
      第 i 路：(nums1[i]+nums2[0], nums1[i]+nums2[1], nums1[i]+nums2[2], ...)
    - 用最小堆：初始化每路第一个元素 → 弹出最小 → 推入该路下一个
    - 与面试题的区别：面试题是从矩阵每行取元素，本题是从 nums2 取元素配 nums1[i]
    - 核心模式完全相同：K 路归并

Date: 2026-03-24
"""

import heapq


def kSmallestPairs(nums1, nums2, k):
    """
    K 路归并：最小堆
    
    思路：
    - 将 nums1 中每个元素与 nums2[0] 配对作为各路起点，共 len(nums1) 路
    - 堆元素：(sum, i, j) 代表 nums1[i] + nums2[j]
    - 每次弹出最小 pair，然后推入同一路的下一个 (nums1[i], nums2[j+1])
    
    TODO: 实现这个函数
    步骤：
    1. 初始化堆：对 nums1 的前 min(len(nums1), k) 个元素，各与 nums2[0] 配对入堆
    2. 循环 k 次（或堆空）：
       a. 弹出堆顶 (sum, i, j)
       b. 将 (nums1[i], nums2[j]) 加入结果
       c. 若 j+1 < len(nums2)，推入 (nums1[i]+nums2[j+1], i, j+1)
    3. 返回结果
    
    时间复杂度：O(k * log(min(len(nums1), k)))
    空间复杂度：O(min(len(nums1), k))
    """
    pairs = []
    n1 = len(nums1)
    n2 = len(nums2)
    
    # print(len(pairs), len(pairs[0]))
    result = []
    minHeap = []
    for i in range(min(n1, k)):
        heapq.heappush(minHeap, [nums1[i] + nums2[0], i, 0])

    for _ in range(k):
        if len(minHeap) == 0:
            break
        value, idx1, idx2 = heapq.heappop(minHeap)
        result.append([nums1[idx1], nums2[idx2]])
        if idx2 + 1 < n2:
            heapq.heappush(minHeap, [nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1])
            
    return result
        



def kSmallestPairs_brute(nums1, nums2, k):
    """
    暴力法：枚举所有 pair，排序取前 k 个
    
    时间复杂度：O(m*n*log(m*n))
    空间复杂度：O(m*n)
    """
    pass


# ─────────────────────────────────────────────
# 面试原题 Template（直接可复用）
# ─────────────────────────────────────────────

def sort_nxn_matrix(matrix):
    """
    面试题：NxN 矩阵每行已排序，返回整体排序结果

    方法：K 路归并（Min-Heap）
    
    TODO: 实现这个函数
    步骤：
    1. 初始化堆：将每行第一个元素 (matrix[i][0], row=i, col=0) 入堆
    2. 循环直到堆空：
       a. 弹出堆顶 (val, row, col)，val 加入结果
       b. 若 col+1 < n，将 (matrix[row][col+1], row, col+1) 入堆
    3. 返回结果

    时间复杂度：O(N^2 * log N)  — N^2 个元素，每次堆操作 O(log N)
    空间复杂度：O(N)            — 堆中最多 N 个元素
    """
    pass


# Test cases
if __name__ == "__main__":
    print("=" * 50)
    print("Test: sort_nxn_matrix (面试原题)")
    print("=" * 50)

    matrix1 = [
        [1, 3, 5],
        [2, 4, 6],
        [7, 8, 9],
    ]
    result = sort_nxn_matrix(matrix1)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    status = "✓" if result == expected else "✗"
    print(f"{status} matrix={matrix1}")
    print(f"   Output:   {result}")
    print(f"   Expected: {expected}\n")

    matrix2 = [
        [10, 20, 30],
        [1,  5,  25],
        [3,  7,  15],
    ]
    result2 = sort_nxn_matrix(matrix2)
    expected2 = sorted([10, 20, 30, 1, 5, 25, 3, 7, 15])
    status2 = "✓" if result2 == expected2 else "✗"
    print(f"{status2} matrix={matrix2}")
    print(f"   Output:   {result2}")
    print(f"   Expected: {expected2}\n")

    print("=" * 50)
    print("Test: kSmallestPairs (LeetCode 373)")
    print("=" * 50)

    test_cases = [
        (([1, 7, 11], [2, 4, 6], 3), [[1, 2], [1, 4], [1, 6]]),
        (([1, 1, 2], [1, 2, 3], 2), [[1, 1], [1, 1]]),
        (([1, 2], [3], 3), [[1, 3], [2, 3]]),
    ]

    for (nums1, nums2, k), expected in test_cases:
        result = kSmallestPairs(nums1, nums2, k)
        # 排序后比较，因为顺序可能不同
        status = "✓" if sorted(map(tuple, result)) == sorted(map(tuple, expected)) else "✗"
        print(f"{status} nums1={nums1}, nums2={nums2}, k={k}")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}\n")
