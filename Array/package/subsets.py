from typing import List


def subset(nums: List[int]) -> List[List[int]]:
    res = []
    sol = []
    n = len(nums)

    def backtracking(count):
        if n == count:
            return res.append(sol[:])
        
        backtracking(count+1)
        print("Fist")
        sol.append(nums[count])
        print(nums[count])
        backtracking(count+1)
        sol.pop()
        print("2nd")

    backtracking(0)
    return res

print(subset([1,2,3]))