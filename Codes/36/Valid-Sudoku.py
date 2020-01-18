def isValidSudoku(board):
    isValid = True
    # Check row
    n_row, n_col = len(board), len(board[0])
    for row in range(n_row):
        numbers = [0] * n_row
        for col in range(n_col):
            num = board[row][col]
            if num != '.':
                if numbers[int(num) - 1] == 0:
                    numbers[int(num) - 1] += 1
                else:
                    isValid = False
                    break
        if not isValid:
            return isValid
    # Check col
    for col in range(n_col):
        numbers = [0] * n_col
        for row in range(n_row):
            num = board[row][col]
            if num != '.':
                if numbers[int(num) - 1] == 0:
                    numbers[int(num) - 1] += 1
                else:
                    isValid = False
                    break
        if not isValid:
            return isValid
    # Check sub-boxes
    len_boxes = 3
    n_sub_boxes_row = int(n_row / len_boxes)
    n_sub_boxes_col = int(n_col / len_boxes)
    for sub_boxes_row_idx in range(n_sub_boxes_row):
        for sub_boxes_col_idx in range(n_sub_boxes_col):
            numbers = [0] * len_boxes * len_boxes
            startX = sub_boxes_row_idx * 3
            startY = sub_boxes_col_idx * 3
            for row in range(startX, startX + len_boxes):
                for col in range(startY, startY + len_boxes):
                    num = board[row][col]
                    if num != '.':
                        if numbers[int(num) - 1] == 0:
                            numbers[int(num) - 1] += 1
                        else:
                            isValid = False
                            break
                if not isValid:
                    return isValid
    return isValid

# inputs = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
inputs = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(isValidSudoku(inputs))