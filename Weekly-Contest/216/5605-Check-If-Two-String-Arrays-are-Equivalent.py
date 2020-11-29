def arrayStringsAreEqual(word1, word2):
    word1_concat = ""
    word2_concat = ""
    for w in word1:
        word1_concat += w
    for w in word2:
        word2_concat += w
    if word1_concat == word2_concat:
        return True
    else:
        return False

print(arrayStringsAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]))
print(arrayStringsAreEqual(["a", "cb"], word2 = ["ab", "c"]))