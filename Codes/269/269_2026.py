"""
LeetCode 269 - Alien Dictionary (Meta Hard Question)

Problem Description:
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. 
You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language.

Derive the order of letters in this alien dictionary.

For example:
Input: ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] contains only lowercase letters.
- All given words are unique.
- There is at least one valid order of letters returned. In case the given input is invalid, 
  return an empty string.

Example 1:
    Input: ["z","x"]
    Output: "zx"

Example 2:
    Input: ["z","x","z"]
    Output: ""  (invalid - "z" cannot come before "x" and after "x" at the same time)

Example 3:
    Input: ["wrt","wrf","er","ett","rftt"]
    Output: "wertf"

Approach:
1. Build a directed graph where edges represent ordering constraints
2. Use topological sort (Kahn's algorithm or DFS) to determine the order
3. If there's a cycle or invalid ordering, return empty string

Key Insights:
- This is a graph/topological sort problem, not a simple sort problem
- You need to compare adjacent words to find the order of characters
- Handle cycles and invalid inputs
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Determine the order of letters in the alien dictionary.
        
        Args:
            words: List of words sorted in the alien dictionary order
            
        Returns:
            A string representing the order of letters, or empty string if invalid
        """
        # Build the graph
        graph = defaultdict(set)
        all_chars = set()
        
        # Initialize all characters
        for word in words:
            for char in word:
                all_chars.add(char)
        
        # Extract ordering relationships from adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            # Check for invalid case: word1 is longer but word2 is a prefix of word1
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            # Find the first different character
            for j in range(min_len):
                if word1[j] != word2[j]:
                    # Add edge: word1[j] -> word2[j]
                    graph[word1[j]].add(word2[j])
                    break
        
        # DFS + Post-order topological sort
        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = {}
        result = []
        
        def dfs(char):
            """
            DFS with cycle detection
            Returns True if valid (no cycle), False if cycle detected
            """
            if char in state:
                if state[char] == 1:  # Currently visiting -> cycle detected
                    return False
                return state[char] == 2  # Already visited -> valid
            
            # Mark as visiting
            state[char] = 1
            
            # Visit all neighbors
            for neighbor in graph[char]:
                if not dfs(neighbor):
                    return False
            
            # Mark as visited and add to result (post-order)
            state[char] = 2
            result.append(char)
            return True
        
        # Run DFS on all characters
        for char in all_chars:
            if char not in state:
                if not dfs(char):
                    return ""  # Cycle detected
        
        # Reverse result because we want reverse topological order
        return "".join(reversed(result))

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: Basic example
    test1 = ["z", "x"]
    print(f"Test 1: {test1}")
    print(f"Output: {solution.alienOrder(test1)}")
    print(f"Expected: 'zx'\n")
    
    # Test 2: Invalid case - cycle
    test2 = ["z", "x", "z"]
    print(f"Test 2: {test2}")
    print(f"Output: {solution.alienOrder(test2)}")
    print(f"Expected: ''\n")
    
    # Test 3: Complex example
    test3 = ["wrt", "wrf", "er", "ett", "rftt"]
    print(f"Test 3: {test3}")
    print(f"Output: {solution.alienOrder(test3)}")
    print(f"Expected: 'wertf'\n")
    
    # Test 4: Single word
    test4 = ["abc"]
    print(f"Test 4: {test4}")
    print(f"Output: {solution.alienOrder(test4)}")
    print(f"Expected: 'abc' (or any valid ordering)\n")
    
    # Test 5: Already sorted
    test5 = ["a", "b", "ca", "cb", "da", "db"]
    print(f"Test 5: {test5}")
    print(f"Output: {solution.alienOrder(test5)}")
    print(f"Expected: 'acbd'\n")
