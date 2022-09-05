class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        counter_s = Counter(s)
        counter_t = Counter(t)
        res = 0
        for c in counter_t:
            cnt_s = counter_s.get(c) if counter_s.get(c) else 0
            cnt_t = counter_t.get(c) if counter_t.get(c) else 0
            res += max(0, cnt_t - cnt_s)
        return res