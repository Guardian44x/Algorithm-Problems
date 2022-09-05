class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        counter_s = Counter(s)
        counter_t = Counter(t)
        return True if counter_s == counter_t else False