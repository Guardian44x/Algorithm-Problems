
"""
$5424. Maximum Product of Two Elements in an Array
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = 0, 0
        for c in nums:
            if c >= b:
                a, b = b, c
            elif c >= a and c < b:
                a = c
            else:
                continue
        return (a-1) * (b-1)