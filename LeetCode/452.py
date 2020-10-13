"""
$452. Minimum Number of Arrows to Burst Balloons
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: x[1])
        res = 1
        pos = points[0][1]
        for i in range(len(points)):
            if points[i][0] <= pos:
                i += 1
                continue
            pos = points[i][1]
            res += 1
        return res