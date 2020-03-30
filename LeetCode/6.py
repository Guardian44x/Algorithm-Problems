"""
$6. ZigZag Conversion
"""

class Solution:
    def convert(self, s, numRows):
        l = len(s)
        c = 2 * numRows - 2
        idxs = [[] for i in range(numRows)]
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                idxs[i] = [i]
            else:
                idxs[i] = [i, c-i]

        res = ""
        for i in range(numRows):
            sub_i = ""
            k = 0
            while k * c < l:
                for j in idxs[i]:
                    if k*c+j < l:
                        sub_i += s[k*c+j]
                k += 1
            res += sub_i
        return res

sol = Solution()
s = "PAYPALISHIRING"
numRows = 4
print(sol.convert(s, numRows))