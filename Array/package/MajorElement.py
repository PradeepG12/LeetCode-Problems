from collections import Counter
from typing import List

"""
Input: nums = [3,2,3]
Output: [3]
"""

def majorityElement(nums: List[int]) -> List[int]:
    n = len(nums)
    avg = (n/3)
    output = []
    counter = Counter(nums)
    for ele, val in counter.items():
        if val > avg:
            output.append(ele)
    return output
