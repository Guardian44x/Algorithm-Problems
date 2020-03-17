"""
$16. 3Sum Closest
"""

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        sumVal = float("inf")
        diff = float("inf")
        for k in range(len(nums)-2):
            i = k + 1
            j = len(nums) - 1
            
            while i < j:
                total = nums[k] + nums[i] + nums[j]
                if abs(total - target) < diff:
                    result = [nums[k], nums[i], nums[j]]
                    diff = abs(total - target)
                if total < target:
                    i += 1
                else:
                    j -= 1
        return sum(result)


sol = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(sol.threeSumClosest(nums, target))