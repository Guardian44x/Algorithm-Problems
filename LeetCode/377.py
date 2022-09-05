#1 Note that different sequences are counted as same combinations.
class Solution:
    def combinationSum4(self, nums, target):
        nums.sort()
        def combinationSum(max_idx, target):
            if max_idx == 0:
                return 1 if target % nums[0] == 0 else 0
            count = 0
            while target >= 0:
                count += combinationSum(max_idx-1, target)
                target = target - nums[max_idx]
            return count
        
        res = combinationSum(len(nums)-1, target)
        return res
    
Sol = Solution()
nums = [1, 2, 3]
target = 4
res = Sol.combinationSum4(nums, target)
print(res)


#2 Note that different sequences are counted as different combinations.
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