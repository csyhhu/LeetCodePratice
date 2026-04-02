"""
[25] Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end,
should remain as is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

Example 2:
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]

Constraints:
    - The number of nodes in the list is n.
    - 1 <= k <= n <= 5000
    - 0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?

Date: 2026-03-25
"""


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printStack(_stack):
    for node in _stack:
        print(f"{node.val} ")
    print('\n')

"""
def reverseKGroup(head, k):
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    new_head = None
    while head:
        stack = []
        # origin_head = head
        # print(origin_head.val)
        for i in range(k):
            if head:
                stack.append(head)
                head = head.next
        # print('\n')
        # printStack(stack)
        cur = stack[-1]
        if new_head is None:
            new_head = cur
        if len(stack) == k:
            # print('I am here')
            while stack:
                next = stack.pop()
                cur.next = next
                cur = next
                # print(cur.val)
            cur.next = head 
        # else:
        #     # print(origin_head.val)
        #     cur.next = origin_head
        # # print(head.val)
    return new_head
"""

def reverseKGroup(head, k):
    
    dummy = ListNode(0)
    dummy.next = head
    prev_group_tail = dummy

    while True:

        check = prev_group_tail
        for _ in range(k):
            check = check.next
            if not check:
                return dummy.next
        
        group_head = prev_group_tail.next
        next_group_head = check.next

        prev, curr = None, group_head
        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
    
        # 拼接：prev 是新头，group_head 是新尾
        prev_group_tail.next = prev       # 上一组的尾 -> 本组新头
        group_head.next = next_group_head # 本组新尾 -> 下一组头

        prev_group_tail = group_head  # 移动到下一组
            

# ─────────────────────────────────────────────
# 工具函数：方便测试
# ─────────────────────────────────────────────

def make_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def list_to_arr(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1]),
        ([1], 1, [1]),
    ]

    for arr, k, expected in test_cases:
        head = make_list(arr)
        result_node = reverseKGroup(head, k)
        result = list_to_arr(result_node)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {arr}, k={k}")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}\n")
