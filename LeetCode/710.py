"""
$710. Random Pick with Blacklist
"""

from random import randint

class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        blacklist = set(blacklist)  #to avoid TLE
        self.N = N - len(blacklist) #to be used in pick()
        key = [x for x in blacklist if x < N-len(blacklist)]
        val = [x for x in range(N-len(blacklist), N) if x not in blacklist]
        self.mapping = dict(zip(key, val))

    def pick(self) -> int:
        i = randint(0, self.N-1)
        return self.mapping.get(i, i)