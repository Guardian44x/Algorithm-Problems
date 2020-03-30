"""
$377. Combination Sum IV

Dynamic Program
"""

class Solution:
    def combinationSum4(self, nums, target):
        if not nums:
            return 0
        dps = [-1] * (target + 1)
        dps[0] =  1
        nums = sorted(nums)
        return self.pickNum(dps, nums, target)
        
    def pickNum(self, dps, nums, target):
        if dps[target] >= 0:
            return dps[target]
        if target == 0:
            return 1
        if target < nums[0]:
            dps[target] = 0
            return 0
        
        counts = 0
        for c in nums:
            if c > target:
                continue
            val = self.pickNum(dps, nums, target-c)
            counts += val
        dps[target] = counts
        return counts


sol = Solution()
nums = [4, 2, 1]
target = 32
print(sol.combinationSum4(nums, target))