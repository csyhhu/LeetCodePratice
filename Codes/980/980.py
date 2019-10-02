from queue import Queue

def uniquePathsIII(grid):
    import copy
    width, height = len(grid[0]), len(grid)
    print(width, height)

    visit = [ [0] * width ] * height
    n_obstacles = 0
    n_totals = width * height
    # bfs = Queue()
    dfs = []
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                startx=i
                starty=j
            elif grid[i][j] == -1:
                n_obstacles += 1

    visit[startx][starty] = 1
    # bfs.put([startx, starty, visit, 1])
    dfs.append([startx, starty, visit, 1])
    results = 0

    while len(dfs) > 0:
        cur_x, cur_y, vis, n_walk = dfs.pop()
        print(len(dfs), cur_x, cur_y, n_walk)
        if grid[cur_x][cur_y] == 2 and n_walk == (n_totals-n_obstacles):
            results += 1
            continue

        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for dir_x, dir_y in direction:
            next_x = cur_x + dir_x
            next_y = cur_y + dir_y
            print('Candidate pos: %d, %d' %(next_x, next_y))
            if (next_x >= 0) and (next_x < width) and (next_y >= 0) and (next_y < height) and \
                vis[next_x][next_y] == 0 and grid[next_x][next_y] != -1:

                next_vis = copy.deepcopy(vis)
                next_vis[next_x][next_y] = 1
                dfs.append([next_x, next_y, next_vis, n_walk+1])
                print('New pos inserted as %d, %d' %(next_x, next_y))

    return results


grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
results = uniquePathsIII(grid)
print(results)