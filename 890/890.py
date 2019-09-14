def findAndReplacePattern(words, pattern):
    results = []
    for word in words:
        pat_dict = {}
        word_dict = {}
        exists = True
        for w, p in zip(word, pattern): # 'abc', 'abb'

            if w not in word_dict and p not in pat_dict:
                word_dict[w] = p
                pat_dict[p] = w
            else:
                if (p in pat_dict and pat_dict[p] != w) or (w in word_dict and word_dict[w] != p):
                    exists = False
                    break

        if exists:
            results.append(word)
    return results


def findAndReplacePattern2(words, pattern):
    """
    words / pattern is mapped to integer list where each elements represent the
    times of appearance of that elements,
    e.g.: 'abbmm' -> '12222'.
    That is not right.
    :param words:
    :param pattern:
    :return:
    """
    results = []
    base = chr('a')

    pat_count_map = {}
    pattern_map = []
    for p in pattern:
        if p in pat_count_map:
            pat_count_map[p] += 1
        else:
            pat_count_map[p] = 1
    for p in pattern:
        pattern_map.append(pat_count_map[p])

    for word in words:
        exists = True
        count_map = {}
        for w in word:
            if w in count_map:
                count_map[w] += 1
            else:
                count_map[w] = 1

        for idx, w in enumerate(word):
            # if str(count_map[w]) != pattern_map[idx]:
            if ord(count_map[w] + base) != ord(pattern_map[idx] + base):
                exists = False
                break

        if exists:
            results.append(word)

    return results


def findAndReplacePattern3(words, pattern):

    results = []
    pattern_prev_shown = {}
    pattern_map = []
    for p in pattern:
        if p not in pattern_prev_shown:
            pattern_prev_shown[p] = len(pattern_prev_shown)
    for p in pattern:
        pattern_map.append(pattern_prev_shown[p])

    for word in words:
        exists = True
        word_prev_shown = {}
        for w in word:
            if w not in word_prev_shown:
                word_prev_shown[w] = len(word_prev_shown)
        for idx, w in enumerate(word):
            if pattern_map[idx] != word_prev_shown[w]:
                exists = False
                break

        if exists:
            results.append(word)

    return results


words = ["abc","deq","mee","aqq","dkd","ccc"]
# words = ['mee']
pattern = "abb"
outputs = findAndReplacePattern3(words, pattern)
print(outputs)