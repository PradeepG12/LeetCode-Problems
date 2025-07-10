"""Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2"""
from typing import List


data = [
    [[1,1,1,0,0,0,1,1,1,1,0], 2],
    [[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3]
]

def longestOnes(nums: List[int], k: int) -> int:
    n = len(nums)
    maxi = 0
    zeros_cnt = 0
    left, right = 0, 0
    while right < n:
        if nums[right] == 0:
            zeros_cnt += 1
            while zeros_cnt>k:
                if nums[left] == 0:
                    zeros_cnt-=1
                left+=1
        right += 1
        maxi = max(maxi, right-left)
    return maxi
print([longestOnes(ip1, ip2) for ip1, ip2 in data])