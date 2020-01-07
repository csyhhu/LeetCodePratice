def groupAnagrams_sort(strs):

    anagrams = dict()
    for str in strs:
        sorted_str = "".join(sorted([s for s in str]))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(str)
        else:
            anagrams[sorted_str] = [str]

    return anagrams.values()


def groupAnagrams(strs):
    anagrams = dict()
    base = ord('a')
    for str in strs:
        key = [0] * 26
        for s in str:
            key[ord(s)-base] += 1
        key = tuple(key)
        if key in anagrams:
            anagrams[key].append(str)
        else:
            anagrams[key] = [str]
    return anagrams.values()


inputs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(inputs))
