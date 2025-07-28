data = [[3,1],[2,2,2], [3,2,1,5]]

def countMaxOrSubsets(nums: list[int]) -> int:
    n = len(nums)
    maxi = 0
    for num in nums:
        maxi |= num
    tot = 0
    def backtrack(index, value):
        nonlocal tot
        if index == n:
            if value == maxi:
                tot+=1
            return
        backtrack(index+1, value | nums[index])
        backtrack(index+1, value)
    backtrack(0,0)
    return tot
print(countMaxOrSubsets(data[-1]))