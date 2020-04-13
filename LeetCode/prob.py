class Solution:
    def stoneGameIII(self, stoneValue):
        
        scores = [[0, 0]]
        l = len(stoneValue)
        
        for i in range(l-1, -1, -1):
            max_score1 = float("-inf")
            max_score2 = float("-inf")
            for j in range(1, 4):
                if j > len(scores):
                    break
                score1 = sum(stoneValue[i:i+j]) + scores[-1*j][1]
                score2 = scores[-1*j][0]
                if score1 >= max_score1:
                    max_score1 = score1
                    max_score2 = score2
            
            scores.append([max_score1, max_score2])
        
        if scores[-1][0] > scores[-1][1]:
            return "Alice"
        elif scores[-1][0] < scores[-1][1]:
            return "Bob"
        else:
            return "Tie"

sol = Solution()
values = [-1, -2, -3]
print(sol.stoneGameIII(values))