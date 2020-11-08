def ladderLength_0(beginWord: str, endWord: str, wordList):

    visit = dict()
    for word in wordList:
        visit[word] = False

    def neighbor(word_a, word_b):
        n_identity = 0
        # l = len(word_a)
        # for char_a, char_b in zip(word_a, word_b):
        for idx in range(len(word_a)):
            char_a, char_b = word_a[idx], word_b[idx]
            # print(char_a, char_b)
            if char_a == char_b:
                n_identity += 1
            if n_identity > 1:
                break
        return n_identity == 1

    bfs = []
    bfs.append(beginWord)
    steps = 0
    # print(bfs)
    while len(bfs) > 0:
        curWord = bfs.pop(0)
        # print(curWord)
        if curWord == endWord:
            return steps + 1
        for nextWord in wordList:
            if neighbor(curWord, nextWord):
                # visit[nextWord] = True
                bfs.append(nextWord)
                wordList.remove(nextWord) # Remove elements from list while iterating the list will cause error.
        steps += 1
    return 0

    """
    def dfs(curWord):

        if curWord == endWord:
            return 0
        if sum(visit.values()) == len(visit):
            return 1e9

        result = 1e9
        for nextWord in wordList:
            if visit[nextWord]:
                continue
            else:
                visit[nextWord] = True
                if neighbor(curWord, nextWord):
                    cur_result = dfs(nextWord) + 1
                    visit[nextWord] = False
                    result = min(cur_result, result)

        return result
    """

def ladderLength(beginWord: str, endWord: str, wordList):

    bfs = []
    bfs.append(beginWord)
    steps = 0
    while len(bfs) > 0:
        curWord = bfs.pop(0)
        steps += 1
        print(bfs)
        if curWord == endWord:
            return steps
        # Convert string to list for character replacement
        curWordList = list(curWord)
        for idx, char in enumerate(curWordList):
            for new_char in range(0, 26):
                curWordList[idx] = chr(new_char+ord('a'))
                new_word = "".join(curWordList)
                if new_word in wordList:
                    bfs.append(new_word)
                    wordList.remove(new_word)
                    # print(bfs)
            curWordList[idx] = char
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(ladderLength(beginWord, endWord, wordList))