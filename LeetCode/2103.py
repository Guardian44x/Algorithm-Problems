class Solution:
    def countPoints(self, rings: str) -> int:
        counter = {
            'R': [0] * 10,
            'G': [0] * 10,
            'B': [0] * 10
        }
        for i in range(len(rings)//2):
            color = rings[2*i]
            position = rings[2*i+1]
            counter[color][int(position)] += 1
        res = 0
        for i in range(10):
            if counter['R'][i] > 0 and counter['G'][i] > 0 and counter['B'][i] > 0:
                res += 1
        return res