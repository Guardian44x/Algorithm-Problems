"""
$12. Interger to Roman
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        a = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        b = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = [0] * len(a)
        for i in range(len(res)):
            t, num = divmod(num, a[i])
            res[i] = t
        
        val = ""
        for i, c in enumerate(res):
            val += c * b[i]
        return val