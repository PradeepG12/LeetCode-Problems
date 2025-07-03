def kthCharacter(k: int) -> str:
    s = "a"
    while len(s)< k:
        op = ""
        for char in s:
            op += chr(ord(char)+1)
        s += op
    return s[k-1]
