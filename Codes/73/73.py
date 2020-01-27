def setZeroes(matrix):
    rowFlag = False # Whether the first row contain 0
    colFlag = False #
    n, m = len(matrix), len(matrix[0])

    for j in range(m):
        if matrix[0][j] == 0:
            rowFlag = True
            break
    for i in range(n):
        if matrix[i][0] == 0:
            colFlag = True
            break

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, n):
        for j in range(1, m):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    if rowFlag:
        for j in range(0, m):
            matrix[0][j] = 0

    if colFlag:
        for i in range(0, n):
            matrix[i][0] = 0

# inputs = [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# setZeroes(inputs)
# print(inputs)

inputs = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
setZeroes(inputs)
print(inputs)