"""
$955. Delete Columns to Make Sorted II
"""

class Solution:
    def minDeletionSize(self, A):
        L = len(A)
        l = len(A[0])
        aug_set = list(range(L-1))  
        res = 0

        for i in range(l):
            flag = False
            tmp_set = []
            print(aug_set)
            for c in aug_set:
                if A[c][i] > A[c+1][i]:
                    flag = True
                    res += 1
                    break
                if A[c][i] ==  A[c+1][i]:
                    tmp_set.append(c)
            if not flag:
                aug_set = tmp_set
        return res
                
sol = Solution()
A = ["abx","agz","bgc","bfc"]
print(sol.minDeletionSize(A))