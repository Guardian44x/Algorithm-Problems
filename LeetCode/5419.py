"""
$ Max Dot Product of Two Subsequences
"""

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        M = len(nums1)
        N = len(nums2)
        vals = [[-1] * N for i in range(M)]
        
        def Signal(nums):
            min_val = min(nums)
            max_val = max(nums)
            if min_val * max_val <= 0:
                return 0
            if min_val > 0:
                return 1
            if max_val < 0:
                return -1
        a = Signal(nums1)
        b = Signal(nums2)
        if a * b < 0:
            return max(min(nums1)*max(nums2), max(nums1)*min(nums2))
                
        
        def SearchProduct(i, j):
            if i >= M or j >= N:
                return 0
            if vals[i][j] > -1:
                return vals[i][j]
            val = max(SearchProduct(i+1, j), SearchProduct(i, j+1), SearchProduct(i+1, j+1) + max(0, nums1[i]*nums2[j]))
            vals[i][j] = val
            return vals[i][j]
        
        SearchProduct(0, 0)
        res = max([max(c) for c in vals])
        return res
