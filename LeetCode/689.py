"""
$689. Maximum Sum of 3 Non-Overlapping Subarrays
"""
import numpy as np

class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        res = [[[0, []]] * len(nums) for i in range(3)]
        max_res = [[[0, []]] * len(nums) for i in range(3)]

        for i in range(k, len(nums)+1):
            if res[0][i-2][0] == 0:
                res[0][i-1] = [sum(nums[i-k:i]), [i]]
            else:
                res[0][i-1] = [res[0][i-2][0] + nums[i-1] - nums[i-k-1], [i]]
        max_sum = 0
        for i in range(k, len(nums)+1):
            if res[0][i-1][0] > max_sum:
                max_sum, max_idx = res[0][i-1]
                max_res[0][i-1] = res[0][i-1]
            else:
                max_res[0][i-1] = [max_sum, max_idx]

        for i in range(2*k, len(nums)+1):
            max_sum, max_idx = max_res[0][i-k-1]
            tmp_sum = res[0][i-1][0]
            res[1][i-1] = [tmp_sum + max_sum, max_idx+[i]]
        max_sum = 0
        for i in range(2*k, len(nums)+1):
            if res[1][i-1][0] > max_sum:
                max_sum, max_idx = res[1][i-1]
                max_res[1][i-1] = res[1][i-1]
            else:
                max_res[1][i-1] = [max_sum, max_idx]

        final_res = 0
        for i in range(3*k, len(nums)+1):
            max_sum, max_idx = max_res[1][i-k-1]
            tmp_sum = res[0][i-1][0]
            res[2][i-1] = [tmp_sum+max_sum, max_idx+[i]]
            if tmp_sum + max_sum > final_res:
                final_res, idx_res = res[2][i-1]
        res0 = [c-k for c in idx_res]
        return res0

sol = Solution()
nums = [17,9,3,2,7,10,20,1,13,4,5,16,4,1,17,6,4,19,8,3]
k = 4
print(sol.maxSumOfThreeSubarrays(nums, k))