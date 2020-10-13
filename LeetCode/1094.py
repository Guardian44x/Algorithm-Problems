"""
$1094. Car Pooling
"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        steps = []
        for trip in trips:
            steps.append([trip[1], trip[0]])
            steps.append([trip[2], -trip[0]])
        steps.sort()
        for step in steps:
            capacity -= step[1]
            if capacity < 0:
                return False
        return True