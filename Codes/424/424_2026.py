"""
LeetCode 424: Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of
the string and change it to any other uppercase English character. You can
perform this operation at most k times.

Return the length of the longest substring containing the same letter you can
get after performing the above operations.

Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
                 The substring "BBBB" has the longest repeating letters, which
                 is 4. There may exists other ways to achieve this answer too.

Constraints:
    - 1 <= s.length <= 10^5
    - s consists of only uppercase English letters.
    - 0 <= k <= s.length
"""
from typing import List


def characterReplacement(s: str, k: int) -> int:

    def getMaxCharacter(_characterInfo):
        _max_value = 0
        _max_key = ""
        for _key, value in _characterInfo.items():
            if value > _max_value:
                _max_value = value
                _max_key = _key
        return _max_key, _max_value

    left, right = 0, 0
    n = len(s)
    characterInfo = {}
    n_replace = 0
    max_consecutive_same_character = 0
    while right < n:
        if s[right] not in characterInfo:
            characterInfo[s[right]] = 0
        characterInfo[s[right]] += 1
        max_character, max_value = getMaxCharacter(characterInfo)
        n_replace = (right - left) - max_value
        right += 1
        if n_replace >= k:
            if s[left] in characterInfo:
                characterInfo[s[left]] -= 1
            left += 1
        max_consecutive_same_character = max(max_consecutive_same_character, right - left)
    return max_consecutive_same_character


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "s": "ABAB",
            "k": 2,
            "expected": 4,
            "description": "Replace 2 chars, whole string becomes same",
        },
        {
            "s": "AABABBA",
            "k": 1,
            "expected": 4,
            "description": "Replace 1 char, best window is length 4",
        },
        {
            "s": "AAAA",
            "k": 0,
            "expected": 4,
            "description": "No replacement needed, all same",
        },
        {
            "s": "ABCD",
            "k": 0,
            "expected": 1,
            "description": "No replacement, each char different",
        },
        {
            "s": "ABCD",
            "k": 3,
            "expected": 4,
            "description": "Replace 3 chars, whole string can be same",
        },
        {
            "s": "A",
            "k": 0,
            "expected": 1,
            "description": "Single character",
        },
    ]

    print("=" * 65)
    print("LeetCode 424: Longest Repeating Character Replacement - Test Results")
    print("=" * 65)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = characterReplacement(test["s"], test["k"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       s={test['s']!r}, k={test['k']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 65)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 65)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")
