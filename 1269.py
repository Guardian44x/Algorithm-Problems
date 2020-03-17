"""
$1269. Number of Ways to Stay in the Same Place After Some Steps
"""

class Solution:
    def numWays(self, steps, arrlen):
        l = min(steps, arrlen)
        dp = [0] * l
        dp[0] = 1
        for i in range(steps):
            cur = [0] * l
            cur[0] = dp[0] + dp[1]
            cur[-1] = dp[-1] + dp[-2]
            for i in range(1, l-1):
                cur[i] = dp[i-1] + dp[i] + dp[i+1]
            dp = cur
        return dp[0] % (10e8 + 7)