from typing import List

"""k = 5, operations = [0,0,0]"""

# TODO: NEED TO OPTIMIZE
def kthCharacterBrute(k: int, operations: List[int]) -> str:
    
    s = "a"
    for opr in operations:
        if opr == 0:
            s += s
        if opr == 1:
            ns = ""
            for char in s:
                ns += chr(ord(char)+1)
            s += ns
    print(s)
    if len(s) >=k:
        return s[k-1]
# print(kthCharacterBrute(5, [0,0,0]))
print(kthCharacterBrute(10, [0,1,0,1]))
