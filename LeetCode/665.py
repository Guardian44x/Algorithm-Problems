"""
$665. Non-decreasing Array
"""

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
                if count>1 or ((i-1>=0 and nums[i-1]>nums[i+1]) and (i+2<len(nums) and nums[i+2]<nums[i])):
                    return False
        return True