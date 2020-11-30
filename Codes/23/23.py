# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists) -> ListNode:

    merged_list = ListNode(0)
    start = [l.val for l in lists]
    # mid = lists
    for l in lists:
        pass