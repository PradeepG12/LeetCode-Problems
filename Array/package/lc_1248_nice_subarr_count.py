from collections import defaultdict
from typing import List

data = [
    {"nums": [1,1,2,1,1], "k": 3},
    {"nums": [2,4,6], "k": 1},
    {"nums": [2,2,2,1,2,2,1,2,2,2],"k": 2}
]
def numberOfSubarraysBrute(nums: List[int], k: int) -> int:
    n = len(nums)
    tot = 0
    for i in range(n):
        max_1 = 0
        for j in range(i, n):
            if nums[j] % 2 != 0:
                max_1 += 1
            if max_1 == k:
                tot += 1
    return tot

# def numberOfSubarraysBrute(nums: List[int], k: int) -> int: pass
# print(numberOfSubarraysBrute(data[0]["nums"], data[0]["k"]))

def numberOfSubarrays(nums, k):
    prefix_sum = defaultdict(int)
    odd_count = 0
    prefix_sum[0] = 1
    tot = 0
    for num in nums:
        if num % 2 != 0:
            odd_count += 1
        tot += prefix_sum[odd_count-k]
        prefix_sum[odd_count] += 1
    return tot
print([numberOfSubarrays(d["nums"], d["k"]) for d in data ])