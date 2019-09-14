def allPathsSourceTarget(graph):
    import copy
    n_node = len(graph)
    dfs = []
    visit = [0] * n_node
    visit[0] = 1
    dfs.append([[0], visit])
    results = []
    while len(dfs) != 0:
        trace, vis = dfs.pop()
        # print(trace)
        # print(vis)
        cur_pos = trace[-1]
        for possible_pos in graph[cur_pos]:
            if possible_pos == (n_node-1):
                results_trace = copy.deepcopy(trace)
                results_trace.append(n_node-1)
                results.append(results_trace)
                continue
            if vis[possible_pos] == 0:
                next_vis = copy.deepcopy(vis)
                next_vis[possible_pos] = 1
                next_trace = copy.deepcopy(trace)
                next_trace.append(possible_pos)
                # print(trace)
                # print(possible_pos)
                # print(next_trace)
                dfs.append([next_trace, next_vis])
    return results

# inputs = [[1,2], [3], [3], []]
inputs = [[4,3,1],[3,2,4],[3],[4],[]]
outputs = allPathsSourceTarget(inputs)
print(outputs)
