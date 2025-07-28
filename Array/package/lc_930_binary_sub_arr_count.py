from typing import List

data = [[[0,0,0,0,0],0],[[1,0,1,0,1],2]]

def numSubarraysWithSumBrute(nums: List[int], goal: int) -> int:
    n = len(nums)
    count = 0
    for i in range(n):
        val = 0
        for j in range(i, n):
            val += nums[j]
            if val == goal:
                count += 1
            elif val > goal:
                break
    return count

# sliding Window
def numSubarrayWithSum(nums, goal):
    def helper(nums, goal):
        if goal < 0:
            return 0
        n = len(nums)
        i,j = 0,0
        count = 0
        val = 0
        while (j or i) < n:
            val += nums[j]
            j+=1
            while val > goal:
                val -= nums[i]
                i+=1
            count += j-i + 1
        return count
    return helper(nums,goal) - helper(nums, goal-1)

print(numSubarrayWithSum([1,0,1,0,1],2))