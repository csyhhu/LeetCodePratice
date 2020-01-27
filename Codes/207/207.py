def canFinish_(numCourses, prerequisites):
    def dfs(cur_pos, visit):
        visit[cur_pos] = -1
        # print(cur_pos, visit)
        for (cur, prereq) in prerequisites:
            if cur_pos == cur:
                if visit[prereq] == 0:
                    visit[prereq] = -1
                    dfs(prereq, visit)
                    visit[prereq] = 1
                elif visit[prereq] == 1:
                    return True
                else:
                    return False
        return True

    # result = True
    for cur, prereq in prerequisites:
        visit = [0] * numCourses
        if not dfs(prereq, visit):
            return False
        # visit[cur] = True
        # visit[prereq] = True
        # result = (result and dfs(prereq, visit))
    return True


def canFinish_dfs(numCourses, prerequisites):
    """
    visit[i] = 0: never visit; 1: visited and safe; -1: visiting
    :param numCourses:
    :param prerequisites:
    :return:
    """
    graph = dict()
    for start, end in prerequisites:
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
    # print(graph)

    def dfs(graph, cur_pos, visit):
        # print(cur_pos, visit)

        if visit[cur_pos] == -1:
            return False
        elif visit[cur_pos] == 1:
            return True

        # Mark it as visiting
        visit[cur_pos] = -1
        # If it has no prerequist, set it as 1 and return True
        if cur_pos not in graph:
            visit[cur_pos] = 1
            return True
        # If it has prerequist, dfs its prerequists. If any of its prerequists fails, it remain -1. Otherwise, set it to 1
        else:
            for end in graph[cur_pos]:
                if not dfs(graph, end, visit):
                    return False
            visit[cur_pos] = 1
            return True

    visit = [0] * numCourses
    for start in graph.keys():
        if not dfs(graph, start, visit):
            return False
    return True


def canFinish(numCourses, prerequisites):
    graph = dict()
    indegree = [0] * numCourses
    for start, end in prerequisites:
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
        indegree[end] += 1

    import queue
    q = queue.Queue()
    for i in range(numCourses):
        if indegree[i] == 0:
            q.put(i)

    while not q.empty():
        cur_node = q.get()
        if cur_node in graph:
            for end in graph[cur_node]:
                indegree[end] -= 1
                if indegree[end] == 0:
                    q.put(end)

    if sum(indegree) == 0:
        return True
    else:
        return False



print(canFinish(2, [[1,0]]))
print(canFinish(2, [[1,0],[0,1]]))
print(canFinish(3, [[1,0],[0,2],[2,1]]))
print(canFinish(3, [[1,0],[2,0]]))