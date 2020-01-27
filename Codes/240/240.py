def searchMatrix(matrix, target):

    if len(matrix) == 0:
        return False

    n_row, n_col = len(matrix), len(matrix[0])
    row_idx = 0
    col_idx = n_col - 1

    while row_idx <= n_row - 1 and col_idx >= 0:

        if matrix[row_idx][col_idx] == target:
            return True
        elif matrix[row_idx][col_idx] < target:
            row_idx += 1
        else:
            col_idx -= 1

    return False

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
print(searchMatrix(matrix, target))