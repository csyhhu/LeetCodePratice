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

Key Insights (关键洞察):
    - 核心思想: 使用滑动窗口（Sliding Window）来维护一个不含重复字符的子串
    - 需要一个哈希表/字典来追踪窗口内每个字符最后出现的位置
    - 两个指针 left 和 right 定义窗口的边界
    - 当发现重复字符时，移动 left 指针来缩小窗口
    - 时间复杂度: O(n) - 每个字符最多被访问两次
    - 空间复杂度: O(min(m, n)) - m是字符集大小，n是字符串长度

关键思想对比:
    - 暴力法: O(n^3) - 枚举所有子串，检查是否有重复 (太慢)
    - 优化: O(n^2) - 用HashSet，但还是需要两层循环
    - 最优: O(n) - 滑动窗口一次遍历

Date: 2026-03-08
"""

def lengthOfLongestSubstring(s):
    """
    [基础版本] 滑动窗口 + HashSet 法
    
    这是最容易理解的版本，用集合维护当前窗口内的字符
    
    思路：
    1. 用两个指针 left 和 right 定义一个滑动窗口
    2. 用集合 char_set 存储窗口内的所有字符
    3. 不断扩展右指针，直到发现重复字符
    4. 收缩左指针直到重复的字符被移除
    5. 记录最大的窗口长度
    
    步骤：
    1. 初始化 left=0, max_len=0
    2. 初始化空集合 char_set
    3. 用 right 遍历字符串：
       - 如果 s[right] 在 char_set 中：
         不断从左边移除字符直到 s[right] 不在 char_set 中
       - 将 s[right] 加入 char_set
       - 更新 max_len = max(max_len, right - left + 1)
    4. 返回 max_len
    
    时间复杂度：O(n)（每个字符最多被访问两次）
    空间复杂度：O(min(m, n)) 其中 m 是字符集大小
    
    例子: "abcabcbb"
    left=0, right=0: char_set={'a'}, max_len=1
    left=0, right=1: char_set={'a','b'}, max_len=2
    left=0, right=2: char_set={'a','b','c'}, max_len=3
    left=0, right=3: 'a'重复了，left移到1，char_set={'b','c','a'}, max_len=3
    ...依此类推
    """
    right = 0
    longest_substring = []
    max_len = 0
    while right < len(s):
        # print(s[right],longest_substring)
        if s[right] not in longest_substring:
            longest_substring.append(s[right])
            right += 1
        else:
            longest_substring = longest_substring[1:]
        max_len = max(max_len, len(longest_substring))
    return max_len



def lengthOfLongestSubstring_dict(s):
    """
    [优化版本] 滑动窗口 + 字典法（推荐）
    
    相比 HashSet 方法，用字典记录字符位置可以直接跳过重复字符，更高效
    
    思路：
    1. 用字典 char_pos 存储每个字符最后出现的位置
    2. 当发现重复字符时，不用一个一个移除，而是直接跳到重复字符的右边
    
    步骤：
    1. 初始化 left=0, max_len=0
    2. 初始化空字典 char_pos={}
    3. 用 right 遍历字符串：
       - 如果 s[right] 在 char_pos 中且 char_pos[s[right]] >= left：
         说明发现了在窗口内的重复字符
         left = max(left, char_pos[s[right]] + 1)
       - 更新 char_pos[s[right]] = right
       - 更新 max_len = max(max_len, right - left + 1)
    4. 返回 max_len
    
    时间复杂度：O(n)（只需一次遍历）
    空间复杂度：O(min(m, n))
    
    例子: "abcabcbb"
    right=0: char_pos={'a':0}, left=0, max_len=1
    right=1: char_pos={'a':0,'b':1}, left=0, max_len=2
    right=2: char_pos={'a':0,'b':1,'c':2}, left=0, max_len=3
    right=3: 'a' 在 char_pos 且 char_pos['a']=0 >= left=0，left=max(0,0+1)=1, max_len=3
    ...依此类推
    """
    pass


def lengthOfLongestSubstring_brute_force(s):
    """
    [暴力版本] 用来理解问题的天真方法
    
    这不是最优解，但能帮助理解问题的本质
    
    思路：
    枚举所有可能的子串，检查是否有重复字符
    
    步骤：
    1. 遍历所有起始位置 i
    2. 从位置 i 开始，不断扩展到位置 j
    3. 检查 s[i:j+1] 是否有重复字符
    4. 记录最长的无重复子串长度
    
    时间复杂度：O(n^3) - 太慢了！
    空间复杂度：O(min(m, n))
    
    不推荐在实际面试中使用，但理解它能帮助理解为什么滑动窗口更优
    """
    pass


# Test cases
if __name__ == "__main__":
    print("=" * 70)
    print("LeetCode 3 - Longest Substring Without Repeating Characters")
    print("=" * 70)
    
    # 测试用例集合
    test_cases = [
        ("abcabcbb", 3),      # 'abc'
        ("bbbbb", 1),          # 'b'
        ("pwwkew", 3),         # 'wke'
        ("", 0),               # empty
        (" ", 1),              # single space
        ("au", 2),             # 'au'
        ("dvdf", 3),           # 'vdf'
        ("aab", 2),            # 'ab'
        ("abcdefg", 7),        # 'abcdefg'
    ]
    
    print("\n【第1步】测试基础版本 - lengthOfLongestSubstring")
    print("使用 HashSet 方法实现滑动窗口")
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
    # print("使用字典方法，一次遍历完成")
    # print("-" * 70)
    
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
    # print("用于理解问题本质（不推荐在实际使用中用）")
    # print("-" * 70)
    
    # 只测试小规模输入
    # small_test_cases = [
    #     ("abcabcbb", 3),
    #     ("bbbbb", 1),
    #     ("au", 2),
    # ]
    
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
    
    # print("\n" + "=" * 70)
    # print("可视化示例：'abcabcbb'")
    # print("=" * 70)
    # print("我们需要找到最长的不含重复字符的子串\n")
    # print("字符串:  a  b  c  a  b  c  b  b")
    # print("索引:    0  1  2  3  4  5  6  7\n")
    # print("滑动窗口过程:")
    # print("  Step 1: [a]              -> length=1, max=1")
    # print("  Step 2: [ab]             -> length=2, max=2")
    # print("  Step 3: [abc]            -> length=3, max=3 ⭐ 最长")
    # print("  Step 4: 'a'重复了        -> left移到1，窗口=[bca], length=3, max=3")
    # print("  Step 5: 'b'重复了        -> left移到2，窗口=[cab], length=3, max=3")
    # print("  Step 6: 'c'重复了        -> left移到3，窗口=[abc], length=3, max=3")
    # print("  Step 7: 'b'重复了        -> left移到6，窗口=[b], length=1, max=3")
    # print("  Step 8: 'b'重复了        -> left移到7，窗口=[b], length=1, max=3\n")
    # print("答案: 3 (子串 'abc')")
