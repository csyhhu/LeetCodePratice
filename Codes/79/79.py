def exist_TLE(board, word: str):


    n, m = len(board), len(board[0])

    def dfs(board, x, y, subword, visit):

        if len(subword) == 0:
            return True

        # print(x, y)
        result = False
        if x - 1 >= 0 and visit[x - 1][y] == False and subword[0] == board[x - 1][y]:
            visit[x-1][y] = True
            result |= dfs(board, x - 1, y, subword[1:], visit)
            visit[x - 1][y] = False
        if x + 1 < n and visit[x + 1][y] == False and subword[0] == board[x + 1][y]:
            visit[x + 1][y] = True
            result |= dfs(board, x + 1, y, subword[1:], visit)
            visit[x + 1][y] = False
        if y - 1 >= 0 and visit[x][y - 1] == False and subword[0] == board[x][y - 1]:
            visit[x][y - 1] = True
            result |= dfs(board, x, y - 1, subword[1:], visit)
            visit[x][y - 1] = False
        if y + 1 < m and visit[x][y + 1] == False and subword[0] == board[x][y + 1]:
            visit[x][y + 1] = True
            result |= dfs(board, x, y + 1, subword[1:], visit)
            visit[x][y + 1] = False
        return result

    start = word[0]
    # visit = [([False] * m).copy()] * n
    visit = [[False] * m for _ in range(n)]
    # print(visit)
    for i in range(0, n):
        for j in range(0, m):
            if board[i][j] == start:
                visit[i][j] = True
                result = dfs(board, i, j, word[1:], visit)
                visit[i][j] = False
                if result:
                    return True
    return False

def exist(board, word: str):
    n, m = len(board), len(board[0])

    def dfs(steps, x, y):
        # print(x, y)
        if steps == len(word):
            return True

        if 0 <= x < n and 0 <= y < m and board[x][y] == word[steps]:
            cur = board[x][y]
            board[x][y] = ' '
            found = dfs(steps + 1, x - 1, y) or dfs(steps + 1, x + 1, y) or dfs(steps + 1, x, y - 1) or dfs(steps + 1, x, y + 1)
            board[x][y] = cur
            return found

        return False

    for i in range(0, n):
        for j in range(0, m):
            if dfs(0, i, j):
                return True
    return False


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"
print(exist(board, word))
word = "SEE"
print(exist(board, word))
word = "ABCB"
print(exist(board, word))