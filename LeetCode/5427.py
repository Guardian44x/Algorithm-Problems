
from scipy.special import comb, perm

class Solution:
    def getProbability(self, balls):
        K = len(balls)
        N = sum(balls)
        dps = [[[-1] * (N // 2) for j in range(K)] for i in range(N//2+1)]
        
        def func(n, k, t):
            if k >= K:
                return 1 if t == 0 and n == 0 else 0
            if dps[n][k][t] > -1:
                return dps[n][k][t]
            if k < t:
                dps[n][k][t] = 0
                return dps[n][k][t]
            prob = 0
            for c in range(min(grid[k], n, t)+1):
                prob += comb(grid[k], c) / 2 ** grid[k] * func(n-c, k+1, t-(c>=0), nt-c)
        
        func(N//2, 0, )