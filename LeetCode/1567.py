"""
$1567. Maximum Length of Subarray With Positive Product
"""

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        odd = -1
        even = -1
        product = 1
        max_len = 0
        for i, c in enumerate(nums):
            product *= c
            
            if product < 0:
                if odd > -1:
                    max_len = max(max_len, i-odd)
                else:
                    odd = i
            elif product > 0:
                max_len = max(max_len, i-even)
            else:
                odd, even, product = -1, i, 1
            # print(i, c, product, odd, even, max_len)
        return max_len