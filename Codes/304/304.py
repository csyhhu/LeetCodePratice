class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        """
        self.row_prefix_sum = [0] * (self.n + 1)
        self.col_prefix_sum = [0] * (self.m + 1)

        for i in range(1, self.n + 1):
            self.row_prefix_sum[i] = self.row_prefix_sum[i-1] + sum(self.matrix[i-1, :])

        for j in range(1, self.m + 1):
            self.col_prefix_sum[j] = self.col_prefix_sum[j-1] + sum(self.matrix[:, j-1])
        """
        self.integral = [[0] * (self.m + 1) for _ in range(self.n + 1)]

        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                self.integral[i][j] = self.integral[i-1][j] + self.integral[i][j-1] - \
                                      self.integral[i-1][j-1] + self.matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        # print(self.integral[row2 + 1][col2 + 1], self.integral[row1][col2 + 1], self.integral[row2 + 1][col1], self.integral[row1][col1])
        return self.integral[row2 + 1][col2 + 1] - self.integral[row1][col2 + 1] - self.integral[row2 + 1][col1] + self.integral[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))