from typing import List

def findTargetSumWays(nums: List[int], target: int) -> int:
    n = len(nums)
    if (sum(nums) + target) % 2 != 0:
        return 0
    target_sum = (sum(nums) + target) // 2
    # dp = [[0]*(target_sum+1) for _ in range(n+1)]
    # dp[0][0] = 1
    # for i in range(1, n+1):
    #     for j in range(target_sum+1):
    #         current_num = nums[i-1]
    #         dp[i][j] = dp[i-1][j] + (dp[i-1][j-current_num] if j >= current_num else 0)
    # return dp[-1][-1]
    prev = [0]*(target_sum+1)
    prev[0] = 1
    for num in nums:
        for j in range(target_sum, num-1, -1):
            prev[j] += prev[j-num]
    return prev[-1]

d = findTargetSumWays([1,1,1,1,1],3)
print(d)