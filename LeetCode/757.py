"""
$757. Set Intersection Size At Least Two
"""

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        small, big = intervals[0][1] - 1, intervals[0][1]
        ans = 2

        def overlap_interval(interval):
            s, e = interval
            overlap = 0
            overlap += 1 if s <= small <= e else 0
            overlap += 1 if s <= big <= e else 0
            return overlap
        
        for i in range(1, len(intervals)):
            overlap = overlap_interval(intervals[i])
            if overlap == 2:
                continue
            elif overlap == 1:
                ans += 1
                small, big = big, intervals[i][1]
            else:
                ans += 2
                small, big = intervals[i][1] - 1, intervals[i][1]
        return ans