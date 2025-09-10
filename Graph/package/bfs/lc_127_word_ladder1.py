from typing import List
from collections import deque
import string

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList: return 0
    queue = deque([(beginWord, 1)])
    wordList = set(wordList)
    while queue:
        word, level = queue.popleft()
        for idx, char in enumerate(word):
            for alphabet in string.ascii_lowercase:
                new_word = word[:idx]+ alphabet + word[idx+1:]
                if new_word == endWord: return level+1
                elif new_word in wordList:
                    queue.append((new_word, level+1))
                    wordList.remove(new_word)
    return 0