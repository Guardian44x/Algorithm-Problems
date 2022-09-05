"""
$1267.py
"""

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        row_sums = [0] * nrow
        col_sums = [0] * ncol
        count = 0
        for i in range(nrow):
            for j in range(ncol):
                row_sums[i] += grid[i][j]
                col_sums[j] += grid[i][j]
        for i in range(nrow):
            for j in range(ncol):
                if (grid[i][j] > 0) and (row_sums[i] * col_sums[j] > 1):
                    count += 1
        return count