"""
[23] Merge K Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted
in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
        1->4->5
        1->3->4
        2->6
    Merging them into one sorted list: 1->1->2->3->4->4->5->6

Example 2:
    Input: lists = []
    Output: []

Example 3:
    Input: lists = [[]]
    Output: []

Constraints:
    - k == lists.length
    - 0 <= k <= 10^4
    - 0 <= lists[i].length <= 500
    - -10^4 <= lists[i][j] <= 10^4
    - lists[i] is sorted in ascending order
    - The sum of lists[i].length will not exceed 10^4

Key Insights (关键洞察):
    - 本质是 K 路归并，和 373、378、面试矩阵题完全同一套思路
    - 方法一：最小堆（Min-Heap）
        * 堆元素：(node.val, 序号, node) — 序号用于打破 val 相等时的比较冲突
        * 初始化：将每个链表头节点入堆
        * 每次弹出最小节点，接入结果链表，再将该节点的 next 推入堆
        * 时间复杂度：O(N log k)，N 为总节点数，k 为链表数量
        * 空间复杂度：O(k)
    - 方法二：分治归并（Divide & Conquer）
        * 类似归并排序，两两合并链表，共 log k 轮
        * 时间复杂度：O(N log k)
        * 空间复杂度：O(log k) 递归栈

    ⚡ 与面试矩阵题对比：
        矩阵题：堆元素 = (matrix[row][col], row, col)，col 右移
        本题：  堆元素 = (node.val, idx, node)，node 向 next 移动
        ── 模式完全相同！

Date: 2026-03-24
"""

from ast import List
from calendar import c
import heapq
from tarfile import NUL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    """
    方法一：最小堆（Min-Heap）K 路归并
    时间复杂度：O(N log k)
    空间复杂度：O(k)
    """
    """
    allListNode = []
    num_val = 0
    for list in lists:
        start = ListNode(None)
        prev = start
        for l in list:
            listNode = ListNode(l)
            prev.next = listNode
            prev = listNode
        allListNode.append(start)
        num_val += len(list)
    """
    total_size = 0
    for start in lists:
        while start is not None:
            total_size += 1
            start = start.next

    result_size = 0
    result = ListNode(None)
    result_start = result
    while result_size < total_size:
        cur_small = 10001
        cur_small_idx = 0
        for idx, start in enumerate(lists):
            if start is None:
                continue
            if cur_small > start.val:
                cur_small = start.val
                cur_small_idx = idx
        result.next = ListNode(cur_small)
        result = result.next
        lists[cur_small_idx] = lists[cur_small_idx].next
        result_size += 1
    # print(result_size)
    return result_start.next


def mergeKLists_divide(lists):
    """
    方法二：分治归并（Divide & Conquer）
    时间复杂度：O(N log k)
    空间复杂度：O(log k)
    """
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left = mergeKLists_divide(lists[: mid])
    right = mergeKLists_divide(lists[mid:])
    return merge_two(left, right)


def merge_two(l1, l2):
    """辅助：合并两个有序链表"""
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1:
        cur.next = l1
    else:
        cur.next = l2
    return dummy.next
    


# ─────────────────────────────────────────────
# 工具函数：方便测试
# ─────────────────────────────────────────────

def make_list(arr):
    """将数组转为链表"""
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def list_to_arr(node):
    """将链表转为数组"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Test cases
if __name__ == "__main__":
    print("=" * 50)
    print("Test: mergeKLists (Min-Heap)")
    print("=" * 50)

    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1], [0]], [0, 1]),
        ([[2], [1], [3]], [1, 2, 3]),
    ]

    for arrs, expected in test_cases:
        lists = [make_list(a) for a in arrs]
        result_node = mergeKLists(lists)
        result = list_to_arr(result_node)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {arrs}")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}\n")

    print("=" * 50)
    print("Test: mergeKLists_divide (Divide & Conquer)")
    print("=" * 50)

    for arrs, expected in test_cases:
        lists = [make_list(a) for a in arrs]
        result_node = mergeKLists_divide(lists)
        result = list_to_arr(result_node)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {arrs}")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}\n")
