"""
Input: nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]
Output: 6
"""
from typing import List

def MaxSumNode(nums: List[int], k: int, edges: List[List[int]]) -> int:
    # edges.sort(key=lambda x : x[1])
    n = len(nums)
    value = edges[n-2]
    if nums[value[0]] < k:
        nums[value[0]] ^= k
    if nums[value[1]] < k :
        nums[value[1]] ^= k
    return sum(nums)


