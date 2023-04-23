# 3: ((())), ()(())

def generateParenthesis_1(n: int):
    results = set()
    if n == 0:
        results.add("")
        return results
    else:
        pre_results = generateParenthesis(n - 1)
        for pre in pre_results:
            for idx, char in enumerate(pre):
                if char == "(":
                    pre = pre[:idx+1] + '()' + pre[idx+1:]
                    results.add(pre)
                    pre = pre[:idx+1] + pre[idx+3:]
            results.add("()" + pre)
    return results


def generateParenthesis(n: int):

    def generateParenthesisDFS(left, right, cur_res, results):
        if left == 0 and right == 0:
            results.append(cur_res)
            return
        elif left > right:
            return
        else:
            if left > 0:
                next_res = cur_res + '('
                generateParenthesisDFS(left-1, right, next_res, results)
            if right > 0:
                next_res = cur_res + ')'
                generateParenthesisDFS(left, right-1, next_res, results)

    res = []
    generateParenthesisDFS(n, n, "", res)
    return res


print(generateParenthesis(3))

# () => (())