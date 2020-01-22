# def numSquares(n: int):
#     import numpy as np
#     left = n - np.power(int(np.sqrt(n)), 2)
#     print(left)
#     count = 1
#     while left > 3:
#         left = left - np.power(int(np.sqrt(left)), 2)
#         print(left)
#         count += 1
#     count += left
#     return count

def numSquares(n):
    import numpy as np
    # stack = []
    min_count = [1e9]

    def dfs(left, count):
        # print(left)
        if left == 0:
            if count < min_count[0]:
                min_count[0] = count
            return

        for i in range(1, int(np.sqrt(left)) + 1):
            # print('I am here')
            # stack.append(i)
            # cur_count = dfs(left - np.power(i, 2), count + 1)
            dfs(left - np.power(i, 2), count + 1)
            # stack.pop()
            # if cur_count < min_count:
            #     min_count = cur_count

    dfs(n, 0)
    return min_count[0]


def numSquares2(n):
    import numpy as np
    # stack = []
    min_count = [0, 1, 2]
    for left in range(3, n + 1):
        cur_min_count = 1e9
        # print('left: %d' %left)
        for i in range(1, int(np.sqrt(left)) + 1):
            # print('i: %d' %i)
            cur_count = min_count[left - i ** 2] + 1
            if cur_min_count > cur_count:
                cur_min_count = cur_count
        min_count.append(cur_min_count)
        print(min_count)
    return min_count[n]

inputs = 12
print(numSquares2(inputs))