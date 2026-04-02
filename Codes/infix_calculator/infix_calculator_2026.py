"""
[Custom] Infix Expression Calculator (Token Array)
（LeetCode 无原题，综合 LC 224 / LC 227 / LC 150 的延伸练习）

给定一个由字符串组成的 token 数组，表示一个中缀算术表达式，计算其结果。

Token 类型：
    - 整数字符串，如 "3", "14", "-2"
    - 运算符：'+', '-', '*', '/'
    - 括号：'(', ')'

规则：
    - 运算符优先级：'*' 和 '/' 高于 '+' 和 '-'
    - 括号改变优先级
    - 除法向零截断（truncate toward zero）

Example 1:
    Input: tokens = ["3", "+", "2", "*", "2"]
    Output: 7
    Explanation: 3 + (2 * 2) = 7

Example 2:
    Input: tokens = ["10", "+", "(", "6", "/", "(", "9", "+", "3", ")", ")"]
    Output: 10
    Explanation: 10 + (6 / (9 + 3)) = 10 + 0 = 10

Example 3:
    Input: tokens = ["14", "-", "3", "/", "2"]
    Output: 13
    Explanation: 14 - (3 / 2) = 14 - 1 = 13

Example 4:
    Input: tokens = ["(", "1", "+", "(", "4", "+", "5", "+", "2", ")", "-", "3", ")", "+", "(", "6", "+", "8", ")"]
    Output: 23

Approach:
    两种方法：
    方法一：Shunting Yard 算法
        - 用 op_stack 存运算符，num_stack 存操作数
        - 遇到运算符时，将 op_stack 中优先级 >= 当前运算符的弹出并计算
        - 遇到 '(' 直接压栈，遇到 ')' 弹出直到 '('
    方法二：递归下降（Recursive Descent）
        - 参考 LC 224 的括号处理思路扩展到支持 * /

Date: 2026-03-31
"""

PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2}


def apply_op(op: str, a: int, b: int) -> int:
    """计算 a op b"""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return int(a / b)  # 向零截断


def calculate(tokens: list[str]) -> int:
    pass


# Test cases
if __name__ == "__main__":
    test_cases = [
        (["3", "+", "2", "*", "2"], 7),
        (["14", "-", "3", "/", "2"], 13),
        (["3", "+", "5", "/", "2"], 5),
        (["10", "+", "(", "6", "/", "(", "9", "+", "3", ")", ")"], 10),
        (["(", "1", "+", "(", "4", "+", "5", "+", "2", ")", "-", "3", ")", "+", "(", "6", "+", "8", ")"], 23),
        (["2", "*", "(", "3", "+", "4", ")"], 14),
        (["1", "*", "2", "-", "3", "/", "4", "+", "5", "*", "6", "-", "7", "*", "8", "+", "9", "/", "10"], -24),
    ]

    for tokens, expected in test_cases:
        result = calculate(tokens)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {tokens}")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}\n")
