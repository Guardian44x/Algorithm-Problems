"""
$8. String to Interger (atoi)
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        slist = list(str)
        while slist and slist[0] == ' ':
            slist.pop(0)
        if not slist:
            return 0
        if slist[0] == '+' or slist[0] == '-':
            sign = 1 if slist[0] == '+' else -1
            slist.pop(0)
        elif slist[0] >= '0' and slist[0] <= '9':
            sign = 1
        else:
            return 0
           
        val = 0
        for c in slist:
            if c >= '0' and c <= '9':
                val = val*10 + int(c)
            else:
                break
        val *= sign
        if val > 2**31 -1:
            return 2**31-1
        if val < -2**31:
            return -2**31
        
        return val