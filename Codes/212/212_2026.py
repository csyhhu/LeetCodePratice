"""
LeetCode 212 - Word Search II (HARD)
Meta Interview Classic - DFS + Trie

Problem Description:
Given an m x n board of characters and a list of strings words, 
return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in one word.

Input:
- board: List[List[str]] - m x n grid of characters
- words: List[str] - list of words to search for

Output:
- List[str] - all words found on the board

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters
- All the strings of words are unique

Examples:

Example 1:
Input: board = [["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","p"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Explanation:
- "oath" is found at (0,0) → (0,1) → (0,2) → (1,2)
- "eat" is found at (0,1) → (1,0) → (0,2)

Grid visualization:
  o a a n
  e t a e
  i h k r
  i f l p

Example 2:
Input: board = [["a","b"],
                ["c","d"]], words = ["abcb"]
Output: []
Explanation: "abcb" cannot be formed because 'b' can only be used once

Example 3:
Input: board = [["a","a"]], words = ["a"]
Output: ["a"]

Example 4:
Input: board = [["a","a"],
                ["a","a"],
                ["a","a"]], words = ["aaa","aaaa","aaaaaa","aaaaaaa","aaaaaaaaa"]
Output: ["aaa","aaaa","aaaaaa","aaaaaaa"]
Explanation: All reachable combinations of 'a's

Hint 1: You would need to optimize your backtracking to pass the test cases. 
        Could you stop backtracking earlier?

Hint 2: If you stop backtracking when there is no word in all remaining words 
        that starts with the current prefix, you could optimize it well.

Hint 3: The words should be indexed by the Trie tree, to optimize the 
        backtracking procedure.
"""


from asyncio import FastChildWatcher


class TrieNode:
    """
    Trie node for storing word prefixes.
    This helps optimize DFS by pruning non-existent words early.
    """
    def __init__(self):
        self.children = {}
        self.word = ""  # Store the complete word here when we find it
    """
    def display(self):
        root = self
        while root is not None:
            print(root.word)
            for child in root.children:
                child.display()
    """


def findWords_v0(board, words):
    """
    Find all words from the word list that exist on the board using DFS + Trie.
    
    Strategy:
    1. Build a Trie from all words for efficient prefix checking
    2. For each cell on the board, perform DFS with backtracking
    3. At each step, check if current path exists as a prefix in Trie
    4. If we find a complete word, add it to results
    5. Backtrack: restore the cell state and try other directions
    
    Time Complexity: O(N * 4^L) where N is board size, L is max word length
    Space Complexity: O(W * L) where W is number of words, L is word length (for Trie)
    
    Args:
        board: 2D list of characters
        words: List of words to find
        
    Returns:
        List of found words
    """
    def dfs(_board, _cur_i, _cur_j, _visited, _trie):
        
        if _visited[_cur_i][_cur_j]:
            return
        
        _cur_char = _board[_cur_i][_cur_j]
        _cur_trie = TrieNode()
        _cur_trie.word = _cur_char
        _trie.children.append(_cur_trie)

        if _cur_i - 1 >= 0:
            _visited[_cur_i][_cur_j] = True
            dfs(_board, _cur_i - 1, _cur_j, _visited, _trie.children[-1])
            _visited[_cur_i][_cur_j] = False
        if _cur_i + 1 < len(_board[0]):
            _visited[_cur_i][_cur_j] = True
            dfs(_board, _cur_i + 1, _cur_j, _visited, _trie.children[-1])
            _visited[_cur_i][_cur_j] = False
        if _cur_j - 1 >= 0:
            _visited[_cur_i][_cur_j] = True
            dfs(_board, _cur_i, _cur_j - 1, _visited, _trie.children[-1])
            _visited[_cur_i][_cur_j] = False
        if _cur_j + 1 < len(_board):
            _visited[_cur_i][_cur_j] = True
            dfs(_board, _cur_i, _cur_j + 1, _visited, _trie.children[-1])
            _visited[_cur_i][_cur_j] = False


    visited = [[False] * len(board)] * len(board[0])
    trie = TrieNode()
    dfs(board, 0, 0, visited, trie)

    trie.display()

    result = []
    for word in words:
        cur_trie = trie
        flag = True
        for char in word:
            if char != cur_trie.word and cur_trie.word != None:
                break
            for next_trie in cur_trie.children:
                if next_trie.word == char:
                    cur_trie = next_trie

        if flag:
            result.append(word)


def findWords(board, words):

    def dfs(_board, _cur_i, _cur_j, _visited, _trie, _target):
        
        if _visited[_cur_i][_cur_j]:
            return
        if _trie.word == _target:
            return True
        
        _visited[_cur_i][_cur_j] = True
        if _cur_i - 1 >= 0:
            if _board[_cur_i - 1][_cur_j] in _trie.children:
                return dfs(_board, _cur_i - 1, _cur_j, _visited, _trie.children[_board[_cur_i - 1][_cur_j]], _target)
        if _cur_i + 1 < len(_board):
            if _board[_cur_i + 1][_cur_j] in _trie.children:
                return dfs(_board, _cur_i + 1, _cur_j, _visited, _trie.children[_board[_cur_i + 1][_cur_j]], _target)
        if _cur_j - 1 >= 0:
            if _board[_cur_i][_cur_j - 1] in _trie.children:
                return dfs(_board, _cur_i, _cur_j - 1, _visited, _trie.children[_board[_cur_i][_cur_j - 1]], _target)
        if _cur_j + 1 < len(_board[0]): 
            if _board[_cur_i][_cur_j + 1] in _trie.children:
                return dfs(_board, _cur_i, _cur_j + 1, _visited, _trie.children[_board[_cur_i][_cur_j + 1]], _target)
        _visited[_cur_i][_cur_j] = False

        return False


    result = []
    for word in words:
        trie = TrieNode()
        for char in word:
            trie.word += char
            next_trie = TrieNode()
            trie.children[char] = next_trie
            trie = next_trie

        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, visited, trie, word):
                    result.append(word)
                    break
    
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: Multiple words to find
    board1 = [["o","a","a","n"],
              ["e","t","a","e"],
              ["i","h","k","r"],
              ["i","f","l","p"]]
    words1 = ["oath","pea","eat","rain"]
    print("Test 1:")
    print("Board:")
    for row in board1:
        print(row)
    print(f"Words: {words1}")
    result1 = findWords(board1, words1)
    print(f"Output: {sorted(result1)}")
    print(f"Expected: ['eat', 'oath'] (order may vary)")
    print()
    
    # Test case 2: No words found
    board2 = [["a","b"],
              ["c","d"]]
    words2 = ["abcb"]
    print("Test 2:")
    print("Board:")
    for row in board2:
        print(row)
    print(f"Words: {words2}")
    result2 = findWords(board2, words2)
    print(f"Output: {result2}")
    print(f"Expected: []")
    print()
    
    # Test case 3: Single character
    board3 = [["a","a"]]
    words3 = ["a"]
    print("Test 3:")
    print("Board:")
    for row in board3:
        print(row)
    print(f"Words: {words3}")
    result3 = findWords(board3, words3)
    print(f"Output: {result3}")
    print(f"Expected: ['a']")
    print()
    
    # Test case 4: All same characters
    board4 = [["a","a"],
              ["a","a"],
              ["a","a"]]
    words4 = ["aaa","aaaa","aaaaaa","aaaaaaa","aaaaaaaaa"]
    print("Test 4:")
    print("Board:")
    for row in board4:
        print(row)
    print(f"Words: {words4}")
    result4 = findWords(board4, words4)
    print(f"Output: {sorted(result4)}")
    print(f"Expected: ['aaa', 'aaaa', 'aaaaaa', 'aaaaaaa']")
    print()
    
    # Test case 5: Words with common prefixes
    board5 = [["a","b"],
              ["a","a"]]
    words5 = ["aba","baa","ab","ba","aa"]
    print("Test 5:")
    print("Board:")
    for row in board5:
        print(row)
    print(f"Words: {words5}")
    result5 = findWords(board5, words5)
    print(f"Output: {sorted(result5)}")
    print(f"Expected: Found words may vary, but should be reasonable paths")
    print()
    
    # Test case 6: Empty words list
    board6 = [["a","b"],
              ["c","d"]]
    words6 = []
    print("Test 6:")
    print("Board:")
    for row in board6:
        print(row)
    print(f"Words: {words6}")
    result6 = findWords(board6, words6)
    print(f"Output: {result6}")
    print(f"Expected: []")
