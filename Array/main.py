"""from package import Solution

print(soln.Triangle([3,3,3]))
soln = Solution()
res1 = soln.subarraySum(nums = [1,1,1], k = 2)
res2 = soln.subarraySum(nums = [1,2,3], k = 3)
print(res1)
print(res2)
"""
from package2D import spiralOrder

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))