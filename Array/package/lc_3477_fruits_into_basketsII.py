from typing import List
data = [
    {"fruits": [4,2,5], "baskets": [3,5,4]},
    {"fruits": [3,6,1], "baskets": [6,4,7]},
]
def numOfUnplacedFruits(fruits: List[int], baskets: List[int]) -> int:
    n = len(fruits)
    marker = [-1] * n
    for i in range(n):
        fruit = fruits[i]
        for j in range(n):
            if marker[j] == -1:
                if fruit <= baskets[j]:
                    marker[j] = 1
                    break
    return marker.count(-1)

def numOfUnplacedFruits(fruits: List[int], baskets: List[int]) -> int:
    for fruit in fruits:
        for idx, basket in enumerate(baskets):
            if fruit <= basket:
                baskets.pop(idx)
    return len(baskets)

print(numOfUnplacedFruits(data[0]["fruits"], data[0]["baskets"]))