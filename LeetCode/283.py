"""
$283. Move Zeros
"""

class Solution:
    def moveZeroes(self, nums):
        if len(nums) < 2:
            return nums
        
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

        return nums

sol = Solution()
nums = [0, 1, 0, 3, 12]
print(sol.moveZeros(nums))