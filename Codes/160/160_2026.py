"""
[160] Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Given the heads of two singly linked-lists headA and headB, return the node at
which the two lists intersect. If the two linked lists have no intersection at
all, return null.

Example 1:
    A:        4 → 1 ↘
                      8 → 4 → 5
    B:   5 → 6 → 1 ↗

    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5],
           skipA = 2, skipB = 3
    Output: Intersected at '8'

Example 2:
    A:   2 → 6 → 4
    B:        1 → 5
    Output: No intersection (return null)

Constraints:
    - The number of nodes of listA is in the m.
    - The number of nodes of listB is in the n.
    - 1 <= m, n <= 3 * 10^4
    - No cycles anywhere in the entire linked structure.
    - The linked lists must retain their original structure after the function returns.

Date: 2026-03-27
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    """
    双指针法：a 走完 A 链后走 B 链，b 走完 B 链后走 A 链
    若有交点：两者路程相同，必在交点相遇
    若无交点：两者同时走到 None，退出循环

    时间复杂度：O(m + n)
    空间复杂度：O(1)
    """
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB   # 走完 A 就跳到 B 的头
        b = b.next if b else headA   # 走完 B 就跳到 A 的头
    return a  # 交点 or None（无交点时两者同时为 None）


# ─────────────────────────────────────────────
# 工具函数：方便测试
# ─────────────────────────────────────────────

def build_intersecting_lists(listA_vals, listB_vals, intersect_val):
    """构建有公共交点的两条链表"""
    # 先找交点之前的部分和公共部分
    if intersect_val is None:
        # 无交点
        headA = build_list(listA_vals)
        headB = build_list(listB_vals)
        return headA, headB

    # 找公共部分起始索引
    idxA = listA_vals.index(intersect_val)
    idxB = listB_vals.index(intersect_val)

    # 构建公共链
    shared = build_list(listA_vals[idxA:])

    # 构建 A 的独有部分并接上公共链
    headA = build_list(listA_vals[:idxA], tail=shared)
    # 构建 B 的独有部分并接上公共链
    headB = build_list(listB_vals[:idxB], tail=shared)

    return headA, headB


def build_list(vals, tail=None):
    """按顺序构建链表，末尾接 tail"""
    if not vals:
        return tail
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    cur.next = tail
    return dummy.next


# Test cases
if __name__ == "__main__":
    # (listA_vals, listB_vals, intersect_val, expected_val)
    test_cases = [
        ([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 8,  8),   # 有交点
        ([2, 6, 4],        [1, 5],              None, None),  # 无交点
        ([1, 9, 1, 2, 4],  [3, 2, 4],           2,  2),   # 有交点
    ]

    for listA_vals, listB_vals, intersect_val, expected_val in test_cases:
        headA, headB = build_intersecting_lists(listA_vals, listB_vals, intersect_val)
        result = getIntersectionNode(headA, headB)
        result_val = result.val if result else None
        status = "✓" if result_val == expected_val else "✗"
        print(f"{status} intersect={intersect_val}")
        print(f"   Output:   {result_val}")
        print(f"   Expected: {expected_val}\n")
