def canBeValidTLE(s: str, locked: str):
    """
    Time Limit Exceeded
    """
    def isValid(s_stack: list, remain_s: str, remain_loc: str):
        # print(s_stack, remain_s, remain_loc)
        if len(s_stack) == 0:
            if len(remain_s) == 0:
                return True
            elif len(remain_s) > 0:
                next_s = remain_s[0]
                next_loc = remain_loc[0]
        else:
            if len(remain_s) > 0:
                next_s = remain_s[0]
                next_loc = remain_loc[0]
            else:
                return False

        if next_loc == "1":
            if next_s == "(":
                s_stack.append(next_s)
                return isValid(s_stack, remain_s[1:], remain_loc[1:])
            elif next_s == ")":
                if len(s_stack) > 0 and s_stack[-1] == "(":
                    s_stack.pop(-1)
                    return isValid(s_stack, remain_s[1:], remain_loc[1:])
                else:
                    return False
        else:
            add_left_stack = s_stack + ["("]
            if len(s_stack) > 0 and s_stack[-1] == "(":
                add_right_stack = s_stack[:-1]
                return isValid(add_left_stack, remain_s[1:], remain_loc[1:]) or isValid(add_right_stack, remain_s[1:], remain_loc[1:])
            else:
                return isValid(add_left_stack, remain_s[1:], remain_loc[1:])

    stack = []
    return isValid(stack, s, locked)


def canBeValidWA(s: str, locked: str):

    redundancy = 0
    n_changable = 0

    for idx, parentheses in enumerate(s):

        if redundancy < 0:
            if n_changable > 0:
                redundancy += 2
                n_changable -= 1
            else:
                return False

        if locked[idx] == '0':
            n_changable += 1

        if parentheses == "(":
            redundancy += 1
        else:
            redundancy -= 1

    print(redundancy, n_changable)
    if redundancy < 0:
        return False
    elif redundancy == 0:
        return True
    elif redundancy % 2 == 0 or (n_changable - redundancy) % 2 == 0:
        return True
    else:
        return False


def canBeValid(s: str, locked: str):

    redundancy = 0
    n_changable = 0

    for idx, parentheses in enumerate(s):

        if redundancy < 0:
            if n_changable > 0:
                redundancy += 2
                n_changable -= 1
            else:
                return False

        if locked[idx] == '0':
            parentheses = ")"
            n_changable += 1

        if parentheses == "(":
            redundancy += 1
        else:
            redundancy -= 1

    if redundancy == 0:
        return True
    else:
        return False


s = "))()))"
locked = "010100"
print(canBeValid(s, locked))

s = ")"
locked = "0"
print(canBeValid(s, locked))

s =")"
locked ="1"
print(canBeValid(s, locked))

s = "()"
locked = "11"
print(canBeValid(s, locked))

s = "((()(()()))()((()()))))()((()(()"
locked = "10111100100101001110100010001001"
print(canBeValid(s, locked))

s = "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
locked = "100011110110011011010111100111011101111110000101001101001111"
print(canBeValid(s, locked))