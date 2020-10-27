def is_number(c):
    try:
        int(c)
        return True
    except ValueError:
        return False

"""
def calculate(s):

    if len(s) == 0:
        return 0

    # Search for number and operator
    number = ''
    operator = None
    idx = 0
    for idx, c in enumerate(s):
        if is_number(c):
            number += c
        else:
            operator = c
            break

    if operator == '+':
        return int(number) + calculate(s[idx:])
    elif operator == '-':
        return int(number) - calculate(s[idx:])
    elif operator in ['*', '\/']:
        second_number = ''
        for second_idx, c in enumerate(s[idx: ]):
            return None
"""

"""
def calculate(s):

    stack = []
    operator = "+"
    sign = 1
    number = ""
    idx = 0
    while idx < len(s):
        c = s[idx]
        # print(c)
        if is_number(c):
            number += c
            idx += 1
        elif c == '+':
            stack.append(sign * int(number))
            sign = 1
            number = ""
            idx += 1
        elif c == '-':
            stack.append(sign * int(number))
            sign = -1
            number = ""
            idx += 1
        elif c in ['*', '/']:
            print('I am here')
            second_number = ''
            for sec_idx in range(len(s[idx: ])):
                sec_c = s[sec_idx]
                # print(sec_c)
                if is_number(sec_c):
                    second_number += sec_c
                elif sec_c in ['*', '/', '+', '-']:
                    break
            # print(second_number)
            if c == '*':
                tmp_result = int(second_number) * stack[-1]
            else:
                tmp_result = stack[-1] // int(second_number)
            stack.pop(-1)
            stack.append(tmp_result)
            idx += sec_idx
        else:
            idx += 1
        # print(idx)
        # print(stack)

    return sum(stack)
"""

def calculate(s):

    stack = []
    pre_op = '+'
    number = 0
    for idx, c in enumerate(s):
        if is_number(c):
            number = number * 10 + int(c)
        # Previously I use 'elif' below, each is wrong for we need to consider the cases that c is the last character in the string
        if c in ['+', '-', '*', '/'] or idx == (len(s) - 1):
            if pre_op == '+':
                stack.append(number)
            elif pre_op == '-':
                stack.append(-number)
            elif pre_op == '*':
                top = stack.pop()
                stack.append(top * number)
            else:
                top = stack.pop()
                # Attention here: -3//2 = -2 in python, so we need to use -3/2=-1.5 -> int(-1.5)=-1 to deal with it
                if top > 0:
                    stack.append(top // number)
                else:
                    stack.append(int(top / number))
            pre_op = c
            number = 0
            # print(pre_op) # Here for debug
            print(stack)

    return sum(stack)

# inputs = " 3+5 / 2 "
# inputs = "3+2*2"
inputs = "14-3/2"
print(calculate(inputs))
