"""
[787] Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are n cities connected by some number of flights.
Each flight is represented as flights[i] = [from_i, to_i, price_i].

You are also given three integers src, dst, and k.
Return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.

Note:
    - A stop means an intermediate city.
    - At most k stops means the route can use at most k + 1 flights.

Example 1:
    Input: n = 4,
           flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
           src = 0, dst = 3, k = 1
    Output: 700

Example 2:
    Input: n = 3,
           flights = [[0,1,100],[1,2,100],[0,2,500]],
           src = 0, dst = 2, k = 1
    Output: 200

Example 3:
    Input: n = 3,
           flights = [[0,1,100],[1,2,100],[0,2,500]],
           src = 0, dst = 2, k = 0
    Output: 500

Constraints:
    - 1 <= n <= 100
    - 0 <= flights.length <= n * (n - 1) / 2
    - flights[i].length == 3
    - 0 <= from_i, to_i < n
    - from_i != to_i
    - 1 <= price_i <= 10^4
    - 0 <= src, dst, k < n
    - src != dst

Date: 2026-04-27
"""

import queue

def findCheapestPrice(n, flights, src, dst, k):
    """
    TODO: Implement your solution.

    Suggested directions:
    1. Graph + BFS by layers (stops control)
    2. Dijkstra variant with state: (node, used_stops)
    3. Bellman-Ford style DP for exactly up to k + 1 edges

    Time target: better than brute-force DFS.
    """
    bfs = queue.Queue()
    bfs.put((src, -1, 0))
    default_price = 10e5
    min_price = default_price
    best_plan = {}
    from_to = {}
    for start, end, price in flights:
        if start not in from_to:
            from_to[start] = []
        from_to[start].append((end, price))

    while not bfs.empty():
        cur = bfs.get()
        cur_start, cur_stops, cur_price = cur
        # """
        if cur_start not in best_plan:
            best_plan[cur_start] = {}
        if cur_stops not in best_plan[cur_start]:
             best_plan[cur_start][cur_stops] = cur_price
        if cur_price > best_plan[cur_start][cur_stops]:
            continue
        # """
        if cur_stops > k:
            continue
        if cur_start == dst:
            min_price = min(cur_price, min_price)
            continue

        if cur_start not in from_to:
            continue
        for end, price in from_to[cur_start]:
            if end not in best_plan:
                best_plan[end] = {}
            if cur_stops + 1 not in best_plan[end]:
                best_plan[end][cur_stops + 1] = cur_price + price
                bfs.put((end, cur_stops + 1, cur_price + price))

            if best_plan[end][cur_stops + 1] > cur_price + price:
                best_plan[end][cur_stops + 1] = cur_price + price
                bfs.put((end, cur_stops + 1, cur_price + price))
    if min_price == default_price:
        return -1
    return min_price



def findCheapestPrice_bellman_ford(n, flights, src, dst, k):
    """
    TODO: Implement Bellman-Ford layered DP here.

    Args:
        n: number of cities
        flights: list of [from, to, price]
        src: start city
        dst: target city
        k: max number of stops
    """
    # dp[dst] = min(dp[src], dp[src] + w)
    dp = [float("inf")] * n
    dp[src] = 0
    for _ in range(k + 1): # stop + 1 == total_flight
        next_dp = dp.copy()
        for start, end, price in flights:
            if dp[start] == float("inf"):
                continue
            next_dp[end] = min(next_dp[end], dp[start] + price)
        dp = next_dp
    if next_dp[dst] == float("inf"):
        return -1
    else:
        return next_dp[dst]


if __name__ == "__main__":
    test_cases = [
        # (n, flights, src, dst, k, expected)
        (
            4,
            [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            0,
            3,
            1,
            700,
        ),
        (
            3,
            [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
            0,
            2,
            1,
            200,
        ),
        (
            3,
            [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
            0,
            2,
            0,
            500,
        ),
        (
            5,
            [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 4, 5], [0, 4, 100]],
            0,
            4,
            2,
            100,
        ),
        (
            5,
            [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10]],
            0,
            4,
            1,
            -1,
        ),
        (   
            5, 
            [[1,0,5],[2,1,5],[3,0,2],[1,3,2],[4,1,1],[2,4,1]],
            2,0,2,7
        ),
        (   5,
            [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]],
            2,1,1,-1
        )
    ]

    print("=" * 70)
    print("LeetCode 787 - Cheapest Flights Within K Stops")
    print("=" * 70)

    for i, (n, flights, src, dst, k, expected) in enumerate(test_cases, 1):
        # result = findCheapestPrice(n, flights, src, dst, k)
        result = findCheapestPrice_bellman_ford(n, flights, src, dst, k)
        status = "TODO" if result is None else ("PASS" if result == expected else "FAIL")
        print(f"Case {i}: {status}")
        print(f"  n={n}, src={src}, dst={dst}, k={k}")
        print(f"  flights={flights}")
        print(f"  expected={expected}, got={result}")
        print()
