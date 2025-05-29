from typing import List
from collections import defaultdict

class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     count = 0
    #     n = len(nums)
    #     for i in range(n):
    #         sum = 0
    #         for j in range(i,n):
    #             sum += nums[j]
    #             if sum == k:
    #                 count += 1
    #     return count

    def subarraySum(self, nums: List[int], k: int) -> int:
        
        mpp = defaultdict(int)
        count, prefix_sum = 0, 0 
        mpp[0] = 1

        for i in range(len(nums)):
            prefix_sum += nums[i]
            reminder = prefix_sum - k
            count += mpp[reminder]
            mpp[prefix_sum] += 1
        return count