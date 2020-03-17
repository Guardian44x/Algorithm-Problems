"""
$5303. Decrypt String from Alphabet to Integer Mapping
"""

class Solution:
    def freqAlphabets(self, s):
        prev = []
        res = ""
        for c in s:
            if c != '#':
                prev.append(c)
                if len(prev) > 2:
                   a = prev.pop(0)
                   res += chr(int(a)+96)
            else:
                a = prev[0] + prev[1]
                res += chr(int(a) + 96)
                prev.clear()
        for c in prev:
            res += chr(int(c) + 96)
        return res

sol = Solution()
s = "10#11#12"
res =  sol.freqAlphabets(s)
print(res)