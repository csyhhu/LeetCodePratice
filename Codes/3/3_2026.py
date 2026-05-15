"""
[3] Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
    Input: s = ""
    Output: 0

Constraints:
    - 0 <= s.length <= 5 * 10^4
    - s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s):
    def checkCharacterCount(_characterCount):
        for key, value in _characterCount.items():
            if value > 1:
                return True
        return False
    left, right = 0, 0
    characterCount = {}
    maxLength = 0
    while right < len(s):
        char = s[right]
        if char not in characterCount:
            characterCount[char] = 1
        else:
            characterCount[char] += 1
        # print(characterCount)
        while checkCharacterCount(characterCount) and left <= right:
            characterCount[s[left]] -= 1
            left += 1
        maxLength = max(maxLength, right - left + 1)
        right += 1
    return maxLength


# Test cases
if __name__ == "__main__":
    print("=" * 70)
    print("LeetCode 3 - Longest Substring Without Repeating Characters")
    print("=" * 70)

    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
        ("aab", 2),
        ("abcdefg", 7),
    ]

    print("\n【第1步】测试基础版本 - lengthOfLongestSubstring")
    print("-" * 70)

    for test_input, expected in test_cases:
        try:
            result = lengthOfLongestSubstring(test_input)
            if result is None:
                print(f"⚠️  Input: '{test_input}' -> 还没实现 (返回 None)")
            else:
                status = "✓" if result == expected else "✗"
                print(f"{status} Input: '{test_input}' -> Output: {result}, Expected: {expected}")
        except Exception as e:
            print(f"❌ Input: '{test_input}' -> Error: {e}")

    # print("\n【第2步】测试优化版本 - lengthOfLongestSubstring_dict")
    # print("-" * 70)
    #
    # for test_input, expected in test_cases:
    #     try:
    #         result = lengthOfLongestSubstring_dict(test_input)
    #         if result is None:
    #             print(f"⚠️  Input: '{test_input}' -> 还没实现 (返回 None)")
    #         else:
    #             status = "✓" if result == expected else "✗"
    #             print(f"{status} Input: '{test_input}' -> Output: {result}, Expected: {expected}")
    #     except Exception as e:
    #         print(f"❌ Input: '{test_input}' -> Error: {e}")

    # print("\n【第3步】测试暴力版本 - lengthOfLongestSubstring_brute_force")
    # print("-" * 70)
    #
    # small_test_cases = [
    #     ("abcabcbb", 3),
    #     ("bbbbb", 1),
    #     ("au", 2),
    # ]
    #
    # for test_input, expected in small_test_cases:
    #     try:
    #         result = lengthOfLongestSubstring_brute_force(test_input)
    #         if result is None:
    #             print(f"⚠️  Input: '{test_input}' -> 还没实现 (返回 None)")
    #         else:
    #             status = "✓" if result == expected else "✗"
    #             print(f"{status} Input: '{test_input}' -> Output: {result}, Expected: {expected}")
    #     except Exception as e:
    #         print(f"❌ Input: '{test_input}' -> Error: {e}")
