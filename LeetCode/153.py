"""
$153. Find Minimum in Rotated Sorted Array
"""

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        if nums[right] > nums[left]:
            return nums[left]
        while left < right-1:
            point = (left + right) // 2
            if nums[point] >= nums[left]:
                left = point
            elif nums[point] <= nums[right]:
                right = point
        
        return min(nums[left], nums[right])

sol = Solution()
nums = [4, 5, 6, 1, 2]
print(sol.findMin(nums))