"""
LeetCode 1462 - Course Schedule IV

Problem Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
take course bi first if you want to take course ai.

You are also given queries where queries[j] = [uj, vj]. For each query, determine whether 
course vj is a prerequisite of course uj (not necessarily direct - could be indirect).

Return a boolean array answer, where answer[j] is true if course vj is a prerequisite of 
course uj, otherwise false.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
    Output: [false,true]
    Explanation: 
    - Query [0,1]: "Is course 1 a prerequisite of course 0?" Answer: No (0 depends on 1, not vice versa)
    - Query [1,0]: "Is course 0 a prerequisite of course 1?" Answer: Yes (1 depends on 0)

Example 2:
    Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
    Output: [false,false]
    Explanation: Both courses are independent.

Example 3:
    Input: numCourses = 3, prerequisites = [[1,0],[2,0],[2,1]], queries = [[1,0],[1,2],[0,1],[0,2],[2,0],[2,1]]
    Output: [true,true,false,false,false,true]

Constraints:
- 2 <= numCourses <= 100
- 0 <= prerequisites.length <= numCourses * (numCourses - 1) / 2
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- ai != bi
- There are no duplicate prerequisites.
- There are no cycles in the graph (guaranteed).
- 1 <= queries.length <= 10^4
- queries[j].length == 2
- 0 <= uj, vj < numCourses
- uj != vj

Approach:
This is an extension of Course Schedule problems with an additional query component.
The key difference is you need to find ALL prerequisites (direct and indirect) for each course.

Methods:
1. Build the prerequisite graph and use DFS/BFS to find all prerequisites for each course
2. Store prerequisites in a set for each course
3. Answer queries in O(1) time

Key Insights:
- For each course, find all courses that are prerequisites (directly or indirectly)
- This is about reachability in a directed graph
- Can use DFS from each course to find all reachable prerequisites
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        Determine whether course v is a prerequisite of course u for each query.
        
        Args:
            numCourses: Total number of courses
            prerequisites: List of prerequisites, where [a, b] means b must come before a
            queries: List of queries asking if v is a prerequisite of u
            
        Returns:
            List of boolean answers for each query
        """
        # Build graph: course -> [its prerequisites]
        graph = {}
        for course, prereq in prerequisites:
            if course not in graph:
                graph[course] = []
            graph[course].append(prereq)
        
        # Store all prerequisites (direct and indirect) for each course
        prereq_set = {}
        
        # DFS to find all prerequisites for a given course
        def dfs(_root, _cur, _graph, _prereq_set):
            """
            Find all prerequisites of _root by traversing from _cur
            """
            if _cur not in _graph:
                return
            for _pre in _graph[_cur]:
                # Initialize the set for _root if not exists
                if _root not in _prereq_set:
                    _prereq_set[_root] = set()
                
                # Add prerequisite only if not already added (avoid duplicate visits)
                if _pre not in _prereq_set[_root]:
                    _prereq_set[_root].add(_pre)
                    # Continue DFS to find prerequisites of _pre
                    dfs(_root, _pre, _graph, _prereq_set)
        
        # For each course, find all its prerequisites
        for course in range(numCourses):
            if course not in graph:
                # Course has no prerequisites
                prereq_set[course] = set()
            else:
                # Initialize the set and start DFS
                prereq_set[course] = set()
                dfs(course, course, graph, prereq_set)
        
        # Answer each query
        result = []
        for u, v in queries:
            # Check if v is in u's prerequisite set
            result.append(v in prereq_set[u])
        return result


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: Basic example
    test1_courses = 2
    test1_prereqs = [[1,0]]
    test1_queries = [[0,1],[1,0]]
    result1 = solution.checkIfPrerequisite(test1_courses, test1_prereqs, test1_queries)
    print(f"Test 1: numCourses = {test1_courses}, prerequisites = {test1_prereqs}")
    print(f"queries = {test1_queries}")
    print(f"Output: {result1}")
    print(f"Expected: [false, true]\n")
    
    # Test 2: No prerequisites
    test2_courses = 2
    test2_prereqs = []
    test2_queries = [[1,0],[0,1]]
    result2 = solution.checkIfPrerequisite(test2_courses, test2_prereqs, test2_queries)
    print(f"Test 2: numCourses = {test2_courses}, prerequisites = {test2_prereqs}")
    print(f"queries = {test2_queries}")
    print(f"Output: {result2}")
    print(f"Expected: [false, false]\n")
    
    # Test 3: Complex example with indirect prerequisites
    test3_courses = 3
    test3_prereqs = [[1,0],[2,0],[2,1]]
    test3_queries = [[1,0],[1,2],[0,1],[0,2],[2,0],[2,1]]
    result3 = solution.checkIfPrerequisite(test3_courses, test3_prereqs, test3_queries)
    print(f"Test 3: numCourses = {test3_courses}, prerequisites = {test3_prereqs}")
    print(f"queries = {test3_queries}")
    print(f"Output: {result3}")
    print(f"Expected: [true, true, false, false, false, true]\n")
    
    # Test 4: Linear chain
    test4_courses = 4
    test4_prereqs = [[1,0],[2,1],[3,2]]
    test4_queries = [[3,0],[0,3],[2,0],[1,3]]
    result4 = solution.checkIfPrerequisite(test4_courses, test4_prereqs, test4_queries)
    print(f"Test 4: numCourses = {test4_courses}, prerequisites = {test4_prereqs}")
    print(f"queries = {test4_queries}")
    print(f"Output: {result4}")
    print(f"Expected: [true, false, true, false]\n")
