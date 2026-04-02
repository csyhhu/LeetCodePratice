"""
LeetCode 72: Edit Distance
https://leetcode.com/problems/edit-distance/

Given two strings word1 and word2, return the minimum number of operations
required to convert word1 into word2.

You have the following three operations permitted on a word:
    - Insert a character
    - Delete a character
    - Replace a character

Example 1:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation:
        horse -> rorse (replace 'h' with 'r')
        rorse -> rose  (delete 'r')
        rose  -> ros   (delete 'e')

Example 2:
    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation:
        intention -> inention  (delete 't')
        inention  -> enention  (replace 'i' with 'e')
        enention  -> exention  (replace 'n' with 'x')
        exention  -> exection  (replace 'n' with 'c')
        exection  -> execution (insert 'u')

Constraints:
    - 0 <= word1.length, word2.length <= 500
    - word1 and word2 consist of lowercase English letters.

与 LeetCode 115 / 1143 对比：
    - 1143：两个字符串最长公共子序列（只能跳过字符）
    - 115：s 中子序列等于 t 的方案数（只能从 s 中删）
    - 72：将 word1 变成 word2 的最少操作数（可插入、删除、替换）
    - 三种操作对应 dp 转移的三个来源，仔细想每种操作对应哪个状态

Hint:
    定义 dp[i][j] = 将 word1[:i] 变成 word2[:j] 所需的最少操作数
    边界条件：
        dp[0][j] = j  (word1 为空，需要插入 j 个字符)
        dp[i][0] = i  (word2 为空，需要删除 i 个字符)
    思考：
        当 word1[i-1] == word2[j-1] 时，这两个字符已经匹配，dp[i][j] = ?
        当 word1[i-1] != word2[j-1] 时，三种操作分别对应哪个子问题？
            - 替换：把 word1[i-1] 替换成 word2[j-1]，代价来自 ?
            - 删除：删掉 word1[i-1]，代价来自 ?
            - 插入：在 word1[:i] 末尾插入 word2[j-1]，代价来自 ?
"""


def minDistance(word1: str, word2: str) -> int:
    pass


# Test cases
if __name__ == "__main__":
    test_cases = [
        {"word1": "horse", "word2": "ros", "expected": 3, "description": "Classic example"},
        {"word1": "intention", "word2": "execution", "expected": 5, "description": "Longer strings"},
        {"word1": "", "word2": "", "expected": 0, "description": "Both empty"},
        {"word1": "", "word2": "abc", "expected": 3, "description": "word1 empty, insert 3"},
        {"word1": "abc", "word2": "", "expected": 3, "description": "word2 empty, delete 3"},
        {"word1": "abc", "word2": "abc", "expected": 0, "description": "Identical strings"},
        {"word1": "a", "word2": "b", "expected": 1, "description": "Single replace"},
        {"word1": "ab", "word2": "ba", "expected": 2, "description": "Swap order"},
        {"word1": "kitten", "word2": "sitting", "expected": 3, "description": "Classic Levenshtein"},
    ]

    print("=" * 60)
    print("LeetCode 72: Edit Distance - Test Results")
    print("=" * 60)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = minDistance(test["word1"], test["word2"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       word1=\"{test['word1']}\", word2=\"{test['word2']}\"")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 60)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")
