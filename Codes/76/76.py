def minWindow(s: str, t: str):

    left = 0
    right = 0
    scount = dict()
    tcount = dict()
    for c in t:
        if c in tcount:
            tcount[c] += 1
        else:
            tcount[c] = 1

    equality = 0
    min_len = 10e9
    min_right = 0
    min_left = 0
    while right < len(s):
        # For each new character added by moving right window, add it to scount
        c = s[right]
        if c not in scount:
            scount[c] = 1
        else:
            scount[c] += 1
        # I set == here instead of >= is because that equality should represent the number of first time sub s contain certain character in t
        if c in tcount and tcount[c] == scount[c]:
            equality += 1
        right += 1
        # print(c, scount)
        # If all characters in t is covered by s, we move the left window.
        while left <= right and equality == len(tcount):
            if min_len > right - left + 1:
                min_len = right - left + 1
                min_right = right
                min_left = left
            remove_c = s[left]
            scount[remove_c] -= 1
            if remove_c in tcount and tcount[remove_c] == scount[remove_c] + 1:
                equality -= 1
            left += 1
        # print(left, right)

    return s[min_left: min_right]

print(minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(minWindow(s = "a", t = "a"))