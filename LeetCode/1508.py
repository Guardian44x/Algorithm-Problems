"""
$1508. Range Sum of Sorted Subarray Sums
"""

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        i,j,amount = 0,0,0
        total_sum = []
        
        while i < len(nums):
            if j == len(nums) - 1:
                amount += nums[j]
                total_sum.append(amount)
                i += 1
                j = i
                amount = 0
            else:
                if i == j:
                    amount = nums[j]
                    total_sum.append(amount)
                    j += 1
                else:
                    amount += nums[j]
                    total_sum.append(amount)
                    j += 1
        
        total_sum.sort()
        return sum(total_sum[left-1:right])%(10**9 + 7)