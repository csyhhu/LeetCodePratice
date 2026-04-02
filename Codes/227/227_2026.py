"""
[227] Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be
in the range of [-2^31, 2^31 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical
expressions, such as eval().

Example 1:
    Input: s = "3+2*2"
    Output: 7

Example 2:
    Input: s = " 3/2 "
    Output: 1

Example 3:
    Input: s = " 3+5 / 2 "
    Output: 5

Constraints:
    - 1 <= s.length <= 3 * 10^5
    - s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
    - '+' is not used as a unary operator (i.e., "+1" and "+(2 + 3)" are invalid).
    - '-' could be used as a unary operator (i.e., "-1" and "-(2 + 3)" are valid).
    - There will be no two consecutive operators in the input.
    - Every number and running calculation will fit in a signed 32-bit integer.

Date: 2026-03-31
"""


import operator


def calculate(s: str) -> int:
    s = s.replace(' ', '')
    if not s:
        return 0
    stack = []
    if s[0].isdigit():
        pre_op = "+"
    else:
        pre_op = s[0]
    pre_digit = 0
    print(len(s))
    for idx in range(len(s)):
        if s[idx].isdigit():
            pre_digit = pre_digit * 10 + int(s[idx])
            # idx += 1
        if s[idx] in ('+', '-', '*', '/') or idx == len(s)-1:
            if pre_op == '+':
                stack.append(pre_digit)
            elif pre_op == '-':
                stack.append(-1 * pre_digit)
            elif pre_op in ('*', '/'):
                operand1 = stack.pop()
                operand2 = pre_digit
                if pre_op == '*':
                    stack.append(operand1 * operand2)
                else:
                    # print("I  am here")
                    stack.append(int(operand1 / operand2))
            pre_digit = 0
            pre_op = s[idx]
        # print(pre_op, stack)
    return sum(stack)

            


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("3+2*2", 7),
        (" 3/2 ", 1),
        (" 3+5 / 2 ", 5),
        ("14-3/2", 13),
        ("1*2-3/4+5*6-7*8+9/10", -24),
    ]

    for s, expected in test_cases:
        result = calculate(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {repr(s)}")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}\n")
