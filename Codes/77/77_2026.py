"""
[77] Combinations
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.

Example 1:
    Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Example 2:
    Input: n = 1, k = 1
    Output: [[1]]

Constraints:
    - 1 <= n <= 20
    - 1 <= k <= n

Key Difference from Subsets (组合 vs 子集):
    - Subsets (子集): 从一个数组中选任意个元素的所有可能
    - Combinations (组合): 从1到n中选恰好k个数字的所有可能
    
    组合的关键特点：
    1. 需要选恰好k个数
    2. 用start参数避免重复（不需要visited数组）
    3. 时间复杂度：O(C(n,k) * k) = O(n!/(k!(n-k)!) * k)

Date: 2026-03-02
"""
import copy

def combine(n, k):
    """
    思路：
    DFS + 回溯：从start开始遍历，确保每个组合内元素有序且不重复
    
    TODO: 实现这个函数
    思考：
    1. 递归终止条件是什么？
    2. 每一层应该如何循环？
    3. 如何避免重复？
    
    时间复杂度：O(C(n,k) * k)
    空间复杂度：O(k)
    """
    results = []
    def dfs(results, cur, val, k):
        if len(cur) == k:
            results.append(copy.deepcopy(cur))
            return
        if val == n + 1:
            return
        cur.append(val)
        dfs(results, cur, val+1, k)
        cur.pop()
        dfs(results, cur, val+1, k)

    dfs(results, [], 1, k)
    return results


def combine_backtrack(n, k):
    """
    回溯法实现（显式）：
    使用显式的选择/撤销过程，更清晰地体现回溯思想
    
    TODO: 实现这个函数
    步骤：
    1. 将当前路径加入结果（当长度达到k时）
    2. 循环从start到n
    3. 做选择：将当前数字加入path
    4. 递归调用
    5. 撤销选择：移除最后一个元素
    
    时间复杂度：O(C(n,k) * k)
    空间复杂度：O(k)
    """
    pass


def combine_iterative(n, k):
    """
    迭代法实现（非递归）：
    使用栈模拟DFS过程
    
    TODO: 实现这个函数
    思考：栈中应该存储什么？(index/start, current_combination)
    
    时间复杂度：O(C(n,k) * k)
    空间复杂度：O(C(n,k) * k)
    """
    pass


def combine_bitmask(n, k):
    """
    位掩码法（非递归）：
    用二进制数表示选择，需要选择恰好k个1的数
    
    TODO: 实现这个函数
    思考：
    1. 如何判断一个数有多少个1？
    2. 需要从哪个数字开始遍历到哪个数字？
    
    时间复杂度：O(2^n * n)
    空间复杂度：O(1)
    """
    pass


def combine_lexicographic(n, k):
    """
    字典序法（非递归）：
    直接生成下一个组合，按字典序
    
    TODO: 实现这个函数（难度较高，可选）
    思想：
    1. 从最小的组合[1,2,...,k]开始
    2. 找到最右边可以递增的位置
    3. 递增该位置，后续位置恢复
    
    时间复杂度：O(C(n,k) * k)
    空间复杂度：O(k)
    """
    pass


# Test cases
if __name__ == "__main__":
    # Test case 1
    n1, k1 = 4, 2
    result1 = combine(n1, k1)
    print(f"Input: n = {n1}, k = {k1}")
    print(f"Output: {result1}")
    print(f"Expected: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]")
    print(f"Length: {len(result1)} (should be C(4,2) = 6)\n")

    # Test case 2
    n2, k2 = 1, 1
    result2 = combine(n2, k2)
    print(f"Input: n = {n2}, k = {k2}")
    print(f"Output: {result2}")
    print(f"Expected: [[1]]")
    print(f"Length: {len(result2)} (should be C(1,1) = 1)\n")

    # Test case 3
    n3, k3 = 5, 3
    result3 = combine(n3, k3)
    print(f"Input: n = {n3}, k = {k3}")
    print(f"Output length: {len(result3)} (should be C(5,3) = 10)\n")

    # Test backtrack implementation
    # print("=" * 50)
    # print("Testing backtrack implementation:")
    # print("=" * 50)

    # # Test case 1 - backtrack
    # n1_bt, k1_bt = 4, 2
    # result1_bt = combine_backtrack(n1_bt, k1_bt)
    # print(f"Input: n = {n1_bt}, k = {k1_bt}")
    # print(f"Output: {result1_bt}")
    # print(f"Length: {len(result1_bt)} (should be C(4,2) = 6)\n")

    # # Test iterative methods
    # print("-" * 50)
    # print("Testing iterative implementations:")
    # print("-" * 50)

    # # Iterative method
    # result_iter = combine_iterative(n1_bt, k1_bt)
    # print(f"Iterative method: {result_iter}")
    # print(f"Length: {len(result_iter) if result_iter else 0}\n")

    # # Bitmask method
    # result_mask = combine_bitmask(n1_bt, k1_bt)
    # print(f"Bitmask method: {result_mask}")
    # print(f"Length: {len(result_mask) if result_mask else 0}\n")

    # # Lexicographic method (optional)
    # result_lex = combine_lexicographic(n1_bt, k1_bt)
    # print(f"Lexicographic method: {result_lex}")
    # print(f"Length: {len(result_lex) if result_lex else 0}\n")
