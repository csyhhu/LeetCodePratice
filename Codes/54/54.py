def spiralOrder(matrix):

    if len(matrix) == 0:
        return []

    n, m = len(matrix), len(matrix[0])
    # print(n, m)
    visited = [[False] * m for _ in range(n)]
    n_visit = 0
    cur = (0, 0)
    direction = (0, 1)
    sprial_order = []
    while True:
        sprial_order.append(matrix[cur[0]][cur[1]])
        visited[cur[0]][cur[1]] = True
        n_visit += 1
        if n_visit == m * n:
            break
        next_pos = (cur[0] + direction[0], cur[1] + direction[1])
        # If bomp into boundary, change direction
        # print(next_pos)
        if next_pos[0] < 0 or next_pos[0] >= n or next_pos[1] < 0 or next_pos[1] >= m or visited[next_pos[0]][next_pos[1]]:
            if direction == (0, 1):
                direction = (1, 0)
            elif direction == (1, 0):
                direction = (0, -1)
            elif direction == (0, -1):
                direction = (-1, 0)
            elif direction == (-1, 0):
                direction = (0, 1)
        cur = (cur[0] + direction[0], cur[1] + direction[1])
    return sprial_order

inputs = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
# print(spiralOrder(inputs))

inputs = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(spiralOrder(inputs))