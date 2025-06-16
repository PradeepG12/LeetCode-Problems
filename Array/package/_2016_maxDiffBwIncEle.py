from typing import List


def maximumDifference(nums: List[int]) -> int:
    n = len(nums)
    mini = nums[0]
    maxi = -1
    for i in range(1, n):
        if nums[i] > mini:
            maxi = max(maxi, nums[i]-nums[i-1])
        else:
            mini = nums[i]
    return maxi
