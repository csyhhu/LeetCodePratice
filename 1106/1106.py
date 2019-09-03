def parseBoolExpr_0(expression):
    # stack = []
    # for exp in list(expression):
    #     if exp == 't':
    #         stack.append(True)
    #     elif exp == 'f':
    #         stack.append(False)

    stack = []
    expression = expression.replace('t', '1')
    expression = expression.replace('f', '0')
    ex = list(expression)
    while len(ex) > 0:
        char = ex.pop(0)
        # Keep pushing character into stack until we meet a )
        # that means it is time to process this part
        if char != ')':
            stack.append(char)
            continue
        # Process a ()
        ts = ''
        while len(stack) > 0:
            item = stack.pop(-1)
            if item == '(':
                break
            ts += item
        ts_list = ts.split(',')
        and_or = stack.pop(-1)
        if and_or == '!':
            stack.append('1' if ts_list[0] == '0' else '0')
        elif and_or == '|':
            stack.append('1' if '1' in ts_list else '0')
        else:
            stack.append('0' if '0' in ts_list else '1')
    return stack[0] == '1'


def parseBoolExpr(expression):

    stack = []
    ex = list(expression)

    while len(ex) > 0:

        char = ex.pop(0)
        if char != ')':
            stack.append(char)
            continue

        cur_phase = ''
        while len(stack) > 0:
            char = stack.pop(-1)
            if char == '(':
                break
            cur_phase += char

        cur_phase = cur_phase.split(',')
        operator = stack.pop(-1)

        if operator == '!':
            stack.append('t' if cur_phase[0] == 'f' else 'f')
        elif operator == '|':
            stack.append('t' if 't' in cur_phase else 'f')
        else:
            stack.append('f' if 'f' in cur_phase else 't')

        # print(stack)

    return (stack[0] == 't')



expression = "|(&(t,f,t),!(t))"
outputs = parseBoolExpr(expression=expression)
print(outputs)