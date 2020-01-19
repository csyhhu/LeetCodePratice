def letterCombinations(digits):
    # import copy
    mappings = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],

    }

    results = []

    def dfs(prefix, digits):

        # results = []

        if len(prefix) == len(digits):
            # print(prefix)
            result = ''
            for p in prefix:
                result += p
            results.append(result)
            return
            # return prefix

        # for digit in digits:
        idx = len(prefix)
        characters = mappings[digits[idx]]
        for char in characters:
            prefix.append(char)
            dfs(prefix, digits)
            # results.append(copy.deepcopy(dfs(prefix, digits)))
            # print(results)
            prefix.pop()

        # return results

    # results = dfs([], digits)

    if len(digits) == 0:
        return []
    else:
        dfs([], digits)
        return results
    # results = dfs([], digits)
    # con_results = []
    # for result in results:
    #     print(result)
    #     con_result = ''
    #     for r in result:
    #         print(r)
    #         con_result = con_result + r
    #     con_results.append(con_results)
    # return con_results


inputs = "23"
print(letterCombinations(inputs))