"""
LeetCode 1104 - Path In Zigzag Labelled Binary Tree (MEDIUM)
Meta Interview - DFS/Tree Navigation

Problem Description:
In an infinite binary tree where every node has two children,
the nodes are labelled in level order with a zigzag pattern:

- Level 1 (odd): 1
- Level 2 (even, reverse): 3, 2
- Level 3 (odd): 4, 5, 6, 7
- Level 4 (even, reverse): 15, 14, 13, 12, 11, 10, 9, 8
- Level 5 (odd): 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31

For example:
          1
       /     \
      3       2
    /  \    /   \
   4    5  6     7
 / \ / \ / \ / \
15 14 13 12 11 10 9 8

The tree is numbered level by level. Within odd levels, nodes are numbered 
left to right. Within even levels, nodes are numbered right to left.

Given the label of a node in this tree, return the labels in the path from
the root of the tree to the node with the given label.

Input:
- label: int - the label of the target node (1 <= label <= 10^6)

Output:
- List[int] - labels from root to the target node

Constraints:
- 1 <= label <= 10^6

Examples:

Example 1:
Input: label = 14
Output: [1, 3, 7, 14]
Explanation:
          1
       /     \
      3       2
    /  \    /   \
   4    5  6     7
 / \ / \ / \ / \
15 14 13 12 11 10 9 8

Path: 1 → 3 → 7 → 14
- 14 is a node in level 4 (even, reversed)
- Its parent is 7 (label 7 in level 3)
- 7's parent is 3 (label 3 in level 2)
- 3's parent is 1 (label 1 in level 1)

Example 2:
Input: label = 26
Output: [1, 2, 4, 8, 16, 26]
Explanation:
Path from root 1 to node 26. Node 26 is in level 5 (odd).
- 26 is in level 5 (odd, left to right): 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
- Parent of 26 in standard binary tree: 26 // 2 = 13
- Adjust 13 for zigzag: 13 is in level 4 (even, reversed), so we find its position
  and map it to its actual parent, which is 16
- Continue upward: 16 → 8 → 4 → 2 → 1

Example 3:
Input: label = 1
Output: [1]

Example 4:
Input: label = 8
Output: [1, 2, 4, 8]

Hint 1: The key is to find the parent of a given node in the zigzag tree.
Hint 2: Each node has a standard binary tree parent at node // 2.
Hint 3: For a node at an even level (reversed), you need to adjust the parent
        based on the zigzag pattern within that level.
"""


def pathInZigZagTree(label):
    """
    Find path from root to target node in zigzag labeled binary tree.
    
    Algorithm:
    1. Find the current level of the label
    2. Work backwards level by level until reaching root (label 1)
    3. For each level, calculate the parent using:
       - Get the standard binary tree parent: parent = label // 2
       - Find which level the parent is in
       - Since even levels are reversed, adjust the parent position within that level
       - The adjusted parent = level_sum - standard_parent
         where level_sum = 2^layer + 2^(layer+1) - 1
    4. Reverse the result path and return
    
    Time Complexity: O(log label) - at most log label iterations
    Space Complexity: O(log label) - for the result list
    """
    def find_layer(num, layer):
        """Find which level (0-indexed) a node belongs to."""
        if num >= 2**layer and num < 2**(layer + 1):
            return layer
        return find_layer(num, layer + 1)
    
    result = [label]
    layer = find_layer(label, 0)
    
    # Traverse from current level to root
    while layer > 0:
        layer -= 1
        fake_label = label // 2
        layer_sum = 2**layer + 2**(layer + 1) - 1
        label = layer_sum - fake_label
        result.append(label)
        print(layer, layer_sum, fake_label, label)
    
    return result[::-1]


# Test cases
if __name__ == "__main__":
    # Test case 1: LeetCode example 1 - Node 14 (level 4, even/reversed)
    print("=" * 50)
    print("Test Case 1: label = 14")
    print("=" * 50)
    label1 = 14
    result1 = pathInZigZagTree(label1)
    print(f"Output: {result1}")
    print(f"Expected: [1,3,4,14]")
    print(f"✓ PASS" if result1 == [1,3,4,14] else "✗ FAIL")
    print()
    

    print("=" * 50)
    print("Test Case 1: label = 16")
    print("=" * 50)
    label1 = 16
    result1 = pathInZigZagTree(label1)
    print(f"Output: {result1}")
    print(f"Expected: [1,3,4,15,16]")
    print(f"✓ PASS" if result1 == [1,3,4,15,16] else "✗ FAIL")
    print()
    
