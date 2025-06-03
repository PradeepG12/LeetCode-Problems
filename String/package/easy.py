"""
(1+(2*3)+((8)/4))+1
"""

def maxDepth(s: str) -> int:
    max_count = 0
    count = 0
    for char in s:
        if char == '(':
            count +=1
            max_count = max(count, max_count)
        if char == ')':
            count-=1
    return max_count