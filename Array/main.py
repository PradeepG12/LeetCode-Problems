"""from package import Solution

print(soln.Triangle([3,3,3]))
soln = Solution()
res1 = soln.subarraySum(nums = [1,1,1], k = 2)
res2 = soln.subarraySum(nums = [1,2,3], k = 3)
print(res1)
print(res2)
"""
from package2D import spiralOrder, pascal_triangle
from package import (
    majorityElement, 
    threeSum, 
    maxAdjacentDistance,
    twoSum,
    removeDuplicates,
    findLucky,
    characterReplacement, longestOnes
)

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(spiralOrder(matrix))

# res1 = majorityElement([3,2,3])
# print(res1)
# res2 = majorityElement([1])
# print(res2)
# res3 = majorityElement([1,2])
# print(res3)

# res=threeSum([-1,0,1,2,-1,-4])
# print(res)


# print(maxAdjacentDistance([1,2,4]))
# print(maxAdjacentDistance([3,2,-5,-3]))
# print(maxAdjacentDistance([2,1,0]))

# data = [[7,1,5,4],[9,4,3,2],[1,5,2,10]]
# print([maximumDifference(ans) for ans in data])

# print(twoSum(nums = [2,7,11,15], target = 9))
# print(twoSum(nums = [3,2,4], target = 6))
# print(twoSum(nums = [3,3], target = 6))

# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# print(removeDuplicates([1,1,2]))

# data = [[2,2,3,4],[1,2,2,3,3,3]]
# print([findLucky(d) for d in data])

# data = [[[1,1,1,0,0,0,1,1,1,1,0], 2],[[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3]]
# print([longestOnes(ip1, ip2) for ip1, ip2 in data])


# data = [
#     ["ABAB",2 ],
#     ["AABABBA",1],
#     ["KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4]
# ]
# print([characterReplacement(d1, d2) for d1, d2 in data])

print(pascal_triangle(4))
