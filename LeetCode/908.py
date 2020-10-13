"""
$908. Smallest Range I
"""

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        max_val, min_val = max(A), min(A)
        return 0 if max_val - min_val <= 2*K else max_val - min_val - 2*KK