"""
$1540.py Can Convert String in K Moves
"""

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        a, b = divmod(k, 26)
        shifts = [a+1] * b + [a] * (26 - b)
        # print(shifts)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            shift = ord(t[i]) - ord(s[i])
            shift = shift if shift >= 0 else 26 + shift
            shifts[shift-1] -= 1
            if shift > 0 and shifts[shift-1] < 0:
                return False
        return True