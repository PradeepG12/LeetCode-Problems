from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def findMin(self) -> int:
        nums = self.nums
        for i in range(len(nums)-1, -1, -1):
            print(i, " fiv")
            if nums[i] < nums[i-1]:
                return nums[i]
        return 0
    
nums = [1,2,3,4,5]
soln = Solution(nums)
soln.findMin()
print(soln.findMin())    
