from typing import List

"""
Input: words = ["e","a","b"], groups = [0,0,1]
Output: ["e","b"]
"""

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        generated_str = []
        n = len(groups)
        for i in range(len(words)):
            if groups[i] != last:
                result.append(words[i])
                last = groups[i]
        return result
        print(generated_str)
soln = Solution()
res = soln.getLongestSubsequence(["e","a","b"], [0,1,0,1])
print(res)