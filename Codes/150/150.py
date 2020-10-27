def evalRPN(tokens):
    def is_number(c):
        try:
            int(c)
            return True
        except ValueError:
            return False
    stack = []
    for t in tokens:
        if is_number(t):
            stack.append(int(t))
        else:
            o1 = stack.pop()
            o2 = stack.pop()
            if t == '+':
                stack.append(o1 + o2)
            elif t == '-':
                stack.append(o2 - o1)
            elif t == '*':
                stack.append(o1 * o2)
            else:
                if o1 > 0 and o2 > 0:
                    stack.append(o2 // o1)
                else:
                    stack.append(int(o2 / o1))
        # print(stack)
    return sum(stack)

# inputs = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
inputs = ["4","3","-"]
print(evalRPN(inputs))