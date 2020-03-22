"""
$898. Bitwise ORs of Subarrays.
"""

class Solution:
    def subarrayBitwiseORs(self, A):
        prev = A.copy()
        l = len(A)
        res = set(A)
        for i in range(1, l):
            new = []
            for j in range(len(prev)-1):
                new.append(prev[j] | A[j+i])
            prev = new
            res.update(set(prev))
        return len(set(res))

sol = Solution()
A = [1, 1, 2]
print(sol.subarrayBitwiseORs(A))