"""
$18. 4Sum
"""

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        if len(nums) < 4:
            return []
        if len(nums) == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return []

        res = []
        last = None
        for p4 in range(3, len(nums)):
            if nums[p4] + sum(nums[:3]) > target:
                break
            if sum(nums[p4:p4-4:-1]) < target:
                continue
            for p3 in range(2, p4):
                if nums[p4] + nums[p3] + sum(nums[:2]) > target:
                    break
                if nums[p4] + sum(nums[p3:p3-3:-1]) < target:
                    continue
                for p2 in range(1, p3):
                    if nums[p4] + nums[p3] + nums[p2] + nums[0] > target:
                        break
                    if nums[p4] + nums[p3] + sum(nums[p2:p2-2:-1]) < target:
                        continue
                    for p1 in range(0, p2):
                        if nums[p4] + nums[p3] + nums[p2] + nums[p1] > target:
                            break
                        val = nums[p4] + nums[p3] + nums[p2] + nums[p1]
                        if val == target:
                            tmp = [nums[p1], nums[p2], nums[p3], nums[p4]]
                            if tmp not in res:
                                res.append(tmp)
                        
        return res

sol = Solution()
nums = [-5,-4,-3,-2,-1,0,0,1,2,3,4,5]
target = 0
res = sol.fourSum(nums, target)
res2 = [[-5,-4,4,5],[-5,-3,3,5],[-5,-2,2,5],[-5,-2,3,4],[-5,-1,1,5],[-5,-1,2,4],[-5,0,0,5],[-5,0,1,4],[-5,0,2,3],[-4,-3,2,5],[-4,-3,3,4],[-4,-2,1,5],[-4,-2,2,4],[-4,-1,0,5],[-4,-1,1,4],[-4,-1,2,3],[-4,0,0,4],[-4,0,1,3],[-3,-2,0,5],[-3,-2,1,4],[-3,-2,2,3],[-3,-1,0,4],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
res2 = [sorted(t) for t in res2]
res.sort()
res2.sort()
print(res)
print(res2)