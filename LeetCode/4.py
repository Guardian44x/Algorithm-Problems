"""
$4. Median of Two Sorted Arrays
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        a = self.findSmallKSortedArrays(nums1, nums2, (m+n)//2)
        print(a)
        b = self.findSmallKSortedArrays(nums1, nums2, (m+n-1)//2)
        print(b)
        return (a + b) / 2
    

    def findSmallKSortedArrays(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            return nums2[k]
        if n == 0:
            return nums1[k]

        if k == 0:
            return min(nums1[0], nums2[0])
        
        t = (k-1) // 2
        t1 = min(t, m-1)
        t2 = min(t, n-1)
        print(m, n, k, t1, t2)
        
        if nums1[t1] > nums2[t2]:
            return self.findSmallKSortedArrays(nums1, nums2[t2+1:], k-(t2+1))
        elif nums1[t1] < nums2[t2]:
            return self.findSmallKSortedArrays(nums1[t1+1:], nums2, k-(t1+1))
        else:
            if (t1 + 1 + t2 + 1)  >= k+1 and (t1+t2) < k:
                return nums1[t1]
            return self.findSmallKSortedArrays(nums1[t1+1:], nums2[t2+1:], k-(t1+1+t2+1))
        
sol = Solution()
nums1 = [1, 2]
nums2 = [1, 2]
print(sol.findMedianSortedArrays(nums1, nums2))
