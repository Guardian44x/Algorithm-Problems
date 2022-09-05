# BFS Solution
from cmath import inf


class Solution:
    def pacificAtlantic(self, heights):
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(heights), len(heights[0])
        visited_p = [[0] * n for _ in range(m)]
        visited_a = [[0] * n for _ in range(m)]
        p_queue = []
        a_queue = []
        # vertical border 
        for i in range(m): 
            p_queue.append([i, 0])
            a_queue.append([i, n-1])
            visited_p[i][0] = 1
            visited_a[i][n-1] = 1
        # horizontal border
        for i in range(n):
            p_queue.append([0, i])
            a_queue.append([m-1, i])
            visited_p[0][i] = 1
            visited_a[m-1][i] = 1
        
        def bfs(queue, visited):
            while len(queue) > 0:
                cur = queue.pop(0)
                for d in dir:
                    x = cur[0] + d[0]
                    y = cur[1] + d[1]
                    if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or (heights[x][y] < heights[cur[0]][cur[1]]):
                        continue
                    visited[x][y] = 1
                    queue.append([x, y])

        bfs(p_queue, visited_p)
        bfs(a_queue, visited_a)

        res = []
        for i in range(m):
            for j in range(n):
                if visited_a[i][j] and visited_p[i][j]:
                    res.append([i, j])
        return res


# DFS Solution
class Solution:
    def pacificAtlantic(self, heights):
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(heights), len(heights[0])
        visited_p = [[0] * n for _ in range(m)]
        visited_a = [[0] * n for _ in range(m)]
        # vertical border 
        for i in range(m): 
            self.dfs(heights, visited_p, float(-inf), i, 0)
            self.dfs(heights, visited_a, float(-inf), i, n-1)
        # horizontal border
        for i in range(n):
            self.dfs(heights, visited_p, float(-inf), 0, i)
            self.dfs(heights, visited_a, float(-inf), m-1, i)

        res = []
        for i in range(m):
            for j in range(n):
                if visited_a[i][j] and visited_p[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, heights, visited, height, x, y):
        m, n = len(heights), len(heights[0])
        if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or (heights[x][y] < height):
            return
        visited[x][y] = 1
        for d in dir:
            self.dfs(heights, visited, heights[x][y], x+d[0], y+d[1])

