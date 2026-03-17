"""
[1249] Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
so that the resulting string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
    - It is the empty string, contains only lowercase characters, or
    - It can be written as AB (A concatenated with B), where A and B are valid strings, or
    - It can be written as (A), where A is a valid string.

Example 1:
    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
    Input: s = "a)b(c)d"
    Output: "ab(c)d"

Example 3:
    Input: s = "))(("
    Output: ""
    Explanation: An empty string is also valid.

Constraints:
    - 1 <= s.length <= 10^5
    - s[i] is either '(' , ')' , or a lowercase English letter.

Key Insights (关键洞察):
    - 核心思想: 使用栈来追踪需要删除的括号位置
    - 遍历字符串，遇到 '(' 入栈（记录索引）
    - 遇到 ')' 时，如果栈不为空则弹出（匹配成功），否则标记该 ')' 需要删除
    - 遍历结束后，栈中剩余的 '(' 都需要删除
    - 最后构建结果字符串，跳过所有需要删除的索引

Date: 2026-03-08
"""



def minRemoveToMakeValid(s):
    """
    思路：
    栈 + 集合标记法
    
    TODO: 实现这个函数
    步骤：
    1. 初始化栈用于存储 '(' 的索引
    2. 初始化集合用于存储需要删除的字符索引
    3. 遍历字符串：
       - 遇到 '(' 入栈
       - 遇到 ')' 时，如果栈不为空则弹出，否则加入删除集合
    4. 将栈中剩余的 '(' 索引加入删除集合
    5. 构建结果字符串，跳过删除集合中的索引
    
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    parentheses = []
    parentheses_remove_index = []
    for idx, c in enumerate(s):
        if c == '(':
            parentheses.append(c)
            parentheses_remove_index.append(idx)
        elif c == ')':
            if parentheses and parentheses[-1] == '(':
                parentheses.pop()
                parentheses_remove_index.pop()
            else:
                parentheses.append(c)
                parentheses_remove_index.append(idx)
    
    result = ""
    for idx, c in enumerate(s):
        if c in ['(', ')'] and idx in parentheses_remove_index:
            continue
        result += c
    return result



def minRemoveToMakeValid_optimized(s):
    """
    优化版本：使用集合存储需要删除的索引
    
    关键优化：用 set 替代 list 存储删除索引，查找从 O(n) 变成 O(1)
    
    TODO: 实现这个函数
    步骤：
    1. 使用栈存储 '(' 的索引
    2. 使用 set 存储需要删除的索引
    3. 遍历字符串处理括号匹配
    4. 栈中剩余的 '(' 索引加入 set
    5. 构建结果字符串时，检查索引是否在 set 中（O(1)查找）
    
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    pass



def minRemoveToMakeValid_one_pass(s):
    """
    单次遍历 + 原地构建法：
    不需要额外存储删除索引，遍历时直接构建结果
    
    关键思路：
    1. 第一遍遍历：构建字符串，用栈记录 '(' 位置，遇到不匹配的 ')' 直接跳过
    2. 第二遍：从后往前扫描，删除多余的 '('
    
    TODO: 实现这个函数
    提示：可以用 list 作为可变字符串，配合 pop() 删除多余括号
    
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    pass


# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "lee(t(c)o)de)"
    result1 = minRemoveToMakeValid(s1)
    print(f"Input: {s1}")
    print(f"Output: {result1}")
    print(f"Expected: lee(t(c)o)de (or other valid)\n")

    # Test case 2
    s2 = "a)b(c)d"
    result2 = minRemoveToMakeValid(s2)
    print(f"Input: {s2}")
    print(f"Output: {result2}")
    print(f"Expected: ab(c)d\n")

    # Test case 3
    s3 = "))(("
    result3 = minRemoveToMakeValid(s3)
    print(f"Input: {s3}")
    print(f"Output: {result3}")
    print(f"Expected: (empty string)\n")

    # Test case 4
    s4 = "(a(b(c)d)"
    result4 = minRemoveToMakeValid(s4)
    print(f"Input: {s4}")
    print(f"Output: {result4}")
    print(f"Expected: a(b(c)d) or (ab(c)d)\n")

    # Edge cases
    print("=" * 50)
    print("Edge cases:")
    print("=" * 50)
    edge_cases = [
        ("", ""),
        ("abc", "abc"),
        ("(", ""),
        (")", ""),
        ("()", "()"),
        ("(a)", "(a)"),
        ("(a(b)c)d)", "(a(b)c)d"),
    ]
    
    for test_input, expected in edge_cases:
        result = minRemoveToMakeValid(test_input)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{test_input}', Output: '{result}', Expected: '{expected}'")
