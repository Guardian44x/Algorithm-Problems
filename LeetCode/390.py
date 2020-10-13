"""
$390. Elimination Game
"""

class Solution:
    def lastRemaining(self, n: int) -> int:
        return self.lastRemaining2(n, True)
        
    def lastRemaining2(self, n: int, flag: bool) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2 if flag else 1
        if flag:
            n -= (n + 1) // 2
            val = self.lastRemaining2(n, False)
            return 2 * val
        else:
            val = self.lastRemaining2(n, True)
            return n + 1 - val