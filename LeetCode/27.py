"""
$27. Remove Element
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) < 1:
            return len(nums)
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        return l