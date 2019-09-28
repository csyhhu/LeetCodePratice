class Solution:

    def regionsBySlashes(self, grid):

        N = len(grid)
        self.n_count = 4 * N * N
        self.parent = list()
        # self.rank = [0] * (self.n_count)
        for i in range(self.n_count):
            self.parent.append(i)

        for row_idx in range(N):
            for col_idx in range(N):
                root_idx = row_idx * (4 * N) + col_idx * 4
                #
                if row_idx > 0:
                    self.union(root_idx + 0, root_idx - 4 * N + 2)
                    # self.union(root_idx + 2, root_idx + 4 * N + 0)
                # if row_idx < N - 1:
                #     self.union(root_idx + 2, root_idx + 4 * N + 0)

                if col_idx > 0:
                    self.union(root_idx + 3, root_idx - 4 + 1)

                # if col_idx < N - 1:
                #     self.union(root_idx + 1, root_idx + 4 + 3)

                if grid[row_idx][col_idx] == '\\':
                    self.union(root_idx + 0, root_idx + 1)
                    self.union(root_idx + 2, root_idx + 3)

                if grid[row_idx][col_idx] == '/':
                    self.union(root_idx + 1, root_idx + 2)
                    self.union(root_idx + 0, root_idx + 3)

        # return self.n_count
        return sum(self.parent[i] == i for i in range(N * N * 4) )

    def union(self, idx1, idx2):
        idx1 = self.find(idx1)
        idx2 = self.find(idx2)
        # if self.rank[idx1] == self.rank[idx2]:
        #     self.parent[idx2] = idx1
        #     self.rank[idx1] += 1
        if idx1 == idx2:
            return
        else:
            self.parent[idx2] = idx1
        self.n_count -= 1

    def find(self, idx):

        if idx == self.parent[idx]:
            return idx
        else:
            return self.parent[idx]

s = Solution()
inputs = [
  "//",
  "/ "
]
outputs = s.regionsBySlashes(inputs)
print(outputs)
