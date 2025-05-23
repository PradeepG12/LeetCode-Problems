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


"""
Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]

Output: 1
"""
def zeroArrayTransform2(nums: List[int], queries: List[List[int]]) -> int:
    queries_n = len(queries)
    nums_n = len(nums)

    diff_arr = [0] * (nums_n + 1)
    for i, j in queries:
        diff_arr[i] += 1
        diff_arr[j+1] -= 1

    count = 0
    for i in range(nums_n):
        count += diff_arr[i]
        if not nums[i] == 0:
            nums[i] -= count
        print(nums, "i ",i, "count ", count)
        if count < nums[i]:
            print(nums[i])
            # return False
    print(diff_arr)
soln = zeroArrayTransform2(nums = [2,0,2], queries = [[0,2],[0,2],[1,1]])