def longestDecomposition(text):

    n = len(text)
    # print(n)
    for i in range(1, int(n/2) + 1):
        if text[:i] == text[n-i:]:
            return 2 + longestDecomposition(text[i:n-i])
    if n == 0:
        return 0
    else:
        return 1

text = "ghiabcdefhelloadamhelloabcdefghi"
print(longestDecomposition(text))