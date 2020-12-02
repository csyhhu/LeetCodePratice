def findWords(board, words):

    class Trie:
        def __init__(self):
            self.root = {}
            self.end = -1

        def insert(self, _word):
            curNode = self.root
            for c in _word:
                if not c in curNode:
                    curNode[c] = {}
                curNode = curNode[c]
            curNode[self.end] = True

    trie = Trie()
    for word in words:
        trie.insert(word)

    # print(trie.root)
    ans = []
    n, m = len(board), len(board[0])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * m for _ in range(n)]
    def dfs(x, y, _board, _trie, _ans, path, _visited):
        if -1 in _trie and path not in ans:
            ans.append(path)
            return

        for direction in directions:
            next_x = x + direction[0]
            next_y = y + direction[1]
            if 0 <= next_x < n and 0 <= next_y < m and \
                    _board[next_x][next_y] in _trie and \
                    not _visited[next_x][next_y]:
                _visited[next_x][next_y] = True
                dfs(
                    next_x, next_y, _board,
                    _trie[_board[next_x][next_y]], _ans,
                    path+_board[next_x][next_y], _visited
                )
                _visited[next_x][next_y] = False

        return

    for i in range(n):
        for j in range(m):
            if board[i][j] in trie.root:
                visited[i][j] = True
                dfs(i, j, board, trie.root[board[i][j]], _ans=ans, path=board[i][j], _visited=visited)
                visited[i][j] = False

    return ans

# print(findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))
# print(findWords(board = [["a","b"],["c","d"]], words = ["abcb"]))
# print(findWords([["a","a"]], ["a"]))
print(findWords([["a","a"]], ["aaa"]))