def longestSubstring(s, k):
    if len(s) < k:
        return 0
    for char in set(s):
        # If there exist such a string with elements whose appearance is smaller than k, continue util we meet a substring with bigger than k appearance.
        if s.count(char) < k:
            return max(longestSubstring(sub_s, k) for sub_s in s.split(char))
    # Code reaches here if every char in s appears more than k times, then return its length.
    return len(s)

s = "aaabb"
k = 3
print(longestSubstring(s, k))
