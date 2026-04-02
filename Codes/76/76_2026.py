"""
[76] Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string "".

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from t.

Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.

Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.

Constraints:
    - m == s.length
    - n == t.length
    - 1 <= m, n <= 10^5
    - s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?

Date: 2026-03-30
"""

from typing import List


def minWindow(s: str, t: str) -> str:

    def dict_include(_s_dict, _t_dict):
        for _char in _t_dict:
            if _char not in _s_dict or _t_dict[_char] > _s_dict[_char]:
                return False
        return True
    
    t_dict = {}
    for char in t:
        t_dict[char] = t_dict.get(char, 0) + 1
    s_dict = {}
    
    start_idx, end_idx = 0, 0
    min_start_idx, min_end_idx = 0, len(s)
    
    while start_idx < len(s) and end_idx < len(s):
        end = s[end_idx]
        s_dict[end] = s_dict.get(end, 0) + 1
        if dict_include(s_dict, t_dict):
            if end_idx - start_idx < min_end_idx - min_start_idx:
                min_start_idx, min_end_idx = start_idx, end_idx
            s_dict[s[start_idx]] -= 1
            start_idx += 1
            if s_dict[s[start_idx]] == 0:
                del s_dict[s[start_idx]]
        else:
            end_idx += 1

    return s[min_start_idx: min_end_idx]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("aa", "aa", "aa"),
        ("bdab", "ab", "ab"),
    ]

    for s, t, expected in test_cases:
        result = minWindow(s, t)
        status = "✓" if result == expected else "✗"
        print(f"{status} s={s!r}, t={t!r}")
        print(f"   Output:   {result!r}")
        print(f"   Expected: {expected!r}\n")
