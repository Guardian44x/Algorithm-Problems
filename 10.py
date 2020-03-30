"""
$10. Regular Expression Matching
"""

class Solution:
    def isMatch(self, s, p):
        ls = len(s)
        lp = len(p)
        dps = [[-1] * (lp+1) for i in range(ls+1)] 
        return self.isMatch2(s, p, dps)

    def isMatch2(self, s, p, dps):
        ls = len(s)
        lp = len(p)
        if dps[ls][lp] > -1:
            return dps[ls][lp] == 1
        if s == p:
            dps[ls][lp] = 1
            return True
        if s == "":
            if len(p) > 1 and p[0] != '*' and p[1] == '*':
                res = self.isMatch2(s, p[2:], dps)
                dps[ls][lp] = int(res)
                return res
            dps[ls][lp] = 0
            return False
        if not p:
            dps[ls][lp] = 0
            return False
        
        if len(p) < 2 or p[1] != '*':
            res = (p[0] == '.' or s[0] == p[0]) and self.isMatch2(s[1:], p[1:], dps)
            dps[ls][lp] = int(res)
            return res
        else:
            if s[0] != p[0] and p[0] != ".":
                res = self.isMatch2(s, p[2:], dps)
            else:        
                res = self.isMatch2(s[1:], p, dps) or \
                    self.isMatch2(s, p[2:], dps) or \
                    self.isMatch2(s[1:], p[2:], dps)
            dps[ls][lp] = int(res)
            return res

sol = Solution()
s = "aaaaaaaaaaaaab"
p = "a*a*a*a*a*a*a*b*"
print(sol.isMatch(s, p))