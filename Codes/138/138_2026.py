"""
[138] Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list of length n is given such that each node contains:
- val: an integer value
- next: pointer to the next node
- random: pointer to any node in the list or null

Return a deep copy of the list.

Example 1:
    Input:  head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
    Input:  head = [[1,1],[2,1]]
    Output: [[1,1],[2,1]]

Example 3:
    Input:  head = []
    Output: []

Constraints:
    - 0 <= n <= 1000
    - -10^4 <= Node.val <= 10^4
    - Node.random is null or points to a node in the list

Date: 2026-04-28
"""


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random



def copyRandomList(head: "Node") -> "Node":
    """
    TODO: Implement your solution.

    Suggested directions:
    1) Hash map: old_node -> new_node
    2) O(1) extra space interleaving trick

    Time target: O(n)
    Space target: O(n) or O(1) extra (advanced)
    """
    cur = head
    new_head = Node(cur.val, next=cur.next, random=cur.random)
    cur_new = new_head
    while cur:
        # print(cur.val, cur.random)
        # cur = cur.next
        # """
        cur_new.next = Node(cur.val, next=cur.next, random=cur.random)
        cur = cur.next
        cur_new = cur_new.next
        # """
    return new_head


# -------------------------
# Helpers for local testing
# -------------------------

def build_list(spec):
    """
    Build linked list from LeetCode-style spec:
    spec[i] = [val, random_index]
    """
    if not spec:
        return None

    nodes = [Node(val) for val, _ in spec]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    for i, (_, random_idx) in enumerate(spec):
        nodes[i].random = nodes[random_idx] if random_idx is not None else None

    return nodes[0]


def to_spec(head):
    """Serialize linked list to LeetCode-style spec for quick compare."""
    if not head:
        return []

    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next

    idx = {node: i for i, node in enumerate(nodes)}
    ans = []
    for node in nodes:
        random_idx = idx[node.random] if node.random is not None else None
        ans.append([node.val, random_idx])
    return ans


if __name__ == "__main__":
    test_cases = [
        (
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        ),
        (
            [[1, 1], [2, 1]],
            [[1, 1], [2, 1]],
        ),
        (
            [],
            [],
        ),
    ]

    print("=" * 70)
    print("LeetCode 138 - Copy List with Random Pointer")
    print("=" * 70)

    for i, (spec, expected) in enumerate(test_cases, 1):
        head = build_list(spec)
        copied = copyRandomList(head)
        result = to_spec(copied)
        status = "TODO" if copied is None and spec else ("PASS" if result == expected else "FAIL")

        print(f"Case {i}: {status}")
        print(f"  input={spec}")
        print(f"  expected={expected}")
        print(f"  got={result}")
        print()
