from typing import List

def triangularSum(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    tempArray = nums.copy()
    for i in range(1,n):
        newArray = [0]*(n-i)
        for j in range(n-i):
            newArray[j] = (tempArray[j] + tempArray[j+1])%10
            print(newArray)
        tempArray = newArray
    return tempArray[0]

def triangularSumBetter(nums: List[int]) -> int:
    n = len(nums)
    while n>1:
        nums = [(nums[i] + nums[i+1])%10 for i in range(n-1)]
        n-=1
    return nums[0]

print(triangularSumBetter([1,2,3,4,5]))