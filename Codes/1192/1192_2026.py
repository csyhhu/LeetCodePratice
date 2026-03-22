"""
LeetCode 1192 - Critical Connections in a Network (HARD)
Meta Interview Classic - Bridge Finding Algorithm

Problem Description:
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections 
forming a network where any two servers can reach each other.

A critical connection is a connection that, if removed, will make some servers unable to reach each other.

Your task is to find all the critical connections in the network.

Input:
- n: int - the number of servers (2 <= n <= 100000)
- connections: List[List[int]] - list of connections where connections[i] = [a, b] 
  means a server a and server b are connected

Output:
- List[List[int]] - a list of critical connections in any order

Constraints:
- 2 <= n <= 100000
- n - 1 <= len(connections) < n
- 0 <= a, b < n
- a != b
- There are no repeated connections

Examples:

Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: The only critical connection is (1, 3). If removed, the server 0, 1, 2 cannot reach 3.

       0---1
       |   |
       +---2   3
           |
           (critical edge)

Example 2:
Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
Explanation: (0, 1) is the only connection and it's critical.

Example 3:
Input: n = 4, connections = [[0,1],[1,2],[2,3],[3,1]]
Output: []
Explanation: No critical connections exist. Removing any edge, all nodes remain connected.
(cycle structure - no bridges)

Example 4:
Input: n = 5, connections = [[0,1],[1,2],[1,3],[3,2],[2,4]]
Output: [[0,1],[2,4]]
Explanation: Connections [0,1] and [2,4] are critical. Edge [1,3] is not critical because there's a cycle 1-3-2-1.
"""


def criticalConnections(n, connections):
    """
    Find all critical connections (bridges) in an undirected graph.
    
    A critical connection is an edge whose removal increases the number of connected components.
    This is equivalent to finding "bridges" in graph theory.
    
    Args:
        n: Number of servers/nodes
        connections: List of undirected edges
        
    Returns:
        List of critical connections (bridges)
    """
    graph = {}
    for a, b in connections:
        if a not in graph:
            graph[a] = set()
        graph[a].add(b)
        if b not in graph:
            graph[b] = set()
        graph[b].add(a)

    def dfs(_graph, _cur, _selected_a, _selected_b, _visited):
        if _cur not in _graph:
            return
        _visited[_cur] = True
        # Search its all connections
        for _next in _graph[_cur]:
            # Let's see if (selected_a, selected_b) or (selected_b, selected_a) is a crticial connection
            if (_next == _selected_b and _cur == _selected_a) or (_next == _selected_a and _cur == _selected_b):
                continue
            if _visited[_next]:
                continue
            dfs(_graph, _next, _selected_a, _selected_b, _visited)

    result = []
    for selected_a, selected_b in connections:
        visited = [False] * n
        dfs(graph, 0, selected_a, selected_b, visited)
        if sum(visited) < n:
            result.append([selected_a, selected_b])
    return result



# Test cases
if __name__ == "__main__":
    # Test case 1: Simple cycle with one bridge
    n1 = 4
    connections1 = [[0,1],[1,2],[2,0],[1,3]]
    print(f"Test 1: n={n1}, connections={connections1}")
    result1 = criticalConnections(n1, connections1)
    print(f"Output: {result1}")
    print(f"Expected: [[1,3]] (or [[3,1]])")
    print()
    
    # Test case 2: Single edge (always critical)
    n2 = 2
    connections2 = [[0,1]]
    print(f"Test 2: n={n2}, connections={connections2}")
    result2 = criticalConnections(n2, connections2)
    print(f"Output: {result2}")
    print(f"Expected: [[0,1]]")
    print()
    
    # Test case 3: Complete cycle (no bridges)
    n3 = 4
    connections3 = [[0,1],[1,2],[2,3],[3,0]]
    print(f"Test 3: n={n3}, connections={connections3}")
    result3 = criticalConnections(n3, connections3)
    print(f"Output: {result3}")
    print(f"Expected: [] (no critical connections)")
    print()
    
    # Test case 4: Multiple bridges with cycle
    n4 = 5
    connections4 = [[0,1],[1,2],[1,3],[3,2],[2,4]]
    print(f"Test 4: n={n4}, connections={connections4}")
    result4 = criticalConnections(n4, connections4)
    print(f"Output: {result4}")
    print(f"Expected: [[0,1],[2,4]] (edges 0-1 and 2-4 are bridges, 1-3-2 forms a cycle)")
    print()
    
    # Test case 5: Linear chain (all are critical)
    n5 = 4
    connections5 = [[0,1],[1,2],[2,3]]
    print(f"Test 5: n={n5}, connections={connections5}")
    result5 = criticalConnections(n5, connections5)
    print(f"Output: {result5}")
    print(f"Expected: [[0,1],[1,2],[2,3]] (all edges are critical)")
