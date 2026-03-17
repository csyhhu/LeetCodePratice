"""
[46] Permutations
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:
    Input: nums = [1]
    Output: [[1]]

Constraints:
    - 1 <= nums.length <= 6
    - -10 <= nums[i] <= 10
    - All the integers of nums are unique.

Key Difference from Subsets (组合 vs 排列):
    - Subsets (组合): [1,2] 和 [2,1] 是同一个子集，顺序无关
    - Permutations (排列): [1,2] 和 [2,1] 是不同的排列，顺序有关

    组合：从 start 开始往后选，避免重复
    排列：每次都从头开始选，但需要标记已使用的元素

Date: 2026-02-28
"""

def permute(nums):
    """
    思路：
    DFS, 需要保留一个visited数组，标记已使用的元素

    时间复杂度：O(n! * n)
    空间复杂度：O(n)
    """
    def dfs(nums, results, cur, visited):
        if len(cur) == len(nums):
            results.append(cur)
            return
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                dfs(nums, results, cur + [nums[i]], visited)
                visited[i] = False
    
    results = []
    dfs(nums, results, [], [False] * len(nums))
    return results


def permute_swap(nums):
    """
    交换法（更高效）：
    通过交换元素位置来生成排列，避免visited数组

    时间复杂度：O(n! * n)
    空间复杂度：O(n)
    """
    pass


def permute_iterative(nums):
    """
    迭代法（非递归）：
    逐个构建排列

    时间复杂度：O(n! * n)
    空间复杂度：O(n! * n)
    """
    results = [[]]

    for num in nums:
        new_results = []
        for perm in results:
            # 在每个位置插入新元素
            for i in range(len(perm) + 1):
                new_perm = perm[:i] + [num] + perm[i:]
                new_results.append(new_perm)
        results = new_results

    return results


def permute_next_permutation(nums):
    """
    字典序法（非递归）：
    使用 next_permutation 算法

    时间复杂度：O(n! * n)
    空间复杂度：O(1) (不算输出)
    """
    pass


def permute_heap(nums):
    """
    Heap算法：
    专门生成排列的算法，通过交换相邻元素实现

    时间复杂度：O(n! * n)
    空间复杂度：O(n)
    """
    pass


def permute_sjt(nums):
    """
    Steinhaus-Johnson-Trotter算法：
    每次只移动一个元素，所有排列通过相邻交换生成

    时间复杂度：O(n! * n)
    空间复杂度：O(n)
    """
    pass


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3]
    result1 = permute(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Length: {len(result1)} (should be 3! = 6)")
    expected1 = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(f"Expected: {expected1}\n")

    # Test case 2
    nums2 = [0, 1]
    result2 = permute(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Length: {len(result2)} (should be 2! = 2)")
    print(f"Expected: [[0,1],[1,0]]\n")

    # Test case 3
    nums3 = [1]
    result3 = permute(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print(f"Length: {len(result3)} (should be 1! = 1)")
    print(f"Expected: [[1]]\n")

    # Test iterative method
    print("=" * 50)
    print("Testing iterative method:")
    print("=" * 50)
    result_iter = permute_iterative(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result_iter}")
    print(f"Length: {len(result_iter)} (should be 3! = 6)\n")
