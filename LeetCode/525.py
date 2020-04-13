"""
$525. Contiguous Array
"""


class Solution(object):
    def findMaxLength(self, nums):

        max_contiguous = 0
        accumulate = 0
		
        first_accumulate_idx = [None]*(2*len(nums)+1)
		
        first_accumulate_idx[0] = -1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                accumulate -= 1
            else:
                accumulate += 1
                
            if first_accumulate_idx[accumulate] is None:
                first_accumulate_idx[accumulate] = i
            else:
                contiguous = i - first_accumulate_idx[accumulate]
                if max_contiguous < contiguous:
                    max_contiguous = contiguous
                    
        return max_contiguous