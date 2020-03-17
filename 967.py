"""
$967. Numbers With Same Consecutive Differences
"""

class Solution:
    def numsSameConsecDiff(self, N, K):
        if N == 1:
            return list(range(10))
        
        res = list(range(1, 10))
        for i in range(2, N+1):
            news = []
            for c in res:
                r = c % 10
                if r + K < 10:
                    news.append(c*10+(r+K))
                if r - K >= 0 and K != 0:
                    news.append(c*10+(r-K))
            res = news
        return res


sol = Solution()
N = 2
K = 1
print(sol.numsSameConsecDiff(N, K))