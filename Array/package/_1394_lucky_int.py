from collections import Counter
from typing import List

def findLucky(arr: List[int]) -> int:
    count = Counter(arr)
    res = -1
    for num in arr:
        if num in count and count[num] is num:
            res = max(res,num)
    return res