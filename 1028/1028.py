from utils.printResults import printTreePreorder

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recoverFromPreorder(S):

    stack = []
    str_idx = 0
    while str_idx < len(S):

        level = 0
        val = ''

        while str_idx < len(S) and S[str_idx] == '-':
            level += 1
            str_idx += 1
        while str_idx < len(S) and S[str_idx] != '-': # Pay attention to 401
            val += S[str_idx]
            str_idx += 1
        while len(stack) > level: # Retrace back
            stack.pop()

        node = TreeNode(val)
        if stack and stack[-1].left is None:
            stack[-1].left = node
        elif stack:
            stack[-1].right = node
        stack.append(node)

    return stack[0]

inputs = "1-401--349---90--88"
# inputs =  "1-2--3--4-5--6--7"
outputs = recoverFromPreorder(inputs)
printTreePreorder(outputs)