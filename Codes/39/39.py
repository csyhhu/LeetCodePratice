def combinationSum_1(candidates:list, target: int):
    """
    Basic dfs method.
    :param candidates:
    :param target:
    :return:
    """

    answers = []
    n = len(candidates)
    candidates.sort()
    # print(candidates)

    def dfs(idx:int, cur:int, _res:list, _answers:list):
        if cur == target:
            _answers.append(_res.copy())
            return
        elif cur > target:
            return
        # Give a sorted candidates, if the remain space is smaller than the current candidates, return
        if target - cur < candidates[idx]:
            return

        for add in range(n):
            if idx + add < n:
                added_idx = idx + add
                dfs(added_idx, cur + candidates[added_idx], _res + [candidates[added_idx]], _answers)

    for i in range(n):
        dfs(i, candidates[i], [candidates[i]], answers)

    return answers

def combinationSum_2(candidates:list, target: int):
    """
    Divide the problem into two actions in each step:
    1) Take candidiates[idx]
    2) Don't take candidiates[idx]
    :param candidates:
    :param target:
    :return:
    """
    answers = []
    candidates.sort()
    n = len(candidates)

    def dfs(idx:int, cur:int, _res:list, _answers:list):

        if cur == target:
            _answers.append(_res.copy())
            return
        elif cur > target:
            return

        if target - cur < candidates[idx]:
            return

        # Put candidate[idx] into path
        dfs(idx, cur + candidates[idx], _res + [candidates[idx]], _answers)
        # Skip the current idx
        if idx + 1 < n:
            dfs(idx + 1, cur, _res, _answers)

    dfs(0, 0, [], answers)

    return answers


def combinationSum(candidates:list, target: int):
    answers = []
    candidates.sort()
    n = len(candidates)
    stack = [[0, [], 0]]
    while len(stack) > 0:
        idx, path, cur = stack.pop(-1)

        if cur == target:
            answers.append(path.copy())
        elif cur > target:
            continue

        if target - cur < candidates[idx]:
            continue

        for add in range(n):
            if idx + add < n:
                added_idx = idx + add
                stack.append([added_idx, path + [candidates[added_idx]], cur + candidates[added_idx]])

    return answers


print(combinationSum(candidates = [2,3,6,7], target = 7))
print(combinationSum(candidates = [2,3,5], target = 8))
print(combinationSum([2,7,6,3,5,1],9))