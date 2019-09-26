def customSortString(S, T):

    chara_dict = {}
    for t in T:
        if t in chara_dict:
            chara_dict[t] += 1
        else:
            chara_dict[t] = 1
    results = ''
    for s in S:
        if s in chara_dict:
            results += (s*chara_dict[s])
            chara_dict.pop(s)
    for remain_t, n in chara_dict.items():
        results += remain_t*n

    return results


def customSortString2(S, T):
    import collections
    pos = collections.defaultdict(int)
    for i in range(len(S)):
        pos[S[i]] = i
    print(pos)
    res = sorted(T, key=lambda x: pos[x])
    return "".join(res)

S = "cba"
T = "abcd"
outputs = customSortString2(S, T)
print(outputs)