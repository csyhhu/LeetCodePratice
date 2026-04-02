"""
[438] Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's
anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

Example 1:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0, 6]
    Explanation:
        The substring starting at index 0 is "cba", which is an anagram of "abc".
        The substring starting at index 6 is "bac", which is an anagram of "abc".

Example 2:
    Input: s = "abab", p = "ab"
    Output: [0, 1, 2]
    Explanation:
        The substring starting at index 0 is "ab", which is an anagram of "ab".
        The substring starting at index 1 is "ba", which is an anagram of "ab".
        The substring starting at index 2 is "ab", which is an anagram of "ab".

Constraints:
    - 1 <= s.length, p.length <= 3 * 10^4
    - s and p consist of lowercase English letters.

Date: 2026-03-29
"""

from tkinter import S
from typing import List


def anagram_init(_word):
    dict = {}
    for char in _word:
        dict[char] = dict.get(char, 0) + 1
    return dict

def chechk_anagram(_dict):
    for char, rest in _dict.items():
        if rest != 0:
            return False
    return True

def match(s: str, p: str) -> bool:
    s_anagram = {}
    p_anagram = {}
    for char in s:
        s_anagram[char] = s_anagram.get(char, 0) + 1
    for char in p:
        p_anagram[char] = p_anagram.get(char, 0) + 1
    # print(s_anagram, p_anagram)
    for char in p:
        if char not in s_anagram or p_anagram[char] != s_anagram[char]:
            return False
    
    return True & (len(s_anagram) == len(p_anagram))

"""
def findAnagrams(s: str, p: str) -> List[int]:


    start, end = 0, 0
    p_set = anagram_init(p)
    result = []
    while end < len(s):
        # print(p_set, s[end])
        if chechk_anagram(p_set):
            result.append(start)
            p_set = anagram_init(p)
            start = end
            print("check anagram")
        if s[end] in p_set:
            if p_set[s[end]] > 0:
                p_set[s[end]] -= 1
                end += 1
            else:
                end += 1
                start = end
                p_set = anagram_init(p)
        else:
            end += 1
            start = end
            p_set = anagram_init(p)
        print(p_set)

    return result
"""

def findAnagrams(s: str, p: str) -> List[int]:
    result = []
    p_anagram = anagram_init(p)
    s_anagram = anagram_init(s[:len(p)])
    for end in range(len(p), len(s)):
        start = end - len(p)
        if p_anagram == s_anagram:
            result.append(start)
        # 加入右侧新字符（用 .get 防止 KeyError）
        s_anagram[s[end]] = s_anagram.get(s[end], 0) + 1
        # 移出左侧旧字符
        s_anagram[s[start]] -= 1
        # Removing to activate p_anagram == s_anagram
        if s_anagram[s[start]] == 0:
            del s_anagram[s[start]]

    if p_anagram == s_anagram:
        result.append(len(s) - len(p))

    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
        ("aa", "bb", []),
        ("baa", "aa", [1]),
        ("ababababab", "aab", [0, 2, 4, 6]),
    ]

    for s, p, expected in test_cases:
        result = findAnagrams(s, p)
        status = "✓" if result == expected else "✗"
        print(f"{status} s={s!r}, p={p!r}")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}\n")
