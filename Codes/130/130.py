def solve(board):

    if len(board) == 0:
        return

    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    # print(visited)
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def dfs(stack, visited):
        trace = []
        flip = True
        while len(stack)> 0:
            x, y = stack.pop(-1)
            trace.append((x, y))
            # print(trace)
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                # print(new_x, new_y, visited[new_x][new_y])
                if 0 <= new_x < n and 0 <= new_y < m and visited[new_x][new_y] is False and board[new_x][new_y]in ['O', '#']:
                    # print(new_x, new_y)
                    visited[new_x][new_y] = True
                    stack.append((new_x, new_y))
                    if board[new_x][new_y] == '#':
                        flip = False
                        # print('No Flip')
        # print(flip)
        if flip:
            # print(trace)
            for x, y in trace:
                board[x][y] = 'X'

    for i in [0, n-1]:
        for j in range(m):
            if board[i][j] == 'O':
                board[i][j] = '#'
    for j in [0, m-1]:
        for i in range(n):
            if board[i][j] == 'O':
                board[i][j] = '#'

    # print(board)

    for i in range(1, n-1):
        for j in range(1, m-1):
            if board[i][j] == 'O' and visited[i][j] is False:
                stack = [(i, j)]
                visited[i][j] = True
                dfs(stack, visited)

    for i in [0, n-1]:
        for j in range(m):
            if board[i][j] == '#':
                board[i][j] = 'O'
    for j in [0, m-1]:
        for i in range(n):
            if board[i][j] == '#':
                board[i][j] = 'O'




# inputs = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
# inputs = [["O","O","O"],["O","O","O"],["O","O","O"]]

inputs = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]



solve(inputs)
print(inputs)