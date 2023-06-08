from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        format_dict = {}
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                format_temp = word[: i] + "*" + word[i + 1:]
                format_dict[format_temp] = format_dict.get(format_temp, []) + [word]
        
        print(format_dict)
        visited = set([beginWord])
        q = deque()
        q.append(beginWord)
        relation = 1
        while q:
            length = len(q)
            for i in range(length):
                word = q.popleft()
                if word == endWord:
                    return relation
                for i in range(len(word)):
                    format_temp = word[: i] + "*" + word[i + 1:]
                    for temp in format_dict[format_temp]:
                        if temp not in visited:
                            visited.add(temp)
                            q.append(temp)
            relation += 1
        return relation
                
beginWord = "hot"
endWord = "dog"
wordList = ['hot', 'dog']
test = Solution()
print(test.ladderLength(beginWord, endWord, wordList))
