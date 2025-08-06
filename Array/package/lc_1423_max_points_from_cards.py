from typing import List

data = [
    {"cp": [1,2,3,4,5,6,1],"k":3},
    {"cp": [2,2,2],"k":2},
    {"cp": [9,7,7,9,7,7,9],"k":7},
]

def maxScore(cardpoints: List[int], k: int) -> int:
    n = len(cardpoints)
    if n == k:
        return sum(cardpoints)
    prefix_sum = maxi = sum(cardpoints[:k])
    front = k-1
    back = 0
    while back<k:
        prefix_sum -= cardpoints[front]
        front -= 1
        prefix_sum += cardpoints[n-1-back]
        back += 1
        maxi = max(maxi, prefix_sum)
    return maxi

def maxScoreBetter(cardpoints: List[int], k: int) -> int:
    """[1,2,3,4,5,6,1]"""
    n = len(cardpoints)
    if n == k:
        return sum(cardpoints)
    prefix_sum = maxi = sum(cardpoints[:k])
    for i in range(k):
        prefix_sum = prefix_sum - cardpoints[k-1-i] + cardpoints[n-1-i]
        maxi = max(maxi, prefix_sum)
    return maxi

print([maxScore(d["cp"], d["k"]) for d in data])