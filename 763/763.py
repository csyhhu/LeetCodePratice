def find_last_shown(char, S):

    for idx, s in enumerate(S[::-1]):
        if char == s:
            return len(S) - idx - 1

    return -1

def partitionLabels(S):

    results = []
    n = len(S)

    # Find a HashMap recording the last shown idx for each character
    last_shown = {}
    for char in S:
        if char not in last_shown:
            last_shown[char] = find_last_shown(char, S)

    # Begin Process
    idx = -1
    while idx < n-1:
        start = idx + 1
        # print(start)
        end = last_shown[S[start]]
        for i in range(start, n):
            if last_shown[S[i]] < end:
                continue
            else:
                end = last_shown[S[i]]
            if i == end:
                break
        # print(end)
        results.append(end-start+1)
        idx = end

    return results

inputs = 'ababcbacadefegdehijhklij'
outputs = partitionLabels(inputs)
print(outputs)