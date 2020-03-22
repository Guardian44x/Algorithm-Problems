"""
$909. Snakes and Ladders
"""

class Solution:
    def snakesAndLadders(self, board):
        step = 0
        h = len(board)
        w = len(board[0])
        starts = [1]
        
        while starts:
            print(starts)
            destinations = []
            step += 1
            if step >= w*h:
                return -1
            for start in starts:
                no_skip = start
                for i in range(0, 6):
                    now = start + 1 + i
                    if now >= w*h:
                        return step
                    r, c = (now-1) // w, (now-1) % w
                    c = w - 1 - c if r % 2 == 1 else c  
                    r = h - 1 - r
                    if board[r][c] != -1:
                        destination = board[r][c]
                        destinations.append(destination)
                        if destination == w*h:
                            return step
                    else:
                        no_skip = start + i + 1
                if no_skip != start:
                    destinations.append(no_skip)
            starts = list(set(destinations))
        return step

sol = Solution()
board = [[1,1,-1],[1,1,1],[-1,1,1]]

res = sol.snakesAndLadders(board)
print(res)