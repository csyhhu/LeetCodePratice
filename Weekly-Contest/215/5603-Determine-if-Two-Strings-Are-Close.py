def closeStrings(word1: str, word2: str):
    """
    1) Swap any two existing characters
    2) Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    :param word1:
    :param word2:
    :return:
    """
    if len(word1) != len(word2):
        return False

    word1_dict = dict()
    for c in word1:
        if c in word1_dict:
            word1_dict[c] += 1
        else:
            word1_dict[c] = 1

    word2_dict = dict()
    for c in word2:
        if c in word2_dict:
            word2_dict[c] += 1
        else:
            word2_dict[c] = 1

    if len(word1_dict) != len(word2_dict):
        return False

    if set(word1_dict.keys()) != set(word2_dict.keys()):
        return False

    for start, n_start in word1_dict.items():
        for end, n_end in word2_dict.items():
            if n_start == n_end:
                word2_dict.pop(end)
                break

    if len(word2_dict) == 0:
        return True
    else:
        return False

# word1 = "cabbba"
# word2 = "abbccc"
# print(closeStrings(word1, word2))

word1 = "usu"
word2 = "aax"
print(closeStrings(word1, word2))