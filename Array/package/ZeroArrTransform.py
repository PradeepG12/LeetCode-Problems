"""
Input: nums = [1,0,1], queries = [[0,2]]
Output: true

Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]
Output: false
"""
from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff_array = [0] * (n + 1)
        for i, j in queries:
            diff_array[i] += 1
            diff_array[j+1] -= 1
        print("diff array : ", diff_array)
        current = 0
        for i in range(n):
            current += diff_array[i]
            if nums[i] > current:
                print(nums)
            nums[i] -= current
        print(nums)


soln = Solution()
res=soln.isZeroArray( nums = [4,3,2,1], queries = [[1,3],[0,2]])
print(res)