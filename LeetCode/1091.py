"""
$1091. Shortest Path in Binary Matrix
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        l = len(grid)
        if l == 1:
            return 1
        if grid[0][0] or grid[-1][-1]:
            return -1
        visited = [[0] * l for _ in range(l)]
        visited[0][0] = 1
        states = [[0, 0]]
        x_steps = [-1, 0, 1]
        y_steps = [-1, 0, 1]
        step = 1
        while states and visited[-1][-1] == 0:
            # print(step, states)
            new_states = []
            step += 1
            for xs, ys in states:
                for x in x_steps:
                    for y in y_steps:
                        xn, yn = xs+x, ys+y
                        if xn < 0 or xn >= l or yn < 0 or yn >= l or grid[xn][yn] or visited[xn][yn]:
                            continue
                        new_states.append([xn, yn])
                        visited[xn][yn] = 1
            states = new_states
        return step if visited[-1][-1] else -11
