from collections import defaultdict
from typing import List


data = [[1,2,1], [0,1,2,2], [1,2,3,2,2], [3,3,3,1,2,1,1,2,3,3,4]]
def totalFruit(fruits: List[int]) -> int:
    count = defaultdict(int)
    maxi = left = 0
    for right in range(len(fruits)):
        count[fruits[right]] += 1
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1
        maxi = max(maxi, right-left+1)
    return maxi
print([totalFruit(d) for d in data])
