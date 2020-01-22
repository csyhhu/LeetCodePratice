def partition(s):

    results = []
    if len(s) == 0:
        return results
    # Construct the first result
    result = []
    for char in s:
        result.append(char)
    results.append(result)
    while True:
        last_result = results[-1]
        result = []
        for idx in range(len(last_result)):
            pass
            # if idx == 0 and palindrome == last_result[idx + 1]:
            #     result.append(palindrome + last_result[idx + 1])
            # elif idx == len(last_result) - 1 and palindrome == last_result[idx - 1]:
            #     result.append(last_result[idx - 1] + palindrome)
            # else:
            #     if last_result[idx - 1] == last_result[idx + 1]:
            #         result.append(last_result[idx - 1] + palindrome + last_result[idx + 1])
            #     else:
            #         result.append(palindrome)

        if result == last_result[-1]:
            break
        else:
            results.append(result)


def partition_DFS(s):
    import copy

    def isPalindrome(subs):
        n_subs = len(subs)
        for i in range(int(n_subs / 2)):
            if subs[i] != subs[n_subs - i - 1]:
                return False
        return True

    results = []
    stack = []
    n = len(s)
    def dfs(start):
        if start == n:
            results.append(copy.deepcopy(stack))
            return
        for i in range(start + 1, n + 1):
            # print(s[start: i])
            if isPalindrome(s[start: i]):
                stack.append(s[start: i])
                dfs(i)
                stack.pop()
    dfs(0)
    return results

# inputs = "aab"
inputs = "aaabc"
print(partition_DFS(inputs))


def isPalindrome(subs):
    n_subs = len(subs)
    for i in range(int(n_subs / 2)):
        if subs[i] != subs[n_subs - i - 1]:
            return False
    # print(subs)
    return True