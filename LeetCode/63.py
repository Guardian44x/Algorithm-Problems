"""
$63. Unique Paths II
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h = len(obstacleGrid)
        if h == 0:
            return 0
        w = len(obstacleGrid[0])
        if w == 0:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[h-1][w-1] == 1:
            return 0
        paths = [[0] * (w+1) for i in range(h+1)]
        paths[h-1][w-1] = 1
    
        for i in range(h-1, -1, -1):
            for j in range(w-1, -1, -1):
                if i == h-1 and j == w-1:
                    continue
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                else:
                    paths[i][j] = paths[i+1][j] + paths[i][j+1]
        
        return paths[0][0]]
