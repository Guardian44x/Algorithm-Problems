'''
$5112. Hexspeak 
'''

class Solution:
    def toHexspeak(self, num):
        num = int(num)
        res = []
        while num != 0:
            num, left = divmod(num, 16)
            if left > 1 and left < 10:
                return "ERROR"
            res.append(left)
        
        def hexmapping(dec):
            mapping = {0: 'O', 1: 'I', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            return mapping[dec]
        
        res = map(hexmapping, res)
        return ''.join(res[::-1])

sol = Solution()
num = "3"
print(sol.toHexspeak(num))