from typing import List


""""
nums = [0,0,1,1,1,2,2,3,3,4]
0,0,1,1,1,2,2,3,3,4
i,j
i, ,j
0,0,1,1,1,2,2,3,3,4
 ,i,j
0,1,0,1,1,2,2,3,3,4
 ,i, ,j
 ,i, , ,j
 ,i, , , ,j
0,1,0,1,1,2,2,3,3,4
 , ,i, , ,j
0,1,2,1,1,0,2,3,3,4
 , ,i, , , ,j
 , ,i, , , , ,j
0,1,2,1,1,0,2,3,3,4
 , , ,i, , , ,j
0,1,2,3,1,0,2,1,3,4
 , , ,i, , , , , ,j
"""
def removeDuplicates(nums: List[int]) -> int:
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i]=nums[j]
            nums[j]=nums[i] # not need
    print(nums)
    return i+1
