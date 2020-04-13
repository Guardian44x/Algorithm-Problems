"""
$31. Next Permutation
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                j = i + 1
                while j < len(nums):
                    if nums[j] <= nums[i]:
                        break
                    j += 1
                j -= 1
                print(i,j)
                nums[i], nums[j] = nums[j], nums[i]
                nums[i+1:] = nums[-1:i:-1]
                break
        else:
            nums[:] = nums[::-1] 