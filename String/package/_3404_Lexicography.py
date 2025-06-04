data = "dbca"

def answerString(word: str, numFriends: int) -> str:
    if numFriends == 1:
        return word
    length = len(word) - numFriends + 1
    res = ''
    for i in range(len(word)):
        temp = word[i:i+length]
        if temp > res:
            res = temp
    return res