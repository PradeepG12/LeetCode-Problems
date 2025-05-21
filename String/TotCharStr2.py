from typing import List

"""
Input: 
s = "abcyy", 
t = 2, 
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
"""
"""
Input: 
s = "azbk", 
t = 1, 
nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
Output: 8
"""
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MODULO = 10 ** 9 + 7
        length = 0
        for i in range(t):
            count = 0
            for char in s:
                num = (ord(char) - ord('a'))+ i
                count += nums[num]
            length = count
        print("end")
        return length % MODULO
    
soln = Solution()
ans = soln.lengthAfterTransformations("azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
print(ans)