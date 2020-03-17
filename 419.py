"""
$419. Battleships in a Board
"""

class Solution:
    def countBattleships(self, board):
        h = len(board)
        w = len(board[0])
        c = 0
        for i in range(h):
            for j in range(w):
                if board[i][j] == '.':
                    continue
                if i < h-1 and j < h-1 and \
                    (board[i][j] == 'X' + board[i][j+1] == 'X' + \
                    board[i+1][j] == 'X' + board[i+1][j+1] == 'X') > 2:
                    return -1
                if board[i][j] == 'X':
                    if i > 0 and board[i-1][j] == 'X':
                        continue
                    if j > 0 and board[i][j-1] =='X':
                        continue
                    c += 1
        
        return c