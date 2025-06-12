from typing import List

def maxAdjacentDistance(nums: List[int]) -> int:
    n = len(nums)
    max_diff = 0
    for i in range(n):
        diff = abs(nums[i] - nums[(i+1) % n])
        max_diff = max(diff, max_diff)
    return max_diff