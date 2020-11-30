def longestIncreasingPath_WA(matrix):

    if len(matrix) == 0:
        return 0

    n, m = len(matrix), len(matrix[0])
    # print(n, m)
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    numSteps = [[1] * m for _ in range(n)]
    ans = 0

    def dfs(x, y, _numSteps, reverse=False):

        for dir_x, dir_y in directions:
            next_x, next_y = x + dir_x, y + dir_y
            # if 0 <= next_x < n and 0 <= next_y  < m and \
            #         (matrix[next_x][next_y] > matrix[x][y] if not reverse else matrix[next_x][next_y] < matrix[x][y]):
            # # if 0 <= next_x < n and 0 <= next_y < m and matrix[next_x][next_y] > matrix[x][y]:
            #     if matrix[next_x][next_y] == 0:
            #         dfs(next_x, next_y, _numSteps)
            #         _numSteps[x][y] = max(_numSteps[next_x][next_y] + 1, _numSteps[x][y])
            #     else:
            #         _numSteps[x][y] = max(_numSteps[next_x][next_y] + 1, _numSteps[x][y])
            #     # global ans
            #     # ans = max(_numSteps[x][y], ans)
            if 0 <= next_x < n and 0 <= next_y  < m:
                if not reverse:
                    if matrix[next_x][next_y] > matrix[x][y]:
                        if matrix[next_x][next_y] == 0:
                            dfs(next_x, next_y, _numSteps)
                        _numSteps[x][y] = max(_numSteps[next_x][next_y] + 1, _numSteps[x][y])
                else:
                    if matrix[next_x][next_y] > matrix[x][y]:
                        dfs(next_x, next_y, _numSteps)
                    _numSteps[x][y] = max(_numSteps[next_x][next_y], _numSteps[x][y])

    for i in range(n):
        for j in range(m):
            dfs(i, j, numSteps)

    print(numSteps)

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            dfs(i, j, numSteps, reverse=True)

    # return ans
    print(numSteps)
    return max(max(numSteps))


def longestIncreasingPath(matrix):

    if len(matrix) == 0:
        return 0

    n, m = len(matrix), len(matrix[0])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    numSteps = [[0] * m for _ in range(n)]
    ans = 0

    def dfs(x, y):
        if numSteps[x][y] != 0:
            return numSteps[x][y]
        local_ans = 1
        for dir_x, dir_y in directions:
            next_x, next_y = x + dir_x, y + dir_y
            if 0 <= next_x < n and 0 <= next_y < m and matrix[next_x][next_y] > matrix[x][y]:
                local_ans = max(dfs(next_x, next_y) + 1, local_ans)
        numSteps[x][y] = local_ans
        return numSteps[x][y]

    for i in range(n):
        for j in range(m):
            ans = max(dfs(i, j), ans)

    return ans

print(longestIncreasingPath(matrix =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] ))

print(longestIncreasingPath(matrix =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] ))

print(longestIncreasingPath([[1,2]]))

print(longestIncreasingPath([[7,7,5],[2,4,6],[8,2,0]]))