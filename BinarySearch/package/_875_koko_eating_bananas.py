from typing import List
from math import ceil

data = [
    [[30,11,23,4,20],5],
    [[30,11,23,4,20],6],
    [[3,6,7,11],8]
]
def minEatingSpeedBrute(piles: List[int], h: int) -> int:
    k = 1
    output = 0
    while output < h:
        for pile in piles:
            output += ceil(pile/k)
        print(output)
        if output>h:
            output = 0
            k+=1
    print(k)

def minEatingSpeedBetter(piles, h):
    maxi = max(piles)
    for i in range(1, maxi+1):
        speed = 0
        for pile in piles:
            speed += ceil(pile/i)
        if speed <= h:
            return i


def minEatingSpeed(piles, h):
    low, high = 1, max(piles)
    while low<=high:
        mid = (low+high) // 2
        speed = sum([ceil(pile/mid) for pile in piles])
        # if speed == h:
        #     return mid
        if speed > h:
            low = mid+1
        else:
            high = mid-1
    return low
print(minEatingSpeed([312884470],312884469))
# print([minEatingSpeedBetter(piles, h) for piles, h in data])


