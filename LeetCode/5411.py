
"""
Cherry Pickup II
"""

class Solution:
    def cherryPickup(self, grid):
        r, c = len(grid), len(grid[0])
        dps = [[0] * (c+2) for i in range(c+2)]
        for k in range(r-1, -1, -1):
            news = [[0] * (c+2) for i in range(c+2)]
            for i in range(c):
                for j in range(c):
                    if i == j:
                        news[i+1][j+1] = max(dps[i+1][j], dps[i+1][j+1], dps[i+1][j+2], \
                                            dps[i][j], dps[i][j+1], dps[i][j+2], \
                                            dps[i+2][j], dps[i+2][j+1], dps[i+2][j+2]) + grid[k][i]
                    else:
                        news[i+1][j+1] = max(dps[i+1][j], dps[i+1][j+1], dps[i+1][j+2], \
                                            dps[i][j], dps[i][j+1], dps[i][j+2], \
                                            dps[i+2][j], dps[i+2][j+1], dps[i+2][j+2]) + grid[k][i] + grid[k][j]
            dps = news
        return dps[1][c]

sol = Solution()
grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
print(sol.cherryPickup(grid))