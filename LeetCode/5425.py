
"""
5425. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
"""
        
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        a, b = horizontalCuts[0], verticalCuts[0]
        horizontalCuts.append(h)
        verticalCuts.append(w)
        # print(horizontalCuts)
        for i in range(len(horizontalCuts)-1):
            a = max(horizontalCuts[i+1]-horizontalCuts[i], a)
        for i in range(len(verticalCuts)-1):
            b = max(verticalCuts[i+1]-verticalCuts[i], b)
        # print(a, b)
        return (a * b) % int(1e9+7) 