"""
[743] Network Delay Time
https://leetcode.com/problems/network-delay-time/

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of
travel times as a directed edge times[i] = (ui, vi, wi), where ui is the source node, vi is the
target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all n nodes to
receive the signal. If it is impossible for all n nodes to receive the signal, return -1.

Example 1:
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2

Example 2:
    Input: times = [[1,2,1]], n = 2, k = 1
    Output: 1

Example 3:
    Input: times = [[1,2,1]], n = 2, k = 2
    Output: -1
    Explanation: Node 1 never receives the signal.

Constraints:
    - 1 <= k <= n <= 100
    - 1 <= times.length <= 6000
    - times[i].length == 3
    - 1 <= ui, vi <= n
    - ui != vi
    - 0 <= wi <= 100
    - All the pairs (ui, vi) are unique (no repeated edges).

Approach:
    - Single-source shortest paths from k (Dijkstra; all wi >= 0).
    - Answer = max shortest distance over all nodes 1..n; if any node is unreachable, return -1.
    - Note: nodes are 1-indexed (unlike many LC graph problems that use 0-indexed labels).
"""


def networkDelayTime(times, n, k):
    import heapq
    # Build adjency graph
    graph = {}
    for start, end, cost in times:
        if start not in graph:
            graph[start] = []
        graph[start].append([end, cost])
    # print(graph)
    # Initialize dist
    dist = [10000] * (n + 1) # dist[i]: Shortest distance to i
    dist[k] = 0
    heap = [(0, k)]
    # Dijistra get get shortest distance from start k
    while heap:
        current_dist, u = heapq.heappop(heap)
        if dist[u] < current_dist:
            continue
        if u not in graph:
            continue
        for end, cost in graph[u]:
            new_dist = current_dist + cost
            if dist[end] > new_dist:
                dist[end] = new_dist
                heapq.heappush(heap, (new_dist, end))
    
    max_dist = max(dist[1:])
    if max_dist == 101:
        return -1
    else:
        return max_dist


if __name__ == "__main__":
    test_cases = [
        # (times, n, k, expected) — LeetCode examples
        # ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        # ([[1, 2, 1]], 2, 1, 1),
        # ([[1, 2, 1]], 2, 2, -1),
        # Edge cases
        # ([], 1, 1, 0),  # single node, no edges
        # ([[1, 2, 1]], 3, 1, -1),  # node 3 unreachable
        # ([[1, 2, 3], [1, 3, 1]], 3, 1, 3),  # node 3 at 1, node 2 at 3 -> max = 3
        # ([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1, 3),  # 1 -> 2 -> 3 is faster than 1 -> 3
        # ([[1, 2, 0]], 2, 1, 0),  # zero-weight edge
        # ([[1, 2, 1], [1, 3, 2], [1, 4, 3], [1, 5, 4]], 5, 1, 4),  # star from source
        # ([[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 2, 1]], 4, 1, 3),  # cycle, longest shortest path
        # ([[2, 1, 1], [2, 3, 1]], 4, 2, -1),  # node 4 unreachable (same as ex1 without 3->4)
        # ([[1, 2, 1], [2, 1, 3]], 2, 1, 1),  # only forward path matters for broadcast from 1
        # ([[1, 2, 4], [2, 1, 2], [3, 4, 7], [4, 3, 1], [1, 4, 3], [3, 1, 6], [4, 2, 5]], 4, 1, 4),
        # LC Wrong Example
        ([[2,7,63],[4,3,60],[1,3,53],[5,6,100],[1,4,40],[4,7,95],[4,6,97],[3,4,68],[1,7,75],[2,6,84],[1,6,27],[5,3,25],[6,2,2],[3,7,57],[5,4,2],[7,1,53],[5,7,35],[4,1,60],[5,2,95],[3,5,28],[6,1,61],[2,5,28]], 7, 3, 119)
    ]

    print("=" * 70)
    print("LeetCode 743 - Network Delay Time")
    print("=" * 70)

    for i, (times, n, k, expected) in enumerate(test_cases, 1):
        try:
            result = networkDelayTime(times, n, k)
            if result is None:
                status = "TODO"
            else:
                status = "PASS" if result == expected else "FAIL"
            print(f"Case {i}: {status}")
            print(f"  n={n}, k={k}, times={times}")
            print(f"  expected={expected}, got={result}")
        except Exception as e:
            print(f"Case {i}: ERROR")
            print(f"  n={n}, k={k}, times={times}")
            print(f"  expected={expected}, error={e}")
        print()
