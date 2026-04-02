"""
[224] Basic Calculator
https://leetcode.com/problems/basic-calculator/

Given a string s representing a valid expression, implement a basic calculator
to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings
as mathematical expressions, such as eval().

The expression may contain:
    - Non-negative integers
    - '+', '-' operators
    - Parentheses '(' and ')'
    - Spaces ' '

Example 1:
    Input: s = "1 + 1"
    Output: 2

Example 2:
    Input: s = " 2-1 + 2 "
    Output: 3

Example 3:
    Input: s = "(1+(4+5+2)-3)+(6+8)"
    Output: 23

Constraints:
    - 1 <= s.length <= 3 * 10^5
    - s consists of digits, '+', '-', '(', ')', and ' '.
    - s represents a valid expression.
    - '+' is not used as a unary operator.
    - '-' could be used as a unary operator (i.e., "-1" and "-(2+3)" are valid).
    - There will be no two consecutive operators.
    - Every number and running calculation will fit in a signed 32-bit integer.

Hint:
    - 遇到 '(' 时，把当前的 result 和 sign 压栈，然后重置
    - 遇到 ')' 时，弹出栈中保存的 sign 和 result，还原上一层状态

Date: 2026-03-31
"""


def calculate(s: str) -> int:
    pass


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("1 + 1", 2),
        (" 2-1 + 2 ", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
        ("1-(3-2)", 0),
        ("- (3 + (4 - 2))", -5),
    ]

    for s, expected in test_cases:
        result = calculate(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {repr(s)}")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}\n")
