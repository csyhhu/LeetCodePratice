"""
LeetCode 127: Word Ladder
https://leetcode.com/problems/word-ladder/

A transformation sequence from word beginWord to word endWord using a dictionary
wordList is a sequence of words:
    beginWord -> s1 -> s2 -> ... -> endWord
such that:
    - Every adjacent pair of words differs by exactly one letter.
    - Every si (1 <= i <= k) is in wordList. Note that beginWord does not need to be in wordList.
    - endWord is in wordList.

Return the number of words in the shortest transformation sequence from beginWord to endWord,
or 0 if no such sequence exists.

Example 1:
    Input: beginWord = "hit", endWord = "cog",
           wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5
    Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog"

Example 2:
    Input: beginWord = "hit", endWord = "cog",
           wordList = ["hot","dot","dog","lot","log"]
    Output: 0
    Explanation: endWord "cog" is not in wordList, so no transformation possible.

Constraints:
    - 1 <= beginWord.length <= 10
    - endWord.length == beginWord.length
    - 1 <= wordList.length <= 5000
    - wordList[i].length == beginWord.length
    - beginWord, endWord, and wordList[i] consist of lowercase English letters.
    - beginWord != endWord
    - All the words in wordList are unique.

思路：
    BFS，把每个单词看作图的节点，相差一个字母的单词之间有边。
    从 beginWord 出发，BFS 找到 endWord 的最短路径长度。

    关键：如何快速生成邻居？
        方法一：枚举当前单词每个位置，替换成 a-z，看是否在 wordList 中 → O(26 * L)
        方法二：预处理 wordList 建 pattern 图（更复杂，适合多次查询）

    注意：
        - 访问过的单词要从 wordList（或 visited 集合）中移除，避免重复访问
        - 返回值是序列长度（包含 beginWord 和 endWord），不是边数
"""


def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    pass


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "beginWord": "hit", "endWord": "cog",
            "wordList": ["hot", "dot", "dog", "lot", "log", "cog"],
            "expected": 5,
            "description": "Classic example: hit->hot->dot->dog->cog"
        },
        {
            "beginWord": "hit", "endWord": "cog",
            "wordList": ["hot", "dot", "dog", "lot", "log"],
            "expected": 0,
            "description": "endWord not in wordList"
        },
        {
            "beginWord": "a", "endWord": "c",
            "wordList": ["a", "b", "c"],
            "expected": 2,
            "description": "Short words: a->c"
        },
        {
            "beginWord": "hot", "endWord": "dog",
            "wordList": ["hot", "dog"],
            "expected": 0,
            "description": "No path exists"
        },
        {
            "beginWord": "hot", "endWord": "dog",
            "wordList": ["hot", "dot", "dog"],
            "expected": 3,
            "description": "hot->dot->dog"
        },
        {
            "beginWord": "leet", "endWord": "code",
            "wordList": ["lest", "leet", "lose", "code", "lode", "robe", "lost"],
            "expected": 6,
            "description": "Longer path"
        },
    ]

    print("=" * 60)
    print("LeetCode 127: Word Ladder - Test Results")
    print("=" * 60)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = ladderLength(test["beginWord"], test["endWord"], test["wordList"][:])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  beginWord:   \"{test['beginWord']}\"")
        print(f"  endWord:     \"{test['endWord']}\"")
        print(f"  wordList:    {test['wordList']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 60)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")
