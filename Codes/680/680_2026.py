"""
LeetCode 680: Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/

Given a string s, return true if the s can be palindrome after deleting
at most one character from it.

Example 1:
    Input: s = "aba"
    Output: true

Example 2:
    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'c'.

Example 3:
    Input: s = "abc"
    Output: false

Constraints:
    - 1 <= s.length <= 10^5
    - s consists of lowercase English letters.
"""
from typing import Optional

"""
def validPalindrome(s: str) -> bool:
    n = len(s)
    left, right = 0, n - 1
    deleted = False
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if deleted:
                return False
            else:
                if s[left + 1] == s[right]:
                    deleted = True
                    left += 2
                    right -= 1
                elif s[left] == s[right - 1]:
                    deleted = True
                    left += 1
                    right -= 2
                else:
                    return False
    return True
"""
def validPalindrome(s: str) -> bool:
    
    def isParlinedrome(_s, _left, _right):
        while _left < _right:
            if _s[_left] == _s[_right]:
                _left += 1
                _right -= 1
            else:
                return False
        return True
    
    n = len(s)
    left, right = 0, n - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return isParlinedrome(s, left+1, right) or isParlinedrome(s, left, right-1)
    return True


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "s": "aba",
            "expected": True,
            "description": "Already a palindrome",
        },
        {
            "s": "abca",
            "expected": True,
            "description": "Delete 'c' to get palindrome",
        },
        {
            "s": "abc",
            "expected": False,
            "description": "Cannot form palindrome with one deletion",
        },
        {
            "s": "deeee",
            "expected": True,
            "description": "Delete first 'd' to get 'eeee'",
        },
        {
            "s": "a",
            "expected": True,
            "description": "Single character",
        },
        {
            "s": "raceacar",
            "expected": False,
            "description": "Cannot form palindrome",
        },
        {
            "s": "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsmydgjpfdhooxfuupuculmgmqfvnbgtagpekouga",
            "expected": True,
            "description": "Long palindrome with one char delete",
        },
    ]

    print("=" * 60)
    print("LeetCode 680: Valid Palindrome II - Test Results")
    print("=" * 60)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = validPalindrome(test["s"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        s_display = test['s'] if len(test['s']) <= 30 else test['s'][:27] + "..."
        print(f"  Input:       s=\"{s_display}\"")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 60)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")
