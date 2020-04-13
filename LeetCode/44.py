"""
$44. Wildcard Matching
"""

class Solution:
    def isMatch(self, s, p):
        dps = [[-1] * (len(p)+1) for i in range(len(s)+1)]
        return True if self.isMatch2(s, p, dps) else False
    
    def isMatch2(self, s, p, dps):
        ls, lp = len(s), len(p)
        if dps[ls][lp] > -1:
            return dps[ls][lp]
        if s == p:
            dps[len(s)][len(p)] = 1
            return True
        if s == "":
            if p[0] == '*':
                dps[ls][lp] = self.isMatch2(s, p[1:], dps)
                return dps[ls][lp]
            else:
                dps[ls][lp] = 0
                return False
        if p == "":
            dps[ls][lp] = 0
            return dps[ls][lp]

        if s[0] == p[0]:
            dps[ls][lp] = self.isMatch2(s[1:], p[1:], dps)
            return dps[ls][lp]
        if s[0] != p[0] and p[0] != '*' and p[0] != "?":
            dps[ls][lp] = 0
            return dps[ls][lp]
        if p[0] == "?":
            dps[ls][lp] = self.isMatch2(s[1:], p[1:], dps)
            return dps[ls][lp]
        if p[0] == '*':
            dps[ls][lp] = self.isMatch2(s, p[1:], dps) or self.isMatch2(s[1:], p, dps) or self.isMatch2(s[1:], p[1:], dps)
            return dps[ls][lp]

