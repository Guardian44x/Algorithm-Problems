"""
$1547. Minimum Cost to Cut a Stick
"""

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        l = len(cuts)
        dps = [[0] * l for _ in range(l)]
        for i in range(l-2):
            dps[i][i+2] = cuts[i+2] - cuts[i]
        for k in range(3, l):
            for i in range(l - k):
                val = float("inf")
                for t in range(1, k):
                    val = min(val, dps[i][i+t] + dps[i+t][i+k])
                dps[i][i+k] = val + cuts[i+k] - cuts[i]
        return dps[0][l-1]    