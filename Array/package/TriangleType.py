class Solution:
    def Triangle(self, nums):
        if not self.is_triangle(nums):
            return "None"
        if self.isEqualateral(nums):
            return "equalateral"
        if self.isIsosceles(nums):
            return "isosceles"
        else:
            return "scalene"
        
    def is_triangle(self, nums):
        return (
            nums[0]+nums[1] > nums[2] and nums[1]+nums[2] > nums[0] and nums[0]+nums[2] > nums[0]
        )
    
    def isEqualateral(self, nums):
        return (nums[0] == nums[1] == nums[2])
    
    def isIsosceles(self, nums):
        return nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]