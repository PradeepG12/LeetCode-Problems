from collections import Counter

def maxDifference(s: str) -> int:
    
    res = Counter(s)
    max_odd = 0
    max_even = float('inf')
    for _, val in res.items():
        if val % 2 != 0:
            max_odd = max(max_odd, val)
        if val % 2 == 0:
            max_even = min(max_even, val)
    return max_odd-max_even