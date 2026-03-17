"""
LeetCode 210 - Course Schedule II

Problem Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid 
answers, return any of them. If it is impossible to finish all the courses, return an empty array.

Example 1:
    Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]
    Explanation: There are a total of 4 courses to take. To take course 3 you should have finished 
    both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
    So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 2:
    Input: numCourses = 1, prerequisites = []
    Output: [0]

Example 3:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: []
    Explanation: There is no way to finish all courses.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= numCourses * (numCourses - 1)
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- ai != bi
- There are no duplicate prerequisites.

Approach:
This is an extension of Course Schedule I. The key difference is we need to return the actual 
ordering (topological sort result) instead of just checking if it's possible.

You can use:
1. Kahn's Algorithm (BFS with indegree)
2. DFS with post-order traversal

Key Insights:
- Use topological sorting to find the valid course order
- If cycle exists, return empty list
- Handle both visited and visiting states to detect cycles
"""

from queue import Queue
from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Find a valid ordering of courses to complete all courses.
        
        Args:
            numCourses: Total number of courses
            prerequisites: List of prerequisites, where [a, b] means b must come before a
            
        Returns:
            A valid course ordering, or empty list if impossible
        """
        graph = {}
        for curr, prev in prerequisites:
            if prev not in graph:
                graph[prev] = set()
            graph[prev].add(curr)

        def dfs(_graph, _cur, _visited, _result):
            if _visited[_cur] == 1:
                return False
            if _visited[_cur] == 2:
                return True
            _visited[_cur] = 1
            if _cur in _graph:
                for _next in _graph[_cur]:
                    if not dfs(_graph, _next, _visited, _result):
                        return False
            _visited[_cur] = 2
            _result.append(_cur)
            return True

        visited = [0] * numCourses
        result = []
        # Process all courses, including those without prerequisites
        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(graph, course, visited, result):
                    return []
        return list(reversed(result))

    def findOrder_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Find a valid ordering of courses using BFS (Kahn's Algorithm).
        
        Args:
            numCourses: Total number of courses
            prerequisites: List of prerequisites, where [a, b] means b must come before a
            
        Returns:
            A valid course ordering, or empty list if impossible
        """
        # Build graph and calculate indegree
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        # TODO: Initialize queue with courses that have no prerequisites
        # TODO: BFS process
        # TODO: Check if all courses are processed and return result
        result = []
        queue = deque()
        for course, ind in enumerate(indegree):
            if ind == 0:
                queue.append(course)
        while queue:
            prereq = queue.pop()
            result.append(prereq)
            for course in graph[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        if len(result) != numCourses:
            return []
        return result



# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: Basic example with valid ordering
    test1_courses = 4
    test1_prereqs = [[1,0],[2,0],[3,1],[3,2]]
    result1 = solution.findOrder_bfs(test1_courses, test1_prereqs)
    print(f"Test 1: numCourses = {test1_courses}, prerequisites = {test1_prereqs}")
    print(f"Output: {result1}")
    print(f"Expected: [0,2,1,3] or [0,1,2,3] (any valid ordering)")
    print()
    
    # Test 2: Single course
    test2_courses = 1
    test2_prereqs = []
    result2 = solution.findOrder_bfs(test2_courses, test2_prereqs)
    print(f"Test 2: numCourses = {test2_courses}, prerequisites = {test2_prereqs}")
    print(f"Output: {result2}")
    print(f"Expected: [0]")
    print()
    
    # Test 3: Cycle detected
    test3_courses = 2
    test3_prereqs = [[1,0],[0,1]]
    result3 = solution.findOrder_bfs(test3_courses, test3_prereqs)
    print(f"Test 3: numCourses = {test3_courses}, prerequisites = {test3_prereqs}")
    print(f"Output: {result3}")
    print(f"Expected: []")
    print()
    
    # Test 4: More complex valid case
    test4_courses = 3
    test4_prereqs = [[1,0],[2,0]]
    result4 = solution.findOrder_bfs(test4_courses, test4_prereqs)
    print(f"Test 4: numCourses = {test4_courses}, prerequisites = {test4_prereqs}")
    print(f"Output: {result4}")
    print(f"Expected: [0,1,2] or [0,2,1]")
    print()
    
    # Test 5: Cycle with 3 courses
    test5_courses = 3
    # test5_prereqs = [[1,0],[0,2],[2,1]]
    test5_prereqs = [[1,0],[1,2],[0,1]]
    result5 = solution.findOrder_bfs(test5_courses, test5_prereqs)
    print(f"Test 5: numCourses = {test5_courses}, prerequisites = {test5_prereqs}")
    print(f"Output: {result5}")
    print(f"Expected: []")
