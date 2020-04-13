"""
$41. First Missing Positive
"""

class Solution:
    def firstMissingPositive(self, nums):
        idx = 0
        while idx < len(nums):
            if nums[idx] <= 0:
                idx += 1
            elif nums[idx] > len(nums):
                idx += 1
            elif nums[idx] == idx + 1:
                idx += 1
            elif nums[nums[idx]-1] == nums[idx]:
                idx += 1
            else:
                a, b = idx, nums[idx] - 1
                nums[a], nums[b] = nums[b], nums[a]
            
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i+1
        return len(nums) + 1

sol = Solution()
nums = [1, 1]
print(sol.firstMissingPositive(nums))