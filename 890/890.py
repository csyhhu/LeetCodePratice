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

    for word in words:

        if exists:
            results.append(word)

    return results

# words = ["abc","deq","mee","aqq","dkd","ccc"]
words = ['mee']
pattern = "abb"
outputs = findAndReplacePattern2(words, pattern)
print(outputs)