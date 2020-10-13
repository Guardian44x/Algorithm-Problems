"""
$877. Stone Game
"""

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l = len(piles)
        dps = [[0] * l for i in range(l)]
        tag = (l % 2) * 2 - 1
        for k in range(l):
            for i in range(l-k):
                if k == 0:
                    dps[i][i+k] = tag * piles[i]
                else:
                    if (k + 1) % 2 == l % 2:
                        dps[i][i+k] = max(dps[i][i+k-1] + piles[i+k], dps[i+1][i+k] + piles[i])
                    else:
                        dps[i][i+k] = min(dps[i][i+k-1] - piles[i+k], dps[i+1][i+k] - piles[i])
        if dps[0][l-1] > 0:
            return True
        else:
            return False