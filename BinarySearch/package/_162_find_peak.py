from typing import List


n1, n2 = [1,2,3,1],[1,2,1,3,5,6,4]

def findPeakElement(nums: List[int]) -> int:
    n = len(nums)-1
    low = 0
    high = n
    while(low<high):
        mid = (low+high) //2
        if nums[mid] < nums[mid+1]:
            low = mid+1
        else:
            high = mid
    return low
print(n1[findPeakElement(n1)])
print(n2[findPeakElement(n2)])