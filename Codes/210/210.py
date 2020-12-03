def findOrder(numCourses, prerequisites):

    order = []
    zeroDegree = []

    indegree = dict()
    from collections import defaultdict
    graph = defaultdict(list)
    for cur, prev in prerequisites:
        if prev not in indegree:
            indegree[prev] = 0
        if cur not in indegree:
            indegree[cur] = 1
        else:
            indegree[cur] += 1
        graph[prev].append(cur)
    # print(graph)
    # print(indegree)
    for node, degree in indegree.items():
        if degree == 0:
            zeroDegree.append(node)

    # print(zeroDegree)

    while len(zeroDegree) != 0:
        prev = zeroDegree.pop(0)
        if prev not in order:
            order.append(prev)
        for cur in graph[prev]:
            if cur in indegree:
                indegree[cur] -= 1
                if indegree[cur] == 0:
                    zeroDegree.append(cur)
                    order.append(cur)
                    # indegree.pop(cur)
        # print('In Degree:', indegree)
        # print('Zero Degree:', zeroDegree)
        # print('Current Order: ', order)
        # print('---------')

    if len(order) != numCourses:
        return []
    else:
        return order


def findOrder2(numCourses, prerequisites):
    """
    Topological Sort
    :param numCourses:
    :param prerequisites:
    :return:
    """
    from collections import defaultdict
    indegree = defaultdict(int)
    for i in range(numCourses):
        indegree[i] = 0

    graph = defaultdict(list)

    for cur, prev in prerequisites:
        indegree[cur] += 1
        graph[prev].append(cur)

    zeroDegree = []
    order = []
    for node, degree in indegree.items():
        if degree == 0:
            zeroDegree.append(node)

    while len(zeroDegree) != 0:
        prev = zeroDegree.pop(0)
        if prev not in order:
            order.append(prev)
        for cur in graph[prev]:
            if cur in indegree:
                indegree[cur] -= 1
                if indegree[cur] == 0:
                    zeroDegree.append(cur)
                    order.append(cur)

    if len(order) != numCourses:
        return []
    else:
        return order


def findOrder3(numCourses, prerequisites):
    from collections import defaultdict
    graph = defaultdict(list)
    visit = [0] * numCourses # 0: non-visit, 1: visiting, 2: visited
    for cur, prev in prerequisites:
        graph[prev].append(cur)

    order = []

    def dfs(order, visit, graph, node):

        if visit[node] == 2:
            return True
        if visit[node] == 1:
            return False

        visit[node] = 1

        for next_node in graph[node]:
            return dfs(order, visit, graph, next_node)

        visit[node] = 2
        order.append(node)

        return True

    for i in range(numCourses):
        # print(i)
        if not dfs(order, visit, graph, i):
            return []

    return order

# There are a total of n courses you have to take, labeled from 0 to n-1.

solution = findOrder3
print(solution(4, [[1,0],[2,0],[3,1],[3,2]]))
print(solution(2, [[1,0]]))
print(solution(3, [[1,0]]))
print(solution(1, []))

