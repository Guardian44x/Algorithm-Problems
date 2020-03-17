'''
$521. Longest Uncommon Subsequence I
'''

class Solution:
    def findLUSlength(self, a, b):
        a_length = len(a)
        b_length = len(b)
        if a_length != b_length:
            return max(a_length, b_length)
        elif a == b:
            return -1
        else:
            return a_length

sol = Solution()
a = "aba"
b = "cdc"
print(sol.findLUSlength(a, b))