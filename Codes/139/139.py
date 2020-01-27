def wordBreak_TLE(s, wordDict):
    n_s = len(s)
    def dfs(cur_s):
        # print(cur_s)
        if len(cur_s) == n_s:
            return (cur_s == s)
        elif len(cur_s) > n_s:
            return False
        else:
            for seg in wordDict:
                 if dfs(cur_s+seg):
                     return True
        return False

    return dfs('')


def wordBreak_TLE2(s, wordDict):

    max_len = max(len(w) for w in wordDict)
    def dfs(seg):
        # print(seg)
        if len(seg) == 0:
            return True
        for i in range(1, max_len+1):
            # print(seg[0: i])
            if seg[0: i] in wordDict:
                if dfs(seg[i: ]):
                    return True
        return False
    return dfs(s)


def wordBreak(s, wordDict):

    # To record whether this segmentation is in wordDict
    breakable = dict()
    def canBreak(s):
        if s in breakable:
            return breakable[s]
        if s in wordDict:
            breakable[s] = True
            return True
        # Make segmentation of s: to tell whether the front / back part is in breakable or in wordDict
        for i in range(1, len(s)):
            rest = s[i: ]
            # Both ways work
            # if rest in wordDict and canBreak(s[0: i]):
            if s[0: i] in wordDict and canBreak(rest):
                breakable[s] = True
                return True
        breakable[s] = False
        return False

    return canBreak(s)



s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))
s = "applepenapple"
wordDict = ["apple", "pen"]
print(wordBreak(s, wordDict))
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s, wordDict))