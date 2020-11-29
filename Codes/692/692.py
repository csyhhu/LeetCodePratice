def topKFrequent(words, k: int):
    import functools
    # from collections import OrderedDict
    word_freq = dict()
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 0

    def cmp(item1, item2):
        if item1[1] > item2[1]:
            return 1
        elif item1[1] < item2[1]:
            return -1
        else:
            if item1[0] < item2[0]:
                return 1
            else:
                return -1

    # sorted_num_freq = sorted(word_freq.items(), key=lambda item: item[1])
    sorted_num_freq = sorted(word_freq.items(), key=functools.cmp_to_key(cmp))
    sorted_num_freq.reverse()

    results = []
    for i in range(k):
        results.append(sorted_num_freq[i][0])

    return results

print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2))

print(topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))