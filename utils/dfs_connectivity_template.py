"""
标准DFS连通性检查模板
用于判断图是否连通或能否从某个起点访问所有节点
"""

# ============================================================
# 方案1：基础DFS（检查从start能到达多少个节点）
# ============================================================

def dfs_count_reachable_basic(graph, start, n, exclude_edge=None):
    """
    基础DFS：计算从start能到达的节点数
    
    Args:
        graph: 邻接表表示的图 {node: set(neighbors)}
        start: 起点
        n: 总节点数 (0 到 n-1)
        exclude_edge: 需要排除的边 (a, b)，两个方向都会排除
        
    Returns:
        能到达的节点数
    """
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        count = 1  # 计算当前节点
        
        for neighbor in graph.get(node, set()):
            # 【关键】排除指定的边
            if exclude_edge:
                a, b = exclude_edge
                if (node == a and neighbor == b) or (node == b and neighbor == a):
                    continue
            
            # 【关键】只访问未访问过的邻接点
            if not visited[neighbor]:
                count += dfs(neighbor)
        
        return count
    
    return dfs(start)


def is_connected_basic(graph, n, exclude_edge=None):
    """
    判断图是否连通（排除指定边后）
    
    Args:
        graph: 邻接表
        n: 总节点数
        exclude_edge: 排除的边
        
    Returns:
        bool: 图是否连通
    """
    # 从任意节点（如0）出发，检查能否到达所有n个节点
    reachable_count = dfs_count_reachable_basic(graph, 0, n, exclude_edge)
    return reachable_count == n


# ============================================================
# 方案2：使用visited集合（更清晰的实现）
# ============================================================

def dfs_connectivity_with_set(graph, start, n, exclude_edge=None):
    """
    使用visited集合的DFS连通性检查
    """
    visited = set()
    
    def dfs(node):
        visited.add(node)
        
        for neighbor in graph.get(node, set()):
            # 排除指定的边
            if exclude_edge:
                a, b = exclude_edge
                if (node == a and neighbor == b) or (node == b and neighbor == a):
                    continue
            
            # 只访问未访问过的邻接点
            if neighbor not in visited:
                dfs(neighbor)
    
    dfs(start)
    return len(visited) == n  # 返回是否访问了所有节点


# ============================================================
# 方案3：迭代版本（避免递归深度问题）
# ============================================================

def dfs_connectivity_iterative(graph, start, n, exclude_edge=None):
    """
    迭代版本的DFS连通性检查（使用栈）
    """
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbor in graph.get(node, set()):
            # 排除指定的边
            if exclude_edge:
                a, b = exclude_edge
                if (node == a and neighbor == b) or (node == b and neighbor == a):
                    continue
            
            # 只访问未访问过的邻接点
            if neighbor not in visited:
                stack.append(neighbor)
    
    return len(visited) == n


# ============================================================
# 应用示例：查找所有关键连接（Bridge）
# ============================================================

def find_critical_connections(n, connections):
    """
    使用DFS连通性检查来找所有关键连接（桥）
    
    思路：对每条边进行删除测试，如果删除后图不连通，则该边是关键连接
    
    时间复杂度：O(E * (V + E)) - 对每条边删除并检查连通性
    """
    # 构建邻接表
    graph = {}
    for a, b in connections:
        if a not in graph:
            graph[a] = set()
        graph[a].add(b)
        
        if b not in graph:
            graph[b] = set()
        graph[b].add(a)
    
    result = []
    
    # 对每条边进行测试
    for a, b in connections:
        # 删除这条边后，检查图是否仍然连通
        if not dfs_connectivity_with_set(graph, 0, n, exclude_edge=(a, b)):
            # 如果不连通，说明这是一条关键连接
            result.append([a, b])
    
    return result


# ============================================================
# 测试用例
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("DFS连通性检查模板测试")
    print("=" * 60)
    
    # 测试用例1：简单连通图
    print("\n【测试1】简单连通图：0-1-2")
    graph1 = {0: {1}, 1: {0, 2}, 2: {1}}
    print(f"删除边前连通: {dfs_connectivity_with_set(graph1, 0, 3)}")  # True
    print(f"删除边(1,2)后连通: {dfs_connectivity_with_set(graph1, 0, 3, (1, 2))}")  # False
    
    # 测试用例2：有环的图
    print("\n【测试2】有环的图：0-1-2-0形成环，1-3")
    graph2 = {
        0: {1, 2},
        1: {0, 2, 3},
        2: {0, 1},
        3: {1}
    }
    print(f"删除边前连通: {dfs_connectivity_with_set(graph2, 0, 4)}")  # True
    print(f"删除边(1,3)后连通: {dfs_connectivity_with_set(graph2, 0, 4, (1, 3))}")  # False
    print(f"删除边(0,2)后连通: {dfs_connectivity_with_set(graph2, 0, 4, (0, 2))}")  # True
    
    # 测试用例3：找关键连接
    print("\n【测试3】查找关键连接")
    n3 = 4
    connections3 = [[0, 1], [1, 2], [2, 0], [1, 3]]
    critical = find_critical_connections(n3, connections3)
    print(f"输入: n={n3}, connections={connections3}")
    print(f"关键连接: {critical}")  # [[1, 3]]
    
    # 测试用例4：线性链（所有边都是关键）
    print("\n【测试4】线性链（所有边都是关键连接）")
    n4 = 4
    connections4 = [[0, 1], [1, 2], [2, 3]]
    critical4 = find_critical_connections(n4, connections4)
    print(f"输入: n={n4}, connections={connections4}")
    print(f"关键连接: {critical4}")  # [[0, 1], [1, 2], [2, 3]]
    
    print("\n" + "=" * 60)
