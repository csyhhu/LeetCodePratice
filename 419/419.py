def countBattleships(board):

    def change_surrounding(startx, starty, boa):

        dfs = [(startx, starty)]
        while len(dfs) > 0:
            cur_x, cur_y = dfs.pop(0)
            boa[cur_x][cur_y] = '.'
            direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            for direc in direction:
                next_x, next_y = cur_x + direc[0], cur_y + direc[1]
                if next_x >= 0 and next_y >= 0 and next_x < len(boa) and next_y < len(boa[0]):
                    if boa[next_x][next_y] == 'X':
                        dfs.append((next_x, next_y))

    n_row, n_col = len(board), len(board[0])
    results = 0
    for row_idx in range(n_row):
        for col_idx in range(n_col):
            if board[row_idx][col_idx] == 'X':
                results += 1
                change_surrounding(row_idx, col_idx, board)

    return results


def countBattleships2(board):

    """
    An optimized version, which only finds the starting point of battleship
    :param board:
    :return:
    """
    n_row, n_col = len(board), len(board[0])
    results = 0
    for row_idx in range(n_row):
        for col_idx in range(n_col):
            if board[row_idx][col_idx] == 'X':
                """
                If it is a starting point, then there is not X on its left and top. For the searching direction is from left to right, top to bottom
                """
                if row_idx > 0 and board[row_idx - 1][col_idx] == 'X':
                    continue
                elif col_idx > 0 and board[row_idx][col_idx - 1] == 'X':
                    continue
                else:
                    results += 1
    return results