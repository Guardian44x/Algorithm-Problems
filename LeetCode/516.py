from pprint import pprint
class Solution:
    def longestPalindromeSubseq(self, s):
        l = len(s)
        dps = [[0] * len(s) for _ in range(l)]
        for i in range(l):
            dps[i][i] = 1
        for i in range(l-1):
            dps[i][i+1] = 2 if s[i] == s[i+1] else 1
        pprint(dps)
        for k in range(2, l):
            for i in range(l):
                if i+k >= l:
                    continue
                dps[i][i+k] = dps[i+1][i+k-1] + 2 if s[i] == s[i+k] else dps[i+1][i+k-1]
                dps[i][i+k] = max(dps[i][i+k], dps[i+1][i+k], dps[i][i+k-1])
                print(i, i+k, dps[i][i+k], dps[i+1][i+k-1], dps[i+1][i+k], dps[i][i+k-1])
            pprint(dps)
        return dps[0][l-1]


class Solution(object):

    def longestPalindromeSubseq(self, s1):
        """
        :type s: str
        :rtype: int
        """
        s2 = s1[::-1]
        n =len(s1)
        t = [[0 for i in range(n+1)]for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    t[i][j]=1 + t[i-1][j-1]
                else:
                    t[i][j]= max(t[i-1][j],t[i][j-1])
            pprint(t)
        return t[n][n]


sol = Solution()
s = "bbbab"
sol.longestPalindromeSubseq(s)