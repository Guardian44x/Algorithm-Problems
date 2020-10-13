"""
$1144. Decrease Elements To Make Array Zigzag
"""

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        ans1 = 0
        for i in range(1, len(nums), 2):
            val = min(nums[i-1], nums[i+1] if i+1 < len(nums) else float("inf"))
            ans1 += max(nums[i]-val+1, 0)
        ans2 = 0
        for i in range(0, len(nums), 2):
            val = min(nums[i-1] if i-1 > -1 else float("inf"), \
                    nums[i+1] if i+1 < len(nums) else float("inf"))
            ans2 += max(nums[i]-val+1, 0)
        return min(ans1, ans2)