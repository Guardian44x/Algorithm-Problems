"""
$154. Find Minimum in Rotated Sorted Array II
"""

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        if nums[right] > nums[left]:
            return nums[left]
        while left < right - 1:
            if nums[left] == nums[right]:
                if nums[left+1] >= nums[left]:
                    left += 1
                elif nums[right-1] <= nums[right]:
                    right -= 1
                continue
            point = (left + right) // 2
            if nums[point] >= nums[left]:
                left = point
            elif nums[point] <= nums[right]:
                right = point
        
        return min(nums[left], nums[right])

sol = Solution()
nums = [2, 2, 2, 0, 1, 2]
print(sol.findMin(nums))