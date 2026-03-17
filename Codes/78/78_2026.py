"""
[78] Subsets
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
    Input: nums = [1]
    Output: [[],[1]]

Constraints:
    - 1 <= nums.length <= 10
    - -10 <= nums[i] <= 10
    - All the numbers of nums are unique.

Date: 2026-02-28
"""

def subsets(nums):
    """
    思路：
    DFS: 每一层选择取或者不取，并记录取的情况

    时间复杂度：O(n * 2^n)
    空间复杂度：O(n)
    """
    import copy
    results = []
    def dfs(nums, results, cur, index):
        if index == len(nums):
            results.append(copy.deepcopy(cur))
            return
        # 先探索不选当前元素的分支
        dfs(nums, results, cur, index + 1)
        # 再探索选当前元素的分支
        cur.append(nums[index])
        dfs(nums, results, cur, index + 1)
        cur.pop()
    
    dfs(nums, results, [], 0)
    return results


def subsets_backtrack(nums):
    """
    回溯法实现：
    回溯：通过循环和递归组合，在每一步做选择，然后撤销选择

    时间复杂度：O(n * 2^n)
    空间复杂度：O(n)
    """
    results = []

    def backtrack(start, path):
        # TODO: 实现回溯逻辑
        # 1. 将当前路径加入结果
        # 2. 循环从start到末尾
        # 3. 做选择：将当前元素加入path
        # 4. 递归调用
        # 5. 撤销选择：移除最后一个元素
        pass

    backtrack(0, [])
    return results


def subsets_iterative(nums):
    """
    迭代法实现（非递归）：
    使用位掩码或动态添加

    时间复杂度：O(n * 2^n)
    空间复杂度：O(1) (不算输出数组)
    """
    results = [[]]

    # 方法1：动态添加
    for num in nums:
        # 对于每个新数字，把它添加到所有现有子集中
        new_subsets = []
        for subset in results:
            new_subset = subset + [num]
            new_subsets.append(new_subset)
        results.extend(new_subsets)

    return results


def subsets_bitmask(nums):
    """
    位掩码法（非递归）：
    用二进制数的每一位表示是否选择对应元素

    时间复杂度：O(n * 2^n)
    空间复杂度：O(1) (不算输出数组)
    """
    n = len(nums)
    results = []

    # 从0到2^n-1，每个数代表一个子集
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            # 检查第i位是否为1
            if mask & (1 << i):
                subset.append(nums[i])
        results.append(subset)

    return results


def subsets_stack(nums):
    """
    栈模拟DFS（非递归）：
    用显式栈替代递归调用栈

    时间复杂度：O(n * 2^n)
    空间复杂度：O(n)
    """
    results = []
    stack = [(0, [])]  # (index, current_path)

    while stack:
        index, path = stack.pop()

        if index == len(nums):
            results.append(path)
            continue

        # 先压入"不选"的分支（后处理）
        stack.append((index + 1, path.copy()))

        # 再压入"选"的分支（先处理）
        new_path = path.copy()
        new_path.append(nums[index])
        stack.append((index + 1, new_path))

    return results


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3]
    result1 = subsets(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]")
    print(f"Length: {len(result1)} (should be 2^3 = 8)\n")

    # Test case 2
    nums2 = [0]
    result2 = subsets(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: [[], [0]]")
    print(f"Length: {len(result2)} (should be 2^1 = 2)\n")

    # Test case 3
    nums3 = [1, 2, 3, 4]
    result3 = subsets(nums3)
    print(f"Input: {nums3}")
    print(f"Output length: {len(result3)} (should be 2^4 = 16)\n")

    # Test backtrack implementation
    print("=" * 50)
    print("Testing backtrack implementation:")
    print("=" * 50)

    # Test case 1 - backtrack
    nums1_bt = [1, 2, 3]
    result1_bt = subsets_backtrack(nums1_bt)
    print(f"Input: {nums1_bt}")
    print(f"Output: {result1_bt}")
    print(f"Length: {len(result1_bt)} (should be 2^3 = 8)\n")

    # Test iterative methods
    print("-" * 50)
    print("Testing iterative implementations:")
    print("-" * 50)

    # Iterative method
    result_iter = subsets_iterative(nums1_bt)
    print(f"Iterative method: {result_iter}")
    print(f"Length: {len(result_iter)}\n")

    # Bitmask method
    result_mask = subsets_bitmask(nums1_bt)
    print(f"Bitmask method: {result_mask}")
    print(f"Length: {len(result_mask)}\n")

    # Stack method
    result_stack = subsets_stack(nums1_bt)
    print(f"Stack method: {result_stack}")
    print(f"Length: {len(result_stack)}\n")
