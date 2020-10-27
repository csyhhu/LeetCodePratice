def ladderLength(beginWord: str, endWord: str, wordList):

    visit = dict()
    for word in wordList:
        visit[word] = False

    def neighbor(word_a, word_b):
        n_identity = 0
        for char_a, char_b in zip(word_a, word_b):
            print(char_a, char_b)
            if char_a == char_b:
                n_identity += 1
            if n_identity > 1:
                break
        return n_identity == 1

    bfs = []
    bfs.append(beginWord)
    steps = 0
    while len(bfs) > 0:
        curWord = bfs.pop(0)
        # print(curWord)
        if curWord == endWord:
            return steps + 1
        for nextWord in wordList:
            if neighbor(curWord, nextWord):
                # visit[nextWord] = True
                bfs.append(nextWord)
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



beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))