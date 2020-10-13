"""
$318. Maximum Product of Word Lengths
"""

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dicts = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= 1 << (ord(c) - ord(a))
            dicts[mask] = max(dicts.get(mask, 0), len(w))
        return max([dicts[x] * dicts[y] for x in dicts for y in dicts if not x & y] or [0])
