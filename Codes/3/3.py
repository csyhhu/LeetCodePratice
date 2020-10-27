def lengthOfLongestSubstring(s):

    ans = 0
    last = [-1] * 128
    start = 0
    for idx, char in enumerate(s):
        if last[ord(char)] != -1: # It means char has ever appeared before
            # If char appeared before, the valid substring will be at least starts from the last index char visit,
            # or the current start point, which means from [start, idx], char didn't show
            start = max(start, last[ord(char)] + 1)
        # Update answer for the [start, idx] is a valid substring now.
        ans = max(ans, idx - start + 1)
        last[ord(char)] = idx
    return ans

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
s = "bbbbb"
print(lengthOfLongestSubstring(s))
s = "pwwkew"
print(lengthOfLongestSubstring(s))