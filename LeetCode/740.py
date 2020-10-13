"""
$740. Delete and Earn
"""

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        scores = {}
        for c in nums:
            if c in scores:
                scores[c] += c
            else:
                scores[c] = c
        scores_list = []
        for key in scores:
            scores_list.append([key, scores[key]])
        scores_list.sort()
        dps = [0] * (len(scores_list) + 1)
        dps[1] = scores_list[0][1]
        for i in range(1, len(scores_list)):
            if scores_list[i][0] > scores_list[i-1][0] + 1:
                dps[i+1] = dps[i] + scores_list[i][1]
            else:
                dps[i+1] = max(dps[i-1]+scores_list[i][1], dps[i])
        return dps[-1]