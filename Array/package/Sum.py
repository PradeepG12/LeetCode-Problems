from typing import List

#[-4, -1, -1, 0, 1, 2]
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    op = []
    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        j,k = i+1, n-1
        while j<k:
            tot = nums[i]+nums[j]+nums[k]
            if tot == 0:
                op.append([nums[i],nums[j],nums[k]])
                j += 1
                k -= 1
                while j<k and nums[j] == nums[j-1]:
                    j+=1
                while j<k and nums[k] == nums[k+1]:
                    k-=1
            elif tot < 0:
                j += 1
            else:
                k -= 1
    return op
    # res = set()
    # for i in range(n):
    #     temp_set = set()
    #     for j in range(i+1, n):
    #         k = -(nums[i]+nums[j])
    #         if k in temp_set:
    #             res.add(tuple(sorted([nums[i],nums[j],k])))
    #         temp_set.add(nums[j])
    # return [list(t) for t in res]

"""nums = [2,7,11,15], target = 9"""

# brute-force
def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i]+nums[j] == target:
                return [i, j]

# better
def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    mpp = {}
    for i in range(n):
        res = target - nums[i]
        if res in mpp:
            return [mpp[res], i]
        mpp[nums[i]] = i
